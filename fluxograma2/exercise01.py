# 1)Escreva o algoritmo de um programa que solicite dois números quaisquer ao usuário,
#   se os números forem iguais mostre uma mensagem e mostre a media dos dois,
#   caso contrário mostre qual o maior número e qual o menor número. 

print("Type 2 numbers, please!")
print("First number: ")
num1 = int(input())

print("Second number: ")
num2 = int(input())

if num1 == num2:
    mean = (num1 + num2) / 2
    
    print(f"As the numbers are equal, the mean is: {mean:.0f}")

else:
    if num1 > num2:
        print(f"The highest number is: {num1:.0f} and the smallest is: {num2:.0f}")
    
    if num2 > num1:
        print(f"The highest number is: {num2:.0f} and the smallest is: {num1:.0f}")