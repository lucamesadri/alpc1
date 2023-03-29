# 6)Escreva um algoritmo que calcule o numero de prateleiras necessárias
#   para guardar uma quantidade informada de livros.
#   Considerando que em média uma prateleira comporta 32 livros.

print("Let's see how many bookshelves you need to store your books!")

print("Type how many books you need to store: ")
books = int(input())

bookshelves = books / 32

print(f"It'll be needed {bookshelves:.0f} bookshelves to store all the books!")