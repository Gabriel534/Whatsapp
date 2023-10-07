from typing import Optional
import PySide6.QtCore
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel,
    QPushButton, QHBoxLayout, QStatusBar)
from PySide6.QtGui import QIcon, QKeyEvent
from variaveis import (TAMANHO_MAXIMO_LOGIN, TAMANHO_MAXIMO_SENHA,
                       ICON, SERVERIP, SERVERPORT, ICON_VOLTAR)
from login import login
import socket
from _main import Main
from telaCadastro import Ui_MainWindow


class UserLogin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        statusBar = QStatusBar()
        statusBar.setSizeGripEnabled(False)

        self.setStatusBar(statusBar)
        self.statusLabel = QLabel()
        self.statusBar().addWidget(self.statusLabel)

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

        self.adjustSize()
        self.setFixedSize(self.size())

    def logar(self):
        if self.lineEditLogin.text() == "" or self.lineEditSenha.text() == "":
            self.statusLabel.setText("Login e/ou senha não preenchidos")
            return
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            cliente.connect((SERVERIP, SERVERPORT))
        except ConnectionRefusedError:
            self.statusLabel.setText("Erro ao se comunicar com o servidor")
            return
        except ConnectionError:
            self.statusLabel.setText("Erro ao se comunicar com o servidor")
            return

        dados = login(cliente, self.lineEditLogin.text(),
                      self.lineEditSenha.text())
        cliente.close()
        if dados is None:
            self.statusLabel.setText("Erro! Login ou senha incorretos")
        elif dados == 0:
            self.statusLabel.setText("Erro ao se comunicar com o servidor")
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
        self.telaCadastro = Cadastrar(self)
        self.telaCadastro.show()
        self.setHidden(True)

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

# Classe da tela de cadastro


class Cadastrar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: UserLogin) -> None:
        super().__init__()
        iconVoltar = QIcon(str(ICON_VOLTAR))
        self.setupUi(self)

        self.setWindowTitle("WhatsApp2")
        self.setWindowIcon(QIcon(str(ICON)))

        self.setFixedSize(self.size())
        self.pushButtonVoltar.setIcon(iconVoltar)
        self.pushButtonVoltar.clicked.connect(lambda: parent.setHidden(False))
        self.pushButtonVoltar.clicked.connect(self.deleteLater)


if __name__ == "__main__":
    app = QApplication()
    window = UserLogin()
    window.show()
    app.exec()
