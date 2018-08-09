'''Questão 5.1'''
times = ('vasco','flamengo','fluminense','botafogo')
elemento = input("Digite o nome de um clube carioca: ").lower()

if(times.__contains__(elemento)):
    print(f'\nO elemento está na tupla, o elemento é {elemento}\n')
else:
    print('Elemento não está na tupla\n')

'''Questão 5.2'''
print(f'\n Primeira metade da Tupla: {times[0:2]}, Segunda metade da Tupla: {times[2:4]}\n')





'''Questão 5.4'''
print(times[::-1])



