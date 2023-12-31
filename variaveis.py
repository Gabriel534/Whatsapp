from pathlib import Path
import re

# Variáveis próprias do cliente
MAIN = Path(__file__).parent.resolve()
DATA = MAIN / "data"
ICON = DATA / "icon.jpg"
ICON_VOLTAR = DATA / "voltar.png"

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
RESPOSTA_CADASTRO_INVALIDO = "INVALIDERROR"
RESPOSTA_SOLICITACAO_NOVO_CONTATO = "NovoConTaTo"
RESPOSTA_CONTATO_INVALIDO = "ConTAToInvaliDo"
RESPOSTA_CADASTRO_CONTATO_REALIZADO = "sjkbksjd"
RESPOSTA_CONTATO_JA_EXISTENTE = "jnbsdfnb"  # Fala que tu já cadastrou o contato
RESPOSTA_CONTATO_NAO_EXISTE = "jkdfnjksdfn"  # Fala que o contato não existe
EXPRESSAO_REGULAR_VALIDA_EMAIL = re.compile(
    r"""^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$""")
EXPRESSAO_REGULAR_VALIDA_SENHA = re.compile(
    r'(?=.*[}{,.^?~%=!@#$+\-_\/*\-+.\|])(?=.*[a-zA-Z])(?=.*[0-9]).{8,}')
RESPOSTA_CREDENCIAIS_INVALIDAS = "jsdnadsa"
RESPOSTA_RESGATAR_CONTATOS = "juisdhbi"
