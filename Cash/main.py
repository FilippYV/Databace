import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from add import Ui_Add_user
from Databace_gui import Ui_MainWindow


def Create_Bace_if_Data():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Dean(
        NameFaculty TEXT PRIMARY KEY,
        Room TEXT,
        Corps TEXT,
        Telephone TEXT,
        NameDean TEXT 
        )""")
    Base_of_data.commit()


# def open_add_ser_window():
#     global Add_user
#     Add_user = QtWidgets.QMainWindow()
#     uia = Ui_Add_user()
#     uia.setupUi(Add_user)
#     Add_user.show()
#     uia.pushButton.clicked.connect()

def open_add_ser_window():
        Add_text = QMessageBox
        Add_text.setText('Добавление')
        # Add_text.setGeometry(221, 283)
        Add_text.NameFaculty = QtWidgets.QDialog
        Add_text.Room = QtWidgets.QDialog
        Add_text.Corps = QtWidgets.QDialog
        Add_text.Telephone = QtWidgets.QDialog
        Add_text.NameDean = QtWidgets.QDialog
        Add_text.Button = QtWidgets.QDialog

        # Add_text.NameFaculty.setPlaceholderText("Факультет")
        # Add_text.Room.setPlaceholderText("Aудитория")
        # Add_text.Corps.setPlaceholderText("Корпус")
        # Add_text.Telephone.setPlaceholderText("Контактный телефон")
        # Add_text.NameDean.setPlaceholderText("Фамилия декана")
        # Add_text.pushButton.setText("ADD")



if __name__ == '__main__':
    Base_of_data = sqlite3.connect('Data_bace_deans_office.bd')
    cursor = Base_of_data.cursor()
    Create_Bace_if_Data()


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.button_add_user.clicked.connect(open_add_ser_window)


    Base_of_data.close()
    sys.exit(app.exec_())

