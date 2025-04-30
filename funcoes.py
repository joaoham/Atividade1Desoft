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

def calcula_pontos_regra_simples(dados):
    dic = {}

    for face in range(1, 7):
        dic[face] = 0

    for i in range(len(dados)):
        valor = dados[i]
        if 1 <= valor <= 6:
            dic[valor] += valor  

    return dic


def calcula_pontos_soma (lista):
    soma = 0
    for i in range (len(lista)):
        soma+=lista[i]
    return soma

def calcula_pontos_sequencia_baixa (lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
        return 15
    elif 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 15
    elif 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 15
    else:
        return 0

def calcula_pontos_sequencia_alta (lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 30
    elif 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 30
    else:
        return 0
def calcula_pontos_full_house(dados):
    checados =[]
    cont = []
    soma = 0
    for valor in dados:
        if valor not in checados:
            checados.append(valor)
            repetidos = 0
            for numero in dados:
                if numero == valor:
                    repetidos +=1
            cont.append(repetidos)
    if len(cont) == 2:
        if (cont[0] == 2 and cont[1] == 3) or (cont[0] == 3 and cont[1] == 2):
            for elem in dados:
                soma += elem
            return soma
    return 0
def calcula_pontos_quadra(dados):
    checados =[]
    soma = 0
    for valor in dados:
        if valor not in checados:
            checados.append(valor)
            repetidos = 0
            for numero in dados:
                if numero == valor:
                    repetidos +=1
            if repetidos >= 4:
                for elem in dados:
                    soma += elem
                return soma
    return 0
def calcula_pontos_quina(dados):
    checados =[]
    for valor in dados:
        if valor not in checados:
            checados.append(valor)
            repetidos = 0
            for numero in dados:
                if numero == valor:
                    repetidos +=1
            if repetidos >= 5:
                return 50
    return 0
def calcula_pontos_regra_avancada(dados):
    dicionario = {}
    regrasavancadas = ["cinco_iguais", "full_house", "quadra", "sem_combinacao", "sequencia_alta", "sequencia_baixa" ]
    resultados = [calcula_pontos_quina(dados), calcula_pontos_full_house(dados), calcula_pontos_quadra(dados), calcula_pontos_soma(dados), calcula_pontos_sequencia_alta(dados), calcula_pontos_sequencia_baixa(dados)]
    for i in range (len(regrasavancadas)):
        dicionario[regrasavancadas[i]] = resultados[i]
    return dicionario
#kikku acabei de gabaritar de first esse de cima ai
def faz_jogada(dados, categoria, dicionario):
    novovalor = 0
    categoriasavancadas = {"cinco_iguais": calcula_pontos_quina, "full_house": calcula_pontos_full_house, "quadra": calcula_pontos_quadra, "sem_combinacao": calcula_pontos_soma, "sequencia_alta": calcula_pontos_sequencia_alta, "sequencia_baixa": calcula_pontos_sequencia_baixa}
    if categoria in categoriasavancadas:
        novovalor = categoriasavancadas[categoria](dados)
        dicionario["regra_avancada"][categoria] = novovalor
    else: 
        novovalor = calcula_pontos_regra_simples(dados)
        pontuacaosimples = novovalor[int(categoria)]
        dicionario["regra_simples"][int(categoria)] = pontuacaosimples
    return dicionario