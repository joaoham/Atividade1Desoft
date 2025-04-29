import random
def rolar_dados (n):
    dados = []
    for i in range(n):
        numero = random.randint(1,6)
        dados.append(numero)
    
    return dados

def guardar_dado(sorteados, armazenados, numero):
    resultado = []
    sorteados_mantidos = []

    valor = sorteados[numero]  
    armazenados.append(valor)  

    for i in range(len(sorteados)):
        if i != numero:  
            sorteados_mantidos.append(sorteados[i])

    resultado.append(sorteados_mantidos)
    resultado.append(armazenados)
    return resultado

def remover_dado(rolados,estoque,indiceremover):
    valor = estoque[indiceremover]
    rolados.append(valor)
    estoque.pop(indiceremover)
    fim_jogada = []
    fim_jogada.append(rolados)
    fim_jogada.append(estoque)
    return fim_jogada

def calcula_pontos_regra_simples(faces):
    numero = 0
    dic = {}
    i = 0
    while i < 7:
        quant = 0
        e = 0
        while e < len(faces):
            if i == faces[e]:
                quant += 1
            e += 1
        if quant == 0:
            dic[i]=i
        else:
            dic[i] = (i*quant)
        i += 1
    return {quant}