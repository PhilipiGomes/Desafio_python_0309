lista = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
print(lista)


if "junho" in lista:
    print("O mes de junho esta na lista")
else:
    print("O mes de junho nao esta na lista  ")

lista.insert(2, 'Abril')
lista.pop(5)
lista.insert(5,'Dezembro')
lista.pop()
print(lista)


