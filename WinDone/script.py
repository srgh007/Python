from datetime import date, datetime, timedelta
from tkinter import *
from tkinter import messagebox, ttk

# import datetime
import psycopg2
import psycopg2.extras
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry

connect_dict = dict(
    dbname="strength", user="postgres", password="postgres", host="localhost"
)

conn = psycopg2.connect(
    dbname="strength", user="postgres", password="postgres", host="localhost"
)

cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("SELECT * FROM tasks order by title")

records = cursor.fetchall()

cursor.close()
conn.close()

db_task_list = {}  # СПИСОК ЗАПЛАНИРОВАННЫХ ТАСКОВ


def get_tasks(data=datetime.now(), dblist=db_task_list):
    dblist.clear()
    selsql = "SELECT public.tasks.title , id_task, created_at, plan_date, is_done FROM public.queue_tasks join public.tasks on (public.queue_tasks.id_task = public.tasks.id) where plan_date ='{}';".format(
        data.strftime("%Y-%m-%d")
    )
    print(selsql)
    conn3 = psycopg2.connect(
        dbname="strength", user="postgres", password="postgres", host="localhost"
    )
    cursor3 = conn3.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor3.execute(selsql)
    records = cursor3.fetchall()
    for row in records:
        dblist[row["title"]] = dict(
            id_task=row["id_task"],
            plan_date=row["plan_date"],
            is_done=row["is_done"],
            title=row["title"],
        )
    # print(list(dblist))
    cursor3.close()
    conn3.close()


get_tasks()


def update_tasks_view(treeview_element):
    tmplist = []
    for tsk in db_task_list:
        db = db_task_list[tsk]["plan_date"]
        tmplist.append((f"{tsk}", f"{db}"))
    print(tmplist)
    for t in tmplist:
        treeview_element.insert("", END, values=t)


def add_task_in_view(treeview_element, tskname, tskdate):
    tmplist = ()
    tmplist = (f"{tskname}", f"{tskdate}")
    treeview_element.insert("", END, values=tmplist)  # type: ignore


# print(db_task_list[tsk]["plan_date"])


# print(list(db_task_list))

db = {}  # СЛОВАРЬ ДЛЯ СПИСКА ТАСКОВ

for row in records:
    db[row["title"]] = dict(title=row["title"], id=row["id"])
    # listTID.append(dict(title=row["title"], id=row["id"]))

    # list1.append(row["title"])
# type: ignore    print()

print(db["Domino with Max"]["id"])  # КАК БЫСТРО ПОЛУЧИТЬ ID
# print(list(db))


# def findID(key):
#     for ltid in listTID:
#         if ltid["title"] == key:
#             return ltid["id"]


# print([n["title"] for n in listTID])
# print("{} {} ".format("Domino with Max ", findID("Domino with Max")))

root = Tk()
root.title("Органайзер")
root.iconbitmap("WinDone\\process.ico")
# root.geometry("600x400+200+200")

window_height = 400
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
# for c in range(3):
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
# root.columnconfigure(2, weight=1)
# for r in range(10):
# root.rowconfigure(index=r, weight=1)

