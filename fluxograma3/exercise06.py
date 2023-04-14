# 6)Faça um programa que receba duas notas, e calcule e mostre a média aritmética e a mensagem que esta na tabela abaixo:

#     Média   | Mensagem
#   0,0 – 4,0 | Reprovado
#   4,0 – 7,0 |  Exame
#   7,0 – 10  |  Aprovado

print("Let's calculate your arithmetic mean and see if you are approved acording to this table:")
print(" |    Mean   | Situation |")
print(" | 0,0 - 4,0 |  Failed   |")
print(" | 4,0 - 7,0 |  Exam     |")
print(" | 7,0 - 10  |  Passed   |")

print("Type your first grade:")
firstGrade = int(input())

print("Type your second grade:")
secondGrade = int(input())

mean = (firstGrade + secondGrade) / 2

if mean >= 0 and mean < 4:
    print(f"Your arithmetic mean is {mean:.1f} and you failed this year at school.")
else:
    if mean >= 4 and mean < 7:
        print(f"Your arithmetic mean is {mean:.1f} and you have to do the exam!")
    else:
        if mean > 10:
            print("Your arithmetic mean is 10 and you passed this year at school")
        else:
            print(f"Your arithmetic mean is {mean:.1f} and you passed this year at school")
