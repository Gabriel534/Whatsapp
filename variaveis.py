from pathlib import Path

MAIN = Path(__file__).parent.resolve()
DATA = MAIN / "data"
ICON = DATA / "icon.jpg"
ICON_VOLTAR = DATA / "voltar.png"

TAMANHO_MAXIMO_LOGIN = 30
TAMANHO_MAXIMO_SENHA = 30


SERVERIP = "127.0.0.1"
SERVERPORT = 12345
LARGURA_DADOS = 1024

SENHACLIENTESGERAL = "PEDIDODECONEXÃO"
RESPOSTA_SOLICITACAO_LOGIN = "Login"
RESPOSTA_SOLICITACAO_CADASTRO = "Cadastrar"
SERVER_ACEITACAO = "TRUE"
RESPOSTA_LOGIN_NAO_ENCONTRADO = "UserNotFound"
RESPOSTA_SENHA_INCORRETA = "InvalidPassword"
