import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Carregar dados da Lotofácil
file_path = 'Lotofacil.xlsx'
df = pd.read_excel(file_path, sheet_name='LOTOFÁCIL')

# Histórico de combinações únicas
historico = set(
    tuple(sorted(row)) for row in df[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14']].values
)

def mostrar_estatisticas():
    """Mostra estatísticas básicas dos números mais e menos sorteados."""
    numeros = df[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14']].values.flatten()
    numeros_contagem = pd.Series(numeros).value_counts()

    print("Números mais sorteados:")
    print(numeros_contagem.head(20))

    print("\nNúmeros menos sorteados:")
    print(numeros_contagem.tail(20))

    numeros_contagem.plot(kind='bar', figsize=(12, 6), title='Frequência dos números sorteados')
    plt.show()

def gerar_combinacoes(criterio='mais', tamanho=15, quantidade=1):
    """Gera combinações baseadas nos números mais ou menos sorteados."""
    numeros = df[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14']].values.flatten()
    numeros_contagem = pd.Series(numeros).value_counts()

    if criterio == 'mais':
        base_numeros = numeros_contagem.head(30).index
    elif criterio == 'menos':
        base_numeros = numeros_contagem.tail(30).index
    else:
        print("Critério inválido! Use 'mais' ou 'menos'.")
        return

    combinacoes = []
    for _ in range(quantidade):
        while True:
            combinacao = tuple(sorted(random.sample(list(base_numeros), tamanho)))
            if combinacao not in combinacoes and combinacao not in historico:
                combinacoes.append(combinacao)
                break

    return combinacoes

def gerar_jogos_manualmente(numeros_inseridos, tamanho=15, quantidade=1):
    """Gera jogos exclusivamente a partir dos números inseridos manualmente."""
    if len(numeros_inseridos) < tamanho:
        print("Erro: A quantidade de números inseridos deve ser igual ou maior que o tamanho do jogo.")
        return []

    combinacoes = []
    numeros_possiveis = list(numeros_inseridos)

    for _ in range(quantidade):
        while True:
            combinacao = tuple(sorted(random.sample(numeros_possiveis, tamanho)))
            if combinacao not in combinacoes and combinacao not in historico:
                combinacoes.append(combinacao)
                break

    return combinacoes

def menu():
    """Menu interativo."""
    while True:
        print("\n=== MENU ===")
        print("1. Mostrar estatísticas básicas")
        print("2. Gerar combinações com números mais frequentes")
        print("3. Gerar combinações com números menos frequentes")
        print("4. Inserir números manualmente e gerar jogos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            mostrar_estatisticas()
        elif escolha == '2':
            tamanho = int(input("Quantos números no jogo (15)? "))
            quantidade = int(input("Quantos jogos você deseja gerar? "))
            jogos = gerar_combinacoes(criterio='mais', tamanho=tamanho, quantidade=quantidade)
            print("\nJogos gerados:")
            for jogo in jogos:
                print(jogo)
        elif escolha == '3':
            tamanho = int(input("Quantos números no jogo (15)? "))
            quantidade = int(input("Quantos jogos você deseja gerar? "))
            jogos = gerar_combinacoes(criterio='menos', tamanho=tamanho, quantidade=quantidade)
            print("\nJogos gerados:")
            for jogo in jogos:
                print(jogo)
        elif escolha == '4':
            numeros_inseridos = list(map(int, input("Insira os números desejados separados por vírgula: ").split(',')))
            tamanho = int(input("Quantos números no jogo (15)? "))
            quantidade = int(input("Quantos jogos você deseja gerar? "))
            jogos = gerar_jogos_manualmente(numeros_inseridos, tamanho=tamanho, quantidade=quantidade)
            print("\nJogos gerados:")
            for jogo in jogos:
                print(jogo)
        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
