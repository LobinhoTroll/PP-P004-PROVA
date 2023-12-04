from ListaDatas import ListaDatas

def main():
    
    datas = ListaDatas()
    #nomes = ListaNomes()
    #salarios = ListaSalarios()
    #idades = ListaIdades()
    
    while True:

            print("========== Menu de opções ==========")
            print(" ")
            print("[1] - Incluir um nome na lista de nomes: ")
            print("[2] - Incluir um salário na lista de salários: ")
            print("[3] - Incluir uma data na lista de datas: ")
            print("[4] - Incluir uma idade na lista de idades: ")
            print("[5] - Percorrer as listas de nomes e salários: ")
            print("[6] - Calcular o valor da folha com um reajuste de 10% ")
            print("[7] - Modificar o dia das datas anteriores a 2019")
            print("[8] - Sair. ")

            opcao = int(input("Escolha uma opção: "))
            print(" ")
            
            if opcao == 1:
                # Precisa Implementar
                print(" ")
                        
            elif opcao == 2:
                # Precisa Implementar
                print(" ")  
                        
            elif opcao == 3:
                datas.entradaDeDados()
                print("---------------")
                datas.mostraMaior()
                print("---------------")
                datas.mostraMenor()
                print("---------------")
                datas.mostraMediana()
                print("---------------")
                datas.listarEmOrdem()
                print(" ")
                
            elif opcao == 4:
                # Precisa Implementar
                print(" ")
                
            elif opcao == 5:
                # Precisa Implementar
                print(" ")
                
            elif opcao == 6:
                # Precisa Implementar
                print(" ")
                
            elif opcao == 7:
                datas.modificaData()
                datas.listarEmOrdem()
                print(" ")
                
            elif opcao == 8:
                print("Programa finalizado. Até a próxima!")
                exit(0)
            else:
                print("Opcão inválida. Tente novamente.")
                print(" ")

if __name__ == "__main__":
    main()
