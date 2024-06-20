from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):  # Настройка основного окна
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 600)
        # Создание центрального виджета для основного окна
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")  # Создание левой боковой панели
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 91, 661))
        self.frame.setStyleSheet("background-color:rgb(20, 20, 20)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame)  # Добавление кнопки-ссылки в боковую панель
        self.commandLinkButton.setGeometry(QtCore.QRect(40, 40, 31, 48))
        self.commandLinkButton.setText("")
        self.commandLinkButton.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtWidgets.QLabel(self.frame)  # Добавление метки в боковую панель
        self.label.setGeometry(QtCore.QRect(20, 500, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget) # Создание первой панели справа от боковой панели
        self.frame_4.setGeometry(QtCore.QRect(100, 20, 281, 261))
        self.frame_4.setStyleSheet("background-color: rgb(100, 100, 100); border: 1px rgb(100, 100, 100); border-radius: 10px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)  # Создание второй панели справа от первой панели
        self.frame_5.setGeometry(QtCore.QRect(410, 20, 371, 261))
        self.frame_5.setStyleSheet("background-color: rgb(214, 214, 214); border: 1px rgb(100, 100, 100); border-radius: 10px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5) # Добавление меток во вторую панель
        self.label_2.setGeometry(QtCore.QRect(10, 10, 351, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 351, 201))
        self.label_3.setObjectName("label_3")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(100, 310, 281, 271)) # Создание третьей панели снизу от первой панели
        self.frame_6.setStyleSheet("background-color: rgb(214, 214, 214); border: 1px rgb(100, 100, 100); border-radius: 10px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_5 = QtWidgets.QLabel(self.frame_6) # Добавление меток в третью панель
        self.label_5.setGeometry(QtCore.QRect(110, 90, 55, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 251, 171))
        self.label_6.setObjectName("label_6")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)  # Создание четвёртой панели справа от третьей панели
        self.frame_7.setGeometry(QtCore.QRect(410, 310, 371, 271))
        self.frame_7.setStyleSheet("background-color: rgb(214, 214, 214); border: 1px rgb(100, 100, 100); border-radius: 10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)  # Создание четвёртой панели справа от третьей панели
        self.label_4.setGeometry(QtCore.QRect(20, 20, 351, 221))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)  # Установка центрального виджета основного окна

        self.retranslateUi(MainWindow) # Текст
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "dish1"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff5500;\">Тыквенный крем-суп</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">Время приготовления: 40 минут<br/><br/>Сложность: Легкая<br/><br/>Распространенный аллерген:<br/>Молоко</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">- Тыква<br/>- Морковь<br/>- Лук<br/>- Чеснок<br/>- Овощной бульон<br/>- Сливки<br/></span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#000000;\">ИНСТРУКЦИЯ:</span><span style=\" font-size:20pt; color:#000000;\"><br/><br/></span><span style=\" font-size:14pt; color:#000000;\">1. Нарежте тыкву<br/>2. Обжарьте тыкву с овощами<br/>3. Добавьте бульон и сливки<br/>4. Измельчить до однородности</span></p></body></html>"))
