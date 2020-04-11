import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QCompleter
import pymongo
from PyQt5.QtCore import Qt

#ADD ITEM BUTTON CONFIGURED
#AUTO TYPE CONFIGURED
#TABLE VIEW MEIN REMOVE COLUMN AND INDEX

myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['Billing']
mycol = mydb['Items']


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class Ui_MainWindow(object):
    billed = [['Item Name', 'Quantity', 'Price', 'Total']]
    items = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 410, 261, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.completer = QCompleter()
        self.model = QStringListModel()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 410, 101, 17))
        self.label.setObjectName("label")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(120, 460, 91, 26))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 470, 67, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 510, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 381, 391))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 389))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableView = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 381, 591))
        self.tableView.setObjectName("tableView")
        self.model2 = TableModel(self.billed)
        self.tableView.setModel(self.model2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 40, 121, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 40, 151, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 90, 131, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(610, 80, 121, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 160, 111, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 160, 111, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 20, 101, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 10, 131, 41))
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(460, 130, 271, 81))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(583, 20, 51, 231))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 280, 101, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 280, 101, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 384, 101, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(460, 220, 131, 41))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(610, 220, 131, 41))
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 380, 101, 81))
        self.pushButton_5.setObjectName("pushButton_5")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(457, 190, 271, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuItems = QtWidgets.QMenu(self.menubar)
        self.menuItems.setObjectName("menuItems")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Bill = QtWidgets.QAction(MainWindow)
        self.actionNew_Bill.setObjectName("actionNew_Bill")
        self.actionView_Bills = QtWidgets.QAction(MainWindow)
        self.actionView_Bills.setObjectName("actionView_Bills")
        self.actionLog_Out = QtWidgets.QAction(MainWindow)
        self.actionLog_Out.setObjectName("actionLog_Out")
        self.actionTotal_Sale = QtWidgets.QAction(MainWindow)
        self.actionTotal_Sale.setObjectName("actionTotal_Sale")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_Item = QtWidgets.QAction(MainWindow)
        self.actionAdd_Item.setObjectName("actionAdd_Item")
        self.actionRemove_Item = QtWidgets.QAction(MainWindow)
        self.actionRemove_Item.setObjectName("actionRemove_Item")
        self.actionView_Items = QtWidgets.QAction(MainWindow)
        self.actionView_Items.setObjectName("actionView_Items")
        self.menuFile.addAction(self.actionNew_Bill)
        self.menuFile.addAction(self.actionView_Bills)
        self.menuFile.addAction(self.actionTotal_Sale)
        self.menuFile.addAction(self.actionLog_Out)
        self.menuFile.addAction(self.actionExit)
        self.menuItems.addAction(self.actionAdd_Item)
        self.menuItems.addAction(self.actionRemove_Item)
        self.menuItems.addAction(self.actionView_Items)
        self.menuItems.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuItems.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.lineEdit.setCompleter(self.completer)
        self.completer.setModel(self.model)
        self.get_items(self.model)

        self.label.setText(_translate("MainWindow", "Item Name"))
        self.label_2.setText(_translate("MainWindow", "Quantity"))

        self.pushButton.setText(_translate("MainWindow", "Add Item"))
        self.pushButton.clicked.connect(self.onAddItemClick)

        self.label_3.setText(_translate("MainWindow", "Total Amount"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "Discount"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Net Amount"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "Total Items"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "Cash"))
        self.pushButton_3.setText(_translate("MainWindow", "Credit/Debit"))
        self.pushButton_4.setText(_translate("MainWindow", "Gift Voucher"))
        self.label_11.setText(_translate("MainWindow", "Bill Number"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("MainWindow", "Paytm"))
        self.menuFile.setTitle(_translate("MainWindow", "Options"))
        self.menuItems.setTitle(_translate("MainWindow", "Items"))
        self.actionNew_Bill.setText(_translate("MainWindow", "New Bill"))
        self.actionView_Bills.setText(_translate("MainWindow", "View Bills"))
        self.actionLog_Out.setText(_translate("MainWindow", "Log Out"))
        self.actionTotal_Sale.setText(_translate("MainWindow", "Total Sale"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAdd_Item.setText(_translate("MainWindow", "Add Item"))
        self.actionRemove_Item.setText(_translate("MainWindow", "Remove Item"))
        self.actionView_Items.setText(_translate("MainWindow", "View Items"))

    def get_items(self, model):
        items = []
        mydoc = mycol.find()
        for i in mydoc:
            items.append(i['name'])
        model.setStringList(items)
        self.items = items


    def onAddItemClick(self):
        itemName = self.lineEdit.text()
        mydoc = mycol.find({'name': itemName})
        quantity = self.spinBox.text()
        row = []
        # if itemName not in self.items:
            # ADD DIALOG BOX
        if int(quantity) == 0:
            self.lineEdit.setText('')
            self.spinBox.setValue('')

        else:
            a = 0
            for i in self.billed:
                if i[0] == itemName:
                    ogQuantity = i[1]
                    self.billed.remove(i)
                    row.append(mydoc[0]['name'])
                    row.append(int(ogQuantity)+int(quantity))
                    row.append(str(mydoc[0]['price']))
                    row.append((int(ogQuantity)+int(quantity)) * int(mydoc[0]['price']))
                    self.billed.append(row)
                    self.lineEdit.setText('')
                    self.spinBox.setValue(0)
                    self.model2 = TableModel(self.billed)
                    self.tableView.setModel(self.model2)
                    a = 2

            if (a != 2):
                row.append(mydoc[0]['name'])
                row.append(quantity)
                row.append(str(mydoc[0]['price']))
                row.append(int(quantity) * int(mydoc[0]['price']))
                print(row)
                self.billed.append(row)
                print(self.billed)
                self.lineEdit.setText('')
                self.spinBox.setValue(0)

                self.model2 = TableModel(self.billed)
                self.tableView.setModel(self.model2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
