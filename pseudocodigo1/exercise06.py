# 6)Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação.
#     Preço	                Percentual Aumento
#   Até R$ 50,00	                5
#   Entre R$ 50,00 e R$ 100,00	    10
#   Acima de R$ 100,00	            15
#     Novo preço	                         Classificação
#  Até R$ 80,00	                                Barato
#  Entre R$ 80,00 e R$120,00(inclusive)	        Normal
#  Entre R$ 120,00 e R$ 200,00 (inclusive)	    Caro
#  Maior que R$ 200,00	                        Muito Caro

print("Let's calculate the new price of a product")

print("Enter the price")
price = int(input())

perc = 0

if price < 50:
    perc = 1.05
else:
    if price >= 50 and price <= 100:
        perc = 1.1
    else:
        perc = 1.15

newPrice = price * perc

if newPrice < 80:
    message = "cheap"
else:
    if newPrice >= 80 and newPrice <= 120:
        message = "normal"
    else:
        if newPrice > 120 and newPrice <= 200:
            message = "expensive"
        else:
            message = "really expensive"

print(f"The new price is {newPrice:.2f} reais and it is {message}")
