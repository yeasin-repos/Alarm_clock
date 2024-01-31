import sys
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pygame import mixer

#get minutes and seconds from total seconds
def get_minutes_and_seconds(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return minutes, seconds

def activate_alarm():
    #user-selected time
    selected_hour = int(c_hour.get())
    selected_minute = int(c_min.get())
    selected_second = int(c_sec.get())
    selected_period = c_period.get()

    #current time
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    #user-selected time to 24-hour format
    if selected_period == "PM" and selected_hour != 12:
        selected_hour += 12

    #time difference
    time_difference = (selected_hour - current_hour) * 3600 + (selected_minute - current_minute) * 60 + (selected_second - current_second)

    # Check if the alarm's in the future
    if time_difference > 0:
        # Schedule the alarm after the time difference
        window.after(time_difference * 1000, play_alarm)

#play alarm sound
def play_alarm():
    mixer.music.load('./alarm.mp3')
    mixer.music.play()

#stop alarm sound
def deactivate_alarm():
    mixer.music.stop()

mixer.init()

#dynamic combobox values
def generate_combobox_values(start, end):
    return [str(i).zfill(2) for i in range(start, end)]

#window:
window = tk.Tk()
window.title("Alarm Clock")
window.geometry('500x250')
window.configure(bg='#BB9CC0')

#frames:
frame_line = tk.Frame(window, width=500, height=5, bg='#7E30E1')
frame_line.pack(pady=5)

frame_body = tk.Frame(window, width=500, height=300, bg='#BB9CC0')
frame_body.pack(pady=10)

#display image
img_path = './image/alarm-clock.png'
img = Image.open(img_path)
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)
app_img = tk.Label(frame_body, image=img, bg='#BB9CC0')
app_img.grid(row=0, column=0, padx=10, rowspan=3)

# labels and comboboxes
name = tk.Label(frame_body, text="Alarm", font=('Arial 20 bold'), bg='#BB9CC0', fg='#49108B')
name.grid(row=0, column=1, columnspan=4)

labels = ["hour", "min", "sec", "period"]
#generate dynamic combobox values
hour_values = generate_combobox_values(1, 13)
min_sec_values = generate_combobox_values(0, 60)
period_values = ["AM", "PM"]

#combobox widgets and position using grid
c_hour = ttk.Combobox(frame_body, width=4, font=('Arial 12'), justify=tk.CENTER)
c_hour['values'] = hour_values
c_hour.current(0)
c_hour.grid(row=1, column=1, padx=5)

c_min = ttk.Combobox(frame_body, width=4, font=('Arial 12'), justify=tk.CENTER)
c_min['values'] = min_sec_values
c_min.current(0)
c_min.grid(row=1, column=2, padx=5)

c_sec = ttk.Combobox(frame_body, width=4, font=('Arial 12'), justify=tk.CENTER)
c_sec['values'] = min_sec_values
c_sec.current(0)
c_sec.grid(row=1, column=3, padx=5)

c_period = ttk.Combobox(frame_body, width=4, font=('Arial 12'), justify=tk.CENTER)
c_period['values'] = period_values
c_period.current(0)
c_period.grid(row=1, column=4, padx=5)

#labels using grid
for i, label_text in enumerate(labels):
    label = tk.Label(frame_body, text=label_text, font=('Arial 9 bold'), bg='#FAFAFA', foreground='#7E30E1')  # Change 'fg' to 'foreground'
    label.grid(row=2, column=i+1)

#activate button
activate_button = tk.Button(frame_body, text="Activate", font=('Arial 10 bold'), command=activate_alarm, bg='#4CAF50', fg='#ffffff', relief='flat')
activate_button.grid(row=3, column=1, columnspan=2, pady=10)

# deactivate button
deactivate_button = tk.Button(frame_body, text="Deactivate", font=('Arial 10 bold'), command=deactivate_alarm, bg='#FF5722', fg='#ffffff', relief='flat')
deactivate_button.grid(row=3, column=3, columnspan=2, pady=10)

window.mainloop()
