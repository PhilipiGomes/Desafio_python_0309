Lista = {1,54,7,7,645,87,32,45,3}

print[0]
print[0:5]

lista.sort()
lista.sort(reverse=true)
print(f'lista ordena {lista}')

lista.remove(8)
lista.pop(7)
del lista[2:5]

nome = 'bernardo'
lista.append(nome)
print(lista)

lista.insert(1,'cordeiro')
print(lista)

lista[2] = 'bernardo'
print(lista)

print('cordeiro' in lista)

if 'bernardo' in lista:
    #esse bloco só será executado quando a condição é true
   print('sim, o bernardo está na lista')
else:
    #esse bloco só será executado quando a condição é false
    print('não, o bernardo não está na lista')