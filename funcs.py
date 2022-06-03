import json
class OrdemVenda:
    def __init__(self, idVendedor:int, vendedorNome:str, item:str, lance_atual:int, lance_maximo:int, lance_minimo:int, qtd_lances:int, lances:list):
        self.idVendedor = idVendedor
        self.vendedorNome = vendedorNome
        self.item = item
        self.lance_atual = lance_atual
        self.lance_maximo = lance_maximo
        self.lance_minimo = lance_minimo
        self.qtd_lances = qtd_lances
        self.lances = lances

class OrdemLance:
    def __init__(self, idVendedor:int ,nome:str, valorLance:float):
        self.idVendedor = idVendedor
        self.nome = nome
        self.valorLance = valorLance

def lerBancoDeDados() -> list:
    try:
        with open ('registros.json', 'r', encoding='utf-8') as arq:
            jsonList = json.load(arq)
        return jsonList
    except FileNotFoundError as err:
        print(err)

def inserirVenda(banco:list, venda:object):
    try:
        banco.append(venda.__dict__)
        with open('registros.json', 'w', encoding='utf-8') as arq:
            json.dump(banco, arq, indent=2, separators=(',', ': '))
    except FileNotFoundError:
        print("Não foi possível achar o arquivo")

def inserirLance(banco:list, lance:object):
    try:
        banco[lance.idVendedor]["lances"].append(lance.__dict__)
        with open('registros.json', 'w', encoding='utf-8') as arq:
            json.dump(banco, arq, indent=2, separators=(',', ': '))
    except FileNotFoundError:
        print("Não foi possível achar o arquivo")

def ordemDeVenda(idVendedor:int, nome:str, item:str, vMax:float, vMinimo:float) -> OrdemVenda:
    ordem = OrdemVenda(idVendedor, nome, item, 0, vMax, vMinimo, 0, [])
    return ordem

def ordemDeLance(idVendedor:int, nome:str, valorLance:float) -> OrdemLance:
    lance = OrdemLance(idVendedor, nome, valorLance)
    return lance

jsonList = lerBancoDeDados()

venda = ordemDeVenda(len(jsonList), "Kaua", "Moto", 18000, 300.0)
lance = ordemDeLance(1, "Vinicius", 400)

#inserirVenda(jsonList, venda)
#inserirLance(jsonList, lance)