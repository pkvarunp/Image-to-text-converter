import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Set the path for tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class TextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Text Extractor")

        self.label = tk.Label(root, text="Select an image to extract text")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse Image", command=self.browse_image)
        self.browse_button.pack(pady=5)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.extract_button = tk.Button(root, text="Extract Text", command=self.extract_text)
        self.extract_button.pack(pady=5)

        self.text_box = tk.Text(root, height=10, width=50)
        self.text_box.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Text", command=self.save_text)
        self.save_button.pack(pady=5)

        self.filename = None

    def browse_image(self):
        self.filename = filedialog.askopenfilename(
            initialdir="/", 
            title="Select an Image",
            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"))
        )
        if self.filename:
            image = Image.open(self.filename)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def extract_text(self):
        if self.filename:
            text = pytesseract.image_to_string(Image.open(self.filename))
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, text)
        else:
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, "Please select an image first.")

    def save_text(self):
        text = self.text_box.get(1.0, tk.END)
        if text.strip():
            with open("ExtractedText.txt", "a") as file:
                file.write(text)
            self.text_box.insert(tk.END, "\nText saved successfully.")
        else:
            self.text_box.insert(tk.END, "\nNo text to save.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()
