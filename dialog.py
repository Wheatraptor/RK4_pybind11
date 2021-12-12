from PyQt5 import QtCore, QtGui, QtWidgets

import ctypes
myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(903, 581)
        Dialog.setWindowIcon(QtGui.QIcon('unn.png'))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 40, 471, 531))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("rk4.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 391, 531))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Описание"))
        self.label_2.setText(_translate("Dialog", "Метод Рунге-Кутта явный 4-го порядка для систем ОДУ"))
        self.label_3.setText(_translate("Dialog", "Задача 11, вариант 3"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Груз массы </span><span style=\" font-size:11pt; font-weight:600;\">m </span><span style=\" font-size:11pt;\">может совершать прямолинейные перемещения по горизонтальной плоскости вдоль оси абсцисс. Трение отсутствует. Для стабилизации положения груза используется </span><span style=\" font-size:11pt; font-style:italic;\">система с подвеской </span><span style=\" font-size:11pt;\">: пружина постоянной жесткости </span><span style=\" font-size:11pt; font-weight:600;\">k</span><span style=\" font-size:11pt;\">, демпфер с коэффициентом демпфирования </span><span style=\" font-size:11pt; font-weight:600;\">c</span><span style=\" font-size:11pt;\"> и пружина с нелинейной характеристикой </span><span style=\" font-size:11pt; font-weight:600;\">k*</span><span style=\" font-size:11pt;\">, которые при отклонении груза от равновесного положения создают силы, восстанавливающие равновесие. Пружина с характеристикой </span><span style=\" font-size:11pt; font-weight:600;\">k</span><span style=\" font-size:11pt;\"> создает силу, пропорциональную смещению груза, пружина с характеристикой </span><span style=\" font-size:11pt; font-weight:600;\">k*</span><span style=\" font-size:11pt;\"> - силу, пропорциональную третьей степени смещения (указанные силы действуют в направлении, противоположном смещению), демпфер - силу, пропорциональную скорости (в направлении, противоположном скорости). Положение груза в системе с подвеской описывает нелинейное дифференциальное уравнение:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">m u\'\' + c u\' + k u + k u</span><span style=\" font-size:11pt; font-weight:600; vertical-align:super;\">3 </span><span style=\" font-size:11pt; font-weight:600;\">= 0 ,</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">u(0) = u</span><span style=\" font-size:11pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:11pt; font-weight:600;\"> ; u\'(x</span><span style=\" font-size:11pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:11pt; font-weight:600;\">) = u\'</span><span style=\" font-size:11pt; font-weight:600; vertical-align:sub;\">0 </span><span style=\" font-size:11pt; font-weight:600;\">,</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">где </span><span style=\" font-size:11pt; font-weight:600;\">u(x)</span><span style=\" font-size:11pt;\"> - смещение груза вдоль оси абсцисс относительно положения равновесия, </span><span style=\" font-size:11pt; font-weight:600;\">x</span><span style=\" font-size:11pt;\"> - время, </span><span style=\" font-size:11pt; font-weight:600;\">u</span><span style=\" font-size:11pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:11pt; font-weight:600;\"> </span><span style=\" font-size:11pt;\">начальное отклонение груза от равновесия и </span><span style=\" font-size:11pt; font-weight:600;\">u\'</span><span style=\" font-size:11pt; font-weight:600; vertical-align:sub;\">0 </span><span style=\" font-size:11pt;\">- его начальная скорость.</span></p></body></html>"))


