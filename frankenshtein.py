# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from add_window_code import Ui_Add_window

import mysql.connector
from mysql.connector import Error


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


def show_tables():
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""show tables;"""
    cursors.execute(create_db_sql_query)
    tables = cursors.fetchall()
    conn.close()
    cursors.close()
    for i in range(len(tables)):
        tables[i] = tables[i][0]
    return tables


def select_max_id(name_table):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""select * from {name_table};"""
    cursors.execute(create_db_sql_query)
    x = cursors.fetchall()
    conn.close()
    cursors.close()
    return x


def select_name_table(name_table):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""describe {name_table};"""
    cursors.execute(create_db_sql_query)
    y = cursors.fetchall()
    conn.close()
    cursors.close()
    return y


def select_max__id(name_table):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""select count(*) from {name_table};"""
    cursors.execute(create_db_sql_query)
    x = cursors.fetchall()
    conn.close()
    cursors.close()
    return x[0][0] + 1


def add_in_passport_user_sql(data):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    into = f"""INSERT INTO passport_user (id_passport, last_name,
       patronymic, first_name, series, number, registration) VALUES
    ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}');"""
    cursors.execute(into)
    conn.commit()
    conn.close()
    cursors.close()


def add_in_user(data):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    into = f"""INSERT INTO user (id_passport, id_user, email, phone) VALUES
        ('{data[0]}', '{data[0]}', '{data[-2]}', '{data[-1]}');"""
    cursors.execute(into)
    conn.commit()
    conn.close()
    cursors.close()


