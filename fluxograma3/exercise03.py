# 3)Pedro comprou um saco de ração com peso em quilos. 
#   Pedro possui dois gatos para os quais fornece a quantidade de ração em gramas. 
#   Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato. 
#   Calcule e mostre quanto restará de ração no saco após cinco dias.

print("Let's calculate how much cat food will remain after 5 days")

print("What is the weight of the cat food bag in grams")
foodBagWeight = int(input())

print("How much food is given to the first cat per day?")
foodGivenFirstCat = int(input())

print("How much food is given to the second cat per day?")
foodGivenSecondCat = int(input())

foodGiven = (foodGivenFirstCat + foodGivenSecondCat) * 5

remainedFood = (foodBagWeight - foodGiven) / 1000


print(f"After 5 days, the remained food is {remainedFood} KG")





