from funcs import *

jsonList = lerBancoDeDados()

venda = ordemDeVenda(len(jsonList), "Cesar", "Carro", 300, 1500.0)
lance = ordemDeLance(0, "Vladimit", 800)

#inserirVenda(jsonList, venda)
#inserirLance(jsonList, lance)