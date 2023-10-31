import socket
from PySide6.QtWidgets import QLabel
from variaveis import (SERVERIP, SERVERPORT, LARGURA_DADOS,
                       SENHACLIENTESGERAL, SERVER_ACEITACAO,
                       RESPOSTA_LOGIN_NAO_ENCONTRADO,
                       RESPOSTA_SOLICITACAO_LOGIN,
                       RESPOSTA_SENHA_INCORRETA,
                       RESPOSTA_SOLICITACAO_CADASTRO,
                       RESPOSTA_USUARIO_JA_CADASTRADO,
                       RESPOSTA_CADASTRO_BEM_SUCEDIDO, TIMEOUT,
                       RESPOSTA_CADASTRO_INVALIDO,
                       RESPOSTA_SOLICITACAO_NOVO_CONTATO,
                       RESPOSTA_CONTATO_INVALIDO,
                       RESPOSTA_CADASTRO_CONTATO_REALIZADO,
                       RESPOSTA_CONTATO_JA_EXISTENTE,
                       RESPOSTA_CONTATO_NAO_EXISTE,
                       RESPOSTA_CREDENCIAIS_INVALIDAS,
                       RESPOSTA_RESGATAR_CONTATOS)
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


def login(email: str, senha: str, statusLabel: QLabel | None = None) -> dict | int | None:
    """ 
    Envia os dados do usuário do servidor em forma de dicionário 
    caso usuário e senha estejam corretos
    Retorna 0 se houve erro na comunicação com o servidor
    retorna 1 caso a senha estar incorreta
    retorna None caso o email esteja incorreto
    """

    cliente = conectar(statusLabel)

    if cliente is None:
        return 0

    autenticarCliente(cliente)

    cliente.send(RESPOSTA_SOLICITACAO_LOGIN.encode())
    if cliente.recv(LARGURA_DADOS).decode() == RESPOSTA_SOLICITACAO_LOGIN:
        cliente.send(f"\"{email}\" \"{senha}\"".encode())
        resp = cliente.recv(LARGURA_DADOS)
        try:
            resp = resp.decode()  # type: ignore
            if resp == RESPOSTA_LOGIN_NAO_ENCONTRADO:
                print("Email incorreto")
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
              senha: str, statusLabel: QLabel | None = None) -> int:
    """
    Esta função manda uma solicitação ao servidor para o cadastro de um usuário
    Caso o cadastro recebido pelo servidor for inválido retorna 3
    Caso o cadastro for mal sucedido, a função retornará 2
    Caso seja bem sucedido retornará 1
    Caso o usuário já esteja cadastrado, ele retornará 0
    """
    cliente = conectar(statusLabel)
    if cliente is None:
        return 2

    autenticarCliente(cliente)
    cliente.settimeout(TIMEOUT)
    print(f"\"{nome}\" \"{telefone}\" \"{email}\" \"{senha}\"")

    # Envia o cadastro se o servidor responder corretamente
    cliente.send(RESPOSTA_SOLICITACAO_CADASTRO.encode())
    if cliente.recv(LARGURA_DADOS).decode() == RESPOSTA_SOLICITACAO_CADASTRO:
        cliente.send(
            f"\"{nome}\" \"{telefone}\" \"{email}\" \"{senha}\"".encode())
        try:
            resp = cliente.recv(LARGURA_DADOS).decode()
        except TimeoutError:
            return 2
        if resp == RESPOSTA_USUARIO_JA_CADASTRADO:
            print("Usuário já cadastrado")
            cliente.close()
            return 0
        elif resp == RESPOSTA_CADASTRO_BEM_SUCEDIDO:
            print("Cadastro bem sucedido")
            cliente.close()
            return 1
        elif resp == RESPOSTA_CADASTRO_INVALIDO:
            print("Cadastro inválido")
            return 3
        else:
            print("Erro desconhecido")
            cliente.close()
            return 2
    print("Erro sincronização")
    cliente.close()
    return 0


