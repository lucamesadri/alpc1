# 7)Escreva um algoritmo que calcule o valor de uma chamada de telefone. 
#   Deverá ser informado a quantidade de minutos falados durante a ligação além de sua origem. 
#   Considere que uma ligação “local” custa R$0.020,
#   ligação “intermunicipal” R$0,08 e “interestadual” R$0,1.

print("Let's calculate the cost of your call")

print("How many minutes was your call? ")
minutes = int(input())

print("Write the number corresponding to where your call was")
print("+--------------+")
print("|1- Local      |")
print("|2- Intercity  |")
print("|3- Interstate |")
print("+--------------+")
origin = int(input())

if origin == 1:
    cost = minutes * 0.02
    print(f"The cost of your call will be: {cost:.2f} reais")
elif origin == 2:
    cost = minutes * 0.08
    print(f"The cost of your call will be: {cost:.2f} reais")
elif origin == 3:
    cost = minutes * 0.1
    print(f"The cost of your call will be: {cost:.2f} reais")
