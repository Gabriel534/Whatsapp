# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(816, 582)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u" QScrollArea {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 8px;\n"
"                background-color: #f0f0f0;\n"
"            }\n"
"\n"
"            QScrollArea > QWidget {\n"
"                background-color: transparent;\n"
"            }\n"
"\n"
"            QScrollBar:vertical {\n"
"                width: 12px;\n"
"            }\n"
"\n"
"            QScrollBar::handle:vertical {\n"
"                background: #d3d3d3;\n"
"                border-radius: 6px;\n"
"            }\n"
"\n"
"            QScrollBar::handle:vertical:hover {\n"
"                background: #b0b0b0;\n"
"            }\n"
"\n"
"            QScrollBar::add-line:vertical,\n"
"            QScrollBar::sub-line:vertical {\n"
"                border: none;\n"
"                background: transparent;}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignVCenter)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.User = QPushButton(self.centralwidget)
        self.User.setObjectName(u"User")
        self.User.setStyleSheet(u"QPushButton {\n"
"                background-color: #f0f0f0;\n"
"                border: 1px solid #d3d3d3;\n"
"                padding: 10px;\n"
"                text-align: left;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #e0e0e0;\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #c0c0c0;\n"
"                border: 1px solid #b0b0b0;\n"
"            }")

        self.verticalLayout_5.addWidget(self.User)

        self.Chats = QScrollArea(self.centralwidget)
        self.Chats.setObjectName(u"Chats")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Chats.sizePolicy().hasHeightForWidth())
        self.Chats.setSizePolicy(sizePolicy)
        self.Chats.setMinimumSize(QSize(250, 500))
        self.Chats.setMaximumSize(QSize(16777215, 500))
        font = QFont()
        font.setPointSize(9)
        self.Chats.setFont(font)
        self.Chats.setStyleSheet(u"")
        self.Chats.setLineWidth(1)
        self.Chats.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Chats.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Chats.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 248, 498))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Chats.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.Chats)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget_3)

        self.Conversa = QScrollArea(self.widget_2)
        self.Conversa.setObjectName(u"Conversa")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Conversa.sizePolicy().hasHeightForWidth())
        self.Conversa.setSizePolicy(sizePolicy1)
        self.Conversa.setMinimumSize(QSize(500, 400))
        self.Conversa.setMaximumSize(QSize(16777215, 16777215))
        self.Conversa.setStyleSheet(u" QScrollArea {\\n                border: 1px solid #d3d3d3;\\n                border-radius: 8px;\\n                background-color: #f0f0f0;\\n            }\\n\\n            QScrollArea > QWidget {\\n                background-color: transparent;\\n            }\\n\\n            QScrollBar:vertical {\\n                width: 12px;\\n            }\\n\\n            QScrollBar::handle:vertical {\\n                background: #d3d3d3;\\n                border-radius: 6px;\\n            }\\n\\n            QScrollBar::handle:vertical:hover {\\n                background: #b0b0b0;\\n            }\\n\\n            QScrollBar::add-line:vertical,\\n            QScrollBar::sub-line:vertical {\\n                border: none;\\n                background: transparent;}")
        self.Conversa.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 498, 429))
        self.Conversa.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.Conversa)

        self.textEdit = QTextEdit(self.widget_2)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMaximumSize(QSize(16777215, 26))
        self.textEdit.setStyleSheet(u"background-color: rgb(241, 240, 255);")

        self.verticalLayout.addWidget(self.textEdit)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 816, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.User.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pessoal Tal", None))
    # retranslateUi
