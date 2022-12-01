import mysql.connector
from PyQt5.QtWidgets import QMessageBox
from mysql.connector import Error
from PyQt5 import QtCore, QtGui, QtWidgets

mass_sing = ['=', '>=', '>', '<', '<=', 'like', 'not like']


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


def select_name_t(name_table, column, sing, value):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""delete from {name_table} where {column} {sing} {value};"""
    print(create_db_sql_query)
    cursors.execute(create_db_sql_query)
    otvet = cursors.fetchall()
    conn.commit()
    conn.close()
    cursors.close()
    print('dell')


def describe_table(name_table):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""describe {name_table};"""
    cursors.execute(create_db_sql_query)
    y = cursors.fetchall()
    conn.close()
    cursors.close()
    for i in range(len(y)):
        y[i] = y[i][0]
    print(y)
    return y


def show_tables():
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""show tables;"""
    cursors.execute(create_db_sql_query)
    y = cursors.fetchall()
    conn.close()
    cursors.close()
    for i in range(len(y)):
        y[i] = y[i][0]
    print(y)
    return y


def describe_table_for_search(name_table):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""describe {name_table};"""
    cursors.execute(create_db_sql_query)
    y = cursors.fetchall()
    print(y)
    conn.close()
    cursors.close()
    for i in range(len(y)):
        y[i] = y[i][0]
    print(y)
    return y


class Ui_Dell_window(object):
    def setupUi(self, Dell_window):
        Dell_window.setObjectName("Dell_window")
        Dell_window.resize(446, 600)
        self.centralwidget = QtWidgets.QWidget(Dell_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 20pt \"Consolas\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 20pt \"Consolas\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_dell = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dell.setObjectName("pushButton_dell")
        self.gridLayout.addWidget(self.pushButton_dell, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 20pt \"Consolas\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.pushButton_2_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_clear.setObjectName("pushButton_2_clear")
        self.gridLayout.addWidget(self.pushButton_2_clear, 8, 0, 1, 1)
        self.pushButton_2_clear.hide()
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 6, 0, 1, 1)
        Dell_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Dell_window)
        self.statusbar.setObjectName("statusbar")
        Dell_window.setStatusBar(self.statusbar)

        self.retranslateUi(Dell_window)
        QtCore.QMetaObject.connectSlotsByName(Dell_window)

    def retranslateUi(self, Dell_window):
        _translate = QtCore.QCoreApplication.translate
        Dell_window.setWindowTitle(_translate("Dell_window", "MainWindow"))
        self.label_2.setText(_translate("Dell_window", "TextLabel"))
        self.pushButton_dell.setText(_translate("Dell_window", "Удалить"))
        self.label_3.setText(_translate("Dell_window", "Знак"))
        self.pushButton_2_clear.setText(_translate("Dell_window", "Очистить"))

        self.label.setText(_translate("Dell_window", "Что удалить?"))
        y = show_tables()
        for i in range(len(y)):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, y[i])
        self.label_2.setText(_translate("Dell_window", "По столбцу:"))
        self.comboBox.currentIndexChanged.connect(self.output_line_to_dell)
        self.pushButton_dell.clicked.connect(self.dell_funck)
        y = show_tables()
        for i in range(len(y)):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, y[i])
        name_table = self.comboBox.currentText()
        y = describe_table_for_search(name_table)
        for i in range(len(y)):
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(i, y[i])
        for i in range(len(mass_sing)):
            self.comboBox_3.addItem("")
            self.comboBox_3.setItemText(i, mass_sing[i])

    def output_line_to_dell(self):
        self.comboBox_2.clear()
        name_table = self.comboBox.currentText()
        if name_table == '':
            y = describe_table('airline')
        else:
            y = describe_table(name_table)
        for i in range(len(y)):
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(i, y[i])
        for i in range(len(mass_sing)):
            self.comboBox_3.addItem("")
            self.comboBox_3.setItemText(i, mass_sing[i])


    def dell_funck(self):
        try:
            if self.comboBox.currentText() != '' and self.comboBox_2.currentText() != '' \
                    and self.lineEdit.text() != '':
                name_table = self.comboBox.currentText()
                column = self.comboBox_2.currentText()
                sing = self.comboBox_3.currentText()
                value = self.lineEdit.text()
                print(name_table, column, sing, value)
                select_name_t(name_table, column, sing, value)
                ok = QMessageBox()
                ok.setWindowTitle("Удаление")
                ok.setText("Вы удалили данные!")
                ok.setIcon(QMessageBox.Information)
                ok.setStandardButtons(QMessageBox.Ok)
                ok.exec_()
                print('Ошибка!!!')
            else:
                ok = QMessageBox()
                ok.setWindowTitle("Ошибка")
                ok.setText("Заполните все поля!")
                ok.setIcon(QMessageBox.Warning)
                ok.setStandardButtons(QMessageBox.Ok)
                ok.exec_()
                print('Ошибка!!!')

        except:
            print(1)
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Некоректный запрос!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            print('Ошибка!!!')