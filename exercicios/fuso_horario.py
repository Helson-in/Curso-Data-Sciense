# Paulo e Pedro fizeram uma longa viagem para a copa e tiveram que ajustar seus relógios por causa do fuso horário.
# Assim, para melhor se organizarem para as próximas viagens, eles pediram que você fizesse um aplicativo para celular que, dada a hora de saída, tempo de viagem e o fuso do destino com relação à origem, você informe a hora de chegada de cada voo no destino.
# Entrada
# A entrada contém 3 inteiros: S (0 ≤ S ≤ 23), T (1 ≤ T ≤ 12) e F (-5 ≤ F ≤ 5), separados por um espaço, indicando respectivamente a hora da saída, o tempo de viagem e o fuso horário do destino com relação à origem.
# Saída
# Imprima um inteiro que indica a hora local prevista no destino, conforme os exemplos abaixo.

hora_saida = int(input("Digite a hora de saída: "))
tempo_viagem = int(input("Digite o tempo de viagem: "))
fuso_horario = int(input("Digite o fuso horário: "))

if hora_saida >= 0 and hora_saida <= 23 and tempo_viagem >= 1 and tempo_viagem <= 12 and fuso_horario >= -5 and fuso_horario <= 5:
    horario_chegada = hora_saida + tempo_viagem + fuso_horario
    print("Você chegará ao seu destino às {} do fuso horário local.".format(horario_chegada))
    
else:
    print("Valor inválido! Tente novamente.")
    exit()