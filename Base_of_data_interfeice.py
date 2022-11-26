import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QTableWidgetItem, QVBoxLayout, QTableView

def Create_Bace_if_Data():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Deans(
        NameFaculty TEXT PRIMARY KEY,
        Room TEXT,
        Corps TEXT,
        Telephone INTEGER,
        NameDean TEXT
    )""")
    Base_of_data.commit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_window = QtWidgets.QLabel(self.centralwidget)
        self.centralwidget.setStyleSheet("background-color: 153,153,153")
        self.output_window.setGeometry(QtCore.QRect(10, 130, 620, 100))
        self.output_window.setObjectName("output_window")
        self.output_window.show()

        self.output_windows = QtWidgets.QListView(self.centralwidget)
        self.output_windows.setGeometry(QtCore.QRect(10, 300, 620, 350))
        self.output_windows.setObjectName("output_window")
        self.output_windows.show()

        self.output_window.setAlignment(Qt.AlignTop)
        self.add_user = QtWidgets.QPushButton(self.centralwidget)
        self.add_user.setGeometry(QtCore.QRect(10, 30, 200, 25))
        self.add_user.setObjectName("add_user")
        self.del_user = QtWidgets.QPushButton(self.centralwidget)
        self.del_user.setGeometry(QtCore.QRect(10, 55, 200, 25))
        self.del_user.setObjectName("del_user")
        self.sort_user = QtWidgets.QPushButton(self.centralwidget)
        self.sort_user.setGeometry(QtCore.QRect(220, 55, 200, 25))
        self.sort_user.setObjectName("sort_user")
        self.add_from_file = QtWidgets.QPushButton(self.centralwidget)
        self.add_from_file.setGeometry(QtCore.QRect(430, 30, 200, 25))
        self.add_from_file.setObjectName("add_from_file")
        self.vrite_ty_file = QtWidgets.QPushButton(self.centralwidget)
        self.vrite_ty_file.setGeometry(QtCore.QRect(430, 55, 200, 25))
        self.vrite_ty_file.setObjectName("vrite_ty_file")
        self.search_user = QtWidgets.QPushButton(self.centralwidget)
        self.search_user.setGeometry(QtCore.QRect(220, 30, 200, 25))
        self.search_user.setObjectName("search_user")
        self.input_str = QtWidgets.QLineEdit(self.centralwidget)
        self.input_str.setGeometry(QtCore.QRect(10, 110, 621, 20))
        self.input_str.setObjectName("input_str")
        self.input_str.hide()

        self.button_print = QtWidgets.QPushButton(self.centralwidget)
        self.button_print.setGeometry(QtCore.QRect(10, 80, 200, 25))
        self.button_print.setObjectName("button_print")
        self.button_print.hide()

        self.statusbar = QtWidgets.QLabel(self.centralwidget)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setGeometry(QtCore.QRect(5, 10, 200, 15))
        self.commit = QtWidgets.QPushButton(self.centralwidget)
        self.commit.setObjectName("commit")
        self.commit.hide()
        self.commit.setGeometry(QtCore.QRect(10, 30, 200, 25))
        self.commit_del = QtWidgets.QPushButton(self.centralwidget)
        self.commit_del.setObjectName("commit_del")
        self.commit_del.hide()
        self.commit_del.setGeometry(QtCore.QRect(10, 55, 200, 25))
        self.commit_find = QtWidgets.QPushButton(self.centralwidget)
        self.commit_find.setObjectName("commit_find")
        self.commit_find.hide()
        self.commit_find.setGeometry(QtCore.QRect(220, 30, 200, 25))
        self.canceled_button = QtWidgets.QPushButton(self.centralwidget)
        self.canceled_button.setObjectName("out_button")
        self.commit_find.hide()
        self.canceled_button.setGeometry(QtCore.QRect(10, 80, 310, 25))
        self.commit_find = QtWidgets.QPushButton(self.centralwidget)
        self.commit_find.setObjectName("commit_find")
        self.commit_find.hide()

        self.button_print_window = QtWidgets.QPushButton(self.centralwidget)
        self.button_print_window.setGeometry(QtCore.QRect(320, 80, 310, 25))
        self.button_print_window.setObjectName("add_from_file")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 620, 500))
        self.tableWidget.setStyleSheet("background-color: 105,105,105")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.commit_find.setGeometry(QtCore.QRect(270, 4, 100, 25))
        MainWindow.setCentralWidget(self.centralwidget)

        # self.out.clicked.conect(self.Output_window)
        self.add_user.clicked.connect(self.Metod_add)  # --------------------
        self.commit.clicked.connect(self.commit_add)
        self.commit_del.clicked.connect(self.del_of_base)
        self.del_user.clicked.connect(self.commit_dell)
        self.search_user.clicked.connect(self.serch_find)
        self.commit_find.clicked.connect(self.metod_find)
        self.sort_user.clicked.connect(self.fun_sor_user)
        self.add_from_file.clicked.connect(self.add_from_file_fun)
        self.vrite_ty_file.clicked.connect(self.out_from_file_fun)
        self.canceled_button.clicked.connect(self.canceled_button_fun)
        self.button_print.clicked.connect(self.print_data_base)
        self.button_print_window.clicked.connect(self.print_table_in_window)
        self.retranslateUi(MainWindow)
        # self.del_user.clicked.conecet(self.)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_str.setPlaceholderText("Введите данные")
        self.add_user.setText(_translate("MainWindow", "Добавить пользователя"))
        self.commit.setText(_translate("MainWindow", "Подтвердить"))
        self.del_user.setText(_translate("MainWindow", "Удалить пользователя"))
        self.sort_user.setText(_translate("MainWindow", "Сортировать"))
        self.add_from_file.setText(_translate("MainWindow", "Записать базу данных в файл"))
        self.vrite_ty_file.setText(_translate("MainWindow", "Записать базу данных из файла"))
        self.search_user.setText(_translate("MainWindow", "Найти пользователя"))
        self.button_print_window.setText('Вывод таблицы в окне')
        self.button_print.setText('Вывод таблицы')
        self.statusbar.setText("Ожидание функций...")
        self.canceled_button.setText("Отменить")
        self.commit_del.setText("Подтвердить")
        self.commit_find.setText("Подтвердить")
        # self.tableWidget.show()

    def canceled_button_fun(self):
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.commit.hide()
        self.commit_find.hide()
        # self.commit.hide()
        self.retranslateUi(MainWindow)




    def Metod_add(self):
        self.input_str.show()
        self.statusbar.setGeometry(QtCore.QRect(5, 10, 500, 15))
        self.statusbar.setText(f"Выполнения функции добавления!")
        self.output_window.setText(f"Введите данные через запятую: Факультет, Aудитория, Корпус,"
                                   f" Контактный телефон, Фамилия декана")
        self.commit.show()
        self.commit.setGeometry(QtCore.QRect(10, 30, 200, 25))
        self.commit.setObjectName("commit")
        x = []
        # self.print_in_lable()

    def commit_add(self):
        data = self.input_str.text()
        data = data.replace(' ', '')
        data = data.split(',')
        if len(data[0]) == 0 or len(data[1]) == 0 or \
                len(data[2]) == 0 or len(data[3]) == 0 or \
                len(data[4]) == 0:
            return
        cursor.execute(f'SELECT NameFaculty FROM Deans WHERE NameFaculty="{data[0]}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO Deans VALUES ("{data[0]}", "{data[1]}", '
                           f'"{data[2]}", "{data[3]}", "{data[4]}")')
            self.statusbar.setText(f'Функция добавления выполнена!!!')
            Base_of_data.commit()
            self.commit_del.setGeometry(QtCore.QRect(10, 55, 200, 25))
            self.output_window.setText(f'Факультет {data[0]} успешно внесён в базу данных!\n'
                                       f"Факультет: {data[0]}; Аудитория: {data[1]}; "
                                       f"Корпус: {data[2]}; Номер телефона: {data[3]} "
                                       f"Фамилия: {data[4]}.")
        else:
            self.output_window.setText('Такая записать уже имеется!')
        self.print_table_in_window()
        self.commit.hide()
        self.input_str.hide()



    def commit_dell(self):
        self.input_str.show()
        self.statusbar.setText('Выполение функции удаления!')
        self.output_window.setText("Введите для удаления: Факультет")
        self.commit_del.setObjectName("commit_del")
        self.commit_del.show()
        self.commit_del.setGeometry(QtCore.QRect(10, 55, 200, 25))

    def del_of_base(self):
        delit_el = self.input_str.text()
        cursor.execute(f"DELETE FROM Deans WHERE NameFaculty = '{delit_el}'")
        # print("hello world")
        Base_of_data.commit()
        self.output_window.setText(f'Факультет {delit_el} удалён!')
        # self.commit_del.setGeometry(QtCore.QRect(270, 4, 100, 25))
        self.commit_del.hide()
        self.input_str.hide()

    def metod_find(self):
        self.output_window.show()
        find = self.input_str.text()
        for NameFaculty in cursor.execute(f"SELECT * FROM Deans WHERE NameFaculty == '{str(find)}'"):
            for i in NameFaculty:
                if i == find:
                    self.output_window.setText(f'Факультет {find} найден!\n'
                                               f"Факультет: {str(NameFaculty[0])};"
                                                f" Аудитория: {str(NameFaculty[1])}; "
                                               f"Корпус: {str(NameFaculty[2])}; "
                                                f"Номер телефона: {str(NameFaculty[3])}; "
                                               f"Фамилия: {str(NameFaculty[4])}."
                                               )
                    break
            else:
                self.output_window.setText(f'В базе нет факультета: {find}'
                                           f'')

        self.commit_find.hide()
        # self.input_str.hide()

    def serch_find(self):
        self.input_str.show()
        self.statusbar.setText('Выполение функции поиска!')
        self.output_window.setText("Введите для поиска: Факультет")
        self.commit_find.show()
        self.commit_find.setGeometry(QtCore.QRect(220, 30, 200, 25))


    def fun_sor_user(self):
        x = []
        for Deans in cursor.execute(f"SELECT * FROM Deans"):
            x.append(Deans)
        ONE_STR = []
        for j in range(len(x)):
            for i in range(len(x) - 1):
                if x[i][0] > x[i + 1][0]:
                    x[i], x[i + 1] = x[i + 1], x[i]
        cursor.execute(f"DELETE FROM Deans WHERE NameFaculty != '0'")
        for i in range(len(x)):
            cursor.execute(f'INSERT INTO Deans VALUES ("{x[i][0]}", "{x[i][1]}", '
                           f'"{x[i][2]}", "{x[i][3]}", "{x[i][4]}")')
        self.output_window.setText("База данных отсортирована по ключу")
        Base_of_data.commit()

    def add_from_file_fun(self):
        x = []
        for Deans in cursor.execute(f"SELECT * FROM Deans"):
            x.append(Deans)
        myfile = open('Base.txt', 'w')
        for i in x:
            myfile.write(str(i) + '\n')
        myfile.close()
        self.output_window.show()
        self.output_window.setText("База записана в txt файл")


    def out_from_file_fun(self):
        f = open('Base_new.txt', 'r')
        try:
            x = f.readlines()
            for i in range(len(x)):
                x[i] = x[i].replace('\n', '')
                x[i] = x[i].replace(';', '')
                x[i] = x[i].split(',')
            Y = []
            cursor.execute(f"DELETE FROM Deans WHERE NameFaculty != '0'")
            Base_of_data.commit()
            for i in range(len(x)):
                if len(x[i]) == 5:
                    cursor.execute(f'INSERT INTO Deans VALUES ("{x[i][0]}", "{x[i][1]}", '
                                   f'"{x[i][2]}", "{x[i][3]}", "{x[i][4]}")')
                    self.output_window.setText("База записана из txt файла")
                else:
                    self.output_window.setText("Ошибка записи из файла!!!")
                    break
            Base_of_data.commit()
        finally:
            f.close()

    def print_data_base(self):
        x = []
        for Deans in cursor.execute(f"SELECT * FROM Deans"):
            x.append(Deans)
        maxdistance = 0
        for i in x:
            for j in i:
                if type(j) is str and len(j) > maxdistance:
                    maxdistance = len(j)
        text = ''
        text += 150 * '-'
        text += '\n'
        for i in range(len(x)):
            text += (f"| Факультет: {x[i][0]} | Аудитория: {x[i][1]} | "
                     f"Корпус: {x[i][2]} | Номер телефона: {x[i][3]} |"
                     f"Фамилия: {x[i][4]} |\n")
            text += 150 * '-'
            text += '\n'
        self.output_window.show()
        self.output_window.setText(text)

    def print_table_in_window(self):
        x = []
        for Deans in cursor.execute(f"SELECT * FROM Deans"):
            x.append(Deans)
        row = len(x) + 1
        column = 5
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(column)
        self.tableWidget.setItem(500, 600, QTableWidgetItem("Databace"))
        self.tableWidget.setItem(0,  0, QTableWidgetItem('Факультет'))
        self.tableWidget.setItem(0,  1, QTableWidgetItem('Аудитория'))
        self.tableWidget.setItem(0,  2, QTableWidgetItem('Корпус'))
        self.tableWidget.setItem(0,  3, QTableWidgetItem('Номер телефона'))
        self.tableWidget.setItem(0,  4, QTableWidgetItem('Фамилия'))
        for i in range(len(x)):
            for j in range(len(x[i])):
                self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(x[i][j])))
                self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(x[i][j])))
                self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(x[i][j])))
                self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(x[i][j])))
                self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(x[i][j])))
        self.tableWidget.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    Base_of_data = sqlite3.connect('Data_bace_Students.db')
    cursor = Base_of_data.cursor()
    Create_Bace_if_Data()
    sys.exit(app.exec_())