def create_new_def():
    print(1)
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = """select * from plane;"""
    cursors.execute(create_db_sql_query)
    for i in cursors.fetchall():
        print(i)
    conn.close()
    cursors.close()




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1227, 810)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setStyleSheet("")
        self.tab_widget.setObjectName("tab_widget")
        self.Airline_tab = QtWidgets.QWidget()
        self.Airline_tab.setObjectName("Airline_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Airline_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.airline_tableView = QtWidgets.QTableWidget(self.Airline_tab)
        self.airline_tableView.setStyleSheet("")
        self.airline_tableView.setObjectName("airline_tableView")
        self.gridLayout_3.addWidget(self.airline_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.Airline_tab, "")
        self.Plane_tab = QtWidgets.QWidget()
        self.Plane_tab.setObjectName("Plane_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Plane_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plane_tableView = QtWidgets.QTableWidget(self.Plane_tab)
        self.plane_tableView.setStyleSheet("")
        self.plane_tableView.setObjectName("plane_tableView")
        self.gridLayout_4.addWidget(self.plane_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.Plane_tab, "")
        self.passport_users_tab = QtWidgets.QWidget()
        self.passport_users_tab.setObjectName("passport_users_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.passport_users_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.passpor_user_tableView = QtWidgets.QTableWidget(self.passport_users_tab)
        self.passpor_user_tableView.setStyleSheet("")
        self.passpor_user_tableView.setObjectName("passpor_user_tableView")
        self.gridLayout_5.addWidget(self.passpor_user_tableView, 0, 0, 1, 1)

        self.tab_widget.addTab(self.passport_users_tab, "")
        self.users_tab = QtWidgets.QWidget()
        self.users_tab.setObjectName("users_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.users_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.users_tableView = QtWidgets.QTableWidget(self.users_tab)
        self.users_tableView.setStyleSheet("")
        self.users_tableView.setObjectName("users_tableView")
        self.gridLayout_6.addWidget(self.users_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.users_tab, "")
        self.airport_out_tab = QtWidgets.QWidget()
        self.airport_out_tab.setObjectName("airport_out_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.airport_out_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.airport_out_tableView = QtWidgets.QTableWidget(self.airport_out_tab)
        self.airport_out_tableView.setStyleSheet("")
        self.airport_out_tableView.setObjectName("airport_out_tableView")
        self.gridLayout_7.addWidget(self.airport_out_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.airport_out_tab, "")
        self.airport_in_tab = QtWidgets.QWidget()
        self.airport_in_tab.setObjectName("airport_in_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.airport_in_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.airport_in_tableView = QtWidgets.QTableWidget(self.airport_in_tab)
        self.airport_in_tableView.setStyleSheet("")
        self.airport_in_tableView.setObjectName("airport_in_tableView")
        self.gridLayout_8.addWidget(self.airport_in_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.airport_in_tab, "")
        self.route_tab = QtWidgets.QWidget()
        self.route_tab.setObjectName("route_tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.route_tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.route_tableView = QtWidgets.QTableWidget(self.route_tab)
        self.route_tableView.setStyleSheet("")
        self.route_tableView.setObjectName("route_tableView")
        self.gridLayout_9.addWidget(self.route_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.route_tab, "")
        self.flight_tab = QtWidgets.QWidget()
        self.flight_tab.setObjectName("flight_tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.flight_tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.flight_tableView = QtWidgets.QTableWidget(self.flight_tab)
        self.flight_tableView.setStyleSheet("")
        self.flight_tableView.setObjectName("flight_tableView")
        self.gridLayout_10.addWidget(self.flight_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.flight_tab, "")
        self.ticket_tab = QtWidgets.QWidget()
        self.ticket_tab.setObjectName("ticket_tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.ticket_tab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.ticket_tableView = QtWidgets.QTableWidget(self.ticket_tab)
        self.ticket_tableView.setStyleSheet("")
        self.ticket_tableView.setObjectName("ticket_tableView")
        self.gridLayout_11.addWidget(self.ticket_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.ticket_tab, "")
        self.gridLayout.addWidget(self.tab_widget, 2, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(8)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.add_fuck)



        masssiv = [self.airline_tableView, self.airport_in_tableView,
                   self.airport_out_tableView, self.flight_tableView,
                   self.passpor_user_tableView, self.plane_tableView,
                   self.route_tableView, self.ticket_tableView,
                   self.users_tableView]
        tables = show_tables()
        for k in range(len(masssiv)):
            x = select_max_id(tables[k])
            y = select_name_table(tables[k])
            masssiv[k].setRowCount(len(x) + 1)
            masssiv[k].setColumnCount(len(y))
            for i in range(len(y)):
                masssiv[k].setItem(0, i, QTableWidgetItem(str(y[i][0])))
            for i in range(len(x)):
                for j in range(len(x[i])):
                    masssiv[k].setItem(i + 1, j, QTableWidgetItem(str(x[i][j])))


    def update_data(self):
        masssiv = [self.airline_tableView, self.airport_in_tableView,
                   self.airport_out_tableView, self.flight_tableView,
                   self.passpor_user_tableView, self.plane_tableView,
                   self.route_tableView, self.ticket_tableView,
                   self.users_tableView]
        tables = show_tables()
        print(tables)
        for k in range(len(masssiv)):
            x = select_max_id(tables[k])
            y = select_name_table(tables[k])
            masssiv[k].setRowCount(len(x) + 1)
            masssiv[k].setColumnCount(len(y))
            for i in range(len(y)):
                masssiv[k].setItem(0, i, QTableWidgetItem(str(y[i][0])))
            for i in range(len(x)):
                for j in range(len(x[i])):
                    masssiv[k].setItem(i + 1, j, QTableWidgetItem(str(x[i][j])))

    def passport_user(self):
        self.passpor_user_tableView.show()
        self.passpor_user_tableView.setColumnWidth(7, 7)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Добавить данные"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.Airline_tab), _translate("MainWindow", "Авиакомпании"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.Plane_tab), _translate("MainWindow", "Самолёты"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.passport_users_tab),
                                   _translate("MainWindow", "Паспорта"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.users_tab), _translate("MainWindow", "Пользователи"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.airport_out_tab),
                                   _translate("MainWindow", "Аэропрот вылета"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.airport_in_tab),
                                   _translate("MainWindow", "Аэропорт назначения"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.route_tab), _translate("MainWindow", "Маршрут"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.flight_tab), _translate("MainWindow", "Рейс"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.ticket_tab), _translate("MainWindow", "Билет"))
        self.pushButton_4.setText(_translate("MainWindow", "Сортировать данные"))
        self.pushButton_3.setText(_translate("MainWindow", "Найти в базе данных"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить данные"))

    def add_fuck(self):
        self.add_Window = QtWidgets.QMainWindow()
        self.ui_add = Ui_Add_window()
        self.ui_add.setupUi_add(self.add_Window)
        self.add_Window.show()

    def setupUi_add(self, Add_window):
        Add_window.setObjectName("Add_window")
        Add_window.resize(716, 470)
        Add_window.setLayoutDirection(QtCore.Qt.RightToLeft)
        Add_window.setAutoFillBackground(True)
        Add_window.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Add_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_add = QtWidgets.QLabel(self.centralwidget)
        self.label_add.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_add.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_add.setAutoFillBackground(False)
        self.label_add.setStyleSheet("font: 20pt \"Consolas\";")
        self.label_add.setAlignment(QtCore.Qt.AlignCenter)
        self.label_add.setObjectName("label_add")
        self.gridLayout_2.addWidget(self.label_add, 0, 0, 1, 1)
        self.comboBox_add = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_add.setStyleSheet("font: 18pt \"Consolas\";")
        self.comboBox_add.setEditable(False)
        self.comboBox_add.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_add.setObjectName("comboBox_add")
        self.comboBox_add.addItem("")
        self.comboBox_add.addItem("")
        self.comboBox_add.addItem("")
        self.comboBox_add.addItem("")
        self.comboBox_add.addItem("")
        self.comboBox_add.addItem("")
        self.comboBox_add.addItem("")
        self.comboBox_add.addItem("")
        self.comboBox_add.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_add, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_add = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add.setInputMask("")
        self.lineEdit_add.setText("")
        self.lineEdit_add.setObjectName("lineEdit_add")
        self.gridLayout.addWidget(self.lineEdit_add, 0, 0, 1, 1)
        self.lineEdit_add_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add_2.setInputMask("")
        self.lineEdit_add_2.setText("")
        self.lineEdit_add_2.setObjectName("lineEdit_add_2")
        self.gridLayout.addWidget(self.lineEdit_add_2, 1, 0, 1, 1)
        self.lineEdit_add_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add_3.setInputMask("")
        self.lineEdit_add_3.setText("")
        self.lineEdit_add_3.setObjectName("lineEdit_add_3")
        self.gridLayout.addWidget(self.lineEdit_add_3, 2, 0, 1, 1)
        self.lineEdit_add_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add_4.setInputMask("")
        self.lineEdit_add_4.setText("")
        self.lineEdit_add_4.setObjectName("lineEdit_add_4")
        self.gridLayout.addWidget(self.lineEdit_add_4, 3, 0, 1, 1)
        self.lineEdit_add_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add_5.setInputMask("")
        self.lineEdit_add_5.setText("")
        self.lineEdit_add_5.setObjectName("lineEdit_add_5")
        self.gridLayout.addWidget(self.lineEdit_add_5, 4, 0, 1, 1)
        self.lineEdit_add_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add_6.setInputMask("")
        self.lineEdit_add_6.setText("")
        self.lineEdit_add_6.setObjectName("lineEdit_add_6")
        self.gridLayout.addWidget(self.lineEdit_add_6, 5, 0, 1, 1)
        self.lineEdit_add_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add_7.setInputMask("")
        self.lineEdit_add_7.setText("")
        self.lineEdit_add_7.setObjectName("lineEdit_add_7")
        self.gridLayout.addWidget(self.lineEdit_add_7, 6, 0, 1, 1)
        self.lineEdit_add_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add_8.setInputMask("")
        self.lineEdit_add_8.setText("")
        self.lineEdit_add_8.setObjectName("lineEdit_add_8")
        self.gridLayout.addWidget(self.lineEdit_add_8, 7, 0, 1, 1)
        self.lineEdit_add_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add_9.setInputMask("")
        self.lineEdit_add_9.setText("")
        self.lineEdit_add_9.setObjectName("lineEdit_add_9")
        self.gridLayout.addWidget(self.lineEdit_add_9, 8, 0, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 9, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 10, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        Add_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Add_window)
        self.statusbar.setObjectName("statusbar")
        Add_window.setStatusBar(self.statusbar)

        self.comboBox_add.currentIndexChanged.connect(self.output_line_to_add)

        self.retranslateUi_add(Add_window)
        QtCore.QMetaObject.connectSlotsByName(Add_window)

    def show_lines(self):
        self.lineEdit_add.show()
        self.lineEdit_add_2.show()
        self.lineEdit_add_3.show()
        self.lineEdit_add_4.show()
        self.lineEdit_add_5.show()
        self.lineEdit_add_6.show()
        self.lineEdit_add_7.show()
        self.lineEdit_add_8.show()
        self.lineEdit_add_9.show()

    def hide_lines(self):
        self.lineEdit_add.hide()
        self.lineEdit_add_2.hide()
        self.lineEdit_add_3.hide()
        self.lineEdit_add_4.hide()
        self.lineEdit_add_5.hide()
        self.lineEdit_add_6.hide()
        self.lineEdit_add_7.hide()
        self.lineEdit_add_8.hide()
        self.lineEdit_add_9.hide()

    def retranslateUi_add(self, Add_window):
        _translate = QtCore.QCoreApplication.translate
        Add_window.setWindowTitle(_translate("Add_window", "Добавить данные"))
        self.label_add.setText(_translate("Add_window", "Что добавить?"))
        self.comboBox_add.setItemText(0, _translate("Add_window", "Пользователя"))
        self.comboBox_add.setItemText(1, _translate("Add_window", "Рейс"))
        self.comboBox_add.setItemText(2, _translate("Add_window", "Маршрут"))
        self.comboBox_add.setItemText(3, _translate("Add_window", "Аэропорт вылета"))
        self.comboBox_add.setItemText(4, _translate("Add_window", "Аэропорт назначения"))
        self.comboBox_add.setItemText(5, _translate("Add_window", "Билет"))
        self.comboBox_add.setItemText(6, _translate("Add_window", "Авиакомпанию"))
        self.comboBox_add.setItemText(7, _translate("Add_window", "Самолёт"))
        self.comboBox_add.setEnabled(True)
        self.lineEdit_add.setPlaceholderText(_translate("Add_window", "Фамилия"))
        self.lineEdit_add_2.setPlaceholderText(_translate("Add_window", "Имя"))
        self.lineEdit_add_3.setPlaceholderText(_translate("Add_window", "Отчество"))
        self.lineEdit_add_4.setPlaceholderText(_translate("Add_window", "Серия"))
        self.lineEdit_add_5.setPlaceholderText(_translate("Add_window", "Номер"))
        self.lineEdit_add_6.setPlaceholderText(_translate("Add_window", "Регистрация"))
        self.lineEdit_add_7.setPlaceholderText(_translate("Add_window", "Почта"))
        self.lineEdit_add_8.setPlaceholderText(_translate("Add_window", "Телефон"))
        self.lineEdit_add_9.setPlaceholderText(_translate("Add_window", ""))
        self.pushButton_add.setText(_translate("Add_window", "Добавить"))
        self.pushButton_clear.setText(_translate("Add_window", "Очистить"))
        self.lineEdit_add_9.hide()

        self.pushButton_add.clicked.connect(self.add_data_in_sql)


    def add_funck(self):
        self.add_data_in_sql()
        self.update_data()

    def add_data_in_sql(self):
        if self.comboBox_add.currentText() == 'Пользователя':
            if self.lineEdit_add.text() != '' and self.lineEdit_add_2.text() != '' and \
                    self.lineEdit_add_3.text() != '' and self.lineEdit_add_4.text() != '' and \
                    self.lineEdit_add_5.text() != '' and self.lineEdit_add_6.text() != '' and \
                    self.lineEdit_add_7.text() != '' and self.lineEdit_add_8.text() != '':
                max_id = select_max_id('passport_user')
                data = [max_id, self.lineEdit_add.text(), self.lineEdit_add_2.text(), self.lineEdit_add_3.text(),
                        self.lineEdit_add_4.text(), self.lineEdit_add_5.text(), self.lineEdit_add_6.text(),
                        self.lineEdit_add_7.text(), self.lineEdit_add_8.text()]
                add_in_passport_user_sql(data)
                add_in_user(data)
        self.update_data_in_table()
                # self.conn = self.connection_db
                # self.cursors = self.conn.cursor()
                # create_db_sql_query = """select max(id_passport) from passport_user;"""
                # self.cursors.execute(create_db_sql_query)
                # max_id = self.cursors.fetchall()
                # max_id = int(max_id[0][0]) + 1
                # self.conn.close()
                # self.cursors.close()
                #
                # print(1)
                # self.conn = self.connection_db
                # self.cursors = self.conn.cursor()
                # into = f"""INSERT INTO passport_user (id_passport, last_name,
                # patronymic, first_name, series, number, registration) VALUES
                # ('{max_id}','{data[0]}','{data[1]}','{data[2]}',
                # '{data[3]}','{data[4]}','{data[5]});"""
                # print(into)
                # self.cursors.execute(into)
                # print(3)
                # # INSERT INTO passport_user (id_passport, last_name, patronymic, first_name, series, number, registration) VALUES
                # # ('1','Рудакова','Василиса','Данииловна','4506','567353','УФМС ПО ГОР. МОСКВЕ'),
                # self.conn.close()
                # self.cursors.close()

    def output_line_to_add(self):
        self.show_lines()
        if self.comboBox_add.currentText() == 'Пользователя':
            self.show_lines()
            self.lineEdit_add.setPlaceholderText("Фамилия")
            self.lineEdit_add_2.setPlaceholderText("Имя")
            self.lineEdit_add_3.setPlaceholderText("Отчество")
            self.lineEdit_add_4.setPlaceholderText("Серия")
            self.lineEdit_add_5.setPlaceholderText("Номер")
            self.lineEdit_add_6.setPlaceholderText("Регистрация")
            self.lineEdit_add_7.setPlaceholderText("Почта")
            self.lineEdit_add_8.setPlaceholderText("Телефон")
            self.lineEdit_add_9.hide()
        elif self.comboBox_add.currentText() == 'Авиакомпанию':
            self.show_lines()
            self.lineEdit_add.setPlaceholderText("Название")
            self.lineEdit_add_2.setPlaceholderText("Телефон")
            self.lineEdit_add_3.setPlaceholderText("Сайт")
            self.lineEdit_add_4.setPlaceholderText("Номер в рейтинге")
            self.lineEdit_add_5.hide()
            self.lineEdit_add_6.hide()
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()
        elif self.comboBox_add.currentText() == 'Самолёт':
            self.show_lines()
            self.lineEdit_add.setPlaceholderText("Срок эксплуатации")
            self.lineEdit_add_2.setPlaceholderText("Год выпуска")
            self.lineEdit_add_3.setPlaceholderText("Количество мест")
            self.lineEdit_add_4.setPlaceholderText("Марка")
            self.lineEdit_add_5.setPlaceholderText("Модель")
            self.lineEdit_add_6.setPlaceholderText("ID авиакомпании")
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()
        elif self.comboBox_add.currentText() == 'Аэропорт вылета':
            self.show_lines()
            self.lineEdit_add.setPlaceholderText("Адрес")
            self.lineEdit_add_2.setPlaceholderText("Номер телефона")
            self.lineEdit_add_3.setPlaceholderText("Сайт")
            self.lineEdit_add_4.setPlaceholderText("Название")
            self.lineEdit_add_5.setPlaceholderText("Марка")
            self.lineEdit_add_6.setPlaceholderText("Модель")
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()
        elif self.comboBox_add.currentText() == 'Аэропорт назначения':
            self.show_lines()
            self.lineEdit_add.setPlaceholderText("Адрес")
            self.lineEdit_add_2.setPlaceholderText("Номер телефона")
            self.lineEdit_add_3.setPlaceholderText("Сайт")
            self.lineEdit_add_4.setPlaceholderText("Название")
            self.lineEdit_add_5.setPlaceholderText("Марка")
            self.lineEdit_add_6.setPlaceholderText("Модель")
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()
        elif self.comboBox_add.currentText() == 'Маршрут':
            self.show_lines()
            self.lineEdit_add.setPlaceholderText("ID аэропорта вылета")
            self.lineEdit_add_2.setPlaceholderText("ID аэропорта назначение")
            self.lineEdit_add_3.setPlaceholderText("Город вылета")
            self.lineEdit_add_4.setPlaceholderText("Город назначения")
            self.lineEdit_add_5.hide()
            self.lineEdit_add_6.hide()
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()
        elif self.comboBox_add.currentText() == 'Рейс':
            self.show_lines()
            self.lineEdit_add.setPlaceholderText("ID Маршрута")
            self.lineEdit_add_2.setPlaceholderText("Дата вылета")
            self.lineEdit_add_3.setPlaceholderText("Дата назначения")
            self.lineEdit_add_4.hide()
            self.lineEdit_add_5.hide()
            self.lineEdit_add_6.hide()
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()
        elif self.comboBox_add.currentText() == 'Билет':
            self.show_lines()
            self.lineEdit_add.setPlaceholderText("ID Самолёта")
            self.lineEdit_add_2.setPlaceholderText("ID Рейса")
            self.lineEdit_add_3.setPlaceholderText("Посадочное место")
            self.lineEdit_add_4.setPlaceholderText("ID пользователя")
            self.lineEdit_add_5.hide()
            self.lineEdit_add_6.hide()
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()


# -----------------------------------------------

def open_main_window():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    open_main_window()
