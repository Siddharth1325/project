from tkinter import Tk, Label
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # Update every 1000 milliseconds (1 second)

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")

label = Label(window, font=("Arial Black", 78, "bold"), bg="steelblue", fg="white")
label.pack(pady=100)

time()  # Start the clock
window.mainloop()