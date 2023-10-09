import socket
from variaveis import (SERVERIP, SERVERPORT, LARGURA_DADOS,
                       SENHACLIENTESGERAL, SERVER_ACEITACAO,
                       RESPOSTA_LOGIN_NAO_ENCONTRADO,
                       RESPOSTA_SOLICITACAO_LOGIN,
                       RESPOSTA_SENHA_INCORRETA,
                       RESPOSTA_SOLICITACAO_CADASTRO)
import pickle


def autenticarCliente(cliente):
    # Envia a autenticação de clientes geral
    cliente.send(SENHACLIENTESGERAL.encode())
    if cliente.recv(LARGURA_DADOS).decode() != SERVER_ACEITACAO:
        cliente.close()
        raise ConnectionRefusedError("Erro na validação do cliente")


def login(cliente, login: str, senha: str) -> dict | int | None:
    autenticarCliente(cliente)

    # Envia o login e senha se o servidor responder corretamente
    cliente.send(RESPOSTA_SOLICITACAO_LOGIN.encode())
    if cliente.recv(LARGURA_DADOS).decode() == RESPOSTA_SOLICITACAO_LOGIN:
        cliente.send(f"\"{login}\" \"{senha}\"".encode())
        resp = cliente.recv(LARGURA_DADOS)
        try:
            resp = resp.decode()
            if resp == RESPOSTA_LOGIN_NAO_ENCONTRADO:
                print("Login incorreto")
                return None
            elif resp == RESPOSTA_SENHA_INCORRETA:
                print("Senha incorreta")
                return None
            else:
                print("Servidor inacessível")
                return 0
        except UnicodeDecodeError:
            print("Foi")
            return pickle.loads(resp)


def cadastrar(cliente: socket.socket, nome: str, telefone: str, email: str,
              login: str, senha: str):
    autenticarCliente(cliente)

    # Envia o cadastro se o servidor responder corretamente
    cliente.send(RESPOSTA_SOLICITACAO_CADASTRO.encode())
    if cliente.recv(LARGURA_DADOS).decode() == RESPOSTA_SOLICITACAO_CADASTRO:
        cliente.send(
            f"\"{nome}\" \"{telefone}\" \"{email}\" \"{login}\" \"{senha}\"".encode())


if __name__ == "__main__":
    # Testes de login
    # print("Ir: ", end="")
    # cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # cliente.connect((SERVERIP, SERVERPORT))
    # print(login(cliente, "Gabriel123", "123"))
    # cliente.close()

    # print("Erro login: ", end="")
    # cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # cliente.connect((SERVERIP, SERVERPORT))
    # print(login(cliente, "Gabriel58", "123"))
    # cliente.close()

    # print("Erro senha: ", end="")
    # cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # cliente.connect((SERVERIP, SERVERPORT))
    # print(login(cliente, "Gabriel578", "13"))
    # cliente.close()

    # Testes cadastro

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((SERVERIP, SERVERPORT))
    cadastrar(cliente, "Gabriel", "23231",
              "example@gmail.com", "Wrecking", "234")
    cliente.close()
