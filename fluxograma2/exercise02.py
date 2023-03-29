# 2)Escreva um algoritmo que defina a faixa etária de uma pessoa e apresente a faixa em tela.
#   Caso a idade seja até 20 anos ele será considerado Jovem. 
#   Se a idade esteja entre 21 até 69 ele será considerado “Adulto”. 
#   Caso seja maior ou igual a 70 será considerado “Idoso”.

print("Let's see what age group you are in!")

print("What is your age?")
age = int(input())

if age <= 20:
    print("You are in the young age group!")

elif age >= 21 and age <= 69:
    print("You are in the adult age group")

elif age >= 70:
    print("You are in the elderly age group")
