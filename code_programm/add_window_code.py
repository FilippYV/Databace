import sys

import mysql.connector
from PyQt5.QtWidgets import QMessageBox
from mysql.connector import Error
from PyQt5 import QtCore, QtGui, QtWidgets


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


def select_max_id(name_table):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""select count(*) from {name_table};"""
    cursors.execute(create_db_sql_query)
    x = cursors.fetchall()
    conn.close()
    cursors.close()
    return x[0][0] + 1


def inster_in_bd(string):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    into = f"""{string}"""
    cursors.execute(into)
    conn.commit()
    conn.close()
    cursors.close()


def add_in_passport_user_sql(data):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    into = f"""INSERT INTO passport_user (id_passport, last_name,
       patronymic, first_name, series, numbers, registration) VALUES
    ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}');"""
    cursors.execute(into)
    conn.commit()
    conn.close()
    cursors.close()


def add_in_user(data):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    into = f"""INSERT INTO users (id_passport, id_user, email, phone) VALUES
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


def select_name_t(name_table):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""describe {name_table};"""
    cursors.execute(create_db_sql_query)
    y = cursors.fetchall()
    conn.close()
    cursors.close()
    string = f'INSERT INTO {name_table} ('
    for i in range(len(y)):
        if i != len(y) - 1:
            string += f'{y[i][0]},'
        else:
            string += f'{y[i][0]}'
    string += ') values '
    return string


