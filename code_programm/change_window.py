import mysql.connector
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
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
    return y


def describe_table_for_search(name_table):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""describe {name_table};"""
    cursors.execute(create_db_sql_query)
    y = cursors.fetchall()
    conn.close()
    cursors.close()
    for i in range(len(y)):
        y[i] = y[i][0]
    print(y, '----------------------')
    return y


def select_from_table(name_table):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""select * from {name_table};"""
    cursors.execute(create_db_sql_query)
    y = cursors.fetchall()
    conn.close()
    cursors.close()
    print(y)
    return y


def update_data(name_table, id_name, name_column_to_change, id_value, new_value):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    create_db_sql_query = f"""UPDATE {name_table} SET {name_column_to_change}={new_value}
     WHERE {id_name} = {id_value};"""
    print(create_db_sql_query)
    cursors.execute(create_db_sql_query)
    conn.commit()
    conn.close()
    cursors.close()


class Ui_Change_Window(object):
    def setupUi_change(self, Change_Window):
        Change_Window.setObjectName("Change_Window")
        Change_Window.resize(600, 350)
        self.centralwidget = QtWidgets.QWidget(Change_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_table = QtWidgets.QLabel(self.centralwidget)
        self.label_table.setAlignment(QtCore.Qt.AlignCenter)
        self.label_table.setObjectName("label_table")
        self.gridLayout.addWidget(self.label_table, 0, 0, 1, 2)
        self.tableWidget_show_tables = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_show_tables.setObjectName("tableWidget_show_tables")
        self.tableWidget_show_tables.setColumnCount(0)
        self.tableWidget_show_tables.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_show_tables, 2, 0, 1, 2)
        self.lineEdit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.gridLayout.addWidget(self.lineEdit_input, 4, 0, 1, 2)
        self.comboBox_table = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_table.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_table.setObjectName("comboBox_table")
        self.gridLayout.addWidget(self.comboBox_table, 1, 0, 1, 2)
        self.pushButton_canseld = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_canseld.setObjectName("pushButton_canseld")
        self.gridLayout.addWidget(self.pushButton_canseld, 5, 1, 1, 1)
        self.pushButton_change = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_change.setObjectName("pushButton_change")
        self.gridLayout.addWidget(self.pushButton_change, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        Change_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Change_Window)
        self.statusbar.setObjectName("statusbar")
        Change_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Change_Window)
        QtCore.QMetaObject.connectSlotsByName(Change_Window)

    def retranslateUi(self, Change_Window):
        _translate = QtCore.QCoreApplication.translate
        Change_Window.setWindowTitle('Изенеения')
        Change_Window.setWindowIcon(QIcon('../static/update.png'))
        self.label_table.setText(_translate("Change_Window", "Выберете таблицу для редакртирования:"))
        self.pushButton_canseld.setText(_translate("Change_Window", "Отмена"))
        self.pushButton_change.setText(_translate("Change_Window", "Изменить"))
        self.label.setText(_translate("Change_Window", "Измените данные:"))
        self.comboBox_table.currentIndexChanged.connect(self.update_date_table)
        self.pushButton_change.clicked.connect(self.update_data_in_databases)
        self.pushButton_canseld.clicked.connect(self.clear)
        y = show_tables()
        for i in range(len(y)):
            self.comboBox_table.addItem("")
            self.comboBox_table.setItemText(i, y[i])
        name_table = self.comboBox_table.currentText()
        table_column_name = describe_table_for_search(name_table)
        table_data = select_from_table(name_table)
        self.tableWidget_show_tables.setRowCount(len(table_data) + 1)
        self.tableWidget_show_tables.setColumnCount(len(table_column_name))
        for i in range(len(table_column_name)):
            self.tableWidget_show_tables.setItem(0, i, QTableWidgetItem(str(table_column_name[i])))
        for i in range(len(table_data)):
            for j in range(len(table_data[i])):
                self.tableWidget_show_tables.setItem(i + 1, j, QTableWidgetItem(str(table_data[i][j])))
        self.tableWidget_show_tables.clicked.connect(self.get_data_in_table)
        self.lineEdit_input.setPlaceholderText('Выберете значения')

    def clear(self):
        self.lineEdit_input.clear()
        self.lineEdit_input.setPlaceholderText('Выберете значения')
        self.update_date_table()

    def update_data_in_databases(self):
        try:
            if self.lineEdit_input.text() != '':
                row = self.tableWidget_show_tables.currentRow()
                column = self.tableWidget_show_tables.currentColumn()
                name_column_to_change = self.tableWidget_show_tables.item(0, column).text()
                id_name = self.tableWidget_show_tables.item(0, 0).text()
                id_value = self.tableWidget_show_tables.item(row, 0).text()
                new_value = self.lineEdit_input.text()
                name_table = self.comboBox_table.currentText()
                update_data(name_table, id_name, name_column_to_change, id_value, new_value)
                self.update_date_table()
                ok = QMessageBox()
                ok.setWindowTitle("Изменение")
                ok.setText("Вы изменили данные!")
                ok.setIcon(QMessageBox.Information)
                ok.setStandardButtons(QMessageBox.Ok)
                ok.exec_()
                print('Ошибка!!!')
        except:
            print(1)
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Некоректные данные при изменении!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            print('Ошибка!!!')

    def update_date_table(self):
        y = show_tables()
        for i in range(len(y)):
            self.comboBox_table.addItem("")
            self.comboBox_table.setItemText(i, y[i])
        name_table = self.comboBox_table.currentText()
        table_column_name = describe_table_for_search(name_table)
        table_data = select_from_table(name_table)
        self.tableWidget_show_tables.setRowCount(len(table_data) + 1)
        self.tableWidget_show_tables.setColumnCount(len(table_column_name))
        for i in range(len(table_column_name)):
            self.tableWidget_show_tables.setItem(0, i, QTableWidgetItem(str(table_column_name[i])))
        for i in range(len(table_data)):
            for j in range(len(table_data[i])):
                self.tableWidget_show_tables.setItem(i + 1, j, QTableWidgetItem(str(table_data[i][j])))
        self.tableWidget_show_tables.clicked.connect(self.get_data_in_table)
        self.lineEdit_input.setPlaceholderText('Выберете значения')

    def get_data_in_table(self):
        self.lineEdit_input.clear()
        row = self.tableWidget_show_tables.currentRow()
        column = self.tableWidget_show_tables.currentColumn()
        old_cell_text = self.tableWidget_show_tables.item(row, column).text()
        if row != 0:
            self.lineEdit_input.setText(old_cell_text)
        else:
            self.lineEdit_input.setPlaceholderText('Выберете значения, а не название таблиц!!!')
