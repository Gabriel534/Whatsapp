# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdicionarContato_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(334, 207)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEditNome = QLineEdit(self.centralwidget)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setMaxLength(100)

        self.verticalLayout.addWidget(self.lineEditNome)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEditEmail = QLineEdit(self.centralwidget)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setMaxLength(100)

        self.verticalLayout.addWidget(self.lineEditEmail)

        self.pushButtonAdicionarContato = QPushButton(self.centralwidget)
        self.pushButtonAdicionarContato.setObjectName(u"pushButtonAdicionarContato")

        self.verticalLayout.addWidget(self.pushButtonAdicionarContato)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 334, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Novo Contato", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome*", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email*", None))
        self.pushButtonAdicionarContato.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
    # retranslateUi

