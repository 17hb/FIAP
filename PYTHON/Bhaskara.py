import math
#solicitando os valores de A,B,C
a = float(input("informe o valor de A: "))
b = float(input("informe o valor de B: "))
c = float(input("informe o valor de C: "))
#escrevendo o calculo
delta = b * b - 4 * a * c
print("{}".format(delta))
if delta > 0.0:
    #calculo de dois valores para x
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valoes: x1 = {} e x2 = {}.".format(a,b,c,x1,x2))
elif delta == 0:
    #calculo de 1 valor para x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {}".format(a,b,c,x))
else:
    #mensagem
    print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x.".format(a,b,c))