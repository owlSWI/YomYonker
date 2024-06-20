from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    # Устанавливает основные параметры главного окна
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 631)
        MainWindow.setStyleSheet("background-color: lightgray")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # Создает центральный виджет
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -30, 251, 661))
        self.frame.setStyleSheet("background-color:rgb(20, 20, 20)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # Создает и настраивает внутренний фрейм (frame_2) в боковой панели
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 110, 221, 241))
        self.frame_2.setStyleSheet("background-color: rgb(100, 100, 100); border: 1px rgb(100, 100, 100); border-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        # Создает и настраивает кнопку "Завтрак"
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2) # ЗАВТРАК
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 202, 31))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setTabletTracking(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"border-width: 1px;\n"
" border-radius: 10px;\n"
" font: bold 20px;\n"
" min-width: 8em;\n"
" padding: 5px;")
        # Создает и настраивает кнопку "Обед"
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_6.clicked.connect(self.open_new_window_Breakfast)  # открытие окна
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2) # ОБЕД
        self.pushButton_7.setGeometry(QtCore.QRect(10, 50, 202, 31))
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setTabletTracking(False)
        self.pushButton_7.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"border-width: 1px;\n"
" border-radius: 10px;\n"
" font: bold 20px;\n"
" min-width: 8em;\n"
" padding: 5px;")
        # Создает и настраивает кнопку "Ужин"
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_7.clicked.connect(self.open_new_window_Dinner)  # открытие окна
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2) # УЖИН
        self.pushButton_11.setGeometry(QtCore.QRect(10, 90, 202, 31))
        self.pushButton_11.setMouseTracking(False)
        self.pushButton_11.setTabletTracking(False)
        self.pushButton_11.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"border-width: 1px;\n"
" border-radius: 10px;\n"
" font: bold 20px;\n"
" min-width: 8em;\n"
" padding: 5px;")
        # Создает и настраивает кнопку "Салаты"
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_11.clicked.connect(self.open_new_window_Supper)  # открытие окна
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2) # САЛАТЫ
        self.pushButton_8.setGeometry(QtCore.QRect(10, 130, 202, 31))
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setTabletTracking(False)
        self.pushButton_8.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"border-width: 1px;\n"
" border-radius: 10px;\n"
" font: bold 20px;\n"
" min-width: 8em;\n"
" padding: 5px;")
        # Создает и настраивает кнопку "Закуски"
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.clicked.connect(self.open_new_window_Salads)  # открытие окна
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2) # ЗАКУСКИ
        self.pushButton_9.setGeometry(QtCore.QRect(10, 170, 202, 31))
        self.pushButton_9.setMouseTracking(False)
        self.pushButton_9.setTabletTracking(False)
        self.pushButton_9.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"border-width: 1px;\n"
