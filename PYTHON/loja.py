valor_compra = input("Digite o valor da compra: ")
cupom = input("Digite seu cumpom de desconto: ")

if cupom.upper() == "NIVER10":
    valor_final = float(valor_compra) * 0.9
    print("O valor final da compra é: R${}".format(valor_final))
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
 #Exibindo mensagem com o valor da compra sem desconto
    print("O valor final da compra é: R${}".format(valor_final))