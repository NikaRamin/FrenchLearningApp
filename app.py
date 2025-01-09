import tkinter as tk
from tkinter import messagebox
import random
import pandas as pd

class FrenchLearningApp:
    def __init__(self, root):
        self.load_data()
        self.root = root
        self.root.title("French Learning App")
        self.root.geometry("500x400")
        self.root.config(bg="#3C6D8C")

        main_frame = tk.Frame(root, bg="#3C6D8C")
        main_frame.pack(pady=20)

        # UI Elements
        self.word_label = tk.Label(root, text="English Word:", font=("Arial", 18, "bold"), bg="#3C6D8C", fg="black", highlightthickness=0, highlightbackground="#3C6D8C", highlightcolor="#3C6D8C")
        self.word_label.pack(pady=10)

        self.word_var = tk.StringVar()
        self.word_entry = tk.Entry(root, textvariable=self.word_var, fg="white", font=("Arial", 14), state='readonly', readonlybackground="#3C6D8C", highlightthickness=1, highlightbackground="black", highlightcolor="black")
        self.word_entry.pack(pady=10)

        self.translation_label = tk.Label(root, text="French Translation:", font=("Arial", 18, "bold"), bg="#3C6D8C", fg="black", highlightthickness=0, highlightbackground="#3C6D8C", highlightcolor="#3C6D8C")
        self.translation_label.pack(pady=10)

        self.translation_var = tk.StringVar()
        self.translation_entry = tk.Entry(root, textvariable=self.translation_var, font=("Arial", 14), bg="#3C6D8C", fg="white", highlightthickness=1, highlightbackground="black", highlightcolor="black")
        self.translation_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check", command=self.check_translation, font=("Arial", 14), bg="#3C6D8C", fg="black", highlightthickness=0, bd=0, highlightbackground="#3C6D8C", highlightcolor="#3C6D8C")
        self.check_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_word, font=("Arial", 14), bg="#3C6D8C", fg="black", highlightthickness=0, bd=0, highlightbackground="#3C6D8C", highlightcolor="#3C6D8C")
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14, "bold"), bg="#3C6D8C", fg="black", highlightthickness=0, highlightbackground="#3C6D8C", highlightcolor="#3C6D8C")
        self.score_label.pack(pady=10)
        
        self.score = 0
        self.next_word()

    def load_data(self):
        try:
            data = pd.read_csv("Dictionary.csv")
            self.words = dict(zip(data['English'], data['French']))
            if not self.words:
                raise ValueError("The dictionary is empty.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Dictionary.csv file not found!")
            self.root.destroy()
        except KeyError:
            messagebox.showerror("Error", "The CSV file must have 'English' and 'French' columns.")
            self.root.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.root.destroy()

    def next_word(self):
        """Display the next word."""
        if not self.words:
            messagebox.showinfo("Congratulations", "You've completed all words!")
            self.root.destroy()
            return

        self.current_word = random.choice(list(self.words.keys()))
        self.word_var.set(self.current_word)
        self.translation_var.set("")

    def check_translation(self):
        
        user_translation = self.translation_var.get().strip()
        if not user_translation:
            messagebox.showinfo("Don't leave the box empty! take a guess!")
        correct_translation = self.words[self.current_word]

        if user_translation.lower() == correct_translation.lower():
            messagebox.showinfo("Correct", "Correct! Well done!")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            del self.words[self.current_word] 
            self.next_word()
        else:
            messagebox.showerror("Incorrect", f"Incorrect! The correct translation is '{correct_translation}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FrenchLearningApp(root)
    root.mainloop()
