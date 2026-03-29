import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Clock with Date")

def time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%A, %d %B %Y')
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    time_label.after(1000, time)

time_label = tk.Label(root, font=('calibri', 40, 'bold'),
                      background='black', foreground='white')
time_label.pack()

date_label = tk.Label(root, font=('calibri', 20),
                      background='black', foreground='white')
date_label.pack()

time()
root.mainloop()