from tkinter import *
import tkinter as tk
import sqlite3


# def reg():
#     NameFaculty
#     Room = self.Room.text()
#     Corps = self.Corps.text()
#     Telephone = self.Telephone.text()
#     NameDean = self.NameDean.text()
#     if len(NameFaculty) == 0 or len(Room) == 0 or \
#             len(Corps) == 0 or len(Telephone) == 0 or \
#             len(NameDean) == 0:
#         return
#     cursor.execute(f'SELECT login FROM users WHERE NameFaculty="{NameFaculty}"')
#     if cursor.fetchone() is None:
#         cursor.execute(f'INSERT INTO users VALUES ("{NameFaculty}", "{Room}", '
#                        f'"{Corps}", "{Telephone}", "{NameDean}")')
#         self.label.setText(f'Факультет {NameFaculty} успешно внесён в базу данных!')
#         Base_of_data.commit()
#     else:
#         self.label.setText('Такая записать уже имеется!')
def add_IN_bd():
    addWindow = tk.Tk()
    addWindow.title("Добавление факультета")
    addWindow.geometry("300x300+700+350")
    tk.Label(addWindow, text='Факультет').grid(row=0, column=0)
    NameFaculty = tk.Entry(addWindow).grid(row=0, column=1)
    tk.Label(addWindow, text='Aудитория').grid(row=1, column=0)
    Room = tk.Entry(addWindow).grid(row=1, column=1)
    tk.Label(addWindow, text='Корпус').grid(row=2, column=0)
    Corps = tk.Entry(addWindow).grid(row=2, column=1)
    tk.Label(addWindow, text='Контактный телефон').grid(row=3, column=0)
    Telephone = tk.Entry(addWindow).grid(row=3, column=1)
    tk.Label(addWindow, text='Фамилия декана').grid(row=4, column=0)
    NameDean = tk.Entry(addWindow).grid(row=4, column=1)
    def get():
        value = NameFaculty.get()
        print(value)
    def reg():
        global NameFaculty
        global Room
        global Corps
        global Telephone
        global NameDean
        if len(NameFaculty.get()) == 0 or len(Room) == 0 or \
                len(Corps) == 0 or len(Telephone) == 0 or \
                len(NameDean) == 0:
            return
        cursor.execute(f'SELECT login FROM users WHERE NameFaculty="{NameFaculty}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users VALUES ("{NameFaculty}", "{Room}", '
                           f'"{Corps}", "{Telephone}", "{NameDean}")')
            Base_of_data.commit()
    upload = tk.Button(addWindow, text='Добавить в базу', command=get).grid(row=5, column=1)


    addWindow.mainloop()


def main():
    mainWindow = tk.Tk()
    mainWindow.title("Интерфейс программы")
    mainWindow.geometry("900x400+300+300")
    button_add = tk.Button(
        text="Добавить факультет",
        background='#343E40',
        width=25,
        height=3,
        command=add_IN_bd
    )
    button_del_user = tk.Button(
        text="Удалить факультет",
        background='#343E40',
        width=25,
        height=3,
    )
    button_search_user = tk.Button(
        text="Найти факультет",
        background='#343E40',
        width=25,
        height=3,
    )
    button_sort_user = tk.Button(
        text="Найти факультет",
        background='#343E40',
        width=25,
        height=3,
    )
    button_add_in_file = tk.Button(
        text="Добавить базу в файл",
        background='#343E40',
        width=25,
        height=3,
    )
    button_write_is_file = tk.Button(
        text="Внести базу из файла в базу",
        background='#343E40',
        width=25,
        height=3,
    )

    button_add.grid()
    button_del_user.grid()
    button_search_user.grid()
    button_sort_user.grid()
    button_add_in_file.grid()
    button_write_is_file.grid()
    mainWindow.mainloop()


def Create_Bace_if_Data():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
        Id_studenta TEXT PRIMARY KEY,
        Fam TEXT,
        Name TEXT,
        Groupa TEXT,
        Department TEXT,
        discipline TEXT,
        mark INTEGER,
        NameTeacher TEXT
    )""")
    Base_of_data.commit()


if __name__ == '__main__':
    Base_of_data = sqlite3.connect('Data_bace_Students.bd')
    cursor = Base_of_data.cursor()
    Create_Bace_if_Data()

    main()
    Base_of_data.close()
