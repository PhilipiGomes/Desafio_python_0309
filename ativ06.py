lista = []

# Solicitando e recebendo os números para saber o maior e o menor número da lista inserida
num1 = float(input('Digite um número: '))
lista.append(num1)
num2 = float(input('Digite um número: '))
lista.append(num2)
num3 = float(input('Digite um número: '))
lista.append(num3)
num4 = float(input('Digite um número: '))
lista.append(num4)

#Exibindo e fazendo a diferenciação do maior e do menor número da lista
print(f'O maior número da lista é: {max(lista)}')
print(f'O menor número da lista é: {min(lista)}')