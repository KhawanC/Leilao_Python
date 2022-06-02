import json

def lerBancoDeDados() -> dict:
    try:
        with open ('registros.json', 'r') as arq:
            registros = json.load(arq)
        return registros
    except FileNotFoundError as err:
        print(err)

def inserirRegistro(banco:dict, registro:dict):
    try:
        with open ('registros.json', 'w') as arq:
            banco.
            json.dump(registro, arq, ensure_ascii=False, indent=4)
    except FileNotFoundError as err:
        print(err)

def iniciarLeilao(nome:str, item:str, vMinimo:float, vMax:float) -> dict:
    ordem = {
            "Vendedor": nome,
            "Item": item,
            "Lance Atual": 0,
            "Lance Minimo": vMinimo,
            "Lance Máximo": vMax,
            "Quantidade de Lances": 0,
            "Lances":[]
        }
    return ordem

banco = lerBancoDeDados();
registros = iniciarLeilao("Kaua", "Celular Lenovo", 300.0, 1200.0)
inserirRegistro(banco, registros)

banco = lerBancoDeDados();

