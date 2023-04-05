# 1)Faça um programa que receba o salário-base de um funcionário, calcule e mostre o salário a receber, 
#   sabendo-se que esse funcionário tem gratificação de 5% sobre o salário base
#   e paga imposto de 7% sobre o salário-base.

print("Let's calculate how much you will receive with all bonuses and taxes!")

print("Type your base salary: ")
salaryBase = int(input())

gratification = (salaryBase / 100) * 5

taxes = (salaryBase / 100) * 7

salary = (salaryBase - taxes) + gratification

print(f"Your new salary will be {salary:.2f} reais!")