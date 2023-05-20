# # 1)Escreva um programa que receba:
# a.  O código de um produto comprado, supondo que a digitação do código do produto seja sempre válida, 
#     isto é, um número inteiro entre 1 e 10;
# b.  O peso do produto em quilos;
# c.  O código do país de origem, supondo que a digitação do código seja sempre válida, isto é, um número entre 1 e 3.
#     Código do pais de origem  	Imposto
#               1	                   0%
#               2	                   15%
#               3	                   25%

# Código do produto 	Preço por grama
#       1 a 4	              10
#       5 a 7	              25
#       8 a 10                35
# 	Calcule e mostre:
# 	-o peso do produto convertido para gramas;
# 	-o preço total do produto comprado;
# 	-o valor do imposto, sabendo que ele é cobrado sobre o preço total do produto comprado e depende do país de origem;
# 	-o valor total, preço total do produto mais imposto;

print("Lets calculate some things: product's weight, product's price, tax value, total value!")

countryCode = 0
counter = 0
productCode = 0

print("| Origin country code |  Tax  |")
print("|           1         |  0%   |")
print("|           2	     |  15%  |")
print("|           3	     |  25%  |")

while countryCode < 1 or countryCode > 3:
    print("Type the origin country code:")
    countryCode = int(input())

    counter = counter + 1
    
    if counter > 7:
        break

while countryCode < 1 or countryCode > 3:
    print("Type the origin country code:")
    countryCode = int(input())

    counter = counter + 1
    
    if counter > 7:
        break

print("|Código do produto |	Preço por grama|")
print("|     1 a 4	      |       10       |")
print("|     5 a 7	      |       25       |")
print("|     8 a 10       |       35       |")

while productCode < 1 or productCode > 10:
    print("Type the product's code:")
    productCode = int(input())

    counter = counter + 1
    
    if counter > 7:
        break

# if productCode >= 1 and productCode <= 4:
