import json

FILE_PATH = "sistema_bancario/usuarios.json"

def carregar_usuarios():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_usuarios(usuarios):
    with open(FILE_PATH, "w") as file:
        json.dump(usuarios, file, indent=4)

def registrar_usuario(username, senha):
    usuarios = carregar_usuarios()
    usuarios.append({"username": username, "senha": senha, "saldo": 0, "transacoes": []})
    salvar_usuarios(usuarios)

def login(username, senha):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["username"] == username and usuario["senha"] == senha:
            return usuario
    return None

def deposito(usuario, valor):
    usuario["saldo"] += valor
    usuario["transacoes"].append({"tipo": "deposito", "valor": valor})

def saque(usuario, valor):
    if usuario["saldo"] >= valor:
        usuario["saldo"] -= valor
        usuario["transacoes"].append({"tipo": "saque", "valor": valor})
    else:
        return False
    return True

if __name__ == "__main__":
    registrar_usuario("julia", "senha123")
    user = login("julia", "senha123")
    if user:
        deposito(user, 100)
        saque(user, 50)
        print("Usuário:", user)
