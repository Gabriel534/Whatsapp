from typing import Optional
import PySide6.QtCore
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel,
    QPushButton, QHBoxLayout)
from PySide6.QtGui import QIcon
from variaveis import TAMANHO_MAXIMO_LOGIN, TAMANHO_MAXIMO_SENHA, ICON


class UserLogin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        central = QWidget()
        _layout = QVBoxLayout()
        entrarButton = QPushButton("Entrar")
        cadastrarButton = QPushButton("Cadastrar")
        layoutButtons = QHBoxLayout()
        layoutButtons.addWidget(entrarButton)
        layoutButtons.addWidget(cadastrarButton)
        self.setWindowIcon(QIcon(str(ICON)))
        self.setWindowTitle("Whatsapp2")
        self.setMinimumSize(QSize(300, 125))

        textLogin = QLabel("Login")
        labelLogin = QLineEdit()
        labelLogin.setMaxLength(TAMANHO_MAXIMO_LOGIN)
        textSenha = QLabel("Senha")
        labelSenha = QLineEdit()
        labelSenha.setMaxLength(TAMANHO_MAXIMO_SENHA)

        _layout.addWidget(textLogin)
        _layout.addWidget(labelLogin)
        _layout.addWidget(textSenha)
        _layout.addWidget(labelSenha)
        _layout.addLayout(layoutButtons)

        entrarButton.clicked.connect(self.logar)
        cadastrarButton.clicked.connect(self.cadastrar)

        central.setLayout(_layout)
        self.setCentralWidget(central)

    def logar(self):
        print("Implementar login")

    def cadastrar(self):
        print("Implementar cadastro")


if __name__ == "__main__":
    app = QApplication()
    window = UserLogin()
    window.show()
    app.exec()
