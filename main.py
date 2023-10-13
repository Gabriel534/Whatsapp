from typing import Optional
import PySide6.QtCore
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel,
    QPushButton, QHBoxLayout, QStatusBar)
from PySide6.QtGui import QIcon, QKeyEvent
from variaveis import (TAMANHO_MAXIMO_LOGIN, TAMANHO_MAXIMO_SENHA,
                       ICON, SERVERIP, SERVERPORT, ICON_VOLTAR,
                       RESPOSTA_SOLICITACAO_LOGIN)
from serverConnecter import login, cadastrar
from _main import Main
from telaCadastro import Ui_MainWindow
import re


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

        self.textEmail = QLabel("Email")
        self.lineEditEmail = QLineEdit()
        self.lineEditEmail.setMaxLength(TAMANHO_MAXIMO_LOGIN)
        self.textSenha = QLabel("Senha")

        self.lineEditSenha = LineEditSenha(self)

        self.lineEditSenha.setMaxLength(TAMANHO_MAXIMO_SENHA)

        self._layout.addWidget(self.textEmail)
        self._layout.addWidget(self.lineEditEmail)
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
        if self.lineEditEmail.text() == "" or self.lineEditSenha.text() == "":
            self.statusLabel.setText("Login e/ou senha não preenchidos")
            return
        try:
            dados = login(self.lineEditEmail.text(),
                          self.lineEditSenha.text(), self.statusLabel)
        except ConnectionRefusedError:
            self.statusLabel.setText("Erro na validação do cliente")
            return
        if dados is None:
            self.statusLabel.setText("Login incorreto!")
        elif dados == 0:
            self.statusLabel.setText("Erro ao se comunicar com o servidor")
        elif dados == 1:
            self.statusLabel.setText("Senha incorreta!")
        else:
            self.main = Main(dados)  # type: ignore
            self.main.show()
            print(dados)
            self.fecharJanela()

    def fecharJanela(self):
        self.layoutButtons.deleteLater()
        self.textEmail.deleteLater()
        self.lineEditEmail.deleteLater()
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
        self.setupUi(self)

        iconVoltar = QIcon(str(ICON_VOLTAR))
        self.parents = parent

        # Instanciando a statusBar
        self.statusBarWidget = QStatusBar()
        self.setStatusBar(self.statusBarWidget)
        self.statusBar().setSizeGripEnabled(False)

        # Colocando uma label no statusBar
        self.statusCadastroLabel = QLabel()
        self.statusBar().addWidget(self.statusCadastroLabel)

        self.setWindowTitle("WhatsApp2")
        self.setWindowIcon(QIcon(str(ICON)))

        self.setFixedSize(self.size())
        self.pushButtonVoltar.setIcon(iconVoltar)
        self.pushButtonVoltar.clicked.connect(lambda: parent.setHidden(False))
        self.pushButtonVoltar.clicked.connect(self.deleteLater)

        self.pushButtonCadastrar.clicked.connect(self.cadastrar)

    def cadastrar(self) -> None:
        """
        Pegas as informações de cadastro e envia ao servidor, além de validar 
        as informações dos campos
        """
        dados: dict[str, QLineEdit]
        dados = {"nome": self.lineEditNome,
                 "telefone": self.lineEditTelefone,
                 "email": self.lineEditEmail,
                 "senha": self.lineEditSenha,
                 "senha2": self.lineEditSenha2}

        if not self.validaDados(dados):
            return

        print("Implementar validação dos dados")

        # Envio das informações ao servidor
        resp = cadastrar(self.lineEditNome.text(),
                         self.lineEditTelefone.text(),
                         self.lineEditEmail.text(),
                         self.lineEditSenha.text(), self.statusCadastroLabel)

        if resp == 0:
            self.statusCadastroLabel.setText("Usuário já cadastrado")
        elif resp == 1:
            self.statusCadastroLabel.setText("Cadastro bem sucedido")
        elif resp == 2:
            self.statusCadastroLabel.setText(
                "Erro de conexão")

    def validaDados(self, dados: dict[str, QLineEdit]) -> bool:
        """
        Valida os dados recebidos dos line edit
        Se a validação for verdadeira, ele retorna true
        Caso não for verdadeira, retorna false e expõe o erro no statusLabel 
        do statusBar
        """

        naoPreenchidoBool: bool = False

        # Verifica se todos os dados foram preenchidos
        for key, value in dados.items():
            if key == "telefone":
                continue
            if value.text() == "":
                naoPreenchidoBool = True
                getattr(self, "label" + key.capitalize()
                        ).setStyleSheet("color: red;")
            else:
                getattr(self, "label" + key.capitalize()
                        ).setStyleSheet("color: black;")

        if naoPreenchidoBool:
            self.statusCadastroLabel.setText("Há dados não preenchidos")
            return False

        # Verifica se o email é valido
        expressao = re.compile(r"""^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$""")
        email = re.findall(expressao, dados["email"].text())
        if email == [] or len(email) != 1:
            self.statusCadastroLabel.setText("Email inválido")
            return False

        # Verifica se as senhas são iguais
        if dados["senha"].text() != dados["senha2"].text():
            self.labelSenha2.setStyleSheet("color: red;")
            self.labelSenha.setStyleSheet("color: red;")
            self.statusCadastroLabel.setText("As duas senhas não são iguais")
            return False

        return True


if __name__ == "__main__":
    app = QApplication()
    window = UserLogin()
    window.show()
    app.exec()
