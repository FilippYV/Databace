import re

import mysql.connector
from mysql.connector import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


def create_connection_mysql_db():
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host="localhost",  # your host, usually localhost
            port="3306",
            user="root",  # your username
            passwd="1111",  # your password
            db="air_ticket")  # name
        print("Подключение к MySQL успешно выполнено")
    except Error as db_connection_error:
        print("Возникла ошибка: ", db_connection_error)
    return connection_db

def serch(request):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""{request}"""
    cursors.execute(create_db_sql_query)
    data = cursors.fetchall()
    conn.close()
    cursors.close()
    request = request.lower()
    print(request)
    column_name = re.findall(r'select.*?from', request)
    print(column_name)
    for i in range(len(column_name)):
        column_name[i] = column_name[i].replace('select', '')
        column_name[i] = column_name[i].replace('from', '')
        column_name[i] = column_name[i].replace('disticnt', '')
        column_name[i] = column_name[i].replace(' ', '')
    print(column_name)
    for i in range(len(column_name[0])):
        column_name[i] = column_name[i].split(',')
    print(column_name)
    print(1)
    return data, column_name


class Ui_Serch_sql(object):
    def setupUi_line(self, Serch_sql):
        Serch_sql.setObjectName("Serch_sql")
        Serch_sql.resize(525, 289)
        self.centralwidget = QtWidgets.QWidget(Serch_sql)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 11pt \"Consolas\";")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        Serch_sql.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Serch_sql)
        self.statusbar.setObjectName("statusbar")
        Serch_sql.setStatusBar(self.statusbar)

        self.retranslateUi(Serch_sql)
        QtCore.QMetaObject.connectSlotsByName(Serch_sql)

    def retranslateUi(self, Serch_sql):
        _translate = QtCore.QCoreApplication.translate
        Serch_sql.setWindowTitle(_translate("Serch_sql", "MainWindow"))
        self.label.setText(_translate("Serch_sql", "Запрос:"))
        self.pushButton_2.setText(_translate("Serch_sql", "Очистить"))
        self.pushButton.setText(_translate("Serch_sql", "Запрос"))
        self.lineEdit.setPlaceholderText("Введите свой запрос")
        self.pushButton.clicked.connect(self.serch_sql)

    def serch_sql(self):
            try:
                if self.lineEdit.text() != '':
                    data, column_name = serch(self.lineEdit.text())
                    row = len(data) + 1
                    column = len(data[0])
                    self.tableView.setRowCount(row)
                    self.tableView.setColumnCount(column)
                    for i in range(column):
                        self.tableView.setItem(0, i, QTableWidgetItem(str(column_name[i])))
                    for i in range(len(data)):
                        for j in range(len(data[i])):
                            self.tableView.setItem(i + 1, j, QTableWidgetItem(str(data[i][j])))


                else:
                    ok = QMessageBox()
                    ok.setWindowTitle("Ошибка")
                    ok.setText("Введите запрос!")
                    ok.setIcon(QMessageBox.Warning)
                    ok.setStandardButtons(QMessageBox.Ok)
                    ok.exec_()
                    print('Ошибка!!!')
            except:
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Некоректный запрос!")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                print('Ошибка!!!')
