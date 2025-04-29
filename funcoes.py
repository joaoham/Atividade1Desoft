import random
def rolar_dados (n):
    dados = []
    for i in range(n):
        numero = random.randint(1,6)
        dados.append(numero)
    
    return dados

def guardar_dado (sorteados, armazenados, numero):
    resultado = []
    sorteados_mantidos = []
    armazenados.append(sorteados[numero])
    for i in range(len(sorteados)):
        if sorteados[i] != numero:
            sorteados_mantidos.append(sorteados[i])
    
    resultado.append(sorteados_mantidos)
    resultado.append(armazenados)
    return resultado

