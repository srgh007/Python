from datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk

import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    dbname="strength", user="postgres", password="postgres", host="localhost"
)

cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("SELECT * FROM tasks LIMIT 10")

records = cursor.fetchall()

list1 = []

for row in records:
    list1.append(row["title"])
# type: ignore    print()

cursor.close()
conn.close()

root = Tk()
root.title("Органайзер")
root.iconbitmap("WinDone\\process.ico")
# root.geometry("600x400+200+200")

window_height = 300
window_width = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
# type: ignore
root.geometry(
    "{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)
)
# root.config(bg="blue")
root["bg"] = "#4682B4"
root.resizable(False, False)
for c in range(3):
    root.columnconfigure(index=c, weight=1)
for r in range(10):
    root.rowconfigure(index=r, weight=1)

firstLabel = datetime.now().strftime("=== %Y-%m-%d %H:%M ===")

L1 = Label(root, text="{}".format(firstLabel), font=("times new roman", 20))
L1.grid(row=0, column=0, ipadx=6, ipady=6, padx=6, pady=6, sticky=N, columnspan=2)
# L1.place(x=10, y=10, width=100)
L1["bg"] = "#4682B4"

secondLabel = "Поставить задачу в план"

L2 = Label(root, text="{}".format(secondLabel), font=("times new roman", 18, "bold"))
L2.grid(row=1, column=0, ipadx=6, ipady=6, padx=6, pady=6, sticky=E)
# L1.place(x=10, y=10, width=100)
L2["bg"] = "#4682B4"

combobox = ttk.Combobox(values=list1)

# edit = Entry(root, bd=5)
combobox.grid(row=1, column=1, ipadx=6, ipady=6, padx=6, pady=6, sticky=EW)


def clicked():
    print("")
    # var = messagebox.askyesno("Title", "Your question goes here?")


btn = ttk.Button(root, text="OK", command=clicked)
# type: ignore

btn.grid(row=1, column=2, ipadx=6, ipady=6, padx=6, pady=6, sticky=EW)


root.mainloop()
