import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


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


class Add_user(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # super(Add_user, self).__init__()
        # self.setupUi(self)
        super().__init__()
        self.add_user.clicked.connect(self.show_window_2)

    def show_window_add(self):
        self.Ui_Add_user = ADD
        self.Ui_Add_user.show()


if __name__ == '__main__':
    Base_of_data = sqlite3.connect('Data_bace_Students.bd')
    cursor = Base_of_data.cursor()

    Base_of_data.close()


ADD = QtWidgets.QApplication([])
window = Add_user()
window.show()
ADD.exec()