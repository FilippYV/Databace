from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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
        self.any_fucksion()
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


    # def write_down_the_database(self, data):
    #     cursor.execute("INSERT INTO Students VALUES ()")

    def any_fucksion(self):
        self.add_user.clicked.connect(self.add_function())

    # def add_add(self):

    # def add_function(self):
    #     Add_user = QtWidgets.QMainWindow()
    #     uia = add_add()
    #     uia.setupUi_sort(Add_user)
    #     Add_user.show()
    #     button_one = QMessageBox()
    #     button_one.resize(221, 283)
    #     button_one.setWindowTitle("ADD USERS")
    #     self.centralwidget = QtWidgets.QWidget(Add_user)
    #     self.centralwidget.setObjectName("centralwidget")
    #     self.NameFaculty = QtWidgets.QLineEdit(self.centralwidget)
    #     self.NameFaculty.setGeometry(QtCore.QRect(10, 40, 200, 30))
    #     font = QtGui.QFont()
    #     font.setPointSize(10)
    #     self.NameFaculty.setFont(font)
    #     self.NameFaculty.setText("")
    #     self.NameFaculty.setMaxLength(25)
    #     self.NameFaculty.setEchoMode(QtWidgets.QLineEdit.Normal)
    #     self.NameFaculty.setCursorPosition(0)
    #     self.NameFaculty.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    #     self.NameFaculty.setDragEnabled(False)
    #     self.NameFaculty.setObjectName("NameFaculty")
    #     self.label = QtWidgets.QLabel(self.centralwidget)
    #     self.label.setGeometry(QtCore.QRect(10, 0, 200, 30))
    #     font = QtGui.QFont()
    #     font.setPointSize(12)
    #     self.label.setFont(font)
    #     self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    #     self.label.setFrameShape(QtWidgets.QFrame.Box)
    #     self.label.setFrameShadow(QtWidgets.QFrame.Plain)
    #     self.label.setAlignment(QtCore.Qt.AlignCenter)
    #     self.label.setObjectName("label")
    #     self.pushButton = QtWidgets.QPushButton(self.centralwidget)
    #     self.pushButton.setGeometry(QtCore.QRect(20, 240, 75, 23))
    #     self.pushButton.setObjectName("pushButton")
    #     self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
    #     self.pushButton_2.setGeometry(QtCore.QRect(120, 240, 75, 23))
    #     self.pushButton_2.setObjectName("pushButton_2")
    #     self.Room = QtWidgets.QLineEdit(self.centralwidget)
    #     self.Room.setGeometry(QtCore.QRect(10, 80, 200, 30))
    #     font = QtGui.QFont()
    #     font.setPointSize(10)
    #     self.Room.setFont(font)
    #     self.Room.setText("")
    #     self.Room.setMaxLength(25)
    #     self.Room.setEchoMode(QtWidgets.QLineEdit.Normal)
    #     self.Room.setCursorPosition(0)
    #     self.Room.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    #     self.Room.setDragEnabled(False)
    #     self.Room.setObjectName("Room")
    #     self.Corps = QtWidgets.QLineEdit(self.centralwidget)
    #     self.Corps.setGeometry(QtCore.QRect(10, 120, 200, 30))
    #     font = QtGui.QFont()
    #     font.setPointSize(10)
    #     self.Corps.setFont(font)
    #     self.Corps.setText("")
    #     self.Corps.setMaxLength(25)
    #     self.Corps.setEchoMode(QtWidgets.QLineEdit.Normal)
    #     self.Corps.setCursorPosition(0)
    #     self.Corps.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    #     self.Corps.setDragEnabled(False)
    #     self.Corps.setObjectName("Corps")
    #     self.Telephone = QtWidgets.QLineEdit(self.centralwidget)
    #     self.Telephone.setGeometry(QtCore.QRect(10, 160, 200, 30))
    #     font = QtGui.QFont()
    #     font.setPointSize(10)
    #     self.Telephone.setFont(font)
    #     self.Telephone.setText("")
    #     self.Telephone.setMaxLength(25)
    #     self.Telephone.setEchoMode(QtWidgets.QLineEdit.Normal)
    #     self.Telephone.setCursorPosition(0)
    #     self.Telephone.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    #     self.Telephone.setDragEnabled(False)
    #     self.Telephone.setObjectName("Telephone")
    #     self.NameDean = QtWidgets.QLineEdit(self.centralwidget)
    #     self.NameDean.setGeometry(QtCore.QRect(10, 200, 200, 30))
    #     font = QtGui.QFont()
    #     font.setPointSize(10)
    #     self.NameDean.setFont(font)
    #     self.NameDean.setText("")
    #     self.NameDean.setMaxLength(25)
    #     self.NameDean.setEchoMode(QtWidgets.QLineEdit.Normal)
    #     self.NameDean.setCursorPosition(0)
    #     self.NameDean.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    #     self.NameDean.setDragEnabled(False)
    #     self.NameDean.setObjectName("NameDean")
    #     Add_user.setCentralWidget(self.centralwidget)
    #     self.statusbar = QtWidgets.QStatusBar(Add_user)
    #     self.statusbar.setObjectName("statusbar")
    #     Add_user.setStatusBar(self.statusbar)
    #
    #     self.retranslateUi(Add_user)
    #     QtCore.QMetaObject.connectSlotsByName(Add_user)
    #     button_one.setStandardButtons(QtWidgets.QLineEdit(self.NameFaculty))
    #
    #     button_one.exec_()







# def Create_Bace_if_Data():
#     cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
#         Id_studenta TEXT PRIMARY KEY,
#         Fam TEXT,
#         Name TEXT,
#         Groupa TEXT,
#         Department TEXT,
#         discipline TEXT,
#         mark INTEGER,
#         NameTeacher TEXT
#     )""")
#     Base_of_data.commit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    # Base_of_data = sqlite3.connect('Data_bace_Students.bd')
    # cursor = Base_of_data.cursor()
    # Create_Bace_if_Data()
    #
    # Base_of_data.close()
