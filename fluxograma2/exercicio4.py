# 4)Escreva um algoritmo que calcule o número de páginas mínimo que um leitor deve ler 
#   para terminar um livro em um determinado numero de dias informado. 
#   Caso o número de paginas a ler por dia for maior que 100, 
#   informe ao usuário que é impossível de realizar a leitura, 
#   caso contrário apresente o número de paginas.

print("Vamos ver quantas páginas serão necessárias para terminar o livro!")

print("Quantas páginas o livro tem?")
paginas = int(input())

print("Em quantos dias você pretende terminar o livro?")
dias = int(input())

ler = paginas / dias

if ler > 100:
    print(f"Você deveria ler {ler:.0f} páginas a cada dia. Isso é impossível!")

else:
    print(f"Você deverá ler {ler:.0f} páginas a cada dia. Boa sorte!")