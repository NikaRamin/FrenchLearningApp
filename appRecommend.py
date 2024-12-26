import tkinter as tk
from tkinter import messagebox
import random

# Dictionary of English to French words
words = {
    "Hello": "Bonjour",
    "Goodbye": "Au revoir",
    "Please": "S'il vous plaît",
    "Thank you": "Merci",
    "Yes": "Oui",
    "No": "Non"
}

class FrenchLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("French Learning App")

        self.word_label = tk.Label(root, text="English Word:", font=("Arial", 14))
        self.word_label.pack(pady=10)

        self.word_var = tk.StringVar()
        self.word_entry = tk.Entry(root, textvariable=self.word_var, font=("Arial", 14), state='readonly')
        self.word_entry.pack(pady=10)

        self.translation_label = tk.Label(root, text="French Translation:", font=("Arial", 14))
        self.translation_label.pack(pady=10)

        self.translation_var = tk.StringVar()
        self.translation_entry = tk.Entry(root, textvariable=self.translation_var, font=("Arial", 14))
        self.translation_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check", command=self.check_translation, font=("Arial", 14))
        self.check_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_word, font=("Arial", 14))
        self.next_button.pack(pady=10)

        self.next_word()

    def next_word(self):
        self.current_word = random.choice(list(words.keys()))
        self.word_var.set(self.current_word)
        self.translation_var.set("")

    def check_translation(self):
        user_translation = self.translation_var.get().strip()
        correct_translation = words[self.current_word]
        if user_translation.lower() == correct_translation.lower():
            messagebox.showinfo("Correct", "Correct! Well done!")
        else:
            messagebox.showerror("Incorrect", f"Incorrect! The correct translation is '{correct_translation}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FrenchLearningApp(root)
    root.mainloop()