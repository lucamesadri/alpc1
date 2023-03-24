print("Digite quantas pessoas vão ser chamadas para o churraso vegano:")
convidados = int(input())

carneDeSoja = convidados * 250

if convidados >= 4:
    carneDeSoja = carneDeSoja / 1000
    print("O total de carne de soja a ser comprado é: %.3f KG" % carneDeSoja)

else:
    print("O total de carne de soja a ser comprado é: %.0f gramas" % carneDeSoja)