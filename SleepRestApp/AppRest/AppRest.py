import tkinter as tk
from tkinter import ttk
from time import sleep, time

def start_timer(minutes):
    global end_time
    end_time = time() + minutes * 60

def start_countdown():
    remaining_time = end_time - time()
    if remaining_time > 0:
        hours = int(remaining_time // 3600)
        minutes = int((remaining_time % 3600) // 60)
        seconds = int(remaining_time % 60)
        countdown_label.config(text=f"Time until sleep: {hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(1000, start_countdown)
    else:
        countdown_label.config(text="Sleep mode activated")

def show_countdown():
    start_countdown()

def cancel():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Sleep Timer")

# Set white background
root.configure(bg="white")

# Double the size of the window
root.geometry("800x800")

# Description label
description_label = tk.Label(root, text="Select the timer duration:", bg="white", font=("Segoe UI", 20))
description_label.pack()

# Timer presets in minutes
timers = {
    "5 Minutes": 5,
    "15 Minutes": 15,
    "30 Minutes": 30,
    "1 Hour": 60,
}

# Create buttons for preset timer durations using ttk
for timer_label, minutes in timers.items():
    button_timer = ttk.Button(root, text=timer_label, command=lambda m=minutes: start_timer(m), style='TimerButton.TButton')
    button_timer.pack(pady=10)

# Create a button to show countdown
button_show_countdown = ttk.Button(root, text="Show Time Until Sleep", command=show_countdown, style='TimerButton.TButton')
button_show_countdown.pack(pady=10)

# Create a cancel button
button_cancel = ttk.Button(root, text="Cancel", command=cancel, style='CancelButton.TButton')
button_cancel.pack(pady=10)

# Label to display countdown
countdown_label = tk.Label(root, text="", bg="white", font=("Segoe UI", 16))
countdown_label.pack()

# Style for buttons
style = ttk.Style()
style.configure('TimerButton.TButton', font=("Segoe UI", 16))
style.configure('CancelButton.TButton', font=("Segoe UI", 16), foreground='red')

root.mainloop()
