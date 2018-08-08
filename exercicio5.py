times = ('vasco','flamengo','fluminense','botafogo')
elemento = input("Digite o nome de um clube carioca: ").lower()

if(times.__contains__(elemento)):
    print(f'O elemento está na tupla, o elemento é {elemento}')
else:
    print('Elemento não está na tupla')


intercaladas = times(::2), times(1::2)







print('retornando 2 tuplas que sao cada metada da original')
tupla_um = (milhonarios[0],)
tupla_dois = (milhonarios[int(round(len(milhonarios)/2))],)
for i in range(1,int(round(len(milhonarios)/2))):
    tupla_um += (milhonarios[i],)
for o in range(int(round((len(milhonarios)/2)+1)), len(milhonarios)):
    tupla_dois += (milhonarios[o],)
print(tupla_um)
print(tupla_dois)

excluir = int(input(f'''\nDados os segintes elementos:
0 - {milhonarios[0]}
1 - {milhonarios[1]}
2 - {milhonarios[2]}
3 - {milhonarios[3]}
4 - {milhonarios[4]}
5 - {milhonarios[5]}
Qual elemento você deseja excluir? 
'''))

if(excluir != 0):
    milhonarios_dois = (milhonarios[0],)
else:
    milhonarios_dois = (milhonarios[1],)
for i in range(1, len(milhonarios)):
    if i != excluir:
        milhonarios_dois += (milhonarios[i],)
print('tupla alterada:')
print(milhonarios_dois)

print('\n Invertendo a tupla original')
milhonarios_tres = (milhonarios[len(milhonarios)-1],)
for i in range(2,len(milhonarios)+1):
    milhonarios_tres += (milhonarios[len(milhonarios)-i],)
print('tupla invertida')
print(milhonarios_tres)



