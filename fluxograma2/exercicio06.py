# 6)Escreva um algoritmo que calcule o numero de prateleiras necessárias
#   para guardar uma quantidade informada de livros.
#   Considerando que em média uma prateleira comporta 32 livros.

print("Vamos ver quantas prateleiras serão necessárias para guardar seus livros!")

print("Digite quantos livros você precisa armazenar: ")
livros = int(input())

prateleiras = livros / 32

print(f"Será necessário {prateleiras:.0f} prateleiras para armazenar todos os livros!")