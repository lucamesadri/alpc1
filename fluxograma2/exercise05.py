# 5)Escreva um algoritmo que calcule o valor da multa (em UFIR) 
#   que um motorista deve receber de acordo com a velocidade de seu carro. 
#   Acima de 60km/h e ate 100km/h multa media 60 UFIR,
#   acima de 100 km/h até 160km/h grave 120 UFIR,
#   e acima de 160km/h gravíssima 180 UFIR

print("Let's calculate the cost of a speeding ticket (in UFIR):")

print("At what speed were you driving?")
speed = int(input())

ticket_value = 4.3329


if speed > 60 and speed <= 100:
    ticket = ticket_value * 60
    print(f"The cost of the speed ticket is: {ticket:.0f} reais")

elif speed > 100 and speed <= 160:
    ticket = ticket_value * 120
    print(f"The cost of the speed ticket is: {ticket:.2f} reais")

elif speed > 160:
    ticket = ticket_value * 180
    print(f"The cost of the speed ticket is: {ticket:.2f} reais")