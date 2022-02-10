# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crawingUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QLabel, QLineEdit,
                               QPushButton)


class Ui_imgDownload(object):
    def setupUi(self, imgDownload):
        if not imgDownload.objectName():
            imgDownload.setObjectName(u"imgDownload")
        imgDownload.setWindowModality(Qt.NonModal)
        imgDownload.resize(539, 396)
        imgDownload.setMinimumSize(QSize(50, 50))
        imgDownload.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"\u661f\u661f.png", QSize(), QIcon.Normal, QIcon.Off)
        imgDownload.setWindowIcon(icon)
        imgDownload.setAutoFillBackground(False)
        imgDownload.setStyleSheet(u"")
        self.frame = QFrame(imgDownload)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(130, 10, 311, 301))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 220, 171, 31))
        self.lineEdit.setStyleSheet(u"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 260, 101, 31))
        self.pushButton.setMinimumSize(QSize(10, 10))
        self.pushButton.setStyleSheet(u"")
        self.label2 = QLabel(self.frame)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(30, 40, 221, 171))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label2.setFont(font)
        self.label2.setLayoutDirection(Qt.LeftToRight)
        self.label2.setAutoFillBackground(False)
        self.label2.setLineWidth(0)
        self.label2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label2.setWordWrap(True)
        self.label2.setMargin(7)
        self.label2.setIndent(1)
        self.label2.setOpenExternalLinks(False)
        self.label2.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 0, 121, 51))
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.frame2 = QFrame(imgDownload)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setGeometry(QRect(-20, -10, 571, 421))
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.frame2.raise_()
        self.frame.raise_()

        self.retranslateUi(imgDownload)

        QMetaObject.connectSlotsByName(imgDownload)

    # setupUi

    def retranslateUi(self, imgDownload):
        imgDownload.setWindowTitle(QCoreApplication.translate("imgDownload", u"\u58c1\u7eb8\u4e0b\u8f7d\u5668", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("imgDownload",
                                                                    u"\u8bf7\u8f93\u5165\u60a8\u60f3\u4e0b\u8f7d\u7684\u58c1\u7eb8\u7c7b\u578b\uff1a",
                                                                    None))
        self.pushButton.setText(
            QCoreApplication.translate("imgDownload", u"\u70b9\u51fb\u5f00\u59cb\u4e0b\u8f7d\u58c1\u7eb8", None))
        self.label2.setText(QCoreApplication.translate("imgDownload",
                                                       u"1.\u7f8e\u5973 	2.\u660e\u661f 	3.\u5f71\u89c6 	4.\u52a8\u6f2b 	5.\u5361\u901a	6.\u6c7d\u8f66	7.\u7231\u60c5	8.\u6e38\u620f	9.\u4f53\u80b2	10.\u8f66\u6a21	11.\u98ce\u666f	12.\u54c1\u724c	13.\u53ef\u7231	14.\u8282\u65e5	15.\u5efa\u7b51	16.\u690d\u7269	17.\u52a8\u7269	18.\u521b\u610f	19.\u7cbe\u7f8e                ",
                                                       None))
        self.label.setText(
            QCoreApplication.translate("imgDownload", u"\u624b\u673a\u58c1\u7eb8\u4e0b\u8f7d\u5668", None))
    # retranslateUi
