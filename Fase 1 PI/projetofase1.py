from mysql.connector import connect, Error
'''
BD preparado para a execução
deste programa com o comando:

CREATE TABLE IF NOT EXISTS monitoramento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_monitoramento DATE,
    agua INT,
    energia FLOAT,
    residuos_nao_reciclaveis FLOAT,
    percentual_reciclado INT,
    transporte_publico VARCHAR(1),
    bicicleta VARCHAR(1),
    caminhada VARCHAR(1),
    carro_combustao VARCHAR(1),
    carro_eletrico VARCHAR(1),
    carona_fossil VARCHAR(1))
'''
def nomes():
    print('+-----------------------------------------------------------------------+')
    print('|                                                                       |')
    print('|----------------------PROJETO INTEGRADOR - FASE 3----------------------|')
    print('|                                                                       |')
    print('| NOMES:           Lucas Curti Pinto           - 25001822               |') 
    print('|                  Rafael Almeida Trevissan    - 25002001               |')
    print('|                  Vinícius Fortes Heinzl      - 25008058               |')
    print('|                  Vitor Bergantin Ribeiro     - 25006595               |')
    print('|                  William Walter de Oliveira  - 25005201               |')
    print('|                                                                       |')
    print('|-----------------------------------------------------------------------|')
    print('|                                                                       |')
    print('+-----------------------------------------------------------------------+')

nomes()

def obtem_conexao(servidor, usuario, senha, bd):
    if obtem_conexao.conexao==None:
        obtem_conexao.conexao==connect(host    =f"{servidor}",\
                                       user    =f"{usuario}",\
                                       password=f"{senha}",\
                                       database=f"{bd}")
        
        return obtem_conexao.conexao
    obtem_conexao.conexao==None
                                      
def avaliar_sustentabilidade(agua, ene_eletrica, residuos_reciclado_total, transporte):
    avaliacao = {}

    # Água
    if agua < 150:
        avaliacao['agua'] = 'Alta Sustentabilidade'
    elif 150 <= agua <= 200:
        avaliacao['agua'] = 'Moderada Sustentabilidade'
    else:
        avaliacao['agua'] = 'Baixa Sustentabilidade'

    # Energia
    if ene_eletrica < 5:
        avaliacao['energia'] = 'Alta Sustentabilidade'
    elif 5 <= ene_eletrica <= 10:
        avaliacao['energia'] = 'Moderada Sustentabilidade'
    else:
        avaliacao['energia'] = 'Baixa Sustentabilidade'

    # Resíduos recicláveis
    if residuos_reciclado_total > 50:
        avaliacao['residuos'] = 'Alta Sustentabilidade'
    elif 20 <= residuos_reciclado_total <= 50:
        avaliacao['residuos'] = 'Moderada Sustentabilidade'
    else:
        avaliacao['residuos'] = 'Baixa Sustentabilidade'

    # Transporte
    if (transporte['publico'] == 'S' or transporte['bicicleta'] == 'S' or transporte['caminhada'] == 'S' or transporte['eletrico'] == 'S') and transporte['combustao'] == 'N' and transporte['carona_fosseis'] == 'N':
        avaliacao['transporte'] = 'Alta Sustentabilidade'
    elif (transporte['combustao'] == 'S' or transporte['carona_fosseis'] == 'S') and transporte['publico'] == 'N' and transporte['bicicleta'] == 'N' and transporte['caminhada'] == 'N' and transporte['eletrico'] == 'N':
        avaliacao['transporte'] = 'Baixa Sustentabilidade'
    else:
        avaliacao['transporte'] = 'Moderada Sustentabilidade'

    return avaliacao


def input_transporte(msg):
    while True:
        resposta = input(msg).strip().upper()
        if resposta in ['S', 'N']:
            return resposta
        else:
            print("Entrada inválida! Digite apenas 'S' para sim ou 'N' para não.")


dados_registrados = {}

def inserir_dado():
    nome = input("Digite o nome para o registro: ")

    if nome in dados_registrados:
        print("Este nome já foi registrado. Use outro ou atualize o existente.")
        return

    data = input("Data do registro: ")

    try:
        agua = int(input('Quantos litros de água você consumiu hoje aproximadamente?: '))
        ene_eletrica = float(input('Quantos kWh de energia elétrica você consumiu hoje?: '))
        residuos_naoreciclaveis = float(input('Quantos kg de resíduos não recicláveis você gerou hoje?: '))
        residuos_reciclado_total = int(input('Qual a porcentagem de resíduos reciclados no total (em %)?: '))
    except ValueError:
        print('Erro! Os valores devem ser numéricos.')
        return

    print("Responda com S (sim) ou N (não):")
    transporte_publico = input_transporte("1. Transporte público: ")
    bicicleta = input_transporte("2. Bicicleta: ")
    caminhada = input_transporte("3. Caminhada: ")
    carro_combustivel_fosseis = input_transporte("4. Carro a combustão: ")
    carro_eletrico = input_transporte("5. Carro elétrico: ")
    carona_compartilhada_fosseis = input_transporte("6. Carona (fóssil): ")

    transporte = {
        'publico': transporte_publico,
        'bicicleta': bicicleta,
        'caminhada': caminhada,
        'combustao': carro_combustivel_fosseis,
        'eletrico': carro_eletrico,
        'carona_fosseis': carona_compartilhada_fosseis
    }

    avaliacao = avaliar_sustentabilidade(agua, ene_eletrica, residuos_reciclado_total, transporte)

    dados_registrados[nome] = {
        'data': data,
        'agua': agua,
        'energia': ene_eletrica,
        'residuos_nao_reciclaveis': residuos_naoreciclaveis,
        'reciclados': residuos_reciclado_total,
        'transporte': transporte,
        'avaliacao': avaliacao
    }

    print("Registro inserido com sucesso!")


