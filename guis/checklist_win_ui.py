# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checklist_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ChecklistDialog(object):
    def setupUi(self, ChecklistDialog):
        if not ChecklistDialog.objectName():
            ChecklistDialog.setObjectName(u"ChecklistDialog")
        ChecklistDialog.resize(290, 270)
        ChecklistDialog.setStyleSheet(u"#ChecklistDialog {\n"
"	background: #231f1f;\n"
"}")
        self.window_title = QLabel(ChecklistDialog)
        self.window_title.setObjectName(u"window_title")
        self.window_title.setGeometry(QRect(0, 9, 290, 40))
        font = QFont()
        font.setFamily(u"C059")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.window_title.setFont(font)
        self.window_title.setStyleSheet(u"#window_title {\n"
"	color: white;\n"
"}")
        self.window_title.setAlignment(Qt.AlignCenter)
        self.checklist_list_view = QListView(ChecklistDialog)
        self.checklist_list_view.setObjectName(u"checklist_list_view")
        self.checklist_list_view.setGeometry(QRect(0, 60, 290, 210))
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.checklist_list_view.setFont(font1)

        self.retranslateUi(ChecklistDialog)

        QMetaObject.connectSlotsByName(ChecklistDialog)
    # setupUi

    def retranslateUi(self, ChecklistDialog):
        ChecklistDialog.setWindowTitle(QCoreApplication.translate("ChecklistDialog", u"Checklist", None))
        self.window_title.setText(QCoreApplication.translate("ChecklistDialog", u"Anonymity Checklist", None))
    # retranslateUi

