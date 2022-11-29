# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'mian_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from add_window import Ui_Add_window


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
        self.airline_tableView = QtWidgets.QTableView(self.Airline_tab)
        self.airline_tableView.setStyleSheet("")
        self.airline_tableView.setObjectName("airline_tableView")
        self.gridLayout_3.addWidget(self.airline_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.Airline_tab, "")
        self.Plane_tab = QtWidgets.QWidget()
        self.Plane_tab.setObjectName("Plane_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Plane_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plane_tableView = QtWidgets.QTableView(self.Plane_tab)
        self.plane_tableView.setStyleSheet("")
        self.plane_tableView.setObjectName("plane_tableView")
        self.gridLayout_4.addWidget(self.plane_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.Plane_tab, "")
        self.passport_users_tab = QtWidgets.QWidget()
        self.passport_users_tab.setObjectName("passport_users_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.passport_users_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.passpor_user_tableView = QtWidgets.QTableView(self.passport_users_tab)
        self.passpor_user_tableView.setStyleSheet("")
        self.passpor_user_tableView.setObjectName("passpor_user_tableView")
        self.gridLayout_5.addWidget(self.passpor_user_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.passport_users_tab, "")
        self.users_tab = QtWidgets.QWidget()
        self.users_tab.setObjectName("users_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.users_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.users_tableView = QtWidgets.QTableView(self.users_tab)
        self.users_tableView.setStyleSheet("")
        self.users_tableView.setObjectName("users_tableView")
        self.gridLayout_6.addWidget(self.users_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.users_tab, "")
        self.airport_out_tab = QtWidgets.QWidget()
        self.airport_out_tab.setObjectName("airport_out_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.airport_out_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.airport_out_tableView = QtWidgets.QTableView(self.airport_out_tab)
        self.airport_out_tableView.setStyleSheet("")
        self.airport_out_tableView.setObjectName("airport_out_tableView")
        self.gridLayout_7.addWidget(self.airport_out_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.airport_out_tab, "")
        self.airport_in_tab = QtWidgets.QWidget()
        self.airport_in_tab.setObjectName("airport_in_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.airport_in_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.airport_in_tableView = QtWidgets.QTableView(self.airport_in_tab)
        self.airport_in_tableView.setStyleSheet("")
        self.airport_in_tableView.setObjectName("airport_in_tableView")
        self.gridLayout_8.addWidget(self.airport_in_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.airport_in_tab, "")
        self.route_tab = QtWidgets.QWidget()
        self.route_tab.setObjectName("route_tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.route_tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.route_tableView = QtWidgets.QTableView(self.route_tab)
        self.route_tableView.setStyleSheet("")
        self.route_tableView.setObjectName("route_tableView")
        self.gridLayout_9.addWidget(self.route_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.route_tab, "")
        self.flight_tab = QtWidgets.QWidget()
        self.flight_tab.setObjectName("flight_tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.flight_tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.flight_tableView = QtWidgets.QTableView(self.flight_tab)
        self.flight_tableView.setStyleSheet("")
        self.flight_tableView.setObjectName("flight_tableView")
        self.gridLayout_10.addWidget(self.flight_tableView, 0, 0, 1, 1)
        self.tab_widget.addTab(self.flight_tab, "")
        self.ticket_tab = QtWidgets.QWidget()
        self.ticket_tab.setObjectName("ticket_tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.ticket_tab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.ticket_tableView = QtWidgets.QTableView(self.ticket_tab)
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
