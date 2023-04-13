# 12)Escreva um algoritmo em FLUXOGRAMA para calcular o valor da bolsa de estudos paga pela empresa a seus funcionários, 
#    utilize a tabela abaixo. De acordo com o Tipo do curso existe um percentual pago da bolsa, 
#    sendo que o valor calculado do percentual não pode superar o valor limite por tipo. 
#    Insira pelo menos duas restrições nos dados de entrada .
#    +-----------+---------------------+-----------------+
#    |   Tipo    |   Percentual Pago   |  Valor Limite   |
#    +-----------+---------------------+-----------------+
#    |  Ingles   |        40%          |    R$ 200,00    |
#    |  Espanhol |        40%          |    R$ 200,00    |
#    | Graduação |        55%          |    R$ 300,00    |
#    +-----------+---------------------+-----------------+

print("Let's calculate the value of your scholarship!")

print("What is your type of course?")
print("+--------------+")
print("|1- English    |")
print("|2- Spanish    |")
print("|3- Graduation |")
print("+--------------+")
course = int(input())

# THIS IS UNNECESSARY
while course < 1 or course > 3:
    print("Invalid number, write the number correspondent to your course!")
    print("+--------------+")
    print("|1- English    |")
    print("|2- Spanish    |")
    print("|3- Graduation |")
    print("+--------------+")
    course = int(input())

print("What is the value of your course")
courseValue = int(input())

if course == 1:
    percentageValue = (courseValue * 40) / 100
    scholarshipValue = percentageValue

    if percentageValue > 200:
        scholarshipValue = 200
else:   
    if course == 2:
        percentageValue = (courseValue * 40) / 100
        scholarshipValue = percentageValue

        if percentageValue > 200:
            scholarshipValue = 200
    else:
        if course == 3:
            percentageValue = (courseValue * 55) / 100
            scholarshipValue = percentageValue

            if percentageValue > 300:
                scholarshipValue = 300

print(f"The value of your scholarship will be {scholarshipValue:.0f} reais")







