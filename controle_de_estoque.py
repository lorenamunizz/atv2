import json

FILE_PATH = "controle_estoque/estoque.json"

def carregar_estoque():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open(FILE_PATH, "w") as file:
        json.dump(estoque, file, indent=4)

def adicionar_produto(nome, quantidade, preco):
    estoque = carregar_estoque()
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar_estoque(estoque)

def listar_produtos():
    estoque = carregar_estoque()
    return estoque

def calcular_valor_total():
    estoque = carregar_estoque()
    return sum(item["quantidade"] * item["preco"] for item in estoque)

if __name__ == "__main__":
    adicionar_produto("Teclado", 10, 100.0)
    adicionar_produto("Mouse", 5, 50.0)
    print("Estoque:", listar_produtos())
    print("Valor total:", calcular_valor_total())
