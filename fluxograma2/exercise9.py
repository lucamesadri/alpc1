# 9)Construa um algoritmo que calcule o consumo de combustível de um veículo qualquer baseado nas informações de quilometragem inicial e final de um percurso,
#   e a quantidade de gasolina consumida em litros. Caso o consumo esteja entre 10 e 16 litros/km mostre a mensagem “consumo normal”,
#   caso seja maior que 16 litros/km apresente a mensagem “consumo anormal”.

print("Let's calculate how much gasoline you use per Km and see if it is normal!")

print("Type your inicial mileage of the route")
inicial = int(input())

print("Type your final mileage of the route")
final = int(input())

print("Type how much gasoline you used in liters")
gasoline = int(input())

gasolinePerKm = (final - inicial) / gasoline

if gasolinePerKm >= 10 and gasolinePerKm <= 16:
    print(f"You are ok! Your consuming is {gasolinePerKm} and is normal.")

else:
    if gasolinePerKm > 16:
        print(f"You are not ok! Your consuming is {gasolinePerKm} and is anormal.")

    if gasolinePerKm < 10:
        print("Invalid operation! Turning off the program.")