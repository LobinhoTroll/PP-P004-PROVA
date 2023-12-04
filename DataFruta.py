from ListaDatas import ListaDatas

def main():
    #nomes = ListaNomes()
    datas = ListaDatas()
    #salarios = ListaSalarios()
    #idades = ListaIdades()


    datas.entradaDeDados()
    print("___________________")
    datas.mostraMaior()
    print("___________________")
    datas.mostraMenor()
    print("___________________")
    datas.mostraMediana()
    print("___________________")
    datas.modificaData()
    print("___________________")
    datas.listarEmOrdem()

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
