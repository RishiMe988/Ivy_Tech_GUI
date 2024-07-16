# typing_test.py

import tkinter as tk
from tkinter import messagebox
import time

class TypingTestWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("One-Minute Typing Test")
        self.geometry("400x300")

        # Timer label
        self.timer_label = tk.Label(self, text="Timer: 1:00")
        self.timer_label.pack(pady=10)

        # Input box
        self.text_box = tk.Text(self, height=10, width=50)
        self.text_box.pack(pady=10)

        # Start button
        self.start_button = tk.Button(self, text="Start", command=self.start_typing_test)
        self.start_button.pack()

        # Go back button
        self.go_back_button = tk.Button(self, text="Go Back", command=self.destroy)
        self.go_back_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def start_typing_test(self):
        self.start_button.config(state=tk.DISABLED)  # Disable start button during test
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, 60 - elapsed_time)
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        self.timer_label.config(text=f"Timer: {minutes}:{seconds:02}")

        if remaining_time > 0:
            self.after(100, self.update_timer)
        else:
            self.calculate_results()

    def calculate_results(self):
        typed_text = self.text_box.get("1.0", tk.END)
        words = len(typed_text.split())
        characters = len(typed_text.replace(" ", "").replace("\n", ""))
        time_elapsed = time.time() - self.start_time
        characters_per_sec = characters / time_elapsed if time_elapsed > 0 else 0

        result_message = f"Words typed: {words}\nCharacters typed: {characters}\nCharacters per second: {characters_per_sec:.2f}"
        messagebox.showinfo("Typing Test Results", result_message)
        self.start_button.config(state=tk.NORMAL)  # Re-enable start button
        self.text_box.delete("1.0", tk.END)  # Clear the text box