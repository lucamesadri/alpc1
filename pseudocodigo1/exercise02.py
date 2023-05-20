# 2)Construir um programa que efetue o cálculo do salário líquido de um professor. 
#   Para fazer este programa, você deverá possuir alguns dados, tais como:
#   valor da hora aula, número de horas trabalhadas no mês e percentual de desconto do INSS.
#   Em primeiro lugar, deve-se estabelecer qual será o seu salário bruto para efetuar o desconto
#   e ter o valor do salário líquido.

print("Let's calculate a professor's salary:")
print("Type the per-hour value of a class:")
perhourValue = int(input())

print("Type how many hours the professor worked in a month:")
hoursMonth = int(input())

print("Type the INSS discount percentual:")
inssPerc = int(input())

baseSalary = perhourValue * hoursMonth

discount = (baseSalary * inssPerc) / 100

newSalary = baseSalary - discount

print(f"The professor's salary is {newSalary:.2f} reais")

