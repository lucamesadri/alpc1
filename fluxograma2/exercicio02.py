# 2)Escreva um algoritmo que defina a faixa etária de uma pessoa e apresente a faixa em tela.
#   Caso a idade seja até 20 anos ele será considerado Jovem. 
#   Se a idade esteja entre 21 até 69 ele será considerado “Adulto”. 
#   Caso seja maior ou igual a 70 será considerado “Idoso”.

print("Vamos ver qual a sua faixa etária!")

print("Qual a sua idade?")
idade = int(input())

if idade <= 20:
    print("Você está na faixa etária de jovem!")

elif idade >= 21 and idade <= 69:
    print("Você está na faixa etária de adulto")

elif idade >= 70:
    print("Você está na faixa etária de idoso")

