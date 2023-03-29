# 11)Escreva o algoritmo em FLUXOGRAMA que calcule o valor total de aluguel e taxas a serem cobrados de um morador. 
#    Solicite o valor do aluguel, o valor do condomínio, considere que o valor do metro cubico do gas é de R$ 1,80 
#    e o valor da taxa de consumo de agua é de R$ 0,60 por metro cubico de agua consumida. 
#    Apresente também o valor de 5% do valor total do aluguel que pode ser dado como desconto caso seja pago 5 dias antes do vencimento.

print("Let's calculate how much is your total rent and taxes!")

print("Type the value of your rent:")
rent = int(input())

print("Type the value of the condominium:")
condominium = int(input())

print("Type the value of the gas per cubic meter:")
gas = int(input())

print("Type the value of the gas per cubic meter:")
water = int(input())

gas = gas * 1.80

water = water * 0.60

rentTotal = rent + condominium + water + gas

discount = (rentTotal / 100) * 5

print(f"Your total rent value will be {rentTotal:.2f} reais.")

print(f"And if paid during the last 5 days of the expiraton date you will receive a discount of {discount:.2f} reais.")



