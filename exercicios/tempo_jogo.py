# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.
# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)”

hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite a minuto inicial: "))
hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite a minuto final: "))

if hora_final >= 1 and hora_final <= hora_inicial:
        hora_final += 24

inicio_min = (hora_inicial * 60) + minuto_inicial
final_min = (hora_final * 60) + minuto_final

total_horas = final_min - inicio_min

horas = total_horas // 60
minutos = total_horas % 60

if total_horas <= 1 or total_horas >= 60*24:
    print("Valor inválido! Tente novamente.")
    exit()
else:
    print("O jogo durou {hora} hora(s) e {minuto} minuto(s)".format(hora = horas, minuto = minutos))
    
    