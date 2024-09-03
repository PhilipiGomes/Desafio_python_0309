lista = []

nome1 = input('digite um nome:')
lista.append(nome1)

nome2 =input('digite um nome:')
lista.append(nome2)

lista.sort()

if nome1 in lista:
    print(f'sim, o (nome1)esta na lista')
    print(f'nao, o (nome1) nao esta na lista')

num1 = 10
num2 = 20
if num1 > num2:
    print('é maior')
else:
    print('é menor')
    if num1 < num2:
        print('é menor')
    else:
        print('é maior')
print('fim do bloco else')

notas = []
print(20*'-', 'BOLETIM ESCOLAR',20*'-')
numero_usuario1 = int(input('digite uma nota:'))
notas.append(numero_usuario1)

numero_usuario2 = int(input('digite uma nota:'))
notas.append(numero_usuario2)

numero_usuario3 = int(input('digite uma nota:'))
notas.append(numero_usuario3)

numero_usuario4 = int(input('digite uma nota:'))
notas.append(numero_usuario4)

numero_usuario5 = int(input('digite uma nota:'))
notas.append(numero_usuario5)

#len conta a quantidade de elementos dentro de uma lista
quantidade_notas = len(notas)

#sum irá somar todos os valores da lista 
soma = sum(notas)

media = soma / quantidade_notas 

print(f' as notas são: {notas}')
print(f'a quantidade de noats: {quantidade_notas}')
print(f'a soma de todas as notas: {soma}')
print(f'A media: {media}')

'''
#TODO: Situação
aprovado >= 7
recuperacao >= 5
reprovado

'''
if media >= 7:
    print(f'aprovado com media {media}')
elif media >=5:
    print(f'recuperação com media {media}')
else:
    print(f'reprovado com média{media}')