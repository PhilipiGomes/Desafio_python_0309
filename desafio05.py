lista1 = ['segunda','terça','quarta','quinta','sexta'
          ,'Segunda Feira','Terça Feira','Quarta Feira','Quinta Feira','Sexta Feira'
          'segunda feira','terça feira','quarta feira','quinta feira','sexta feira'
          'Segunda','Terça','Quarta','Quinta','Sexta'
          ,'Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira'
          'segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira'
          ]
resposta = input('Informe um dia da semana: ')

if resposta in lista1:
    print(f'{resposta} está na lista')
else:
    print('|------------------------------------------------------|')
    print('| Ainda não temos informações sobre esse dia da semana |')
    print('|------------------------------------------------------|')
