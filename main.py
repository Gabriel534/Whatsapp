from typing import Optional
import PySide6.QtCore
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel,
    QPushButton, QHBoxLayout, QStatusBar)
from PySide6.QtGui import QIcon
from variaveis import TAMANHO_MAXIMO_LOGIN, TAMANHO_MAXIMO_SENHA, ICON, SERVERIP, SERVERPORT
from login import login
import socket
from _main import Main


class UserLogin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setStatusBar(QStatusBar())

        central = QWidget()
        self._layout = QVBoxLayout()
        self.entrarButton = QPushButton("Entrar")
        self.cadastrarButton = QPushButton("Cadastrar")
        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.addWidget(self.entrarButton)
        self.layoutButtons.addWidget(self.cadastrarButton)
        self.setWindowIcon(QIcon(str(ICON)))
        self.setWindowTitle("Whatsapp2")
        self.setMinimumSize(QSize(300, 125))

        self.textLogin = QLabel("Login")
        self.labelLogin = QLineEdit()
        self.labelLogin.setMaxLength(TAMANHO_MAXIMO_LOGIN)
        self.textSenha = QLabel("Senha")
        self.labelSenha = QLineEdit()
        self.labelSenha.setMaxLength(TAMANHO_MAXIMO_SENHA)

        self._layout.addWidget(self.textLogin)
        self._layout.addWidget(self.labelLogin)
        self._layout.addWidget(self.textSenha)
        self._layout.addWidget(self.labelSenha)
        self._layout.addLayout(self.layoutButtons)

        self.entrarButton.clicked.connect(self.logar)
        self.cadastrarButton.clicked.connect(self.cadastrar)

        central.setLayout(self._layout)
        self.setCentralWidget(central)

    def logar(self):
        if self.labelLogin.text() == "" or self.labelSenha.text() == "":
            self.statusBar().setStatusTip("Login e/ou senha não preenchidos")
            return
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((SERVERIP, SERVERPORT))
        dados = login(cliente, self.labelLogin.text(), self.labelSenha.text())
        cliente.close()
        if dados is None:
            self.statusBar().setStatusTip("Erro! Login ou senha incorretos")
        elif dados == 0:
            self.statusBar().setStatusTip("Erro ao se comunicar com o servidor")
        else:
            self.main = Main(dados)
            self.main.show()
            print(dados)
            self.fecharJanela()

    def fecharJanela(self):
        self.layoutButtons.deleteLater()
        self.textLogin.deleteLater()
        self.labelLogin.deleteLater()
        self.textSenha.deleteLater()
        self.labelSenha.deleteLater()
        self._layout.deleteLater()
        self.deleteLater()

    def cadastrar(self):
        print("Implementar cadastro")


if __name__ == "__main__":
    app = QApplication()
    window = UserLogin()
    window.show()
    app.exec()
