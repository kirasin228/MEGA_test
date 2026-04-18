import tkinter as tk
from docx import Document

def cr():
    doc = Document()
    doc.save(name.get()+'.docx')
def create_second_window(parent):
    # Создаем окно уровня Toplevel
    win = tk.Toplevel(parent)
    win.title("Второе окно (функция)")
    win.geometry("300x200")

    # Делаем его зависимым от главного (закроется вместе с ним)
    win.transient(parent)

    # Добавляем элементы

    btn_close = tk.Button(win, text="Закрыть", command=win.destroy)
    btn_close.place(x = 20, y = 180)
    name = tk.Entry(win, width=40)
    name.place(x=20)


    # Возвращаем объект окна (не обязательно, но полезно)
    return win
