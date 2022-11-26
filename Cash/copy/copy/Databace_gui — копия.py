from PyQt5 import QtCore, QtGui, QtWidgets


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





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
