# 8)Escreva um algoritmo que calcule o valor de desconto que será oferecido ao comprador de uma loja de acordo com o valor da compra:
#   compras até R$100 desconto de 5%, compras maiores que R$ 100 e ate R$400 desconto de 10%, e acima de R$ 400 desconto de 13%.
#   Após o calculo do valor com desconto, acrescente o valor da taxa de entrega que é de R$ 1,5 por item comprado.

print("You received a discount! Let's calculate the value of the purchase with the discount and shipping taxes")

print("How many items did you buy?")
items = int(input())

print("How much did the purchase originally cost?")
value = float(input())

if value <= 100:
    discount = value * 0.95

elif value > 100 and value <= 400:
    discount = value * 0.90

elif value > 400:
    discount = value * 0.87

purchase = (items * 1.5) + discount

print(f"Your purchase with the discount is {discount:.2f} reais, but with shipping taxes will be {purchase:.2f} reais.")



