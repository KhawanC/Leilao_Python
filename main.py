from funcs import *

jsonList = lerBancoDeDados()

venda = ordemDeVenda(len(jsonList), "Cesar", "Carro", 18000, 1200)
lance = ordemDeLance(0, "Xarles", 1900)

#inserirVenda(jsonList, venda)
inserirLance(jsonList, lance)