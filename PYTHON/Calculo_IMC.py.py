#Esse programa calcula IMC do usuário e informa categoria de peso.
print("Vamos calcular seu IMC?")
peso = float(input("Por favor, digite seu peso: "))
altura = float(input("Por favor, digite sua altura: "))
altura2= float(altura) * float(altura)
imc = float(peso) / float(altura2)
print("Seu IMC é: {0:.2f}".format(imc))
if imc < 16.00:
    print("Baixo peso Grau III")
elif imc <= 16.99:
     print("Baixo peso Grau II")
elif imc <= 18.49:
     print("Baixo peso Grau I")
elif imc <= 24.99:
     print("Peso Ideal")
elif imc <=29.99:
     print("Sobrepeso")
elif imc <= 34.99:
     print("Obesidade Grau I")
elif imc <= 39.99:
     print("Obesidade Grau II")
elif imc >= 40.00:
     print("Obesidade Grau III")


