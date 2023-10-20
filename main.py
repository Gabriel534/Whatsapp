from typing import Optional
import PySide6.QtCore
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel,
    QPushButton, QHBoxLayout, QStatusBar)
from PySide6.QtGui import QIcon, QKeyEvent
from variaveis import (TAMANHO_MAXIMO_LOGIN, TAMANHO_MAXIMO_SENHA,
                       ICON, ICON_VOLTAR, EXPRESSAO_REGULAR_VALIDA_EMAIL,
                       EXPRESSAO_REGULAR_VALIDA_SENHA)
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
            self.statusLabel.setText("Email e/ou senha não preenchidos")
            return
        try:
            dados = login(self.lineEditEmail.text(),
                          self.lineEditSenha.text(), self.statusLabel)
        except ConnectionRefusedError:
            self.statusLabel.setText("Erro na validação do cliente")
            return
        if dados is None:
            self.statusLabel.setText("Email incorreto!")
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
            self.statusCadastroLabel.setText("Cadastro bem sucedido!")
        elif resp == 2:
            self.statusCadastroLabel.setText(
                "Erro de conexão")
        elif resp == 3:
            self.statusCadastroLabel.setText(
                "Cadastro Inválido")

    def validaDados(self, dados: dict[str, QLineEdit]) -> bool:
        """
        Valida os dados recebidos dos line edit
        Se a validação for verdadeira, ele retorna true
        Caso não for verdadeira, retorna false e expõe o erro no statusLabel
        do statusBar
        """

        # Verifica se os campos contém aspas e caso tenha, impede de ser
        # utilizado
        contemAspas: bool = False

        for i, j in dados.items():
            if "\"" in j.text() != -1:
                getattr(self, "label" + i.capitalize()
                        ).setStyleSheet("color: red;")
                contemAspas = True
            else:
                getattr(self, "label" + i.capitalize()
                        ).setStyleSheet("color: black;")

        if contemAspas is True:
            self.statusCadastroLabel.setText(
                "Nos campos não deve conter aspas")
            return False

        # Verifica se todos os dados foram preenchidos
        naoPreenchidoBool: bool = False

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
        email = re.findall(EXPRESSAO_REGULAR_VALIDA_EMAIL,
                           dados["email"].text())
        if email == [] or len(email) != 1:
            self.statusCadastroLabel.setText("Email inválido")
            return False

        # Verifica se as senhas são iguais
        if dados["senha"].text() != dados["senha2"].text():
            self.labelSenha2.setStyleSheet("color: red;")
            self.labelSenha.setStyleSheet("color: red;")
            self.statusCadastroLabel.setText("As duas senhas não são iguais")
            return False

        """
        Requisitos de senha:
        - Conter no mínimo oito caracteres;

        - Obedecer três dos quatro requisitos:
            1- letras maiúsculas (A-Z);
            2- letras minúsculas (a-z);
            3- números;
            4- caracteres não alfabéticos ($, &, %, @).
            5- não pode conter aspas
                """

        if len(dados["senha"].text()) < 8:
            self.labelSenha2.setStyleSheet("color: red;")
            self.labelSenha.setStyleSheet("color: red;")
            self.statusCadastroLabel.setText("A senha deve conter no mínimo \
8 caracteres")
            return False

        # Regex que valida senha
        requisitos = re.findall(
            EXPRESSAO_REGULAR_VALIDA_SENHA, dados["senha"].text())

        if requisitos == []:
            self.labelSenha2.setStyleSheet("color: red;")
            self.labelSenha.setStyleSheet("color: red;")
            self.statusCadastroLabel.setText(
                "A senha deve conter uma letra, um número e um caractere \n\
especial no mínimo")
            return False

        return True


if __name__ == "__main__":
    app = QApplication()
    window = UserLogin()
    window.show()
    app.setWindowIcon(QIcon(str(ICON)))
    app.exec()
