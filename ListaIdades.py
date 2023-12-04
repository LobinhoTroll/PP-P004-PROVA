from AnaliseDados import AnaliseDados
from Idade import Idade

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(Idade))
        self.__lista = []        
    
    def entradaDeDados(self):
        qtdItens,contador,idade = 0,0,0
        
        print("Informe a quantidade de itens na lista: ")
        qtdItens = int(input())

        if qtdItens > 0:
            while contador < qtdItens:
                print("\nInserindo Idades na lista:")
                
                print("\nIdade", contador + 1, ": ")
                
                idade = int(input("Digite a idade: "))
                
                try:
                    idade = Idade(idade)
                    self.__lista.append(str(idade))
                    contador += 1
                except ValueError as e:
                    print(f"Erro: {e}. Idade inválida. Por favor, insira uma idade válida.")
    
    def mostraMediana(self):
        lista = self.__lista
        mediana = Idade
        tamanho = len(lista)
        
        if (tamanho % 2 == 0):
           index = ((tamanho // 2 - 1) + (tamanho // 2)) // 2
           mediana = lista[index]
        else:
           mediana = lista[tamanho // 2]
        
        print("Mediana: " + mediana)

    def mostraMenor(self):
        lista = self.__lista
        print("Menor idade: " + lista[0])
    
    def mostraMaior(self):
        index = len(self.__lista)
        print("Maior data: " + self.__lista[index - 1])

    def listarEmOrdem(self):
        sortedLista = sorted(self.__lista)
        counter = 1
        for i in sortedLista:
            if i < (len(sortedLista)-1):
                print(counter,". \n",i,",")
                counter += 1
            else:
                print(counter,". \n",i,".")
                counter += 1
    def __str__(self):
        pass