def atualizar_dado():
    nome = input("Digite o nome do registro que deseja atualizar: ")

    if nome not in dados_registrados:
        print("Nome não encontrado!")
        return

    data = input("Nova data do registro: ")

    try:
        agua = int(input('Novo consumo de água (litros): '))
        ene_eletrica = float(input('Novo consumo de energia elétrica (kWh): '))
        residuos_naoreciclaveis = float(input('Novo peso de resíduos não recicláveis (kg): '))
        residuos_reciclado_total = int(input('Nova porcentagem de resíduos reciclados (%): '))
    except ValueError:
        print('Erro! Os valores devem ser numéricos.')
        return

    print("Responda com S (sim) ou N (não):")
    transporte_publico = input_transporte("1. Transporte público: ")
    bicicleta = input_transporte("2. Bicicleta: ")
    caminhada = input_transporte("3. Caminhada: ")
    carro_combustivel_fosseis = input_transporte("4. Carro a combustão: ")
    carro_eletrico = input_transporte("5. Carro elétrico: ")
    carona_compartilhada_fosseis = input_transporte("6. Carona (fóssil): ")

    transporte = {
        'publico': transporte_publico,
        'bicicleta': bicicleta,
        'caminhada': caminhada,
        'combustao': carro_combustivel_fosseis,
        'eletrico': carro_eletrico,
        'carona_fosseis': carona_compartilhada_fosseis
    }

    avaliacao = avaliar_sustentabilidade(agua, ene_eletrica, residuos_reciclado_total, transporte)

    dados_registrados[nome] = {
        'data': data,
        'agua': agua,
        'energia': ene_eletrica,
        'residuos_nao_reciclaveis': residuos_naoreciclaveis,
        'reciclados': residuos_reciclado_total,
        'transporte': transporte,
        'avaliacao': avaliacao
    }

    print("Registro atualizado com sucesso!")


def excluir_dado():
    nome = input("Digite o nome do registro que deseja excluir: ")
    if nome in dados_registrados:
        del dados_registrados[nome]
        print("Registro excluído com sucesso!")
    else:
        print("Nome não encontrado.")


def listar_dados():
    if not dados_registrados:
        print("Nenhum dado registrado ainda.")
        return

    for nome, d in dados_registrados.items():
        print('-' * 60)
        print(f"Nome do registro: {nome}")
        print(f"Data: {d['data']}")
        print(f"Consumo de água: {d['agua']} litros")
        print(f"Consumo de energia elétrica: {d['energia']} kWh")
        print(f"Resíduos não recicláveis: {d['residuos_nao_reciclaveis']} kg")
        print(f"Porcentagem de resíduos reciclados: {d['reciclados']}%")
        print("Transporte utilizado:")
        for t, v in d['transporte'].items():
            print(f"  {t.capitalize()}: {'Sim' if v == 'S' else 'Não'}")
        print("Avaliação de Sustentabilidade:")
        for categoria, resultado in d['avaliacao'].items():
            print(f"  {categoria.capitalize()}: {resultado}")
        print('-' * 60)


def fechaconexao():
    conexao=obtem_conexao("ip","nomedobd","senhadobd","nomedobd")
    cursor=conexao.cursos()
    cursor.fluxo()
    conexao.close()
# Menu principal
while True:
    print("\n" + "-" * 50)
    print("♻️         --- PROJETO INTEGRADOR FASE 3 ---     ♻️-")
    print("-" * 50)
    print("*  1. Inserir novo registro                         ")
    print("*  2. Atualizar registro existente                  ")
    print("*  3. Excluir registro                              ")
    print("*  4. Listar/classificar todos os registros         ")
    print("*  5. Sair                                          ")
    print("-" * 50)
    opcao = input("-  Escolha uma opção (1-5): ")
    print("-" * 50)

    if opcao == '1':
        inserir_dado()
    elif opcao == '2':
        atualizar_dado()
    elif opcao == '3':
        excluir_dado()
    elif opcao == '4':
        listar_dados()
    elif opcao == '5':
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida. Tente novamente.")

