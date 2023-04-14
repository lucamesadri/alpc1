# 5)Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual
#   e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na seguinte tabela:

#   Código |   Cargo      | Percentual
#     1    | Escriturário |    50%
#     2    | Secretário   |    35%
#     3    | Caixa        |    20%
#     4    | Gerente      |    10%
#     5    | Diretor      |    0%

print("Let's calculate the wage increase of a employee!")

# THIS TABLE SHOULD BE IN ENGLISH, BUT I AM LAZY
print("Type the code corresponding to the right employee:")
print("| Código |    Cargo     | Percentual |")
print("|    1   | Escriturário |    50%     |")
print("|    2   | Secretário   |    35%     |")
print("|    3   | Caixa        |    20%     |")
print("|    4   | Gerente      |    10%     |")
print("|    5   | Diretor      |    0%      |")
code = int(input()) 

print("Type the employee's salary:")
salary = int(input())

if code == 1:
    wageIncrease = (salary  * 50) / 100
    salary = salary + wageIncrease
    print(f"The clerk employee who has received a wage increase of {wageIncrease:.2f} reais and now his salary is {salary:.2f} reais.")
else:
    if code == 2:
        wageIncrease = (salary  * 35) / 100
        salary = salary + wageIncrease
        print(f"The secretary employee who has received a wage increase of {wageIncrease:.2f} reais and now his salary is {salary:.2f} reais.")
    else:
        if code == 3:
            wageIncrease = (salary  * 20) / 100
            salary = salary + wageIncrease
            print(f"The cashier employee who has received a wage increase of {wageIncrease:.2f} reais and now his salary is {salary:.2f} reais.")
        else:
            if code == 4:
                wageIncrease = (salary  * 10) / 100
                salary = salary + wageIncrease
                print(f"The manager employee who has received a wage increase of {wageIncrease:.2f} reais and now his salary is {salary:.2f} reais.")
            else:
                if code == 5:
                    print(f"The director didn't receive any wage increasy and his salary is still {salary:.2f} reais")

