# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TelaCadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 501)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #f0f0f0;\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 20px;\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonVoltar = QPushButton(self.widget_7)
        self.pushButtonVoltar.setObjectName(u"pushButtonVoltar")
        self.pushButtonVoltar.setMaximumSize(QSize(40, 16777215))
        self.pushButtonVoltar.setAutoDefault(False)
        self.pushButtonVoltar.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButtonVoltar)

        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(424745, 20))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelNome = QLabel(self.widget_2)
        self.labelNome.setObjectName(u"labelNome")

        self.verticalLayout_2.addWidget(self.labelNome)

        self.lineEditNome = QLineEdit(self.widget_2)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_2.addWidget(self.lineEditNome)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelTelefone = QLabel(self.widget_5)
        self.labelTelefone.setObjectName(u"labelTelefone")

        self.verticalLayout_6.addWidget(self.labelTelefone)

        self.lineEditTelefone = QLineEdit(self.widget_5)
        self.lineEditTelefone.setObjectName(u"lineEditTelefone")
        self.lineEditTelefone.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_6.addWidget(self.lineEditTelefone)


        self.verticalLayout_8.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelEmail = QLabel(self.widget_3)
        self.labelEmail.setObjectName(u"labelEmail")

        self.verticalLayout_4.addWidget(self.labelEmail)

        self.lineEditEmail = QLineEdit(self.widget_3)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_4.addWidget(self.lineEditEmail)


        self.verticalLayout_8.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.labelSenha = QLabel(self.widget_6)
        self.labelSenha.setObjectName(u"labelSenha")

        self.verticalLayout_7.addWidget(self.labelSenha)

        self.lineEditSenha = QLineEdit(self.widget_6)
        self.lineEditSenha.setObjectName(u"lineEditSenha")
        self.lineEditSenha.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_7.addWidget(self.lineEditSenha)


        self.verticalLayout_8.addWidget(self.widget_6)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelSenha2 = QLabel(self.widget)
        self.labelSenha2.setObjectName(u"labelSenha2")

        self.verticalLayout.addWidget(self.labelSenha2)

        self.lineEditSenha2 = QLineEdit(self.widget)
        self.lineEditSenha2.setObjectName(u"lineEditSenha2")
        self.lineEditSenha2.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.lineEditSenha2)


        self.verticalLayout_8.addWidget(self.widget)

        self.pushButtonCadastrar = QPushButton(self.centralwidget)
        self.pushButtonCadastrar.setObjectName(u"pushButtonCadastrar")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonCadastrar.sizePolicy().hasHeightForWidth())
        self.pushButtonCadastrar.setSizePolicy(sizePolicy1)
        self.pushButtonCadastrar.setMinimumSize(QSize(310, 0))
        self.pushButtonCadastrar.setMaximumSize(QSize(300, 16777215))
        self.pushButtonCadastrar.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonCadastrar.setAutoFillBackground(False)
        self.pushButtonCadastrar.setFlat(False)

        self.verticalLayout_8.addWidget(self.pushButtonCadastrar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 338, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButtonVoltar.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonVoltar.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cadastro                       ", None))
        self.labelNome.setText(QCoreApplication.translate("MainWindow", u"Nome*", None))
        self.labelTelefone.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.lineEditTelefone.setInputMask(QCoreApplication.translate("MainWindow", u"(00) 0000-0000", None))
        self.labelEmail.setText(QCoreApplication.translate("MainWindow", u"Email*", None))
        self.labelSenha.setText(QCoreApplication.translate("MainWindow", u"Senha*", None))
        self.labelSenha2.setText(QCoreApplication.translate("MainWindow", u"Repita sua senha*", None))
        self.pushButtonCadastrar.setText(QCoreApplication.translate("MainWindow", u"                                      Cadastrar", None))
    # retranslateUi

