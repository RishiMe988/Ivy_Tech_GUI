import tkinter as tk
from tkinter import messagebox
import time


class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("1 Minute Timer")

        self.label = tk.Label(self.master, text="1:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        self.seconds_left = 60
        self.running = False
        self.update_timer()

    def update_timer(self):
        minutes = self.seconds_left // 60
        seconds = self.seconds_left % 60
        self.label.config(text=f"{minutes:02}:{seconds:02}")
        if self.running:
            if self.seconds_left > 0:
                self.seconds_left -= 1
                self.master.after(1000, self.update_timer)
            else:
                self.running = False
                messagebox.showinfo("Timer", "Timer expired!")
                self.stop_timer()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.update_timer()

    def stop_timer(self):
        self.running = False
        self.seconds_left = 60
        self.label.config(text="1:00")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()