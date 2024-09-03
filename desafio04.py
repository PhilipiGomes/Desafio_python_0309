num1 = input('Digito o primeiro número: ')
num1 = int(num1)
num2 = input('Digite o segundo número: ')
num2 = int(num2)

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num2} é maior que {num1}')
else:
    print(f'Os números tem o mesmo valor ')