def adicionarContato(nome: str, email: str, usuario: str, senha: str, statusLabel: QLabel | None = None) -> int:
    """
    Esta função manda uma solicitação ao servidor para adicionar um contato ao usuário
    Caso o servidor esteja indisponível retorna 5
    Caso o contato esteja inválido internamente retorna 4
    Caso as credenciais de login e senha foram inválidas, retorna 3
    Caso a adição do contato for mal sucedido, a função retornará 2
    Caso seja bem sucedido retornará 1
    Caso o contato já esteja cadastrado, ele retornará 0
    """
    cliente = conectar(statusLabel)

    if cliente is None:
        return 5

    autenticarCliente(cliente)

    cliente.send(RESPOSTA_SOLICITACAO_NOVO_CONTATO.encode())

    dadoRecebido = cliente.recv(LARGURA_DADOS).decode()
    if dadoRecebido == RESPOSTA_SOLICITACAO_NOVO_CONTATO:
        cliente.send(
            f"\"{nome}\" \"{email}\" \"{usuario}\" \"{senha}\"".encode())

        dadoRecebido = cliente.recv(LARGURA_DADOS).decode()
        if dadoRecebido == RESPOSTA_CONTATO_INVALIDO:
            return 4
        elif dadoRecebido == RESPOSTA_CADASTRO_CONTATO_REALIZADO:
            return 1
        elif dadoRecebido == RESPOSTA_CONTATO_JA_EXISTENTE:
            return 0
        elif dadoRecebido == RESPOSTA_CONTATO_NAO_EXISTE:
            return 2
        elif dadoRecebido == RESPOSTA_CREDENCIAIS_INVALIDAS:
            return 3
    else:
        return 5

    print("Erro sincronização")
    cliente.close()
    return 2


def resgatarContatos(usuario: str, senha: str,
                     statusLabel: QLabel | None = None) -> int | list[dict]:
    """
    Esta função manda uma solicitação ao servidor para resgatar os contatos do
    usuário
    Caso haja erro de comunicação com o servidor, retorna 3
    Caso as credenciais forem inválidas, retorna 2
    Caso seja bem sucedido retornará 1
    Caso haja erro, retorna 0
    """
    cliente = conectar(statusLabel)

    if cliente is None:
        return 5

    autenticarCliente(cliente)

    cliente.send(RESPOSTA_RESGATAR_CONTATOS.encode())

    dadoRecebido = cliente.recv(LARGURA_DADOS).decode()
    if dadoRecebido == RESPOSTA_RESGATAR_CONTATOS:
        cliente.send(f"\"{usuario}\" \"{senha}\"".encode())
        # Recebe um possível dicionário ou resposta
        resp = cliente.recv(LARGURA_DADOS)

        try:
            if resp.decode() == RESPOSTA_CREDENCIAIS_INVALIDAS:
                return 2
        except UnicodeDecodeError:
            # Caso não for string, retorna os dados
            print("Foi")
            retorno = pickle.loads(resp)  # type: ignore
            cliente.close()
            return retorno

    else:
        return 3


if __name__ == "__main__":
    # Testes de login

    # print(login("Gabriel123", "123"))
    # print(login("Gabriel58", "123"))
    # print(login("Gabriel123", "13"))

    # Testes cadastro

    # cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # cliente.connect((SERVERIP, SERVERPORT))
    # cadastrar("Gabriel", "23231",
    #           "example@gmail.com", "234")

    # # Cria o usuario de testes
    # cadastrar("Gabriel", "-", "g@gmail.co", "1234!@#A")

    # # Teste credenciais incorretas retorna 3
    # print(adicionarContato("Gabriel", "g@gmail.co", "g@gmail.cosdaasd", "1234!@#A"))

    # # Teste contato não existe retorna 2
    # print(adicionarContato("Gabriel", "sdasdasda", "g@gmail.co", "1234!@#A"))

    # # Teste adicionar a si mesmo como contato, se já existir retorna 0
    # print(adicionarContato("Gabriel", "g@gmail.co", "g@gmail.co", "1234!@#A"))

    # TEsta o resgate de contatos
    print(resgatarContatos("g@gmail.com", "1234!@#A"))
