import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("400x400")

        self.board = [
            [0, 6, 5, 0, 8, 0, 4, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 7, 0, 0, 0, 0, 0, 3],
            [0, 0, 0, 3, 0, 1, 0, 8, 0],
            [0, 0, 0, 8, 6, 3, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 6, 0, 0],
            [3, 0, 0, 0, 0, 0, 2, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 7],
            [5, 2, 0, 0, 0, 0, 6, 3, 0]
        ]

        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    entry = tk.Entry(self.root, width=3, justify='center', bg='green', fg='white', font=('Arial', 18, 'bold'))
                    entry.insert(0, str(self.board[i][j]))
                    entry.config(state='disabled')
                else:
                    entry = tk.Entry(self.root, width=3, justify='center', font=('Arial', 18, 'bold'))
                
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.entries[i][j] = entry

        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=10, column=0, columnspan=9)

    def solve_sudoku(self):
        # TODO: Implement the actual Sudoku solver algorithm
        # Placeholder to show solved Sudoku
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, "1")  # Replace "1" with the actual solved value

        messagebox.showinfo("Solved", "Sudoku solved!")

def main():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
