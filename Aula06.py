lista = {1,54,7,7,645,87,32,45,3}

print[0]
print[0:5]

lista.sort()
lista.sort(reverse=True)
print(f'lista ordena {lista}')

lista.remove(8)
lista.pop(7)
del lista[2:5]

nome = 'philipi'
lista.append(nome)
print(lista)

lista.insert(1,'josé')
print(lista)

lista[2] = 'philipi'
print(lista)

print('josé' in lista)

if 'philipi' in lista:
    #esse bloco só será executado quando a condição é true
   print('sim, o philipi está na lista')
else:
    #esse bloco só será executado quando a condição é false
    print('não, o philipi não está na lista')