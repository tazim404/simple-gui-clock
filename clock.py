from tkinter import Label, Tk, PhotoImage
from time import strftime
window = Tk()
window.title("Clock")
logo_image = PhotoImage(file='logo.png')
window.iconphoto(True, logo_image)
window.resizable(False, False)
label = Label(window, font=('Italic', 44), bg="Orange", fg='Black')


def run_time():
    label.configure(text=strftime('%H:%M:%S'))
    label.after(1000, run_time)


label.pack()
run_time()
window.mainloop()
