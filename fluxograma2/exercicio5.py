# 5)Escreva um algoritmo que calcule o valor da multa (em UFIR) 
#   que um motorista deve receber de acordo com a velocidade de seu carro. 
#   Acima de 60km/h e ate 100km/h multa media 60 UFIR,
#   acima de 100 km/h até 160km/h grave 120 UFIR,
#   e acima de 160km/h gravíssima 180 UFIR

print("Vamos calcular o custo da multa (em UFIR):")

print("Qual a velocidade em que você estava dirigindo?")
velocidade = int(input())

valor_da_multa = 4.3329


if velocidade > 60 and velocidade <= 100:
    multa = valor_da_multa * 60
    print(f"O valor da multa é: {multa:.2f} reais")

elif velocidade > 100 and velocidade <= 160:
    multa = valor_da_multa * 120
    print(f"O valor da multa é: {multa:.2f} reais")

elif velocidade > 160:
    multa = valor_da_multa * 180
    print(f"O valor da multa é: {multa:.2f} reais")