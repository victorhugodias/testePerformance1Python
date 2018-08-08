numero = int(input("Digite um número para achar o fatorial: "))
ajuda = numero
fatorial = numero
if numero == 0:
    print("O fatorial de 0 é 1 ")
elif numero > 0:
    ajuda = ajuda - 1
    for x in range(0, numero - 1):
        fatorial = fatorial * ajuda
        ajuda = ajuda - 1
    print(f"O fatorial é: {fatorial}")
elif numero < 0:
    print('Não pode número negativo')