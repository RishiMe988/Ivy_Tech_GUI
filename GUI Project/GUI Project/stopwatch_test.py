# stopwatch_test.py

import tkinter as tk
from tkinter import messagebox
import time

class StopwatchTestWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Stopwatch Timing Test")
        self.geometry("400x300")

        # Stopwatch label
        self.stopwatch_label = tk.Label(self, text="00:00:00")
        self.stopwatch_label.pack(pady=10)

        # Input box
        self.text_box = tk.Text(self, height=10, width=50)
        self.text_box.pack(pady=10)

        # Start button
        self.start_button = tk.Button(self, text="Start", command=self.start_stopwatch)
        self.start_button.pack()

        # Stop button
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_stopwatch, state=tk.DISABLED)
        self.stop_button.pack()

        # Go back button
        self.go_back_button = tk.Button(self, text="Go Back", command=self.destroy)
        self.go_back_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.start_time = None
        self.running = False

    def start_stopwatch(self):
        self.running = True
        self.start_time = time.time()
        self.update_stopwatch()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_stopwatch(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.calculate_results()

    def update_stopwatch(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            self.stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.after(1000, self.update_stopwatch)

    def calculate_results(self):
        typed_text = self.text_box.get("1.0", tk.END)
        words = len(typed_text.split())
        characters = len(typed_text.replace(" ", "").replace("\n", ""))
        time_elapsed = time.time() - self.start_time
        characters_per_sec = characters / time_elapsed if time_elapsed > 0 else 0

        result_message = f"Time elapsed: {int(time_elapsed // 3600)}:{int((time_elapsed % 3600) // 60)}:{int(time_elapsed % 60)}\nWords typed: {words}\nCharacters typed: {characters}\nCharacters per second: {characters_per_sec:.2f}"
        messagebox.showinfo("Stopwatch Test Results", result_message)
        self.text_box.delete("1.0", tk.END)