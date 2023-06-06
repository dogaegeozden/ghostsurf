# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(410, 240)
        icon = QIcon()
        icon.addFile(u":/logos/ghostsurf.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"	background: #231f1f;\n"
"}")
        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(0, 0, 100, 100))
        self.logo_label.setPixmap(QPixmap(u":/logos/ghostsurf.png"))
        self.logo_label.setScaledContents(True)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(130, 20, 250, 50))
        font = QFont()
        font.setFamily(u"Dyuthi")
        font.setPointSize(35)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"#title_label {\n"
"	color: #6bfffb;\n"
"}")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.start_stop_button = QPushButton(self.centralwidget)
        self.start_stop_button.setObjectName(u"start_stop_button")
        self.start_stop_button.setGeometry(QRect(35, 150, 90, 30))
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        self.start_stop_button.setFont(font1)
        self.change_id_button = QPushButton(self.centralwidget)
        self.change_id_button.setObjectName(u"change_id_button")
        self.change_id_button.setGeometry(QRect(160, 150, 90, 30))
        self.my_ip_button = QPushButton(self.centralwidget)
        self.my_ip_button.setObjectName(u"my_ip_button")
        self.my_ip_button.setGeometry(QRect(285, 150, 90, 30))
        self.status_header_label = QLabel(self.centralwidget)
        self.status_header_label.setObjectName(u"status_header_label")
        self.status_header_label.setGeometry(QRect(105, 90, 81, 30))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.status_header_label.setFont(font2)
        self.status_header_label.setStyleSheet(u"#status_header_label {\n"
"	color: white;\n"
"}")
        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(190, 90, 91, 30))
        self.status_label.setFont(font2)
        self.status_label.setStyleSheet(u"#status_label {\n"
"	color: red;\n"
"}")
        self.status_button = QPushButton(self.centralwidget)
        self.status_button.setObjectName(u"status_button")
        self.status_button.setGeometry(QRect(285, 90, 90, 25))
        self.info_button = QPushButton(self.centralwidget)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(370, 200, 30, 30))
        self.info_button.setStyleSheet(u"#info_button {\n"
"	background: #231f1f;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.info_button.setIcon(icon1)
        self.pandora_bomb_button = QPushButton(self.centralwidget)
        self.pandora_bomb_button.setObjectName(u"pandora_bomb_button")
        self.pandora_bomb_button.setGeometry(QRect(330, 200, 30, 30))
        self.pandora_bomb_button.setStyleSheet(u"#pandora_bomb_button {\n"
"	background: #231f1f;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/bomb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pandora_bomb_button.setIcon(icon2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ghostsurf", None))
        self.logo_label.setText("")
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Ghostsurf", None))
        self.start_stop_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.change_id_button.setText(QCoreApplication.translate("MainWindow", u"Change ID", None))
        self.my_ip_button.setText(QCoreApplication.translate("MainWindow", u"My IP", None))
        self.status_header_label.setText(QCoreApplication.translate("MainWindow", u"Tor Status:", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Deactive", None))
        self.status_button.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.info_button.setText("")
        self.pandora_bomb_button.setText("")
    # retranslateUi

