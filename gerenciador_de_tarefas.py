import json
from datetime import datetime

FILE_PATH = "gerenciador_tarefas/tarefas.json"

def carregar_tarefas():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(FILE_PATH, "w") as file:
        json.dump(tarefas, file, indent=4)

def adicionar_tarefa(descricao, prazo):
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": descricao, "prazo": prazo, "concluida": False})
    salvar_tarefas(tarefas)

def listar_tarefas():
    tarefas = carregar_tarefas()
    tarefas.sort(key=lambda t: datetime.strptime(t["prazo"], "%Y-%m-%d"))
    return tarefas

def marcar_concluida(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)

if __name__ == "__main__":
    adicionar_tarefa("Estudar Python", "2025-04-20")
    adicionar_tarefa("Enviar relatório", "2025-04-21")
    print("Tarefas:", listar_tarefas())
    marcar_concluida(0)
