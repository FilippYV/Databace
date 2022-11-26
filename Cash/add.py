from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

Base_of_data = sqlite3.connect('Data_bace_deans_office.bd')
cursor = Base_of_data.cursor()

class Ui_Add_user(object):
    def setupUi(self, Add_user):
        Add_user.setObjectName("Add_user")
        Add_user.resize(221, 283)
        self.centralwidget = QtWidgets.QWidget(Add_user)
        self.centralwidget.setObjectName("centralwidget")
        self.NameFaculty = QtWidgets.QLineEdit(self.centralwidget)
        self.NameFaculty.setGeometry(QtCore.QRect(10, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NameFaculty.setFont(font)
        self.NameFaculty.setText("")
        self.NameFaculty.setMaxLength(25)
        self.NameFaculty.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.NameFaculty.setCursorPosition(0)
        self.NameFaculty.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.NameFaculty.setDragEnabled(False)
        self.NameFaculty.setObjectName("NameFaculty")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(65, 240, 90, 23))
        self.pushButton.setObjectName("pushButton")
        self.Room = QtWidgets.QLineEdit(self.centralwidget)
        self.Room.setGeometry(QtCore.QRect(10, 80, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Room.setFont(font)
        self.Room.setText("")
        self.Room.setMaxLength(25)
        self.Room.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Room.setCursorPosition(0)
        self.Room.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Room.setDragEnabled(False)
        self.Room.setObjectName("Room")
        self.Corps = QtWidgets.QLineEdit(self.centralwidget)
        self.Corps.setGeometry(QtCore.QRect(10, 120, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Corps.setFont(font)
        self.Corps.setText("")
        self.Corps.setMaxLength(25)
        self.Corps.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Corps.setCursorPosition(0)
        self.Corps.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Corps.setDragEnabled(False)
        self.Corps.setObjectName("Corps")
        self.Telephone = QtWidgets.QLineEdit(self.centralwidget)
        self.Telephone.setGeometry(QtCore.QRect(10, 160, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Telephone.setFont(font)
        self.Telephone.setText("")
        self.Telephone.setMaxLength(25)
        self.Telephone.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Telephone.setCursorPosition(0)
        self.Telephone.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Telephone.setDragEnabled(False)
        self.Telephone.setObjectName("Telephone")
        self.NameDean = QtWidgets.QLineEdit(self.centralwidget)
        self.NameDean.setGeometry(QtCore.QRect(10, 200, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NameDean.setFont(font)
        self.NameDean.setText("")
        self.NameDean.setMaxLength(25)
        self.NameDean.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.NameDean.setCursorPosition(0)
        self.NameDean.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.NameDean.setDragEnabled(False)
        self.NameDean.setObjectName("NameDean")
        Add_user.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Add_user)
        self.statusbar.setObjectName("statusbar")
        Add_user.setStatusBar(self.statusbar)

        self.retranslateUi(Add_user)
        QtCore.QMetaObject.connectSlotsByName(Add_user)

    def retranslateUi(self, Add_user):
        _translate = QtCore.QCoreApplication.translate
        Add_user.setWindowTitle("ADD_user")
        self.NameFaculty.setPlaceholderText("Факультет")
        self.Room.setPlaceholderText("Aудитория")
        self.Corps.setPlaceholderText("Корпус")
        self.Telephone.setPlaceholderText("Контактный телефон")
        self.NameDean.setPlaceholderText("Фамилия декана")
        self.label.setText(_translate("Add_user", "Enter info"))
        self.pushButton.setText("ADD")

    def reg(self):
        NameFaculty = self.NameFaculty.text()
        Room = self.Room.text()
        Corps = self.Corps.text()
        Telephone = self.Telephone.text()
        NameDean = self.NameDean.text()
        if len(NameFaculty) == 0 or len(Room) == 0 or \
                len(Corps) == 0 or len(Telephone) == 0 or \
                len(NameDean) == 0:
            return
        cursor.execute(f'SELECT login FROM users WHERE NameFaculty="{NameFaculty}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users VALUES ("{NameFaculty}", "{Room}", '
                           f'"{Corps}", "{Telephone}", "{NameDean}")')
            self.label.setText(f'Факультет {NameFaculty} успешно внесён в базу данных!')
            Base_of_data.commit()
        else:
            self.label.setText('Такая записать уже имеется!')



