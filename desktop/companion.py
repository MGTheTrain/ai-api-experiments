import os
import customtkinter as ctk
from pathlib import Path
from src.chat_bot import ChatBot
from src.image_generator import ImageGenerator
from src.speech_generator import TextToSpeechGenerator

# Get API key from environment
API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    ctk.CTkMessagebox("Error", "Set your OpenAI API key. On unix systems you would `export OPENAI_API_KEY=<your OpenAI_API_KEY>`")
    exit()

# Initialize models
chatbot = ChatBot(API_KEY)
image_generator = ImageGenerator(API_KEY)
tts_generator = TextToSpeechGenerator(API_KEY)

class AIApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("AI Assistant")
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
        self.generate_button = ctk.CTkButton(self, text="Generate", command=self.generate_output, width=200)
        self.generate_button.pack(pady=20)

        # Replace the output label with a larger Text widget for copying content
        self.output_text = ctk.CTkTextbox(self, wrap="word", height=30, width=120, font=large_font) 
        self.output_text.pack(pady=5, expand=True)

        # Optional: Make the Text widget read-only (disable editing)
        self.output_text.configure(state="disabled")

        self.update_fields()

    def update_fields(self):
        """Dynamically update input fields based on selected category"""
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        category = self.category.get()

        if category == "chatbot":
            ctk.CTkLabel(self.options_frame, text="Select Model", font=self.font).pack(pady=5)
            self.chat_model = ctk.CTkComboBox(self.options_frame, values=["gpt-4o", "gpt-4o-mini", "o1", "o3-mini"])
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

            ctk.CTkLabel(self.options_frame, text="Enter your output file path", font=self.font).pack(pady=5)
            self.speech_output_file_path = ctk.CTkEntry(self.options_frame, width=300, font=self.font)
            self.speech_output_file_path.pack(pady=5, padx=5)

    def generate_output(self):
        """Process user input and call the appropriate AI function"""
        prompt = self.prompt_entry.get().strip()
        if not prompt:
            ctk.CTkMessagebox("Error", "Enter a prompt.")
            return

        category = self.category.get()

        if category == "chatbot":
            model = self.chat_model.get()
            response = chatbot.chat(model, prompt).content
            self.output_text.configure(state="normal")  # Enable editing temporarily
            self.output_text.delete(1.0, "end")  # Clear previous content
            self.output_text.insert("end", response)  # Insert new response
            self.output_text.configure(state="disabled")  # Disable editing

        elif category == "image":
            model = self.image_model.get()
            size = self.image_size.get()
            image_url = image_generator.generate_image(model, prompt, size)
            self.output_text.configure(state="normal")  
            self.output_text.delete(1.0, "end")  
            self.output_text.insert("end", image_url)  
            self.output_text.configure(state="disabled")  

        elif category == "speech":
            model = self.speech_model.get()
            voice = self.speech_voice.get()
            output_path = self.speech_output_file_path.get()
            tts_generator.generate_speech(model, voice, prompt, str(output_path))
            self.output_text.configure(state="normal")  
            self.output_text.delete(1.0, "end")  
            self.output_text.insert("end", f"Speech saved to: {output_path}")  
            self.output_text.configure(state="disabled")  


if __name__ == "__main__":
    app = AIApp()
    app.mainloop()
