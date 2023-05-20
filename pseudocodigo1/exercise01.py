# 1)Elaborar um programa que efetue o cálculo do valor da conversão em real (R$) de um valor lido em tela em dólar (US$). 
#   O programa deverá solicitar o valor da cotação do dólar.

print("Let's convert your currency!")
print("Type the number that corresponds to your choice:")

print("1. Real to Dolar")
print("2. Dolar to Real")
choice = int(input())

print("Type the value:")
value = int(input())

print("Type the quotation:")
quotation = int(input())

if choice == 1:
    newValue = value / quotation
    print(f"Your converted currency is {newValue:.2f} dolars")

if choice == 2:
    newValue = value * quotation
    print(f"Your converted currency is {newValue:.2f} reais")