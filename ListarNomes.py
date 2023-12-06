from AnaliseDados import AnaliseDados
from typing import List
from Nome import Nome

class ListarNomes(AnaliseDados):
    def __init__(self):
        super().__init__('Nomes')
        self.nomes = []

    def entradaDeDados(self):
        primeiro_nome = input("Digite o primeiro nome: ")
        sobrenome = input("Digite o sobrenome: ")
        novo_nome = Nome(primeiro_nome, sobrenome)
        self.nomes.append(novo_nome)
        print("Nome adicionado com sucesso.")

    def mostraMediana(self):
        if not self.nomes:
            print("A lista de nomes está vazia.")
            return

        # Ordenar os nomes antes de calcular a mediana
        nomes_ordenados = sorted(self.nomes, key=lambda x: x.obter_nome_completo())
        tamanho = len(nomes_ordenados)

        if tamanho % 2 == 0:
            # Média dos dois valores do meio se a lista tiver um número par de elementos
            mediana = (nomes_ordenados[tamanho // 2 - 1].obter_nome_completo() +
                       nomes_ordenados[tamanho // 2].obter_nome_completo()) / 2
        else:
            # Valor do meio se a lista tiver um número ímpar de elementos
            mediana = nomes_ordenados[tamanho // 2].obter_nome_completo()

        print("Mediana dos nomes:", mediana)

    def mostraMenor(self):
        if not self.nomes:
            print("A lista de nomes está vazia.")
            return

        menor_nome = min(self.nomes, key=lambda x: x.obter_nome_completo())
        print("Menor nome:", menor_nome.obter_nome_completo())

    def mostraMaior(self):
        if not self.nomes:
            print("A lista de nomes está vazia.")
            return

        maior_nome = max(self.nomes, key=lambda x: x.obter_nome_completo())
        print("Maior nome:", maior_nome.obter_nome_completo())

    def listarEmOrdem(self):
        if not self.nomes:
            print("A lista de nomes está vazia.")
            return

        nomes_ordenados = sorted(self.nomes, key=lambda x: x.obter_nome_completo())
        print("Nomes em ordem alfabética:")
        for nome in nomes_ordenados:
            print(nome.obter_nome_completo())

    def excluirNome(self):
        if not self.nomes:
            print("A lista de nomes está vazia.")
            return

        nome_para_excluir = input("Digite o nome que deseja excluir: ")
        nome_encontrado = None

        for nome in self.nomes:
            if nome_para_excluir.lower() == nome.obter_nome_completo().lower():
                nome_encontrado = nome
                break

        if nome_encontrado:
            self.nomes.remove(nome_encontrado)
            print("Nome excluído com sucesso.")
        else:
            print("Nome não encontrado na lista.")

    def editarNome(self):
        if not self.nomes:
            print("A lista de nomes está vazia.")
            return

        nome_para_editar = input("Digite o nome que deseja editar: ")
        nome_encontrado = None

        for nome in self.nomes:
            if nome_para_editar.lower() == nome.obter_nome_completo().lower():
                nome_encontrado = nome
                break

        if nome_encontrado:
            novo_primeiro_nome = input("Digite o novo primeiro nome: ")
            novo_sobrenome = input("Digite o novo sobrenome: ")
            nome_encontrado.primeiro_nome = novo_primeiro_nome
            nome_encontrado.sobrenome = novo_sobrenome
            print("Nome editado com sucesso.")
        else:
            print("Nome não encontrado na lista.")
