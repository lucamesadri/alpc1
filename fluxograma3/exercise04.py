# 4)Faça um programa que receba o peso de uma pessoa, calcule e mostre:
#   O novo peso da pessoa se engordar 15% sobre o peso digitado
#   O novo peso da pessoa se emagrecer 20% sobre o peso digitado

print("Let's calculate what will be your new weight!")

print("Type your weight in grams:")
weight = int(input())

# THIS IS UNNECESSARY
print("Type what new weight you wanna see:")
print("+-------------------+")
print("|1- Gain 15% weight |")
print("|2- Lose 20% weight |")
print("+-------------------+")
choice = int(input())

weight = weight / 1000

# THIS IS UNNECESSARY TOO, YOU COULD SHOW BOTH RESULTS, BUT I PREFER THIS WAY SO I CAN TRAIN IF STATEMENTS
if choice == 1:
    gainedWeight = (weight * 15) / 100
    weight = weight + gainedWeight
    print(f"Your new weight will be {weight:.2f}KG")
if choice == 2:
    losenWeight = (weight * 20) / 100
    weight = weight - losenWeight
    print(f"Your new weight will be {weight:.2f}KG")