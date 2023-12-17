numeros = []

while True: # função While usada por não saber qual a quantidade exata de números que sera adicionada
    dados = int(input("Insira um número inteiro (digite -1 para sair): "))

    if dados == -1: #como solicitado que serão aceitos números na lista até que seja digitado o "-1", usa-se a função "if dados == -1, break o loop"
        break

    numeros.append(dados) 

print(len(numeros))

print(numeros)

print('\n'.join(map(str, numeros[::-1])) + '\n')

print(f"A soma dos valores é {sum(numeros)}")

media = sum(numeros) / len(numeros)

print(f"A média dos valores é {media}")


# Contar quantos números são maiores que 3.3333333333333335
contagem = 0

for numero in numeros:
    if numero > media:
        contagem += 1

print(f"Quantidade de números maiores que {media}: {contagem}")



# Contar quantos números são menores que 7
contagem = 0

for numero in numeros:
    if numero < 7:
        contagem += 1

print(f"Quantidade de números menores que 7: {contagem}")

print("Obrigado pelas informações")