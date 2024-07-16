# main.py

import tkinter as tk
from tkinter import messagebox
import time
import typing_test
import stopwatch_test

class TypingTestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Test App")
        self.geometry("400x200")

        # Create buttons
        button1 = tk.Button(self, text="One-Minute Typing Test", command=self.open_typing_test)
        button1.pack(pady=20)

        button2 = tk.Button(self, text="Stopwatch Timing Test", command=self.open_stopwatch_test)
        button2.pack()

    def open_typing_test(self):
        typing_test_app = typing_test.TypingTestWindow(self)
        typing_test_app.mainloop()

    def open_stopwatch_test(self):
        stopwatch_test_app = stopwatch_test.StopwatchTestWindow(self)
        stopwatch_test_app.mainloop()

if __name__ == "__main__":
    app = TypingTestApp()
    app.mainloop()