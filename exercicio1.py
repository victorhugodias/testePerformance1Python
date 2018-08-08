ajuda = 0
soma = 0
numero = int(input("Digite um número: "))


while ajuda <= numero:
    if(ajuda % 2 != 0):
        soma += ajuda
    ajuda = ajuda + 1

print(f'A soma dos números ímpares são: {soma}')