velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade- 80)  * 7
    print("""MULTADO! Você excedeu o limite permitido que é de 80KM/H
Você deve pagar uma multa de {:.2f}.""".format(multa))
print('Tenha um bom dia! Dirija com segurança!')