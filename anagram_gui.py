import tkinter as tk
from tkinter import messagebox
from anagram_solver import AnagramSolver

class AnagramApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoAnagram Solver")

        self.solver = AnagramSolver(self.load_dictionary())

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter jumbled letters:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve_anagram)
        self.solve_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="Possible words:")
        self.result_label.pack(pady=10)

        self.result_listbox = tk.Listbox(self.root, width=50, height=10)
        self.result_listbox.pack(pady=10)

    def load_dictionary(self):
        # For the purpose of this example, we use a small list of words.
        # In a real application, this could be loaded from a file or a larger dataset.
        return [
            'cat', 'dog', 'god', 'act', 'tac', 'rat', 'tar', 'art',
            'star', 'rats', 'tars', 'arts', 'start', 'tarts', 'abcdefgh'
        ]

    def solve_anagram(self):
        jumbled_word = self.entry.get().strip()
        if not jumbled_word:
            messagebox.showwarning("Input Error", "Please enter some jumbled letters.")
            return

        solutions = self.solver.solve_anagram(jumbled_word)
        self.result_listbox.delete(0, tk.END)

        if solutions:
            for word in solutions:
                self.result_listbox.insert(tk.END, word)
        else:
            self.result_listbox.insert(tk.END, "No valid words found.")

def main():
    root = tk.Tk()
    app = AnagramApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
