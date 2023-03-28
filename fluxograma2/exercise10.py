# 10)Escreva um algoritmo que calcule o valor de Imposto de Renda que uma Pessoa Física deve pagar de acordo com o valor total de seu rendimento anual: 
# abaixo de R$19.200 isento, acima deste valor e até R$30.000 8%. Mais que R$30.000 anuais 11%.

print("Let's calculate your income tax!")

print("Type your total anual income")
income = int(input())

if income <= 19200:
    print("You are exempt of income tax!")

elif income > 19200 and income <= 30000:
    tax = income * 1.08
    print(f"You have a tax percentage of 8% and will have to pay {tax:.2f} reais")

elif income > 30000:
    tax = income * 1.11
    print(f"You have a tax percentage of 11% and will have to pay {tax:.2f} reais")
