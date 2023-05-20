# 3)Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, utilizando a fórmula:
#   PRESTACAO = VALOR + (VALOR *(TAXA/100) * TEMPOEMDIAS).

print("Let's calculate the value of a delayed installment:")
print("Type the value:")
value = int(input())

print("Type how many days the installment is delaying:")
delay = int(input())

print("Type the tax")
tax = int(input())

installment = (value + (value * (tax / 100)) * delay)

print(f"The installment value is {installment:.2f} reais")


