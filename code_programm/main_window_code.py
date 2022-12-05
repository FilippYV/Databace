import sys
import mysql.connector
from mysql.connector import Error
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from add_window_code import Ui_Add_window
from code_programm.change_window import Ui_Change_Window
from code_programm.sort_window import Ui_sort_window
from dell_window import Ui_Dell_window
from search_window import Ui_Serarch_window
from ui_files.sql_line import Ui_Serch_sql


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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon('../static/bd_icon.png'))
        MainWindow.resize(783, 810)
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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
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
        self.pushButton_change = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_change.setObjectName("pushButton_change")
        self.gridLayout.addWidget(self.pushButton_change, 0, 2, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName("pushButton_coman_line")
        self.gridLayout.addWidget(self.pushButton_exit, 1, 2, 1, 1)
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
        self.gridLayout.addWidget(self.tab_widget, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(8)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.add_fuck)
        self.pushButton_2.clicked.connect(self.dell_fuck)
        self.pushButton_3.clicked.connect(self.search_fuck)
        self.airline_tableView.clicked.connect(self.update_data)
        self.airport_in_tableView.clicked.connect(self.update_data)
        self.airport_out_tableView.clicked.connect(self.update_data)
        self.passpor_user_tableView.clicked.connect(self.update_data)
        self.plane_tableView.clicked.connect(self.update_data)
        self.route_tableView.clicked.connect(self.update_data)
        self.ticket_tableView.clicked.connect(self.update_data)
        self.users_tableView.clicked.connect(self.update_data)
        self.flight_tableView.clicked.connect(self.update_data)
        self.pushButton_4.clicked.connect(self.sort_fuck)
        m = self.update_data()
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle('Лучший интерфейс')
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
        # self.pushButton_coman_line.setText(_translate("MainWindow", "Comandline"))
        self.pushButton_change.setText(_translate("MainWindow", "Заменить"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выйти"))
        self.pushButton_change.clicked.connect(self.change_fuck)
        self.pushButton_exit.clicked.connect(close)

    def change_fuck(self):
        self.Change_winodw = QtWidgets.QMainWindow()
        self.ui_change = Ui_Change_Window()
        self.ui_change.setupUi_change(self.Change_winodw)
        self.Change_winodw.show()

    def sort_fuck(self):
        self.Sorts_window = QtWidgets.QMainWindow()
        self.ui_sort = Ui_sort_window()
        self.ui_sort.setupUi_sort(self.Sorts_window)
        self.Sorts_window.show()

    def add_fuck(self):
        self.Add_Window = QtWidgets.QMainWindow()
        self.ui_add = Ui_Add_window()
        self.ui_add.setupUi_add(self.Add_Window)
        self.Add_Window.show()

    def dell_fuck(self):
        self.Dell_window = QtWidgets.QMainWindow()
        self.ui_dell = Ui_Dell_window()
        self.ui_dell.setupUi(self.Dell_window)
        self.Dell_window.show()

    def search_fuck(self):
        self.Search_window = QtWidgets.QMainWindow()
        self.ui_search = Ui_Serarch_window()
        self.ui_search.setupUi_search(self.Search_window)
        self.Search_window.show()


def close():
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
