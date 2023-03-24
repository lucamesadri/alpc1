# 1)Escreva o algoritmo de um programa que solicite dois números quaisquer ao usuário,
#   se os números forem iguais mostre uma mensagem e mostre a media dos dois,
#   caso contrário mostre qual o maior número e qual o menor número. 

print("Digite 2 números, por favor!")
print("Primeiro número: ")
num1 = int(input())

print("Segundo número: ")
num2 = int(input())

if num1 == num2:
    media = (num1 + num2) / 2
    
    print(f"Como os números são iguais, a média é: {media:.0f}")

else:
    if num1 > num2:
        print(f"O número maior é {num1:.0f} e o menor é {num2:.0f}")
    
    if num2 > num1:
        print(f"O número maior é {num2:.0f} e o menor é {num1:.0f}")