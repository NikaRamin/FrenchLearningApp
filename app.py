import tkinter as tk
from tkinter import messagebox
import random
import pandas as pd

class FrenchLearningApp:
    def __init__(self,root):
        self.root = root
        self.root.title("French Learning App")
        
        self.word_label = self.root.label = tk.Label(root, text="English Word:", font=("Arial", 14))
        self.word_label.pack(pady=10)
        
        
    def load_data(self):
        data = pd.read_csv("Dictionary.csv")
        
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = FrenchLearningApp(root)
    root.mainloop()