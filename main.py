from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel,
    QPushButton)
from PySide6.QtGui import QIcon
from Whatsapp.variaveis import TAMANHO_MAXIMO_LOGIN, TAMANHO_MAXIMO_SENHA, ICON


class UserLogin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        central = QWidget()
        _layout = QVBoxLayout()
        self.setWindowIcon(QIcon(str(ICON)))

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

        central.setLayout(_layout)
        self.setCentralWidget(central)


if __name__ == "__main__":
    app = QApplication()
    window = UserLogin()
    window.show()
    app.exec()
