print("Vamos calcular a quantidade que um cachorro come no mês!")

print("Quantas refeições o cachorro come por dia?")
refeicoesDia = int(input())

print("Digite a quantidade de ração consumida pelo cachorro: ")
quantidadeConsumida = int(input())

print("Digite o mês do cálculo:")
mes = int(input())

if mes == 1:

    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 31

elif mes == 2:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 28

elif mes == 3:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 31

elif mes == 4:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 30

elif mes == 5:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 31

elif mes == 6:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 30

elif mes == 7:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 31

elif mes == 8:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 31

elif mes == 9:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 30

elif mes == 10:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 31

elif mes == 11:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 30

elif mes == 12:
    
    quantidadeTotal = (quantidadeConsumida * refeicoesDia) * 31


print("A quantidade total consumida pelo cachorro no mês é %.0f gramas " % quantidadeTotal)