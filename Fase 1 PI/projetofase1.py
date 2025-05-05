print('PROJETO INTEGRADOR FASE 1 - Grupo 04')
data=str(input('Qual é a data: '))
agua=int(input('Quantos litros de água você consumiu hoje aproximadamente?: '))
ene_eletrica=float(input('Quantos kWh de energia elétrica você consumiu hoje?: '))
residuos_naoreciclaveis=float(input('Quantos kg de resíduos não recicláveis você gerou hoje?: '))
residuos_reciclado_total=int(input('Qual a porcentagem de resíduos reciclados no total (em %)?: '))
print('Qual o meio de transporte você usou hoje?: Responder com S(sim) ou N(não)')
transporte_publico=str(input('1. Transporte público(ônibus, metrô, trem): '))
bicicleta=str(input('2. Bicicleta: '))
caminhada=str(input('3. Caminhada: '))
carro_combustível_fosseis=str(input('4. Carro movido a combustão: '))
carro_eletrico=str(input('5. Carro elétrico: '))
carona_compartilhada_fosseis=str(input('6. Carona compartilhada(fóssil): '))
print(75*'-')
#Consumo de água
if agua<150:
    print('Consumo de água: Alta Sustentabilidade')
else:
    if agua>=150 or agua<=200:
        print('Consumo de água: Moderada Sustentabilidade')
    else:
        if agua>200:
            print('Consumo de água: Baixa Sustentabilidade')
#energia elétrica
if ene_eletrica<5:
    print('Consumo de energia: Alta Sustentabilidade')
else:
    if ene_eletrica>=5 or ene_eletrica<=10:
        print('Consumo de energia: Moderada Sustentabilidade')
    else:
        if ene_eletrica>10:
            print('Consumo de energia: Baixa Sustentabilidade')
#resíduos não reciclaveis
if residuos_reciclado_total>50:
    print('Geração de Resíduos Não Reciclavreis: Alta Sustentabilidade')
else:
    if residuos_reciclado_total>=20 or residuos_reciclado_total<=50:
        print('Geração de Resíduos Não Reciclavreis: Moderada Sustentabilidade')
    else:
        if residuos_reciclado_total<20:
            print('Geração de Resíduos Não Reciclavreis: Baixa Sustentabilidade')
#Uso de transporte
if (transporte_publico=='S' or bicicleta=='S' or caminhada=='S' or carro_eletrico=='S') and carro_combustível_fosseis=='N' and carona_compartilhada_fosseis=='N':
    print('Uso de Transporte: Alta Sustentabilidade')
elif (carro_combustível_fosseis=='S' or carona_compartilhada_fosseis=='S') and transporte_publico=='N' and bicicleta=='N' and caminhada=='N' and carro_eletrico=='N':
    print('Uso de Transporte: Baixa Sustentabilidade')
else:
    print('Uso de Transporte: Moderada Sustentabilidade')