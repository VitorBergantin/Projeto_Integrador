-- 1. Criar o banco de dados
CREATE DATABASE projeto_integrador;
USE projeto_integrador;

-- 2. Criar a tabela de monitoramento
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
    carona_fossil VARCHAR(1)
);

-- 3. Inserir dados de exemplo na tabela monitoramento
INSERT INTO monitoramento (data_monitoramento, agua, energia, residuos_nao_reciclaveis, percentual_reciclado, transporte_publico, bicicleta, caminhada, carro_combustao, carro_eletrico, carona_fossil)
VALUES
    ('2025-05-04', 120, 4.5, 0.8, 55, 'S', 'N', 'N', 'S', 'N', 'N'),
    ('2025-05-05', 180, 6.0, 1.2, 30, 'N', 'S', 'N', 'N', 'N', 'S'),
    ('2025-05-06', 200, 8.0, 2.5, 40, 'N', 'N', 'S', 'S', 'N', 'N');

-- 4. Consulta para selecionar a média e a classificação de cada item, sem somar as médias de cadastros anteriores
SELECT 
    id,
    data_monitoramento,
    agua,
    energia,
    residuos_nao_reciclaveis,
    percentual_reciclado,
    transporte_publico,
    bicicleta,
    caminhada,
    carro_combustao,
    carro_eletrico,
    carona_fossil,
    
    -- Média de água e classificação
    ROUND(agua, 2) AS media_agua,
    CASE 
        WHEN agua < 150 THEN 'Alta Sustentabilidade'
        WHEN agua <= 200 THEN 'Sustentabilidade Moderada'
        ELSE 'Baixa Sustentabilidade'
    END AS classificacao_agua,
    
    -- Média de energia e classificação
    ROUND(energia, 2) AS media_energia,
    CASE 
        WHEN energia < 5 THEN 'Alta Sustentabilidade'
        WHEN energia <= 10 THEN 'Sustentabilidade Moderada'
        ELSE 'Baixa Sustentabilidade'
    END AS classificacao_energia,
    
    -- Média de resíduos não recicláveis e classificação
    ROUND(residuos_nao_reciclaveis, 2) AS media_residuos,
    CASE 
        WHEN residuos_nao_reciclaveis < 1 THEN 'Alta Sustentabilidade'
        WHEN residuos_nao_reciclaveis <= 2 THEN 'Sustentabilidade Moderada'
        ELSE 'Baixa Sustentabilidade'
    END AS classificacao_residuos,
    
    -- Média de percentual reciclado e classificação
    ROUND(percentual_reciclado, 2) AS media_percentual_reciclado,
    CASE 
        WHEN percentual_reciclado > 50 THEN 'Alta Sustentabilidade'
        WHEN percentual_reciclado >= 20 THEN 'Sustentabilidade Moderada'
        ELSE 'Baixa Sustentabilidade'
    END AS classificacao_percentual,
    
    -- Transporte mais utilizado (considerando o cadastro atual) e classificação
    CASE
        WHEN transporte_publico = 'S' THEN 'Transporte Público'
        WHEN bicicleta = 'S' THEN 'Bicicleta'
        WHEN caminhada = 'S' THEN 'Caminhada'
        WHEN carro_combustao = 'S' THEN 'Carro a Combustão'
        WHEN carro_eletrico = 'S' THEN 'Carro Elétrico'
        WHEN carona_fossil = 'S' THEN 'Carona Fóssil'
        ELSE 'Nenhum Transporte'
    END AS transporte_mais_utilizado,
    
    -- Classificação do transporte (só para o transporte mais utilizado)
    CASE 
        WHEN transporte_publico = 'S' THEN 'Alta Sustentabilidade'
        WHEN bicicleta = 'S' THEN 'Alta Sustentabilidade'
        WHEN caminhada = 'S' THEN 'Alta Sustentabilidade'
        ELSE 'Baixa Sustentabilidade'
    END AS classificacao_transporte

FROM monitoramento;
