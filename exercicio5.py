'''Questão 5.1'''
times = ('vasco','flamengo','fluminense','botafogo')
elemento = input("Digite o nome de um clube carioca: ").lower()

if(times.__contains__(elemento)):
    print(f'\nO elemento está na tupla, o elemento é {elemento}\n')
else:
    print('Elemento não está na tupla\n')

'''Questão 5.2'''
print(f'\n Primeira metade da Tupla: {times[0:2]}, Segunda metade da Tupla: {times[2:4]}\n')


'''Questão 5.3'''
print('''
0 - Vasco
1 - Flamengo
2 - Fluminense
3 - Botafogo
''')

excluir = int(input('Qual você deseja excluir da lista? \n'))

tuplaAjuda = ()

if(excluir < 0 or excluir > 3):
    print('Elemento não existente')
else:
    for x in range(0,4):
        if(x != excluir):
            tuplaAjuda += (times[x],)

print(tuplaAjuda)


'''Questão 5.4'''
print(times[::-1])



