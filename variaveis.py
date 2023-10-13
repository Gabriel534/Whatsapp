from pathlib import Path


# Variáveis próprias do cliente
MAIN = Path(__file__).parent.resolve()
DATA = MAIN / "data"
ICON = DATA / "icon.jpg"
ICON_VOLTAR = DATA / "voltar.png"
ICON_MAIS = DATA / "+.png"
ICON_LIGACAO = DATA / "ligacao.png"
ICON_X = DATA / "x.png"

TIMEOUT = 2


# Variáveis comuns do servidor
SERVERIP = "127.0.0.1"
SERVERPORT = 12345
LARGURA_DADOS = 1024

TAMANHO_MAXIMO_LOGIN = 30
TAMANHO_MAXIMO_SENHA = 30
SENHACLIENTESGERAL = "PEDIDODECONEXÃO"
RESPOSTA_SOLICITACAO_LOGIN = "Login"
RESPOSTA_SOLICITACAO_CADASTRO = "Cadastrar"
SERVER_ACEITACAO = "TRUE"
RESPOSTA_LOGIN_NAO_ENCONTRADO = "UserNotFound"
RESPOSTA_SENHA_INCORRETA = "InvalidPassword"
RESPOSTA_USUARIO_JA_CADASTRADO = "UserAlreadyExists"
RESPOSTA_CADASTRO_BEM_SUCEDIDO = "Cadastro_berm_sucedisdo"
RESPOSTA_DESSINCRONIZACAO = "ErroDessincronização"
