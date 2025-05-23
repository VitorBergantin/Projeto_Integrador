import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Lu141414",  # <-- Substitua pela senha do seu MySQL
    database="projeto_integrador"
)
cursor = conexao.cursor()

while True:
    print('PROJETO INTEGRADOR FASE 2')
    data = input('Qual é a data (AAAA-MM-DD): ') 

    print(75*'-')

    while True:
        try:
            agua = int(input('Quantos litros de água você consumiu hoje aproximadamente?: '))
            ene_eletrica = float(input('Quantos kWh de energia elétrica você consumiu hoje?: '))
            residuos_naoreciclaveis = float(input('Quantos kg de resíduos não recicláveis você gerou hoje?: '))
            residuos_reciclado_total = int(input('Qual a porcentagem de resíduos reciclados no total (em %)?: '))
        except ValueError:
            print('ERRO! TENTE NOVAMENTE! O VALOR DEVE SER NUMÉRICO')
            continue
        break

    print(75*'-')

    while True:
        print('Qual o meio de transporte você usou hoje?: Responder com S(sim) ou N(não)')
        
        transporte_publico = input('1. Transporte público(ônibus, metrô, trem): ').strip().upper()
        if transporte_publico not in ['S', 'N']:
            print('ERRO! TENTE NOVAMENTE! A resposta deve ser S(sim) ou N(não)!')
            continue

        bicicleta = input('2. Bicicleta: ').strip().upper()
        if bicicleta not in ['S', 'N']:
            print('ERRO! TENTE NOVAMENTE! A resposta deve ser S(sim) ou N(não)!')
            continue

        caminhada = input('3. Caminhada: ').strip().upper()
        if caminhada not in ['S', 'N']:
            print('ERRO! TENTE NOVAMENTE! A resposta deve ser S(sim) ou N(não)!')
            continue

        carro_combustivel_fosseis = input('4. Carro movido a combustão: ').strip().upper()
        if carro_combustivel_fosseis not in ['S', 'N']:
            print('ERRO! TENTE NOVAMENTE! A resposta deve ser S(sim) ou N(não)!')
            continue

        carro_eletrico = input('5. Carro elétrico: ').strip().upper()
        if carro_eletrico not in ['S', 'N']:
            print('ERRO! TENTE NOVAMENTE! A resposta deve ser S(sim) ou N(não)!')
            continue

        carona_compartilhada_fosseis = input('6. Carona compartilhada (fóssil): ').strip().upper()
        if carona_compartilhada_fosseis not in ['S', 'N']:
            print('ERRO! TENTE NOVAMENTE! A resposta deve ser S(sim) ou N(não)!')
            continue

        break

    # INSERÇÃO NO BANCO DE DADOS
    sql = """
        INSERT INTO monitoramento (
            data_monitoramento, agua, energia, residuos_nao_reciclaveis,
            percentual_reciclado, transporte_publico, bicicleta, caminhada,
            carro_combustao, carro_eletrico, carona_fossil
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        data, agua, ene_eletrica, residuos_naoreciclaveis, residuos_reciclado_total,
        transporte_publico, bicicleta, caminhada, carro_combustivel_fosseis,
        carro_eletrico, carona_compartilhada_fosseis
    )
    cursor.execute(sql, valores)
    conexao.commit()

    print('-' * 75)

    pontuacao = 0

    # Sustentabilidade
    if agua < 150:
        print('Consumo de água: Alta Sustentabilidade')
        pontuacao += 3
    elif agua <= 200:
        print('Consumo de água: Moderada Sustentabilidade')
        pontuacao += 2
    else:
        print('Consumo de água: Baixa Sustentabilidade')
        pontuacao += 1

    if ene_eletrica < 5:
        print('Consumo de energia: Alta Sustentabilidade')
        pontuacao += 3
    elif ene_eletrica <= 10:
        print('Consumo de energia: Moderada Sustentabilidade')
        pontuacao += 2
    else:
        print('Consumo de energia: Baixa Sustentabilidade')
        pontuacao += 1

    if residuos_reciclado_total > 50:
        print('Geração de Resíduos Não Recicláveis: Alta Sustentabilidade')
        pontuacao += 3
    elif residuos_reciclado_total >= 20:
        print('Geração de Resíduos Não Recicláveis: Moderada Sustentabilidade')
        pontuacao += 2
    else:
        print('Geração de Resíduos Não Recicláveis: Baixa Sustentabilidade')
        pontuacao += 1

    if (transporte_publico == 'S' or bicicleta == 'S' or caminhada == 'S' or carro_eletrico == 'S') and carro_combustivel_fosseis == 'N' and carona_compartilhada_fosseis == 'N':
        print('Uso de Transporte: Alta Sustentabilidade')
        pontuacao += 3
    elif carro_combustivel_fosseis == 'S' and all(t == 'N' for t in [transporte_publico, bicicleta, caminhada, carro_eletrico, carona_compartilhada_fosseis]):
        print('Uso de Transporte: Baixa Sustentabilidade')
        pontuacao += 1
    else:
        print('Uso de Transporte: Moderada Sustentabilidade')
        pontuacao += 2

    print(75*'-')

    media = pontuacao / 4
    print(f'Média de Sustentabilidade: ', end="")
    if media >= 2.5:
        print('Classificação Geral = Alta Sustentabilidade ')
    elif media >= 1.5:
        print('Classificação Geral = Sustentabilidade Moderada ')
    else:
        print('Classificação Geral = Baixa Sustentabilidade ')

    print(75*'-')

    repetir = input('Deseja fazer novamente? [S(sim)/N(não)]: ').strip().upper()
    if repetir == 'N':
        print('PROGRAMA ENCERRADO!')
        break
    elif repetir != 'S':
        print('RESPOSTA INVÁLIDA! PROGRAMA ENCERRADO POR SEGURANÇA!')
        break

# Fechamento da conexão
cursor.close()
conexao.close()
