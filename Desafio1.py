# Abaixo estão as variáveis da lista; Foi criada uma nova variável a partir da variável pai.
lista = [5,8,2,9,1] # \
                    #   | Variáveis pai 
lista_ = [5,8,2,9,1]# /

lista2 = lista_ # \
                #   | Variáveis filho
lista3 = lista2 # /
 
print('----------------------------------------')
print(f'Lista sem alterações: {lista} ')
print('----------------------------------------')

lista.sort()
print('------------------------------------------')
print(f'Lista na ordem crescente: {lista}')
print('------------------------------------------')
lista.sort(reverse=True)
print('--------------------------------------------')
print(f'Lista na ordem decrescente: {lista}')
print('--------------------------------------------')


novo_numero1 = 7
novo_numero2 = 3
lista2.append(novo_numero1)
lista2.insert(1, novo_numero2)
print('---------------------------------------------------------------------------------------------------')
print(f'Lista com o número 7 adicionado na última posição e o número 3 na posição 2: {lista2} ')
print('---------------------------------------------------------------------------------------------------')

novo_numero3 = 10
lista3.pop(0)
lista3.insert(0,novo_numero3)
lista3.pop(4)
print('-------------------------------------------------------------------------------------------------------')
print(f'Lista com o número na posição 1 substituído por "10" e número 9 removido da lista: {lista3}')
print('-------------------------------------------------------------------------------------------------------')
del lista3[1:4]
print('------------------------------------------------------------')
print(f'Lista com os numeros da posição 2 a 4 excluidos: {lista3} ')
print('------------------------------------------------------------')
