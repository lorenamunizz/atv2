import json

FILE_PATH = "reservas_eventos/assentos.json"

def carregar_assentos():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [{"numero": i, "reservado": False} for i in range(1, 51)]

def salvar_assentos(assentos):
    with open(FILE_PATH, "w") as file:
        json.dump(assentos, file, indent=4)

def reservar_assento(numero):
    assentos = carregar_assentos()
    for assento in assentos:
        if assento["numero"] == numero:
            assento["reservado"] = True
            salvar_assentos(assentos)
            return True
    return False

def cancelar_reserva(numero):
    assentos = carregar_assentos()
    for assento in assentos:
        if assento["numero"] == numero:
            assento["reservado"] = False
            salvar_assentos(assentos)
            return True
    return False

def exibir_assentos():
    return carregar_assentos()

if __name__ == "__main__":
    print("Assentos disponíveis:", exibir_assentos())
    reservar_assento(1)
    print("Depois de reservar:", exibir_assentos())
    cancelar_reserva(1)
    print("Depois de cancelar:", exibir_assentos())
