from typing import Optional
import PySide6.QtCore
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel,
    QPushButton, QHBoxLayout, QStatusBar)
from PySide6.QtGui import QIcon, QKeyEvent
from variaveis import TAMANHO_MAXIMO_LOGIN, TAMANHO_MAXIMO_SENHA, ICON, SERVERIP, SERVERPORT
from login import login
import socket
from _main import Main
from telaCadastro import Ui_MainWindow

# Classe da tela de cadastro


class Cadastrar(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())


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
        self.lineEditLogin = QLineEdit()
        self.lineEditLogin.setMaxLength(TAMANHO_MAXIMO_LOGIN)
        self.textSenha = QLabel("Senha")

        self.lineEditSenha = LineEditSenha(self)

        self.lineEditSenha.setMaxLength(TAMANHO_MAXIMO_SENHA)

        self._layout.addWidget(self.textLogin)
        self._layout.addWidget(self.lineEditLogin)
        self._layout.addWidget(self.textSenha)
        self._layout.addWidget(self.lineEditSenha)
        self._layout.addLayout(self.layoutButtons)

        self.entrarButton.clicked.connect(self.logar)
        self.cadastrarButton.clicked.connect(self.cadastrar)

        central.setLayout(self._layout)
        self.setCentralWidget(central)

    def logar(self):
        if self.lineEditLogin.text() == "" or self.lineEditSenha.text() == "":
            self.statusBar().setStatusTip("Login e/ou senha não preenchidos")
            return
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((SERVERIP, SERVERPORT))
        dados = login(cliente, self.lineEditLogin.text(),
                      self.lineEditSenha.text())
        cliente.close()
        if dados is None:
            self.statusBar().setStatusTip("Erro! Login ou senha incorretos")
        elif dados == 0:
            self.statusBar().setStatusTip("Erro ao se comunicar com o servidor")
        else:
            self.main = Main(dados)  # type: ignore
            self.main.show()
            print(dados)
            self.fecharJanela()

    def fecharJanela(self):
        self.layoutButtons.deleteLater()
        self.textLogin.deleteLater()
        self.lineEditLogin.deleteLater()
        self.textSenha.deleteLater()
        self.lineEditSenha.deleteLater()
        self._layout.deleteLater()
        self.deleteLater()

    def cadastrar(self):
        self.telaCadastro = Cadastrar()
        self.telaCadastro.show()
        self.fecharJanela()

# Classe que permite o line edit da senha cadastrar ao clickar em enter


class LineEditSenha(QLineEdit):
    def __init__(self, parent: UserLogin):
        super().__init__()
        self.parents = parent

    def keyPressEvent(self, arg__1: QKeyEvent) -> None:
        KEYS = Qt.Key
        if arg__1.key() in [KEYS.Key_Enter, KEYS.Key_Return]:
            self.parents.logar()
        return super().keyPressEvent(arg__1)


if __name__ == "__main__":
    app = QApplication()
    window = UserLogin()
    window.show()
    app.exec()
