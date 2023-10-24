from typing import Optional
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QScrollArea, QStatusBar, QDialog)
from variaveis import (ICON)
from interface import Ui_MainWindow
from AdicionarContato import Ui_Dialog


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, dados: dict) -> None:
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("Whatsapp2")

        self.dados = dados
        # Remove a moldura do scroll area
        # self.Chats.setFrameShape(QScrollArea.Shape.NoFrame)
        # self.Chats.setWidgetResizable(True)

        self.User.setText(self.dados["Nome"])
        self.User.setIcon(QIcon(str(ICON)))
        self.User.setIconSize(QSize(40, 40))

        self.setStatusBar(QStatusBar())

        layoutChat = QVBoxLayout()
        layoutChat.setAlignment(Qt.AlignmentFlag.AlignTop)
        layoutChat.setSizeConstraint(layoutChat.SizeConstraint.SetMaximumSize)

        self.Chats.setLayout(layoutChat)

        layoutConversa = QVBoxLayout()
        layoutConversa.setAlignment(Qt.AlignmentFlag.AlignTop)

        layoutConversa.addWidget(QLabel("A"))
        self.Conversa.setLayout(layoutConversa)

        self.pushButtonAdicionarContato.clicked.connect(self.novoContato)

    def novoContato(self):
        self.tela = Ui_Dialog()
        self.tela.setupUi(QDialog())

    def removerContato(self):
        ...

    def bloquearContato(self):
        ...


class ItemChat(QWidget):
    """
    É o item clickável que direciona pra conversa de cada contato
    """

    def __init__(self, nome: str, conversa: str, horario: str) -> None:
        super().__init__()
        _layout = QHBoxLayout()
        self.setLayout(_layout)
        self.setWindowTitle("Whatsapp2")

        # Definir tamanho mínimo do nome
        if len(nome) > 22:
            nome = nome[:22]

        # Texto do item pra entrar na conversa
        button = QPushButton(nome)

        button.setStatusTip(horario)

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


if __name__ == "__main__":
    from sys import argv
    app = QApplication(argv)
    window = Main({'Id': 1, 'Senha': '5', 'Nome': '1', 'Email': '3', 'Telefone': '2',
                  'IP': '127.0.0.1', 'DataHoraUltimoLogin': '2023-10-12 21:21:11.722339'})
    window.show()
    app.setWindowIcon(QIcon(str(ICON)))
    app.exec()
