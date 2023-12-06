def ajustar_salario(salario):
    return salario * 1.1

salarios_reajustados = map(ajustar_salario, salarios)


salarios_reajustados = list(salarios_reajustados)


for salario_reajustado in salarios_reajustados:
    print(salario_reajustado)
