
import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")

        self.hello = ttk.Label(self.root, text="Hello World!")
        self.hello.pack()


        self.root.mainloop()


if __name__ == "__main__":
    app = App()
