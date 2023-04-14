# 7)Faça um programa que receba o preço de um produto e o seu código de origem e mostre a sua procedência. A procedência obedece a tabela a seguir:

#   Código de origem  |  Procedência
#         1           |    Sul
#         2           |    Norte
#         3           |    Leste
#         4           |    Oeste
#         5 ou 6      |    Nordeste
#         7 ou 8 ou 9 |    Sudeste
#         10 a 20     |    Centro-Oeste
#         21 a 30     |    Nordeste

print("Let's see the origin of a certain product!")

print("Type the product's price:")
productPrice = int(input())

print("Type the product's origin code:")
originCode = int(input())

if originCode == 1:
    print(f"The product with value of {productPrice:.2f} reais comes from the South")
else:
    if originCode == 2:
        print(f"The product with value of {productPrice:.2f} reais comes from the North")
    else:
        if originCode == 3:
            print(f"The product with value of {productPrice:.2f} reais comes from the East")
        else:
            if originCode == 4:
                print(f"The product with value of {productPrice:.2f} reais comes from the West")
            else:
                if originCode == 5 or originCode == 6:
                    print(f"The product with value of {productPrice:.2f} reais comes from the Northeast")
                else:
                    if originCode == 7 or originCode == 8 or originCode == 9:
                        print(f"The product with value of {productPrice:.2f} reais comes from the Southeast")
                    else:
                        if originCode >= 10 and originCode <= 20:
                            print(f"The product with value of {productPrice:.2f} reais comes from the Midwest")
                        else:
                            if originCode >= 21 and originCode <= 30:
                                print(f"The product with value of {productPrice:.2f} reais comes from the Northeast")