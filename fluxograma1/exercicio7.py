print("Vamos calcular o valor da multa por atraso do pagamento do boleto!")
print("Digite o valor do boleto: ")
valorBoleto = int(input())

print("Digite o percentual da multa: ")
multaPerc = int(input())

multa = (multaPerc  / 100) * valorBoleto

print("O valor da multa é: %.2f reais" % multa)