original = Image.open("WinDone\\process.png")
resized = original.resize((30, 30), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(resized)
Llogo = Label(root, image=img)
Llogo.grid(row=0, column=0, ipadx=3, ipady=3, padx=3, pady=3, sticky=W)
Llogo["bg"] = "#4682B4"

nowlabel = datetime.now().strftime("%d.%m.%Y г.")

L1 = Label(root, text="{}".format(nowlabel), font=("times new roman", 16))
L1.grid(row=0, column=1, sticky=EW, columnspan=2)
# L1.place(x=10, y=10, width=100)
L1["bg"] = "#4682B4"

toPlanLabel = "Задача"

L2 = Label(root, text="{}".format(toPlanLabel), font=("times new roman", 16, "bold"))
L2.grid(row=1, column=0, ipadx=3, ipady=3, padx=3, pady=3, sticky=E)
# L1.place(x=10, y=10, width=100)
L2["bg"] = "#4682B4"

taskInform = ""

L3 = Label(root, text="{}".format(taskInform), font=("times new roman", 16, "bold"))
L3.grid(row=3, ipadx=3, ipady=3, padx=3, pady=3, sticky=EW, columnspan=4)
# L1.place(x=10, y=10, width=100)
L3["bg"] = "#4682B4"

combobox = ttk.Combobox(values=list(db), state="readonly", font=("Arial", 12, "bold"))

# edit = Entry(root, bd=5)
combobox.grid(
    row=1, column=1, ipadx=6, ipady=6, padx=6, pady=6, sticky=EW, columnspan=3
)


def clicked():
    if combobox.get() == "":
        var = messagebox.showerror("Внимание!", "Задача не выбрана!")
    # var = messagebox.Message("Title", "Your question goes here?")


# btn = ttk.Button(root, text="OK", command=clicked)
# # type: ignore

# btn.grid(row=1, column=2, ipadx=6, ipady=6, padx=6, pady=6, sticky=EW)


# top = Toplevel(root)


def insert_data(id, data):
    inssql = "INSERT INTO public.queue_tasks (id_task, created_at, plan_date, is_done) VALUES({}, now(), '{}', false);".format(
        id,
        data,
    )
    print(inssql)
    conn2 = psycopg2.connect(
        dbname="strength", user="postgres", password="postgres", host="localhost"
    )
    cursor2 = conn2.cursor()
    cursor2.execute(inssql)
    conn2.commit()
    cursor2.close()
    conn2.close()
    get_tasks()
    # update_tasks_view(tree)


def view_calendar():
    if combobox.get() == "":
        var = messagebox.showerror("Внимание!", "Задача не выбрана!")
        return

    def print_sel():
        print(cal.selection_get())
        if combobox.get() == "":
            var = messagebox.showerror("Внимание!", "Задача не выбрана!")
            top.destroy()
        else:
            dt = datetime.now()
            dt = cal.selection_get()
            # if type(dt) == type(datetime):
            if dt != None:
                L3["text"] = 'Задача "{}" запланирована на {}'.format(
                    combobox.get(), dt.strftime("%d.%m.%Y г.")
                )
            insert_data(db[combobox.get()]["id"], dt)
            get_tasks()
            add_task_in_view(tree, combobox.get(), dt)
            # update_tasks_view(tree)
        top.destroy()

    top = Toplevel(root)
    cal = Calendar(
        top,
        font="Arial 14",
        selectmode="day",
        cursor="hand1",
        year=datetime.now().year,
        month=datetime.now().month,
        day=datetime.now().day,
    )
    top.geometry(
        "{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)
    )
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()


def print_date(n=True):
    if combobox.get() == "":
        var = messagebox.showerror("Внимание!", "Задача не выбрана!")
        return
    dt = date.today()
    if not n:
        dt = date.today() + timedelta(days=1)
        # top.destroy()

        # dt = datetime.now()
        # dt = cal.selection_get()
    L3["text"] = 'Задача "{}" запланирована на {} [{}]'.format(
        combobox.get(), dt.strftime("%d.%m.%Y г."), db[combobox.get()]["id"]
    )
    insert_data(db[combobox.get()]["id"], dt)
    add_task_in_view(tree, combobox.get(), dt)


columns = ("Task", "Data Start")

style = ttk.Style(root)
# set ttk theme to "clam" which support the fieldbackground option
style.theme_use("clam")
style.configure(
    "Treeview",
    background="#4682B4",
    fieldbackground="silver",
    foreground="black",
)

# style.configure("Button", font=("Helvetica", 12))


tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Task", text="Задача")
tree.heading("Data Start", text="Плановая дата")
tree.grid(row=5, column=0, sticky="ew", columnspan=4)

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
tree["yscrollcommand"] = scrollbar.set
# type: ignore
scrollbar.grid(
    row=5,
    column=4,
    sticky="ns",
)

update_tasks_view(tree)

s = ttk.Style()
s.configure("my.TButton", font=("Helvetica", 12))

L4 = Label(root, text="Запланировать", font=("times new roman", 16, "bold"))
L4.grid(row=2, column=0, ipadx=3, ipady=3, padx=3, pady=3, sticky=E)
# L1.place(x=10, y=10, width=100)
L4["bg"] = "#4682B4"

btn2 = ttk.Button(root, text="Календарь", command=view_calendar, style="my.TButton")
btn2.grid(row=2, column=3, ipadx=6, ipady=6, padx=6, pady=6, sticky=EW)

btn3 = ttk.Button(root, text="Сегодня", command=print_date, style="my.TButton")
btn3.grid(row=2, column=1, ipadx=6, ipady=6, padx=6, pady=6, sticky=EW)

btn4 = ttk.Button(
    root,
    text="Завтра",
    command=lambda: print_date(False),
    style="my.TButton",
)
btn4.grid(row=2, column=2, ipadx=6, ipady=6, padx=6, pady=6, sticky=EW)
root.mainloop()
