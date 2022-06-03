#Importações
import json, enum

#Enumerador com os status de uma ordem de venda
class Status(enum.Enum):
    aberto = 1
    fechado = 2
    
#Classe de ordem de venda, ondem são feitos os anuncios de algum item no leilão
class OrdemVenda:
    def __init__(self, idVendedor:int, vendedorNome:str, item:str, lance_atual:int, lance_maximo:int, lance_minimo:int, qtd_lances:int, lances:list):
        self.idVendedor = idVendedor
        self.vendedorNome = vendedorNome
        self.item = item
        self.lance_atual = lance_atual
        self.lance_maximo = lance_maximo
        self.lance_minimo = lance_minimo
        self.qtd_lances = qtd_lances
        self.stauts = Status.aberto.name
        self.lances = lances

#Cladde ordem de lance, ondem é feito um lance de um item no leilão
class OrdemLance:
    def __init__(self, idVendedor:int ,nome:str, valorLance:float):
        self.idVendedor = idVendedor
        self.nome = nome
        self.valorLance = valorLance

#FUnção para ler o conteúdo do JSON, que serve como nosso banco de dados
def lerBancoDeDados() -> list:
    try:
        with open ('/home/kaua/github_clones/Leilao_Python/registros.json', 'r', encoding='utf-8') as arq:
            jsonList = json.load(arq)
        return jsonList
    except FileNotFoundError as err:
        raise Exception("Não foi possível encontrar o arquivo JSON")

#Função para inserir uma ordem de venda no JSON
def inserirVenda(banco:list, venda:object):
    try:
        #Condição para verificar se o lance máximo é menor que o lance mínimo
        if(venda.lance_maximo < venda.lance_minimo):
            raise Exception("O lance máximo é maior que o lance mínimo")
        #Condição para verificar se os lances máximo e mínimo são menores ou iguais a zero  
        if(venda.lance_maximo <= 0 or venda.lance_minimo <= 0):
            raise Exception("Os lances não podem ter valor menor ou igual a zero")
        banco.append(venda.__dict__)
        #With Open para abrir o arquivo JSON e escrever nele a ordem de venda
        with open('/home/kaua/github_clones/Leilao_Python/registros.json', 'w', encoding='utf-8') as arq:
            json.dump(banco, arq, indent=2, separators=(',', ': '))
    except FileNotFoundError:
        raise Exception("Não foi possível achar o arquivo JSON")

#FUnção para inserir uma ordem de lance no JSON
def inserirLance(banco:list, lance:object):
    try:
        indice = lance.idVendedor
        #Verificar se esse é o primeiro lance
        if(banco[indice]["lances"] == []):
            if(lance.valorLance < banco[indice]["lance_minimo"]):
                raise Exception("Não é possível criar um lance com valor menor que o lance mínimo")
            lance.__dict__.pop("idVendedor")
            banco[indice]["lances"].append(lance.__dict__)
            banco[indice]["lance_atual"] = lance.valorLance
        else:
            #Caso não seja o primeiro lance, verificar se o valor do lance é maior que o lance anterior
            if(lance.valorLance < banco[indice]["lance_atual"]):
                raise Exception("O valor do lance não pode ser menor que o último lance")
            indice = lance.idVendedor
            #Remover o id do vendedor passado por argumento no construtor, pois esse lance já está dentro da venda
            lance.__dict__.pop("idVendedor")
            banco[indice]["lances"].append(lance.__dict__)
            banco[indice]["lance_atual"] = lance.valorLance
        with open('/home/kaua/github_clones/Leilao_Python/registros.json', 'w', encoding='utf-8') as arq:
            json.dump(banco, arq, indent=2, separators=(',', ': '))
    except FileNotFoundError:
        raise Exception("Não foi possível achar o arquivo JSON")

#Função para criar um objeto de ordem de venda com alguns valores zerados
def ordemDeVenda(idVendedor:int, nome:str, item:str, vMax:float, vMinimo:float) -> OrdemVenda:
    ordem = OrdemVenda(idVendedor, nome, item, 0, vMax, vMinimo, 0, [])
    return ordem

#Função para criar um objeto de ordem de lance
def ordemDeLance(idVendedor:int, nome:str, valorLance:float) -> OrdemLance:
    lance = OrdemLance(idVendedor, nome, valorLance)
    return lance