print("***************FUVEST***************")

#dados de concorrencia
curso = input("Digite o curso desejado: ")
local = input("Digite o campus desejado: ")
turno = input("Digite o turno desejado: ")
print("****************************************************************************")
red = float(input("Digite a sua nota em redação: "))
cien = float(input("Digite a sua nota em Ciências da Natureza e suas Técnologias: "))
human = float(input("Digite a sua nota em Ciências Humanas e suas Técnologias: "))
ling = float(input("Digite a sua nota em Linguagens, Códigos e suas Técnologias: "))
mate = float(input("Digite a sua nota em Matemática e suas técnologias: "))

# nota de corte
#medicina_diur_sp = 830#
#medicina_notur_sp = 780#
#ads_diur_sp = 640.98}#
#ads_not_sp = 567.08#

o1 = float(red) * 4
o2 = float(cien) * 4
o3 = float(human) * 1
o4 = float(ling) * 2
o5 = float(mate) * 2

somatoria_aluno = float(o1) + float(o2) + float(o3) + float(o4) + float(o5)
media_aluno = float(somatoria_aluno) / 13
print("média obtida: {0:.2f}".format(media_aluno))

#teste logico

if curso == "medicina" and local == "são paulo" and turno == "diurno":
    if media_aluno >= float(830):
        print("Você foi aprovado para o curso: {}, no campi {}, para o turno {}, com a media final de {}.".format(curso,local,turno,media_aluno))
    else:
        print("Você foi reprovado.")