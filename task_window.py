import tkinter as tk
from docx import Document
from tkinter import messagebox

bd = []
tas =[]

def validat(st):
    global tas
    st = str(st)
    if st.count(";")!=2:
        messagebox.showerror("Ошибка", "Выберите хотя бы одну тему!")
        return
    a, b, c = st.split(";")
    if a =="" or b =="" or c=="":
        messagebox.showerror("Ошибка", "Выберите хотя бы одну тему!")
        return
    if st not in tas:
        tas.append(st)


def cr():
    doc = Document()
    doc.save(name.get()+'.docx')
def create_task(win):
    global  bd
    E_tasks = tk.Entry(win, width=14)
    E_tasks.place(x=20,y=win.current_y)
    win.current_y+=25
    bd.append(E_tasks)
def Ok():
    global bd
    l = []
    for i in bd:
        validat(i.get())
def create_second_window(parent):
    # Создаем окно уровня Toplevel
    win = tk.Toplevel(parent)
    win.current_y=80
    win.title("Второе окно (функция)")
    win.geometry("300x200")

    # Делаем его зависимым от главного (закроется вместе с ним)
    win.transient(parent)

    # Добавляем элементы
    btn_add_task_win = tk.Button(win,text="Добавить задания",command=lambda: create_task(win))
    btn_add_task_win.place(x=150,y=70)
    name_tsk = tk.Label(win, text="Введите имя задания")
    name_tsk.place(x=20)
    btn_close = tk.Button(win, text="Закрыть", command=win.destroy)
    btn_close.place(x = 150)
    name = tk.Entry(win, width=40)
    name.place(x=20,y=40)
    btn_Ok = tk.Button(win, text="Ok",command=Ok)
    btn_Ok.place(x=230)

    # Возвращаем объект окна (не обязательно, но полезно)
    return win
