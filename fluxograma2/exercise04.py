# 4)Escreva um algoritmo que calcule o número de páginas mínimo que um leitor deve ler 
#   para terminar um livro em um determinado numero de dias informado. 
#   Caso o número de paginas a ler por dia for maior que 100, 
#   informe ao usuário que é impossível de realizar a leitura, 
#   caso contrário apresente o número de paginas.

print("Let's see how many pages you need to read a day to finish the book!")

print("How many pages does the book have?")
pages = int(input())

print("In how many days do you intend to finish the book")
days = int(input())

read = pages / days

if read > 100:
    print(f"You would have to read {read:.0f} pages a day. This is impossible!")

else:
    print(f"You will have to read {read:.0f} pages a day. Good luck!")