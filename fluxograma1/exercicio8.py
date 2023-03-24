print("Vamos ver qual o percentual livre do HD!")

print("Digite a quantidade livre do HD em megabytes")
qntLivreMb = int(input())

qntLivrePerc = (qntLivreMb * 100) / 40000

print("O percentual de espaço livre no HD é: %.0f%%" % qntLivrePerc)