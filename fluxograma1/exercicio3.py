# 3)Faça um algoritmo que calcule o valor de reembolso de despesas de combustível de um funcionário.  
#   Considere que o carro tem o consumo de 1 litro de gasolina a cada 13km rodado. 
#   E o preço do litro de gasolina é de R$ 2,20.

print("Vamos calcular o valor de o reembolso da gasolina gasta!")
print("Digite o número de Km rodados:")

kmRodados = int(input())

gasolinaGasta = kmRodados / 13

reembolso = gasolinaGasta * 2.20

print("O valor de reembolso será: %.2f R$" % reembolso)