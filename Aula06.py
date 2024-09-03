lista = {1,54,7,7,645,87,32,45,3}

print[0]
print[0:5]

lista.sort()
lista.sort(reverse=True)
print(f'lista ordena {lista} ')

lista.remove(8)
lista.pop(7)
del lista[2:5]

nome = 'Thalita'
lista.append(nome)
print(lista)

lista.insert(1,'Vitória')
print(lista)

lista[2] = 'Thalita'
print(lista)

print('Vitória' in lista)

if 'Thalita' in lista:
    #esse bloco só será executado quando a condição é true
   print('sim, a Thalita está na lista')
else:
    #esse bloco só será executado quando a condição é false
    print('não, a Thalita não está na lista')