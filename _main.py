from typing import Optional
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QScrollArea, QStatusBar, QDialog, QLineEdit)
from variaveis import (ICON)
from interface import Ui_MainWindow
from AdicionarContato import Ui_MainWindow as Ui_AdicionarContato
from serverConnecter import adicionarContato, resgatarContatos


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, dados: dict) -> None:
        super().__init__()

        self.setupUi(self)

        # Aqui estão todos os itens da lista de conversas
        self.chatItens: list[ItemConversas] = []

        self.setWindowTitle("Whatsapp2")

        self.setStatusBar(QStatusBar())
        self.statusBarLabel = QLabel()
        self.statusBar().addWidget(self.statusBarLabel)

        self.dados = dados
        # Remove a moldura do scroll area
        # self.Chats.setFrameShape(QScrollArea.Shape.NoFrame)
        # self.Chats.setWidgetResizable(True)

        self.User.setText(self.dados["Nome"])
        self.User.setIcon(QIcon(str(ICON)))
        self.User.setIconSize(QSize(40, 40))

        layoutChat = QVBoxLayout()
        layoutChat.setAlignment(Qt.AlignmentFlag.AlignTop)
        layoutChat.setSizeConstraint(layoutChat.SizeConstraint.SetMaximumSize)

        self.Chats.setLayout(layoutChat)

        layoutConversa = QVBoxLayout()
        layoutConversa.setAlignment(Qt.AlignmentFlag.AlignTop)

        layoutConversa.addWidget(QLabel("A"))
        self.Conversa.setLayout(layoutConversa)

        # Adiciona as funcionalidades aos botões
        self.pushButtonContatos.clicked.connect(self.atualizaListaContatos)
        self.pushButtonAdicionarContato.clicked.connect(self.novoContato)
        self.pushButtonConversas.clicked.connect(self.atualizaListaConversas)

        # Atualiza a lista de conversas
        self.atualizaListaConversas()

    def atualizaListaConversas(self):
        print("Implementar lista de conversas")

    def atualizaListaContatos(self):
        resposta: list[dict] | int = resgatarContatos(self.dados["Email"],
                                                      self.dados["Senha"],
                                                      self.statusBarLabel)
        self.Chats.setWidget(QWidget())
        if isinstance(resposta, list):
            for a in resposta:
                self.chatItens.append(ItemConversas(a))
                self.Chats.widget().setLayout(QVBoxLayout())
                self.Chats.widget().layout().setAlignment(
                    Qt.AlignmentFlag.AlignTop)
                self.Chats.widget().layout().addWidget(self.chatItens[-1])
        elif resposta == 3:
            self.statusBarLabel.setText("Erro de comunicação com o servidor")
        elif resposta == 2:
            self.statusBarLabel.setText(
                "Credenciais inválidas! Favor fazer o login novamente")
        elif resposta == 0:
            self.statusBarLabel.setText("Erro desconhecido")

    def novoContato(self):
        self.tela = AdicionarContato(
            self, self.dados["Email"], self.dados["Senha"])
        self.tela.show()

    def removerContato(self):
        ...

    def bloquearContato(self):
        ...


class ItemConversas(QWidget):
    """
    É o item clickável que direciona pra conversa de cada contato
    """

    def __init__(self, dados: dict) -> None:
        super().__init__()
        _layout = QHBoxLayout()
        self.setLayout(_layout)
        self.setWindowTitle("Whatsapp2")

        # Definir tamanho mínimo do nome
        if len(dados["NomeContato"]) > 22:
            dados["NomeContato"] = dados["NomeContato"][:22]

        # Texto do item pra entrar na conversa
        button = QPushButton(dados["NomeContato"])

        button.setStatusTip("Adicionar Horário"
                            )

        button.setCheckable(True)
        button.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #d3d3d3;
                border-radius: 20px;
                padding: 10px;
                text-align: left;
            }

            QPushButton:hover {
                background-color: #e0e0e0;
            }

            QPushButton:pressed {
                background-color: #c0c0c0;
                border: 1px solid #b0b0b0;
            }""")
        button.setFlat(True)
        button.setIcon(QIcon(str(ICON)))
        button.setIconSize(QSize(30, 30))
        _layout.addWidget(button)


class AdicionarContato(QMainWindow, Ui_AdicionarContato):
    def __init__(self, parent: Main, email, senha) -> None:
        super().__init__()

        self.parents = parent

        self.setupUi(self)
        self.setWindowTitle("Cadastrar contato")
        self.email = email
        self.senha = senha
        self.setStatusBar(QStatusBar())
        self.statusBarLabel = QLabel()
        self.statusBar().addWidget(self.statusBarLabel)

        self.pushButtonAdicionarContato.clicked.connect(self.adicionarContato)

    def adicionarContato(self):
        retorno = adicionarContato(self.lineEditNome.text(),
                                   self.lineEditEmail.text(),
                                   self.email, self.senha, self.statusBarLabel)
        if (retorno == 0):
            self.statusBarLabel.setText("Contato já adicionado ao usuario")
        elif (retorno == 1):
            self.parents.atualizaListaContatos()
            self.close()
        elif (retorno == 2):
            self.statusBarLabel.setText("Contato não existe")
        elif (retorno == 3):
            self.statusBarLabel.setText(
                "Credenciais inválidas! Favor fazer o login novamente")
        elif (retorno == 4):
            self.statusBarLabel.setText(
                "Contato inválido")


if __name__ == "__main__":
    from sys import argv
    app = QApplication(argv)
    window = Main({'Id': 1, 'Senha': '1234!@#A', 'Nome': '1',
                   'Email': 'g@gmail.com', 'Telefone': '2',
                  'IP': '127.0.0.1',
                   'DataHoraUltimoLogin': '2023-10-12 21:21:11.722339'})
    window.show()
    app.setWindowIcon(QIcon(str(ICON)))
    app.exec()
