import os
import customtkinter as ctk
from pathlib import Path
from src.chat_bot import ChatBot
from src.image_generator import ImageGenerator
from src.speech_generator import TextToSpeechGenerator
from PIL import Image, ImageTk
import requests
from io import BytesIO
import uuid
import threading

API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    ctk.CTkMessagebox("Error", "Set your OpenAI API key. On unix systems you would `export OPENAI_API_KEY=<your OpenAI_API_KEY>`")
    exit()

chatbot = ChatBot(API_KEY)
image_generator = ImageGenerator(API_KEY)
tts_generator = TextToSpeechGenerator(API_KEY)

class AIApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Companion")
        self.geometry("900x900")

        self.font = ('Helvetica', 16)
        
        # Set dark theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Category Selection
        self.category = ctk.StringVar(value="chatbot")
        ctk.CTkLabel(self, text="Select AI Task", font=self.font).pack(pady=5)

        categories = [("ChatBot", "chatbot"), ("Image Generation", "image"), ("Speech Generation", "speech")]
        for text, value in categories:
            ctk.CTkRadioButton(self, text=text, variable=self.category, value=value, command=self.update_fields).pack()

        # Center the Input Prompt Label
        ctk.CTkLabel(self, text="Enter your prompt", font=self.font).pack(pady=5)

        # Center the Entry field (with more padding for visual appeal)
        self.prompt_entry = ctk.CTkEntry(self, width=300, font=self.font)
        self.prompt_entry.pack(pady=5)

        # Center the Additional Options frame
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=5)

        # Center the Generate Button
        self.generate_button = ctk.CTkButton(self, text="Generate", command=self.start_generation, width=200)
        self.generate_button.pack(pady=20)

        # Initialize the output text box and configure it to fill the window
        self.output_text = ctk.CTkTextbox(master=self, font=self.font, corner_radius=0)
        self.output_text.pack(padx=10, pady=10, expand=True, fill="both")

        # Optional: Make the Text widget read-only (disable editing)
        self.output_text.configure(state="disabled")

        # Create a frame for the image label
        self.image_frame = ctk.CTkFrame(self)
        self.image_label = ctk.CTkLabel(self.image_frame, text="Image Preview")
        self.image_label.pack(padx=10, pady=10, expand=True)
        self.image_frame.pack_forget()  # Hide the image frame initially

        # Background task label indicating tasks running in a separate thread in the background
        self.background_task_label = ctk.CTkLabel(self, text="Processing... Please wait.")
        self.background_task_label.pack(pady=10)
        self.background_task_label.pack_forget()  # Hide initially

        self.update_fields()

    def update_fields(self) -> None:
        """Dynamically update input fields based on selected category"""
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        category = self.category.get()

        # Hide or show image label based on category
        if category == "image":
            self.image_frame.pack(padx=10, pady=10, expand=True)  # Show image frame
        else:
            self.image_frame.pack_forget()

        if category == "chatbot":
            ctk.CTkLabel(self.options_frame, text="Select Model", font=self.font).pack(pady=5)
            self.chat_model = ctk.CTkComboBox(self.options_frame, values=["gpt-4o", "gpt-4o-mini"])
            self.chat_model.set("gpt-4o")
            self.chat_model.pack()

        elif category == "image":
            ctk.CTkLabel(self.options_frame, text="Select Image Model", font=self.font).pack(pady=5)
            self.image_model = ctk.CTkComboBox(self.options_frame, values=["dall-e-2", "dall-e-3"])
            self.image_model.set("dall-e-3")
            self.image_model.pack()

            ctk.CTkLabel(self.options_frame, text="Image Size", font=self.font).pack(pady=5)
            self.image_size = ctk.CTkComboBox(self.options_frame, values=["1024x1024", "512x512"])
            self.image_size.set("1024x1024")
            self.image_size.pack()

        elif category == "speech":
            ctk.CTkLabel(self.options_frame, text="Select Speech Model", font=self.font).pack(pady=5)
            self.speech_model = ctk.CTkComboBox(self.options_frame, values=["tts-1", "tts-1-hd"])
            self.speech_model.set("tts-1")
            self.speech_model.pack()

            ctk.CTkLabel(self.options_frame, text="Select Voice", font=self.font).pack(pady=5)
            self.speech_voice = ctk.CTkComboBox(self.options_frame, values=["alloy", "echo", "fable", "onyx", "nova", "shimmer"])
            self.speech_voice.set("alloy")
            self.speech_voice.pack()

    def start_generation(self) -> None:
        """Start the long-running task in a background thread"""
        prompt = self.prompt_entry.get().strip()
        if not prompt:
            ctk.CTkMessagebox("Error", "Enter a prompt.")
            return

        # Show the background task label
        self.background_task_label.pack(pady=10)

        # Disable the Generate button while processing
        self.generate_button.configure(state="disabled")

        # Start a background thread for the task
        task_thread = threading.Thread(target=self.generate_output, args=(prompt,))
        task_thread.start()

    def generate_output(self, prompt: str) -> None:
        """Process user input and call the appropriate AI function"""
        category = self.category.get()

        if category == "chatbot":
            model = self.chat_model.get()
            response = chatbot.chat(model, prompt).content
            self.update_output_text(response)

        elif category == "image":
            model = self.image_model.get()
            size = self.image_size.get()
            image_url = image_generator.generate_image(model, prompt, size)
            self.update_output_text(f"Image url: \n{image_url}")
            self.display_image_from_url(image_url)

        elif category == "speech":
            model = self.speech_model.get()
            voice = self.speech_voice.get()
            output_path = self.generate_output_path()
            tts_generator.generate_speech(model, voice, prompt, str(output_path))
            self.update_output_text(f"Speech saved to \n: {os.path.abspath(output_path)}")

        # Hide the background task label and re-enable the Generate button when the task is done
        self.background_task_label.pack_forget()
        self.generate_button.configure(state="normal")

    def update_output_text(self, text: str) -> None:
        """Update the output text box with results"""
        self.output_text.configure(state="normal")
        self.output_text.delete(1.0, "end")
        self.output_text.insert("end", text)
        self.output_text.configure(state="disabled")


if __name__ == "__main__":
    app = AIApp()
    app.mainloop()
