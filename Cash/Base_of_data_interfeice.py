from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_window = QtWidgets.QListView(self.centralwidget)
        self.output_window.setGeometry(QtCore.QRect(10, 218, 620, 291))
        self.output_window.setObjectName("output_window")
        self.add_user = QtWidgets.QPushButton(self.centralwidget)
        self.add_user.setGeometry(QtCore.QRect(10, 30, 200, 50))
        self.add_user.setObjectName("add_user")
        self.del_user = QtWidgets.QPushButton(self.centralwidget)
        self.del_user.setGeometry(QtCore.QRect(10, 90, 200, 50))
        self.del_user.setObjectName("del_user")
        self.sort_user = QtWidgets.QPushButton(self.centralwidget)
        self.sort_user.setGeometry(QtCore.QRect(220, 90, 200, 50))
        self.sort_user.setObjectName("sort_user")
        self.add_from_file = QtWidgets.QPushButton(self.centralwidget)
        self.add_from_file.setGeometry(QtCore.QRect(430, 30, 200, 50))
        self.add_from_file.setObjectName("add_from_file")
        self.vrite_ty_file = QtWidgets.QPushButton(self.centralwidget)
        self.vrite_ty_file.setGeometry(QtCore.QRect(430, 90, 200, 50))
        self.vrite_ty_file.setObjectName("vrite_ty_file")
        self.search_user = QtWidgets.QPushButton(self.centralwidget)
        self.search_user.setGeometry(QtCore.QRect(220, 30, 200, 50))
        self.search_user.setObjectName("search_user")
        self.input_str = QtWidgets.QListView(self.centralwidget)
        self.input_str.setGeometry(QtCore.QRect(10, 160, 621, 41))
        self.input_str.setObjectName("input_str")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_user.setText(_translate("MainWindow", "Добавить пользователя"))
        self.del_user.setText(_translate("MainWindow", "Удалить пользователя"))
        self.sort_user.setText(_translate("MainWindow", "Сортировать"))
        self.add_from_file.setText(_translate("MainWindow", "Скопировать базу данных из файла"))
        self.vrite_ty_file.setText(_translate("MainWindow", "Записать базу данных в файл"))
        self.search_user.setText(_translate("MainWindow", "Найти пользователя"))


    def add_function(self):
        self.add_user.clicked.connect(lambda: self.write_down_the_database)

    def write_down_the_database(self, data):
        cursor.execute("INSERT INTO Students VALUES ()")



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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    Base_of_data = sqlite3.connect('Data_bace_Students.bd')
    cursor = Base_of_data.cursor()
    Create_Bace_if_Data()

    Base_of_data.close()
