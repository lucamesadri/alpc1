# 3)Escreva um algoritmo que solicite a quantidade total em miligramas de colesterol mau 
#   existente no sangue de um paciente. 
#   Considerando que o valor máximo ideal para uma pessoa saudável é 130mg,
#   caso a quantidade esteja menor apresente uma mensagem indicando que esta menor. 
#   Caso esteja acima, calcule o percentual que esta acima e apresente uma mensagem.

print("Let's see if your cholesterol is ok!")

print("Type the total amount in milligrams of bad cholesterol in your blood: ")
cholesterol = int(input())

if cholesterol <= 130:
    print("You are healthy! Your cholesterol is within the ideal range.")

elif cholesterol > 130:
    cholesterolPerc = ((cholesterol - 130) / 130) * 100

    print(f"Unfortunately, you are unhealthy. Your cholesterol is {cholesterolPerc:.0f}% above the ideal range.") 