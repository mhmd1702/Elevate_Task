import tkinter as tk
from datetime import datetime, timedelta

def start_countdown():
    time_str = time_input.get()
    if len(time_str) == 8 and time_str.count(":") == 2:
        h, m, s = map(int, time_str.split(':'))
        target_time = datetime.now() + timedelta(hours=h, minutes=m, seconds=s)
        update_timer(target_time)
    else:
        time_display.config(text="Invalid format! Use HH:MM:SS")

def update_timer(target_time):
    remaining_time = target_time - datetime.now()
    if remaining_time.total_seconds() > 0:
        time_display.config(text=str(remaining_time).split('.')[0])
        root.after(1000, update_timer, target_time)
    else:
        time_display.config(text="00:00:00")
        time_display.after(1000, lambda: time_display.config(text="Time's up!"))

root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")
root.configure(bg='#2E3B4E')  # Set background color

tk.Label(root, text="Enter time duration (HH:MM:SS):", bg='#2E3B4E', fg='white').pack(pady=10)
time_input = tk.Entry(root)
time_input.pack(pady=5)

tk.Button(root, text="Start Countdown", command=start_countdown, bg='#4CAF50', fg='white', activebackground='#45A049').pack(pady=10)
time_display = tk.Label(root, text="", font=("Helvetica", 20), bg='#2E3B4E', fg='white')
time_display.pack(pady=10)

root.mainloop()