" border-radius: 10px;\n"
" font: bold 20px;\n"
" min-width: 8em;\n"
" padding: 5px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_9.clicked.connect(self.open_new_window_Snacks)  # открытие окна
        # Создает и настраивает виджет в боковой панели
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(20, 400, 221, 251))
        self.widget.setStyleSheet("background-color: rgb(100, 100, 100); border: 1px rgb(100, 100, 100); border-radius: 10px;")
        self.widget.setObjectName("widget")
        # Создает и настраивает область прокрутки внутри виджета
        self.scrollArea_2 = QtWidgets.QScrollArea(self.widget)
        self.scrollArea_2.setGeometry(QtCore.QRect(9, 9, 169, 312))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        # Создает содержимое для области прокрутки
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 173, 2735))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        # Создает вертикальный лэйаут для размещения чекбоксов внутри области прокрутки
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_40 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_40.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_40.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_40.setObjectName("checkBox_40")
        self.verticalLayout.addWidget(self.checkBox_40)
        self.checkBox_39 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_39.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_39.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_39.setObjectName("checkBox_39")
        self.verticalLayout.addWidget(self.checkBox_39)
        self.checkBox_38 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_38.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_38.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_38.setObjectName("checkBox_38")
        self.verticalLayout.addWidget(self.checkBox_38)
        self.checkBox_37 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_37.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_37.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_37.setObjectName("checkBox_37")
        self.verticalLayout.addWidget(self.checkBox_37)
        self.checkBox_36 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_36.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_36.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_36.setObjectName("checkBox_36")
        self.verticalLayout.addWidget(self.checkBox_36)
        self.checkBox_35 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_35.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_35.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_35.setObjectName("checkBox_35")
        self.verticalLayout.addWidget(self.checkBox_35)
        self.checkBox_34 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_34.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_34.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_34.setObjectName("checkBox_34")
        self.verticalLayout.addWidget(self.checkBox_34)
        self.checkBox_33 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_33.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_33.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_33.setObjectName("checkBox_33")
        self.verticalLayout.addWidget(self.checkBox_33)
        self.checkBox_32 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_32.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_32.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_32.setObjectName("checkBox_32")
        self.verticalLayout.addWidget(self.checkBox_32)
        self.checkBox_31 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_31.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_31.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_31.setObjectName("checkBox_31")
        self.verticalLayout.addWidget(self.checkBox_31)
        self.checkBox_30 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_30.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_30.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_30.setObjectName("checkBox_30")
        self.verticalLayout.addWidget(self.checkBox_30)
        self.checkBox_29 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_29.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_29.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_29.setObjectName("checkBox_29")
        self.verticalLayout.addWidget(self.checkBox_29)
        self.checkBox_28 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_28.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_28.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_28.setObjectName("checkBox_28")
        self.verticalLayout.addWidget(self.checkBox_28)
        self.checkBox_27 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_27.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_27.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_27.setObjectName("checkBox_27")
        self.verticalLayout.addWidget(self.checkBox_27)
        self.checkBox_26 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_26.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_26.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_26.setObjectName("checkBox_26")
        self.verticalLayout.addWidget(self.checkBox_26)
        self.checkBox_25 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_25.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_25.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_25.setObjectName("checkBox_25")
        self.verticalLayout.addWidget(self.checkBox_25)
        self.checkBox_24 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_24.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_24.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_24.setObjectName("checkBox_24")
        self.verticalLayout.addWidget(self.checkBox_24)
        self.checkBox_23 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_23.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_23.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_23.setObjectName("checkBox_23")
        self.verticalLayout.addWidget(self.checkBox_23)
        self.checkBox_22 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_22.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_22.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_22.setObjectName("checkBox_22")
        self.verticalLayout.addWidget(self.checkBox_22)
        self.checkBox_21 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_21.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_21.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_21.setObjectName("checkBox_21")
        self.verticalLayout.addWidget(self.checkBox_21)
        self.checkBox_20 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_20.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_20.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_20.setObjectName("checkBox_20")
        self.verticalLayout.addWidget(self.checkBox_20)
        self.checkBox_19 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_19.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_19.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_19.setObjectName("checkBox_19")
        self.verticalLayout.addWidget(self.checkBox_19)
        self.checkBox_18 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_18.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_18.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_18.setObjectName("checkBox_18")
        self.verticalLayout.addWidget(self.checkBox_18)
        self.checkBox_17 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_17.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_17.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_17.setObjectName("checkBox_17")
        self.verticalLayout.addWidget(self.checkBox_17)
        self.checkBox_16 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_16.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_16.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout.addWidget(self.checkBox_16)
        self.checkBox_15 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_15.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_15.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout.addWidget(self.checkBox_15)
        self.checkBox_14 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_14.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_14.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout.addWidget(self.checkBox_14)
        self.checkBox_13 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_13.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_13.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout.addWidget(self.checkBox_13)
        self.checkBox_12 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_12.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_12.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout.addWidget(self.checkBox_12)
        self.checkBox_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_11.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_11.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout.addWidget(self.checkBox_11)
        self.checkBox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_10.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_10.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout.addWidget(self.checkBox_10)
        self.checkBox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_9.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_9.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout.addWidget(self.checkBox_9)
        self.checkBox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_8.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_8.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout.addWidget(self.checkBox_8)
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_7.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_7.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_6.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_6.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_5.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_5.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_4.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_4.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_3.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_3.setStyleSheet("color:rgb(211, 207, 204)")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_2.setMinimumSize(QtCore.QSize(151, 61))
        self.checkBox_2.setStyleSheet("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 50, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 350, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        # Устанавливает содержимое области прокрутки
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(240, 0, 561, 631))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 629))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setGeometry(QtCore.QRect(20, 20, 481, 211))
        self.frame_3.setStyleSheet("background-color: rgb(191, 191, 191); border: 1px rgb(191, 191, 191); border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 221, 191))
        self.frame_4.setStyleSheet("background-color: rgb(100, 100, 100); border: 1px rgb(100, 100, 100); border-radius: 10px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_10.setGeometry(QtCore.QRect(250, 10, 202, 31))
        self.pushButton_10.setMouseTracking(False)
        self.pushButton_10.setTabletTracking(False)
        self.pushButton_10.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-width: 1px;\n"
" border-radius: 10px;\n"
" font: bold 20px;\n"
" min-width: 8em;\n"
" padding: 5px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_10.clicked.connect(self.open_new_window1)  # открытие окна
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setGeometry(QtCore.QRect(20, 240, 481, 211))
        self.frame_5.setStyleSheet("background-color: rgb(191, 191, 191); border: 1px rgb(191, 191, 191); border-radius: 10px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setGeometry(QtCore.QRect(10, 10, 221, 191))
        self.frame_7.setStyleSheet("background-color: rgb(100, 100, 100); border: 1px rgb(100, 100, 100); border-radius: 10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_13.setGeometry(QtCore.QRect(250, 10, 202, 31))
        self.pushButton_13.setMouseTracking(False)
        self.pushButton_13.setTabletTracking(False)
        self.pushButton_13.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-width: 1px;\n"
" border-radius: 10px;\n"
" font: bold 20px;\n"
" min-width: 8em;\n"
" padding: 5px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_13.clicked.connect(self.open_new_window2)  # открытие окна
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setGeometry(QtCore.QRect(20, 460, 481, 211))
        self.frame_8.setStyleSheet("background-color: rgb(191, 191, 191); border: 1px rgb(191, 191, 191); border-radius: 10px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setGeometry(QtCore.QRect(10, 10, 221, 191))
        self.frame_10.setStyleSheet("background-color: rgb(100, 100, 100); border: 1px rgb(100, 100, 100); border-radius: 10px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_15.setGeometry(QtCore.QRect(250, 10, 202, 31))
        self.pushButton_15.setMouseTracking(False)
        self.pushButton_15.setTabletTracking(False)
        self.pushButton_15.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-width: 1px;\n"
" border-radius: 10px;\n"
" font: bold 20px;\n"
" min-width: 8em;\n"
" padding: 5px;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_15.clicked.connect(self.open_new_window3)  # открытие окна
        self.verticalSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.verticalSlider.setGeometry(QtCore.QRect(520, 20, 22, 601))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.frame.raise_()
        # Настраивает главный виджет и центральное окно
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Переопределяет заголовки виджетов в главном окне
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "Завтрак"))
        self.pushButton_7.setText(_translate("MainWindow", "Обед"))
        self.pushButton_11.setText(_translate("MainWindow", "Ужин"))
        self.pushButton_8.setText(_translate("MainWindow", "Салаты"))
        self.pushButton_9.setText(_translate("MainWindow", "Закуски"))
        self.checkBox.setText(_translate("MainWindow", "Говядина на кости"))
        self.checkBox_40.setText(_translate("MainWindow", "Творог"))
        self.checkBox_39.setText(_translate("MainWindow", "Сливочный сыр"))
        self.checkBox_38.setText(_translate("MainWindow", "Яйца"))
        self.checkBox_37.setText(_translate("MainWindow", "Молоко"))
        self.checkBox_36.setText(_translate("MainWindow", "Соль"))
        self.checkBox_35.setText(_translate("MainWindow", "Перец"))
        self.checkBox_34.setText(_translate("MainWindow", "Масло сливочное"))
        self.checkBox_33.setText(_translate("MainWindow", "Петрушка"))
        self.checkBox_32.setText(_translate("MainWindow", "Укроп"))
        self.checkBox_31.setText(_translate("MainWindow", "Свекла"))
        self.checkBox_30.setText(_translate("MainWindow", "Картофель"))
        self.checkBox_29.setText(_translate("MainWindow", "Морковь"))
        self.checkBox_28.setText(_translate("MainWindow", "Капуста"))
        self.checkBox_27.setText(_translate("MainWindow", "Томатная паста"))
        self.checkBox_26.setText(_translate("MainWindow", "Чеснок"))
        self.checkBox_25.setText(_translate("MainWindow", "Говяжий бульон"))
        self.checkBox_24.setText(_translate("MainWindow", "Мясо (говядина)"))
        self.checkBox_23.setText(_translate("MainWindow", "Лавровый лист"))
        self.checkBox_22.setText(_translate("MainWindow", "Масло растительное"))
        self.checkBox_21.setText(_translate("MainWindow", "Сметана"))
        self.checkBox_20.setText(_translate("MainWindow", "Спагетти"))
        self.checkBox_19.setText(_translate("MainWindow", "Томатный соус"))
        self.checkBox_18.setText(_translate("MainWindow", "Оливковое масло"))
        self.checkBox_17.setText(_translate("MainWindow", "Базилик"))
        self.checkBox_16.setText(_translate("MainWindow", "Тертый пармезан"))
        self.checkBox_15.setText(_translate("MainWindow", "Мука"))
        self.checkBox_14.setText(_translate("MainWindow", "Сахар"))
        self.checkBox_13.setText(_translate("MainWindow", "Курица"))
        self.checkBox_12.setText(_translate("MainWindow", "Вермишель"))
        self.checkBox_11.setText(_translate("MainWindow", "Лимон"))
        self.checkBox_10.setText(_translate("MainWindow", "Прованские травы"))
        self.checkBox_9.setText(_translate("MainWindow", "Помидоры"))
        self.checkBox_8.setText(_translate("MainWindow", "Огурцы"))
        self.checkBox_7.setText(_translate("MainWindow", "Красный лук"))
        self.checkBox_6.setText(_translate("MainWindow", "Оливки"))
        self.checkBox_5.setText(_translate("MainWindow", "Фета"))
        self.checkBox_4.setText(_translate("MainWindow", "Орегано"))
        self.checkBox_3.setText(_translate("MainWindow", "Твердый сыр"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.label.setText(_translate("MainWindow", "Рецепты"))
        self.label_2.setText(_translate("MainWindow", "Продукты"))
        self.pushButton_10.setText(_translate("MainWindow", "БЛЮДО 1"))
        self.pushButton_13.setText(_translate("MainWindow", "БЛЮДО 2"))
        self.pushButton_15.setText(_translate("MainWindow", "БЛЮДО 3"))

    #новое окно1
    def open_new_window1(self):
        from aaa1 import Ui_MainWindow1
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        self.window.show()

    #новое окно 2
    def open_new_window2(self):
        from aaa2 import Ui_MainWindow2
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()

    #новое окно3
    def open_new_window3(self):
        from aaa3 import Ui_MainWindow3
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.window.show()

    # Определяет функцию для открытия нового окна для "Завтрака"
    def open_new_window_Breakfast(self):
        from aaaBreakfast import Ui_MainWindow_Breakfast
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Breakfast()
        self.ui.setupUi(self.window)
        self.window.show()

    # Определяет функцию для открытия нового окна для "Обеда"
    def open_new_window_Dinner(self):
        from aaaDinner import Ui_MainWindow_Dinner
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Dinner()
        self.ui.setupUi(self.window)
        self.window.show()

    # Определяет функцию для открытия нового окна для "Ужина"
    def open_new_window_Supper(self):
        from aaaSupper import Ui_MainWindow_Supper
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Supper()
        self.ui.setupUi(self.window)
        self.window.show()

    # Определяет функцию для открытия нового окна для "Салатов"
    def open_new_window_Salads(self):
        from aaaSalads import Ui_MainWindow_Salads
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Salads()
        self.ui.setupUi(self.window)
        self.window.show()


    # Определяет функцию для открытия нового окна для "Закусок"
    def open_new_window_Snacks(self):
        from aaaSnacks import Ui_MainWindow_Snacks
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Snacks()
        self.ui.setupUi(self.window)
        self.window.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
