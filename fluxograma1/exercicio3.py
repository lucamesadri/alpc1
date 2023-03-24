print("Vamos calcular o valor de o reembolso da gasolina gasta!")
print("Digite o número de Km rodados:")

kmRodados = int(input())

gasolinaGasta = kmRodados / 13

reembolso = gasolinaGasta * 2.20

print("O valor de reembolso será: %.2f R$" % reembolso)

# primeiro tu vai precisar descobrir a distancia que o carro percorreu, por isso pergunto os Km rodados no inicio

#depois eu divido os Km rodados por 13, isso porque 