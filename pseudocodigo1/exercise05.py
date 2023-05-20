# 5)Faça um programa que receba a altura e o sexo de uma pessoa e que calcule e mostre o seu peso ideal, utilizando as seguintes formulas:
# a.Para homens: (72.7 * h) – 58
# b.Para mulheres: (62.1 * h) – 44.7

print("Let's calculate your ideal weight!")

print("Enter the number that corresponds to your gender")
print("1. male")
print("2. female")
gender = int(input())

print("Enter your height:")
height = int(input())

if gender == 1:
    weight = (72.7 * height) - 58

else:
    weight = (62.1 * height) - 44.7

print(f"Your ideal weight is {weight:.2f} KG")
