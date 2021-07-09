from PyQt5 import QtCore, QtGui, QtWidgets
from pays import plat
import psycopg2
from psycopg2 import Error
import dbconnect



class Ui_MainWindow(dbconnect.Dbconnect):
    def __init__(self, host, port, dbname):
        super().__init__(host, port, dbname)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 335)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.submit_pushButton.setGeometry(QtCore.QRect(30, 260, 91, 31))
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.submit_pushButton.clicked.connect(lambda: self.submit_it())
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 220, 111, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(plat)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.first_name = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.first_name.setObjectName("first_name")
        self.last_name = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name.setGeometry(QtCore.QRect(20, 90, 113, 20))
        self.last_name.setObjectName("last_name")
        self.date_Edit = QtWidgets.QDateEdit(self.centralwidget)
        self.date_Edit.setGeometry(QtCore.QRect(20, 150, 111, 21))
        self.date_Edit.setObjectName("date_Edit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 40, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 37, 40);\n"
"background-color: rgb(247, 213, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.edite_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.edite_pushButton.setGeometry(QtCore.QRect(220, 260, 81, 31))
        self.edite_pushButton.setObjectName("edite_pushButton")
        self.edite_pushButton.clicked.connect(lambda:self.edite_it())
        self.delet_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delet_pushButton.setGeometry(QtCore.QRect(320, 260, 81, 31))
        self.delet_pushButton.setObjectName("delet_pushButton")
        self.delet_pushButton.clicked.connect(lambda:self.delet_it())
        self.clear_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.clear_pushButton.setGeometry(QtCore.QRect(420, 260, 81, 31))
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.clear_pushButton.clicked.connect(lambda:self.clear_it())
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(160, 60, 431, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit_pushButton.setText(_translate("MainWindow", "submit"))
        self.label_2.setText(_translate("MainWindow", "first name"))
        self.label_3.setText(_translate("MainWindow", "last name"))
        self.label_4.setText(_translate("MainWindow", "Date de naissance"))
        self.label.setText(_translate("MainWindow", "Nationalité"))
        self.label_5.setText(_translate("MainWindow", "liste of student"))
        self.edite_pushButton.setText(_translate("MainWindow", "Edite"))
        self.delet_pushButton.setText(_translate("MainWindow", "Delet item"))
        self.clear_pushButton.setText(_translate("MainWindow", "Clear all"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "first name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "last name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "date de naiss"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "nationalité"))

    

    def submit_it(self):
        dit = {}
        dit[0] = self.first_name.text() 
        dit[1] = self.last_name.text()
        dit[2] = self.date_Edit.text()
        dit[3] = self.comboBox.currentText()
        if dit in self.data_base:
            pass
        else:
            self.data_base.append(dit)
        tablerow=0
        self.tableWidget.setRowCount(len(self.data_base))
        self.pipa()


    def edite_it(self):
        pass

    def delet_it(self):
        try:
            selected = []
            for i in self.tableWidget.selectedIndexes():
                p = (i.row(),i.column())
                selected.append(p)
            for i in selected:
                a = []
                a.append(i[0])
            for i in a:
                for ix in range(4):
                    self.tableWidget.takeItem(i,ix)
                self.data_base.pop(i)     
            self.tableWidget.setRowCount(len(self.data_base))
            self.pipa()
        except:
            pass

    
    def pipa(self):
        tablerow=0
        self.tableWidget.setRowCount(len(self.data_base))
        for i in self.data_base:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(i[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(i[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(i[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(i[3]))
            tablerow +=1
            


    def clear_it(self):
        for i in range(len(self.data_base)):
            for j in range(4):
                self.tableWidget.takeItem(i,j)
        self.tableWidget.setRowCount(0) 
        self.data_base = []       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(host ='localhost'  , port=5432 , dbname="test")
    Ui_MainWindow._auth(username='fiberx01' ,password="0000")
    Ui_MainWindow.connect()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("EST-FES")
    MainWindow.setWindowIcon(QtGui.QIcon('ko.png'))
    MainWindow.show()
    sys.exit(app.exec_()) 