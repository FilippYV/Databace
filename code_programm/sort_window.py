import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from mysql.connector import Error
from PyQt5 import QtCore, QtGui, QtWidgets

mass_sing = ['+', '-']


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




def select_name_t(name_table, column, sing):
    conn = create_connection_mysql_db()
    cursors = conn.cursor()
    if sing == '+':
        create_db_sql_query = f"""select * from {name_table} order by {column} ;"""
    else:
        create_db_sql_query = f"""select * from {name_table} order by {column} desc;"""
    cursors.execute(create_db_sql_query)
    data = cursors.fetchall()
    conn.close()
    cursors.close()
    print('search')
    return data


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


class Ui_sort_window(object):
    def setupUi_sort(self, Sort_window):
        Sort_window.setObjectName("Sort_window")
        Sort_window.resize(446, 600)
        self.centralwidget = QtWidgets.QWidget(Sort_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 8, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 6, 0, 1, 1)
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
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName("pushButton_dell")
        self.gridLayout.addWidget(self.pushButton_search, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 20pt \"Consolas\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.pushButton_2_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_clear.setObjectName("pushButton_2_clear")
        self.gridLayout.addWidget(self.pushButton_2_clear, 10, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 4, 0, 1, 1)
        Sort_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Sort_window)
        self.statusbar.setObjectName("statusbar")
        Sort_window.setStatusBar(self.statusbar)

        self.retranslateUi(Sort_window)
        QtCore.QMetaObject.connectSlotsByName(Sort_window)

    def retranslateUi(self, Serarch_window):
        _translate = QtCore.QCoreApplication.translate
        Serarch_window.setWindowTitle("MainWindow")
        self.label.setText("Из какой таблицы")
        self.label_2.setText("По каким строкам")
        self.pushButton_search.setText("Найти")
        self.label_3.setText("Условие")
        self.pushButton_2_clear.setText("Очистить")
        self.comboBox.currentIndexChanged.connect(self.output_line_to_search)
        self.pushButton_search.clicked.connect(self.search_funck)
        self.listWidget.itemClicked.connect(self.printItemText)
        y = show_tables()
        for i in range(len(y)):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, y[i])
        self.label_2.setText(_translate("Sort_window", "По столбцу:"))
        self.pushButton_2_clear.clicked.connect(self.clear_fuck)
        self.x = []
        self.listWidget.hide()

    def clear_fuck(self):
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.listWidget.clear()

    def output_line_to_search(self):
        try:
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.listWidget.clear()
            name_table = self.comboBox.currentText()
            if name_table == '':
                y = describe_table_for_search('airline')
            else:
                y = describe_table_for_search(name_table)
            for i in range(len(y)):
                self.comboBox_2.addItem("")
                self.comboBox_2.setItemText(i, y[i])
            for i in range(len(mass_sing)):
                self.comboBox_3.addItem("")
                self.comboBox_3.setItemText(i, mass_sing[i])
            for i in range(len(y)):
                self.listWidget.addItem(y[i])
        except:
            print('Ошибка!!!')

    def printItemText(self):
        items = self.listWidget.selectedItems()
        self.x = []
        for i in range(len(items)):
            self.x.append(str(self.listWidget.selectedItems()[i].text()))
        print(self.x)

    #
    def search_funck(self):
        try:
            if self.comboBox.currentText() != '' and self.comboBox_2.currentText() != '' \
                    and self.comboBox_3.currentText():
                name_table = self.comboBox.currentText()
                column = self.comboBox_2.currentText()
                sing = self.comboBox_3.currentText()
                print('('*100)
                print(name_table, column, sing)
                data = select_name_t(name_table, column, sing)
                row = len(data) + 1
                column = len(data[0])
                self.tableView.setRowCount(row)
                self.tableView.setColumnCount(column)
                x = describe_table_for_search(name_table)
                for i in range(column):
                    self.tableView.setItem(0, i, QTableWidgetItem(str(x[i])))
                for i in range(len(data)):
                    for j in range(len(data[i])):
                        self.tableView.setItem(i + 1, j, QTableWidgetItem(str(data[i][j])))
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Заполните все поля!")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                print('Ошибка!!!')
        except:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Некоректный запрос!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            print('Ошибка!!!')
