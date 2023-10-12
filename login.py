import socket
from PySide6.QtWidgets import QLabel
from variaveis import (SERVERIP, SERVERPORT, LARGURA_DADOS,
                       SENHACLIENTESGERAL, SERVER_ACEITACAO,
                       RESPOSTA_LOGIN_NAO_ENCONTRADO,
                       RESPOSTA_SOLICITACAO_LOGIN,
                       RESPOSTA_SENHA_INCORRETA,
                       RESPOSTA_SOLICITACAO_CADASTRO,
                       RESPOSTA_USUARIO_JA_CADASTRADO,
                       RESPOSTA_CADASTRO_BEM_SUCEDIDO, TIMEOUT)
import pickle


def conectar(statusLabel: QLabel | None = None) -> socket.socket | None:
    """
    Cria uma instância de clientes geral e retorna o cliente 
    (classe socket.socket) já com o timeout predefinido nas variáveis
    """
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((SERVERIP, SERVERPORT))
    except ConnectionRefusedError:
        if statusLabel is not None:
            statusLabel.setText(
                "Erro ao se comunicar com o servidor")
        return None
    except ConnectionError:
        if statusLabel is not None:
            statusLabel.setText("Erro ao se comunicar com o servidor")
        return None
    except Exception:
        if statusLabel is not None:
            statusLabel.setText(
                "Erro desconhecido, favor tentar novamente")
        return None
    cliente.settimeout(TIMEOUT)
    return cliente


def autenticarCliente(cliente):

    # Envia a autenticação de clientes geral
    cliente.send(SENHACLIENTESGERAL.encode())
    if cliente.recv(LARGURA_DADOS).decode() != SERVER_ACEITACAO:
        cliente.close()
        raise ConnectionRefusedError("Erro na validação do cliente")


def login(login: str, senha: str, statusLabel: QLabel | None = None) -> dict | int | None:
    """ Envia o login e senha se o servidor responder corretamente
    Retorna 0 se houve erro na comunicação com o servidor
    retorna 1 caso a senha estar incorreta
    retorna None caso o login esteja incorreto
    """

    cliente = conectar(statusLabel)

    if cliente is None:
        return 0

    autenticarCliente(cliente)

    cliente.send(RESPOSTA_SOLICITACAO_LOGIN.encode())
    if cliente.recv(LARGURA_DADOS).decode() == RESPOSTA_SOLICITACAO_LOGIN:
        cliente.send(f"\"{login}\" \"{senha}\"".encode())
        resp = cliente.recv(LARGURA_DADOS)
        try:
            resp = resp.decode()  # type: ignore
            if resp == RESPOSTA_LOGIN_NAO_ENCONTRADO:
                print("Login incorreto")
                cliente.close()
                return None
            elif resp == RESPOSTA_SENHA_INCORRETA:
                print("Senha incorreta")
                cliente.close()
                return 1
            else:
                print("Servidor inacessível ou dessincronizado")
                cliente.close()
                return 0
        except UnicodeDecodeError:
            print("Foi")
            retorno = pickle.loads(resp)  # type: ignore
            cliente.close()
            return retorno


def cadastrar(nome: str, telefone: str, email: str,
              login: str, senha: str, statusLabel: QLabel | None = None) -> int:
    """
    Esta função manda uma solicitação ao servidor para o cadastro de um usuário
    Caso o cadastro for mal sucedido, a função retornará 2
    Caso seja bem sucedido retornará 1
    Caso o usuário já esteja cadastrado, ele retornará 0
    """
    cliente = conectar(statusLabel)
    if cliente is None:
        return 2

    autenticarCliente(cliente)
    cliente.settimeout(TIMEOUT)
    print(f"\"{nome}\" \"{telefone}\" \"{email}\" \"{login}\" \"{senha}\"")

    # Envia o cadastro se o servidor responder corretamente
    cliente.send(RESPOSTA_SOLICITACAO_CADASTRO.encode())
    if cliente.recv(LARGURA_DADOS).decode() == RESPOSTA_SOLICITACAO_CADASTRO:
        cliente.send(
            f"\"{nome}\" \"{telefone}\" \"{email}\" \"{login}\" \"{senha}\"".encode())
        resp = cliente.recv(LARGURA_DADOS).decode()
        if resp == RESPOSTA_USUARIO_JA_CADASTRADO:
            print("Usuário já cadastrado")
            cliente.close()
            return 0
        elif resp == RESPOSTA_CADASTRO_BEM_SUCEDIDO:
            print("Cadastro bem sucedido")
            cliente.close()
            return 1
        else:
            print("Erro desconhecido")
            cliente.close()
            return 2
    print("Erro sincronização")
    cliente.close()
    return 0


if __name__ == "__main__":
    # Testes de login

    print(login("Gabriel123", "123"))
    print(login("Gabriel58", "123"))
    print(login("Gabriel123", "13"))

    # Testes cadastro

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((SERVERIP, SERVERPORT))
    cadastrar("Gabriel", "23231",
              "example@gmail.com", "Wrecking2", "234")
