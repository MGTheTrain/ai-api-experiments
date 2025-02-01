import os
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from src.chat_bot import ChatBot
from src.image_generator import ImageGenerator
from src.speech_generator import TextToSpeechGenerator

# Get API key from environment
API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    messagebox.showerror("Error", "Set your OpenAI API key. On unix systems you would `export OPENAI_API_KEY=<your OpenAI_API_KEY>`")
    exit()

# Initialize models
chatbot = ChatBot(API_KEY)
image_generator = ImageGenerator(API_KEY)
tts_generator = TextToSpeechGenerator(API_KEY)

class RoundedEntry(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.style = ttk.Style()
        self.style.configure("RoundedEntry.TEntry", padding=10, font=('Helvetica', 16))
        self.configure(style="RoundedEntry.TEntry")


class RoundedButton(ttk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.style = ttk.Style()
        self.style.configure("RoundedButton.TButton", padding=10, font=('Helvetica', 10))
        self.configure(style="RoundedButton.TButton")


class AIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Assistant")
        self.geometry("900x900")

        self.font = ('Helvetica', 16)

        # Category Selection
        self.category = tk.StringVar(value="chatbot")
        ttk.Label(self, text="Select AI Task", font=self.font).pack(pady=5)

        categories = [("ChatBot", "chatbot"), ("Image Generation", "image"), ("Speech Generation", "speech")]
        for text, value in categories:
            ttk.Radiobutton(self, text=text, variable=self.category, value=value, command=self.update_fields).pack()

        # Center the Input Prompt Label
        ttk.Label(self, text="Enter your prompt", font=self.font).pack(pady=5)

        # Center the Entry field (with more padding for visual appeal)
        self.prompt_entry = RoundedEntry(self, width=100)
        self.prompt_entry.pack(pady=5)

        # Center the Additional Options frame
        self.options_frame = ttk.Frame(self, width=50)
        self.options_frame.pack(pady=5)

        # Center the Generate Button
        self.generate_button = RoundedButton(self, text="Generate", command=self.generate_output, width=20)
        self.generate_button.pack(pady=20)

        # Replace the output label with a Text widget for copying content
        self.output_text = tk.Text(self, wrap=tk.WORD, height=50, width=100, font=self.font)  # You can add a Canvas widget for rounded text box if needed
        self.output_text.pack(pady=5, expand=True)

        # Optional: Make the Text widget read-only (disable editing)
        self.output_text.config(state=tk.DISABLED)

        self.update_fields()

    def update_fields(self):
        """Dynamically update input fields based on selected category"""
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        category = self.category.get()

        if category == "chatbot":
            ttk.Label(self.options_frame, text="Select Model", font=self.font).pack(pady=5)
            self.chat_model = ttk.Combobox(self.options_frame, values=["gpt-4o", "gpt-4o-mini", "o1", "o3-mini"], state="readonly")
            self.chat_model.set("gpt-4o")
            self.chat_model.pack()

        elif category == "image":
            ttk.Label(self.options_frame, text="Select Image Model", font=self.font).pack(pady=5)
            self.image_model = ttk.Combobox(self.options_frame, values=["dall-e-2", "dall-e-3"], state="readonly")
            self.image_model.set("dall-e-3")
            self.image_model.pack()

            ttk.Label(self.options_frame, text="Image Size", font=self.font).pack(pady=5)
            self.image_size = ttk.Combobox(self.options_frame, values=["1024x1024", "512x512"], state="readonly")
            self.image_size.set("1024x1024")
            self.image_size.pack()

        elif category == "speech":
            ttk.Label(self.options_frame, text="Select Speech Model", font=self.font).pack(pady=5)
            self.speech_model = ttk.Combobox(self.options_frame, values=["tts-1", "tts-1-hd"], state="readonly")
            self.speech_model.set("tts-1")
            self.speech_model.pack()

            ttk.Label(self.options_frame, text="Select Voice", font=self.font).pack(pady=5)
            self.speech_voice = ttk.Combobox(self.options_frame, values=["alloy", "echo", "fable", "onyx", "nova", "shimmer"], state="readonly")
            self.speech_voice.set("alloy")
            self.speech_voice.pack()

            ttk.Label(self.options_frame, text="Enter your output file path", font=self.font).pack(pady=5)
            self.speech_output_file_path = RoundedEntry(self.options_frame, width=50)
            self.speech_output_file_path.pack(pady=5, padx=5)

    def generate_output(self):
        """Process user input and call the appropriate AI function"""
        prompt = self.prompt_entry.get().strip()
        if not prompt:
            messagebox.showerror("Error", "Enter a prompt.")
            return

        category = self.category.get()

        if category == "chatbot":
            model = self.chat_model.get()
            response = chatbot.chat(model, prompt).content
            self.output_text.config(state=tk.NORMAL)  # Enable editing temporarily
            self.output_text.delete(1.0, tk.END)  # Clear previous content
            self.output_text.insert(tk.END, response)  # Insert new response
            self.output_text.config(state=tk.DISABLED)  # Disable editing

        elif category == "image":
            model = self.image_model.get()
            size = self.image_size.get()
            image_url = image_generator.generate_image(model, prompt, size)
            self.output_text.config(state=tk.NORMAL)  
            self.output_text.delete(1.0, tk.END)  
            self.output_text.insert(tk.END, image_url)  
            self.output_text.config(state=tk.DISABLED)  

        elif category == "speech":
            model = self.speech_model.get()
            voice = self.speech_voice.get()
            output_path = self.speech_output_file_path.get()
            tts_generator.generate_speech(model, voice, prompt, str(output_path))
            self.output_text.config(state=tk.NORMAL)  
            self.output_text.delete(1.0, tk.END)  
            self.output_text.insert(tk.END, f"Speech saved to: {output_path}")  
            self.output_text.config(state=tk.DISABLED)  



if __name__ == "__main__":
    app = AIApp()
    app.mainloop()
