#Esse programa recebe a distancia em metros percorrida em determinado tempo em minutos e calcula a velocidade media
print("Esse programa calcula a velocidade média de um patinete")
distancia = input("Digite a distancia percorrida: ")
tempo = input("Digite o tempo de percurso: ")

velocidade_media = float(distancia) / float(tempo)
print("O patinete atingiu uma velocidade de {0:.2f} m/min".format(velocidade_media))