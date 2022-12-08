from tkinter import *

root = Tk()
root.title("Органайзер")
root.iconbitmap("WinDone\\process.ico")
# root.geometry("600x400+200+200")

window_height = 500
window_width = 900

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry(
    "{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)
)


root.resizable(False, False)
root.mainloop()