class Ui_Add_window(object):
    def setupUi_add(self, Add_window):
        Add_window.setObjectName("Add_window")
        Add_window.resize(290, 404)
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
        self.comboBox_add.setEditable(True)
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
        self.pushButton_add.clicked.connect(self.add_data_in_sql)
        self.pushButton_clear.clicked.connect(self.clear_lineedit)
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

    def clear_lineedit(self):
        self.lineEdit_add.clear()
        self.lineEdit_add_2.clear()
        self.lineEdit_add_3.clear()
        self.lineEdit_add_4.clear()
        self.lineEdit_add_5.clear()
        self.lineEdit_add_6.clear()
        self.lineEdit_add_7.clear()
        self.lineEdit_add_8.clear()
        self.lineEdit_add_9.clear()

    def add_data_in_sql(self):
        try:
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
            elif self.comboBox_add.currentText() == 'Авиакомпанию':
                if self.lineEdit_add.text() != '' and self.lineEdit_add_2.text() != '' and \
                        self.lineEdit_add_3.text() != '' and self.lineEdit_add_4.text() != '':
                    max_id = select_max_id('airline')
                    data = [max_id, self.lineEdit_add.text(), self.lineEdit_add_2.text(),
                            self.lineEdit_add_3.text(),
                            self.lineEdit_add_4.text()]
                    string = select_name_t('airline')
                    string += ' ( '
                    for i in range(len(data)):
                        if i != len(data) - 1:
                            string += f"'{data[i]}',"
                        else:
                            string += f"'{data[i]}'"
                    string += ');'
                    print(string)
                    inster_in_bd(string)
            elif self.comboBox_add.currentText() == 'Самолёт':
                if self.lineEdit_add.text() != '' and self.lineEdit_add_2.text() != '' and \
                        self.lineEdit_add_3.text() != '' and self.lineEdit_add_4.text() != '' and \
                        self.lineEdit_add_5.text() != '' and self.lineEdit_add_6.text() != '':
                    max_id = select_max_id('plane')
                    data = [max_id, self.lineEdit_add.text(), self.lineEdit_add_2.text(),
                            self.lineEdit_add_3.text(), self.lineEdit_add_4.text(),
                            self.lineEdit_add_5.text(), self.lineEdit_add_6.text()]
                    string = select_name_t('plane')
                    string += ' ( '
                    for i in range(len(data)):
                        if i != len(data) - 1:
                            string += f"'{data[i]}',"
                        else:
                            string += f"'{data[i]}'"
                    string += ');'
                    print(string)
                    inster_in_bd(string)
            elif self.comboBox_add.currentText() == 'Аэропорт вылета':
                if self.lineEdit_add.text() != '' and self.lineEdit_add_2.text() != '' and \
                        self.lineEdit_add_3.text() != '' and self.lineEdit_add_4.text() != '':
                    max_id = select_max_id('airport_out')
                    data = [max_id, self.lineEdit_add.text(), self.lineEdit_add_2.text(),
                            self.lineEdit_add_3.text(), self.lineEdit_add_4.text()]
                    string = select_name_t('airport_out')
                    string += ' ( '
                    for i in range(len(data)):
                        if i != len(data) - 1:
                            string += f"'{data[i]}',"
                        else:
                            string += f"'{data[i]}'"
                    string += ');'
                    print(string)
                    inster_in_bd(string)
            elif self.comboBox_add.currentText() == 'Аэропорт назначения':
                if self.lineEdit_add.text() != '' and self.lineEdit_add_2.text() != '' and \
                        self.lineEdit_add_3.text() != '' and self.lineEdit_add_4.text() != '':
                    max_id = select_max_id('airport_in')
                    data = [max_id, self.lineEdit_add.text(), self.lineEdit_add_2.text(),
                            self.lineEdit_add_3.text(), self.lineEdit_add_4.text()]
                    string = select_name_t('airport_in')
                    string += ' ( '
                    for i in range(len(data)):
                        if i != len(data) - 1:
                            string += f"'{data[i]}',"
                        else:
                            string += f"'{data[i]}'"
                    string += ');'
                    print(string)
                    inster_in_bd(string)
            elif self.comboBox_add.currentText() == 'Маршрут':
                if self.lineEdit_add.text() != '' and self.lineEdit_add_2.text() != '' and \
                        self.lineEdit_add_3.text() != '' and self.lineEdit_add_4.text() != '':
                    max_id = select_max_id('route')
                    data = [max_id, self.lineEdit_add.text(), self.lineEdit_add_2.text(),
                            self.lineEdit_add_3.text(), self.lineEdit_add_4.text()]
                    string = select_name_t('route')
                    string += ' ( '
                    for i in range(len(data)):
                        if i != len(data) - 1:
                            string += f"'{data[i]}',"
                        else:
                            string += f"'{data[i]}'"
                    string += ');'
                    print(string)
                    inster_in_bd(string)
            elif self.comboBox_add.currentText() == 'Рейс':
                if self.lineEdit_add.text() != '' and self.lineEdit_add_2.text() != '' and \
                        self.lineEdit_add_3.text() != '':
                    max_id = select_max_id('flight')
                    data = [max_id, self.lineEdit_add.text(), self.lineEdit_add_2.text(),
                            self.lineEdit_add_3.text()]
                    string = select_name_t('flight')
                    string += ' ( '
                    for i in range(len(data)):
                        if i != len(data) - 1:
                            string += f"'{data[i]}',"
                        else:
                            string += f"'{data[i]}'"
                    string += ');'
                    print(string)
                    inster_in_bd(string)
            elif self.comboBox_add.currentText() == 'Билет':
                if self.lineEdit_add.text() != '' and self.lineEdit_add_2.text() != '' and \
                        self.lineEdit_add_3.text() != '' and self.lineEdit_add_4.text() != '':
                    max_id = select_max_id('ticket')
                    data = [max_id, self.lineEdit_add.text(), self.lineEdit_add_2.text(),
                            self.lineEdit_add_3.text(), self.lineEdit_add_4.text()]
                    string = select_name_t('ticket')
                    string += ' ( '
                    for i in range(len(data)):
                        if i != len(data) - 1:
                            string += f"'{data[i]}',"
                        else:
                            string += f"'{data[i]}'"
                    string += ');'
                    print(string)
                    inster_in_bd(string)
            ok = QMessageBox()
            ok.setWindowTitle("Добавление")
            ok.setText("Вы добавили данные!")
            ok.setIcon(QMessageBox.Information)
            ok.setStandardButtons(QMessageBox.Ok)
            ok.exec_()
            print('Ошибка!!!')
        except:
            print(1)
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Некоректные данные для ввода!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            print('Ошибка!!!')
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
            self.lineEdit_add.setPlaceholderText("Адрес")
            self.lineEdit_add_2.setPlaceholderText("Номер телефона")
            self.lineEdit_add_3.setPlaceholderText("Сайт")
            self.lineEdit_add_4.setPlaceholderText("Название")
            self.lineEdit_add_5.hide()
            self.lineEdit_add_6.hide()
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()
        elif self.comboBox_add.currentText() == 'Аэропорт назначения':
            self.lineEdit_add.setPlaceholderText("Адрес")
            self.lineEdit_add_2.setPlaceholderText("Номер телефона")
            self.lineEdit_add_3.setPlaceholderText("Сайт")
            self.lineEdit_add_4.setPlaceholderText("Название")
            self.lineEdit_add_5.hide()
            self.lineEdit_add_6.hide()
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()
        elif self.comboBox_add.currentText() == 'Маршрут':
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
            self.lineEdit_add.setPlaceholderText("ID Самолёта")
            self.lineEdit_add_2.setPlaceholderText("ID Рейса")
            self.lineEdit_add_3.setPlaceholderText("ID пользователя")
            self.lineEdit_add_4.setPlaceholderText("Посадочное место")
            self.lineEdit_add_5.hide()
            self.lineEdit_add_6.hide()
            self.lineEdit_add_7.hide()
            self.lineEdit_add_8.hide()
            self.lineEdit_add_9.hide()
