import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from tkinter import font as tkfont

class LibraryItem:
    def __init__(self, name, director, rating=0):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars

        def display_image(self, image_path):
         """Display an image given its path."""
        try:
            print(f"Attempting to load image from: {image_path}")  # Debug print
            img = Image.open(image_path)
            img = img.resize((300, 300), Image.ANTIALIAS)  # Resize the image to fit the label
            photo = ImageTk.PhotoImage(img)
            self.image_lbl.config(image=photo)
            self.image_lbl.image = photo  # Keep a reference to avoid garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Could not load image: {e}")