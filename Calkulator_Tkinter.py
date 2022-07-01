# Main window

import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file='game.png')
win.iconphoto(False, photo)
win.config(bg='#A9F6C3')
win.title('Graphics application')
win.geometry("500x600+10+10")  # Size of screen and screen position +10+10
win.minsize(300, 400)  # Minsize of screen
win.maxsize(700, 800)  # Maxsize of screen
win.resizable(False, False)  # The ability to change th size of the window (width, height True or False)


win.mainloop()
