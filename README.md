# Leilao_Python

<p>Protótipo de um leilão em Python para ser utilizado no <a href="https://github.com/KhawanC/Blockchain_Veicular">Projeto Blockchain</a><src>.</p>

<p>O código está sendo arquitetado com funções pois facilitará no uso de uma API.</p>

## Executando:

```console
git clone https://github.com/KhawanC/Leilao_Python.git
```

```console
cd Leilao_Python
```
## Como o sistema funciona:

Existem duas ordens nesse sistema, uma de compra e outra de venda. No arquivo <a href="https://github.com/KhawanC/Leilao_Python/blob/main/main.py">main.py</a> vocẽ consegue achar um construtor para cada um.

```console
venda = ordemDeVenda(len(jsonList), "Nome", "Item", 300, 1500.0)
lance = ordemDeLance(0, "Nome", 800)
```

Também será utilizado um função para armazenar os dados do arquivo JSON.

```console
jsonList = lerBancoDeDados()
```

Obtidas as informações do banco de dados e de um objeto de venda ou de lance iremos fazer sua inserção no sistmea. Utlizaremos a função "inserirVenda" ou "inserirLance", ambas estão comentadas e conforme seu uso é necessário descomentar uma delas.

```console
#inserirVenda(jsonList, venda)
#inserirLance(jsonList, lance)
```

Existem algumas excessões para a regra de negócio do leilão, e cabe a você testar as possibilidades de erro existentes. Caso ache alguma que não foi tratada, por favor, relate essa <a href="https://github.com/KhawanC/Leilao_Python/issues">Issue</a> no Github.

Com tudo feito, rode o arquivo main.py com o seguinte comando:

Ubuntu:
```console
python3 main.py
```


Windows:
```console
py main.py
```









