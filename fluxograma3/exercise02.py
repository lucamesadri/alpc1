# 2)O custo ao consumidor de um carro novo é a soma do preço da fábrica
#   com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. 
#   Faça um programa que receba o preço de fábrica de um veículo, 
#   o percentual de lucro do distribuidor e o percentual de impostos. Calcule e mostre:
#   
#   a.O valor correspondente ao lucro do distribuidor
#   b.O valor correspondente aos impostos
#   c.O preço final do veículo

print("Let's calculate the distributor's profit")
print("Calculate taxes values too")
print("And finally the final value of the vehicle")

print("Type the vehicle factory gate price:")
factoryPrice = int(input())

print("Type the percentage of distributor's profit")
profitPercentage = int(input())

print("Type the percentage of taxes")
taxesPercentage = int(input())

profitValue = (factoryPrice * profitPercentage) /  100

taxesValue = (factoryPrice * taxesPercentage) /  100

finalValue = factoryPrice + profitValue + taxesValue

print(f"The profit value is {profitValue:.2f} reais")
print(f"The taxes value is {taxesValue:.2f} reais")
print(f"The final price is {finalValue:.2f} reais")