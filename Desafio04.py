# Definição das funções inserir_notas e media
def inserir_notas(n_notas,lista_notas):
    # Insere n elementos em uma lista fornecida
    for i in range(1,n_notas + 1):
        nota = float(input(f'Insira a {i}° nota do aluno: '))
        lista_notas.append(nota)
        i += 1
    return lista_notas

def media(lista_notas):
    # Calcula a média
    media = sum(lista_notas)/len(lista_notas)
    # Faz a verificação (se for maior ou igual a 7: aprovado, se for entre 5 e 6.9: recuperação, senão: reprovado)
    if media >= 7:
        print("Aprovado")
    elif media >= 5 and media <= 6.9:
        print("Recuperação")
    else:
        print("Reprovado")

# Declaração da lista e do número de notas
notas = []
n = 5

# Execução das funções
media(inserir_notas(n, notas))
