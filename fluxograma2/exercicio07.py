# 7)Escreva um algoritmo que calcule o valor de uma chamada de telefone. 
#   Deverá ser informado a quantidade de minutos falados durante a ligação além de sua origem. 
#   Considere que uma ligação “local” custa R$0.020,
#   ligação “intermunicipal” R$0,08 e “interestadual” R$0,1.

print("Vamos calcular o valor da sua chamada")

print("Digite quanto durou sua chamada em minutos: ")
minutos = int(input())

print("Digite o número correspondente a sua chamada:")
print("+-------------------+")
print("|1- Local           |")
print("|2- Intermunicipal  |")
print("|3- Interestadual   |")
print("+-------------------+")
origem = int(input())

if origem == 1:
    custo = minutos * 0.02
    print(f"O custo da sua chamada será: {custo:.2f} reais")
elif origem == 2:
    custo = minutos * 0.08
    print(f"O custo da sua chamada será: {custo:.2f} reais")
elif origem == 3:
    custo = minutos * 0.1
    print(f"O custo da sua chamada será: {custo:.2f} reais")
