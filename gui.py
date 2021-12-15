from numpy import empty
import pandas as pd
import matplotlib.pyplot as plt


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt
from runner import create_df, saveplots, empty_df

ppi = 93

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 668)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.control = False    

        self.fig1, self.ax1 = plt.subplots(figsize=(551/ppi, 350/ppi))
        self.ax1.set_ylabel('Vn₂', fontsize='large')
        self.ax1.set_xlabel('Vn₁', fontsize='large')
        self.fig2, self.ax2 = plt.subplots(figsize=(551/ppi, 350/ppi))
        self.ax2.set_ylabel('Vn₂', fontsize='large')
        self.ax2.set_xlabel('Xn', fontsize='large')
        self.fig3, self.ax3 = plt.subplots(figsize=(551/ppi, 350/ppi))
        self.ax3.set_ylabel('Vn₁', fontsize='large')
        self.ax3.set_xlabel('Xn', fontsize='large')
        self.fig1.savefig('both.png')
        self.fig2.savefig('vn2.png')
        self.fig3.savefig('vn1.png')

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(600, 280, 571, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 551, 301))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("blank.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 551, 301))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("blank.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setGeometry(QtCore.QRect(10, 10, 551, 301))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("blank.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 170, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(10, 30, 241, 64))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setClearButtonEnabled(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_3.addWidget(self.lineEdit_11, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setClearButtonEnabled(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_3.addWidget(self.lineEdit_8, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(280, 10, 311, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget1 = QtWidgets.QWidget(self.groupBox_2)
        self.widget1.setGeometry(QtCore.QRect(10, 30, 296, 156))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.clickBox)
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_7.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setClearButtonEnabled(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_6.addWidget(self.lineEdit_7)
        spacerItem = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setClearButtonEnabled(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.label_17 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setClearButtonEnabled(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_2.addWidget(self.lineEdit_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setClearButtonEnabled(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_3.addWidget(self.lineEdit_10)
        self.label_18 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setClearButtonEnabled(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_3.addWidget(self.lineEdit_13)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(280, 220, 311, 51))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.widget2 = QtWidgets.QWidget(self.groupBox_4)
        self.widget2.setGeometry(QtCore.QRect(10, 0, 291, 51))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.draw)
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clear)
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 20, 571, 251))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../../../Downloads/ezgif.com-gif-maker.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 280, 581, 341))
        self.tableView.setObjectName("tableView")
        df = empty_df()
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.widget5 = QtWidgets.QWidget(self.groupBox)
        self.widget5.setGeometry(QtCore.QRect(11, 30, 245, 116))
        self.widget5.setObjectName("widget5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1179, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.triggered.connect(self.reset)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_3.triggered.connect(self.fill)
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "11.3 Балашов 381903-3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Vn₁ ( xₙ )"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Vn₂ ( xₙ )"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Vn₂ ( Vn₁ )"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Параметры задачи Коши"))
        self.label_9.setText(_translate("MainWindow", "u\'(0)"))
        self.label_8.setText(_translate("MainWindow", "u(0), см"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Параметры метода"))
        self.checkBox.setText(_translate("MainWindow", "Использование контроля локальной погрешности"))
        self.label_7.setText(_translate("MainWindow", "Параметр контроля"))
        self.label_15.setText(_translate("MainWindow", "Граница по x"))
        self.label_17.setText(_translate("MainWindow", "Точность выхода по x"))
        self.label_16.setText(_translate("MainWindow", "Макс. количество шагов"))
        self.label_18.setText(_translate("MainWindow", "Начальный шаг"))
        self.pushButton_2.setText(_translate("MainWindow", "Построить"))
        self.pushButton.setText(_translate("MainWindow", "Стереть"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры системы"))
        self.label_2.setText(_translate("MainWindow", "k, Н/см"))
        self.label_3.setText(_translate("MainWindow", "k*, Н/см"))
        self.label.setText(_translate("MainWindow", "m, Н*с²/см"))
        self.label_5.setText(_translate("MainWindow", "c"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "Сбросить"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_3.setText(_translate("MainWindow", "Загрузить шаблон"))
        self.action_3.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_4.setText(_translate("MainWindow", "Справка"))
        self.action_5.setText(_translate("MainWindow", "Справка"))
        self.action_6.setText(_translate("MainWindow", "Описание задачи"))
    
    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            self.label_7.setEnabled(True)
            self.lineEdit_7.setEnabled(True)
            self.control = True
        else:
            self.label_7.setEnabled(False)
            self.lineEdit_7.setEnabled(False)
            self.control = False
        print(self.control)

    def draw(self):
        try:
            m = float(self.lineEdit_5.text())
            k = float(self.lineEdit_2.text())
            c = float(self.lineEdit.text())
            ks = float(self.lineEdit_3.text())
            v1 = float(self.lineEdit_8.text())
            v2 = float(self.lineEdit_11.text())
            step = float(self.lineEdit_13.text())
            max_steps = float(self.lineEdit_10.text())
            if self.control == True:
                control_val = float(self.lineEdit_7.text())
            else:
                control_val = 0
            limit = float(self.lineEdit_9.text())
            limit_acc = float(self.lineEdit_12.text())

            self.label_24.setPixmap(QtGui.QPixmap("blank.png"))
            self.label_25.setPixmap(QtGui.QPixmap("blank.png"))
            self.label_26.setPixmap(QtGui.QPixmap("blank.png"))
            df = create_df(m, k, c, ks, v1, v2, step, max_steps, self.control, control_val, limit, limit_acc)

            self.ax1.plot(df['vn2'], df['vn1'])
            self.fig1.savefig('both.png')

            self.ax2.plot(df['xn'], df['vn1'])
            self.fig2.savefig('vn2.png')

            self.ax3.plot(df['xn'], df['vn2'])
            self.fig3.savefig('vn1.png')

            model = PandasModel(df)
            self.tableView.setModel(model)
            self.label_24.setPixmap(QtGui.QPixmap("vn1.png"))
            self.label_25.setPixmap(QtGui.QPixmap("vn2.png"))
            self.label_26.setPixmap(QtGui.QPixmap("both.png"))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода')
            msg.setText('Проверьте введенные данные!')
            msg.setIcon(QtWidgets.QMessageBox.Critical)

            x = msg.exec_()

    def clear(self):
        df = empty_df()
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.label_24.setPixmap(QtGui.QPixmap("blank.png"))
        self.label_25.setPixmap(QtGui.QPixmap("blank.png"))
        self.label_26.setPixmap(QtGui.QPixmap("blank.png"))

    def fill(self):
        self.checkBox.setChecked(True)
        self.control = True
        self.lineEdit_5.setText('0.1')
        self.lineEdit_2.setText('2')
        self.lineEdit.setText('0.15')
        self.lineEdit_3.setText('2')
        self.lineEdit_8.setText('10')
        self.lineEdit_11.setText('0')
        self.lineEdit_13.setText('0.001')
        self.lineEdit_10.setText('10000')
        self.lineEdit_7.setText('0.0001')
        self.lineEdit_9.setText('20')
        self.lineEdit_12.setText('0.001')


    def reset(self):
        self.checkBox.setChecked(False)
        self.control = False
        self.lineEdit_5.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_12.setText('')

class PandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
