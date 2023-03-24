print("Vamos calcular o percentual que uma despesa representa do seu salário")
print("Digite o seu salário total")
salarioTotal = int(input())

print("Digite o valor das despesas mensais")
despesaMensal = int(input())

despesaPerc = (despesaMensal * 100) / salarioTotal

print("O percentual que uma depesa mensal representa do seu salário total é: %.0f%%" % despesaPerc)