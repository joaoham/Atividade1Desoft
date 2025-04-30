import funcoes

acoesvalidas = [0, 1, 2, 3, 4]
combinacoesvalidas = ["1", "2", "3", "4", "5", "6", "sem_combinacao", "quadra", "full_house", "sequencia_baixa", "sequencia_alta", "cinco_iguais"]
rodadas = 0
combinacoesusadas = []

cartela = {
    "regra_simples": {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    "regra_avancada": {
        "sem_combinacao": -1,
        "quadra": -1,
        "full_house": -1,
        "sequencia_baixa": -1,
        "sequencia_alta": -1,
        "cinco_iguais": -1,
    },
}

while rodadas < 12:
    funcoes.imprime_cartela(cartela)
    dadosrolados = funcoes.rolar_dados(5)
    dadosguardados = []
    vezesrolados = 0

    print(f"Dados rolados: {dadosrolados}")
    print(f"Dados guardados: {dadosguardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    acoes = int(input())

    while acoes not in acoesvalidas:
        print("Opção inválida. Tente novamente.")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acoes = int(input())

    while acoes == 3 and vezesrolados == 2:
        print("Você já usou todas as rerrolagens.")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acoes = int(input())

    while acoes in acoesvalidas and acoes != 0:
        if acoes == 1:
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            dadosguardados.append(dadosrolados[indice])
            del dadosrolados[indice]
            print(f"Dados rolados: {dadosrolados}")
            print(f"Dados guardados: {dadosguardados}")
        if acoes == 2:
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            dadosrolados.append(dadosguardados[indice])
            del dadosguardados[indice]
            print(f"Dados rolados: {dadosrolados}")
            print(f"Dados guardados: {dadosguardados}")
        if acoes == 3:
            dadosrolados = funcoes.rolar_dados(len(dadosrolados))
            print(f"Dados rolados: {dadosrolados}")
            print(f"Dados guardados: {dadosguardados}")
            vezesrolados += 1
        if acoes == 4:
            funcoes.imprime_cartela(cartela)
            print(f"Dados rolados: {dadosrolados}")
            print(f"Dados guardados: {dadosguardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acoes = int(input())

    if acoes == 0:
        print("Digite a combinação desejada:")
        combinacao = input()
        while combinacao not in combinacoesvalidas:
            print("Combinação inválida. Tente novamente.")
            print("Digite a combinação desejada:")
            combinacao = input()
        while combinacao in combinacoesusadas:
            print("Essa combinação já foi utilizada.")
            print("Digite a combinação desejada:")
            combinacao = input()

        if combinacao in ["1", "2", "3", "4", "5", "6"]:
            combinacao = int(combinacao)

        combinacoesusadas.append(combinacao)
        funcoes.faz_jogada(dadosrolados + dadosguardados, combinacao, cartela)
        funcoes.imprime_cartela(cartela)
        rodadas += 1

total_simples = 0
for valor in cartela["regra_simples"].values():
    if valor != -1:
        total_simples += valor

total_avancado = 0
for valor in cartela["regra_avancada"].values():
    if valor != -1:
        total_avancado += valor

bonus = 35 if total_simples >= 63 else 0
total = total_simples + total_avancado + bonus

print("Cartela final:")
funcoes.imprime_cartela(cartela)
print(f"Pontuação total: {total}")
