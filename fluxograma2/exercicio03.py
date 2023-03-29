# 3)Escreva um algoritmo que solicite a quantidade total em miligramas de colesterol mau 
#   existente no sangue de um paciente. 
#   Considerando que o valor máximo ideal para uma pessoa saudável é 130mg,
#   caso a quantidade esteja menor apresente uma mensagem indicando que esta menor. 
#   Caso esteja acima, calcule o percentual que esta acima e apresente uma mensagem.

print("Vamos ver se seu colesterol está ok!")

print("Digite o valor total de colesterol mau no seu sangue: ")
colesterol = int(input())

if colesterol <= 130:
    print("Você está saudável! O seu colesterol está dentro da faixa ideal.")

elif colesterol > 130:
    colesterolPerc = ((colesterol - 130) / 130) * 100

    print(f"Você infelizmente não está saudável. Seu colesterol está {colesterolPerc:.0f}% acima da faixa ideal.") 