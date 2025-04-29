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
    
    