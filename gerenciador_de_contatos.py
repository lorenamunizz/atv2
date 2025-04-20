import json

FILE_PATH = "gerenciador_contatos/contatos.json"

def carregar_contatos():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_contatos(contatos):
    with open(FILE_PATH, "w") as file:
        json.dump(contatos, file, indent=4)

def adicionar_contato(nome, telefone, email):
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)

def buscar_contato(nome):
    contatos = carregar_contatos()
    return [contato for contato in contatos if nome.lower() in contato["nome"].lower()]

if __name__ == "__main__":
    adicionar_contato("Julia", "123456789", "julia@example.com")
    print("Contatos encontrados:", buscar_contato("Julia"))
