print("Vamos calcular qual é o maior número, o do meio e o menor número!")

print("Digite o primeiro número:")
num1 = int(input())

print("Digite o segundo número:")
num2 = int(input())

print("Digite o terceiro número:")
num3 = int(input())

if num1 > num2:
    if num1 > num3:
        print(f"O maior número é {num1}")
        if num2 > num3:
            print(f"O número do meio é {num2}")
            print(f"O menor número é {num3}")
        else:
            print(f"O número do meio é {num3}")
            print(f"O menor número é {num2}")
    else:
        print("O maior e", num3)
        print("O do meio e", num1)
        print("O menor e", num2)

else:
    if num2 > num1:
        if num2 > num3:
            print(f"O maior número é {num2}")
            if num1 >  num3:
                print(f"O número do meio é {num1}")
                print(f"O menor número é {num3}")
            else:
                print(f"O número do meio é {num3}")
                print(f"O menor número é {num1}")
        
    else:
        if num3 > num1:
            if num3 > num2:
                print(f"O maior número é {num3}")
                if num1 > num2:
                    print(f"O número do meio é {num1}")
                    print(f"O menor número é {num2}")
                else:
                    print(f"O número do meio é {num2}")
                    print(f"O menor número é {num1}")
