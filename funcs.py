#Importações
import json, enum

class Status(enum.Enum): #Enumerador com os status de uma ordem de venda

    aberto = 1
    andamento = 2
    fechado = 3 
class OrdemVenda: #Classe de ordem de venda, ondem são feitos os anuncios de algum item no leilão

    def __init__(self, idVendedor:int, vendedorNome:str, item:str, lance_atual:int, lance_maximo:int, lance_minimo:int, qtd_lances:int, lances:list):
        self.idVendedor = idVendedor
        self.vendedorNome = vendedorNome
        self.item = item
        self.lance_atual = lance_atual
        self.lance_maximo = lance_maximo
        self.lance_minimo = lance_minimo
        self.qtd_lances = qtd_lances
        self.status = Status.aberto.name
        self.lances = lances

class OrdemLance: #Classe ordem de lance, ondem é feito um lance de um item no leilão

    def __init__(self, idVendedor:int ,nome:str, valorLance:float):
        self.idVendedor = idVendedor
        self.nome = nome
        self.valorLance = valorLance


def lerBancoDeDados() -> list: #Função para ler o conteúdo do JSON, que serve como nosso banco de dados

    try:
        with open ('./registros.json', 'r', encoding='utf-8') as arq:
            jsonList = json.load(arq)
        return jsonList
    except FileNotFoundError as err:
        raise Exception("Não foi possível encontrar o arquivo JSON")

def inserirVenda(banco:list, venda:object): #Função para inserir uma ordem de venda no JSON

    try:
        
        if(venda.lance_maximo < venda.lance_minimo): #Condição para verificar se o lance máximo é menor que o lance mínimo
            raise Exception("O lance máximo é maior que o lance mínimo")
        
        if(venda.lance_maximo <= 0 or venda.lance_minimo <= 0): #Condição para verificar se os lances máximo e mínimo são menores ou iguais a zero  
            raise Exception("Os lances não podem ter valor menor ou igual a zero")

        banco.append(venda.__dict__)

        with open('./registros.json', 'w', encoding='utf-8') as arq: #With Open para abrir o arquivo JSON e escrever nele a ordem de venda
            json.dump(banco, arq, indent=2, separators=(',', ': '))
    
    except FileNotFoundError:
        raise Exception("Não foi possível achar o arquivo JSON")

def inserirLance(banco:list, lance:object): #Função para inserir uma ordem de lance no JSON

    try:
        indice = lance.idVendedor
        
        if(banco[indice]["lances"] == []): #Verificar se esse é o primeiro lance
            if(lance.valorLance < banco[indice]["lance_minimo"]):
                raise Exception("Não é possível criar um lance com valor menor que o lance mínimo")
            lance.__dict__.pop("idVendedor") #Remover o id do vendedor passado por argumento no construtor, pois esse lance já está dentro da venda
            banco[indice]["lances"].append(lance.__dict__)
            banco[indice]["lance_atual"] = lance.valorLance
            banco[indice]["status"] = Status.andamento.name
        else:
            
            if(lance.nome == banco[indice]["lances"][-1]["nome"]): #Verificar se o último lance contém o mesmo nome que o lance atual 
                raise Exception("Você acabou de fazer um lance.")
            
            if(lance.valorLance <= banco[indice]["lance_atual"]): #Caso não seja o primeiro lance, verificar se o valor do lance é maior que o lance anterior
                raise Exception("O valor do lance não pode ser menor ou igual ao último lance")
            
            indice = lance.idVendedor
            lance.__dict__.pop("idVendedor") #Remover o id do vendedor passado por argumento no construtor, pois esse lance já está dentro da venda
            banco[indice]["lances"].append(lance.__dict__)
            banco[indice]["lance_atual"] = lance.valorLance

        with open('./registros.json', 'w', encoding='utf-8') as arq:
            json.dump(banco, arq, indent=2, separators=(',', ': '))

    except FileNotFoundError:
        raise Exception("Não foi possível achar o arquivo JSON")

def ordemDeVenda(idVendedor:int, nome:str, item:str, vMax:float, vMinimo:float) -> OrdemVenda: #Função para criar um objeto de ordem de venda com alguns valores zerados

    ordem = OrdemVenda(idVendedor, nome, item, 0, vMax, vMinimo, 0, [])
    return ordem

def ordemDeLance(idVendedor:int, nome:str, valorLance:float) -> OrdemLance: #Função para criar um objeto de ordem de lance

    lance = OrdemLance(idVendedor, nome, valorLance)
    return lance