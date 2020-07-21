import streamlit as st

import pandas as pd
import numpy as np
import joblib

#Título
st.title('Descubra sua nota do ENEM')

#dicts da respostas
#peruntas 4 e 5
Q001_Q002_dict = {"Nunca estudou.": 'A',
           "Não completou a 4ª série/5º ano do Ensino Fundamental." : 'B',
          "Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental." : 'C',
          "Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio." : 'D',
          "Completou o Ensino Médio, mas não completou a Faculdade." : 'E',
          "Completou a Faculdade, mas não completou a Pós-graduação." : 'F',
          "Completou a Pós-graduação." : 'G',
          "Não sei." : 'H'}
#perguntas 3 e 4
Q003_Q004_dict = {"Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor, pescador, lenhador, seringueiro, extrativista." : 'A',
             "Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, faxineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria." : 'B',
             "Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista." : 'C',
             "Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria." : 'D',
             "Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel, professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados." : 'E',
             "Não sei." : 'F'}

# pergunta 7
Q007_dict = {"Não":'A',
          "Sim, um ou dois dias por semana":'B',
          "Sim, três ou quatro dias por semana.":'C',
          "Sim, pelo menos cinco dias por semana.":'D'}

#perguntas
tipoEscola_dict = {"Parte Pública, Parte Privada" :1 ,"Pública":2, "Privada":3, "Exterior":4}

simNao_dict = {"Sim" : "B", "Não" : "A"}

IN_TREINEIRO_dict = {"Sim" : 1, "Não" : 0}

abcde_dict = {"Não": 'A',
             "Sim, um": 'B',
             "Sim, dois.": 'C',
             "Sim, três.": 'D',
             "Sim, quatro ou mais" : 'E'}

Q006_dict = {'Nenhuma renda.' : 'A',
            'Até R$ 954,00.' : 'B',
             'De R$ 954,01 até R$ 1.431,00.' : 'C',
             'De R$ 1.431,01 até R$ 1.908,00.' : 'D',
             'De R$ 1.908,01 até R$ 2.385,00.' : 'E',
             'De R$ 2.385,01 até R$ 2.862,00.' : 'F',
             'De R$ 2.862,01 até R$ 3.816,00.' : 'G',
             'De R$ 3.816,01 até R$ 4.770,00.' : 'H',
             'De R$ 4.770,01 até R$ 5.724,00.' : 'I',
             'De R$ 5.724,01 até R$ 6.678,00.' : 'J',
             'De R$ 6.678,01 até R$ 7.632,00.' : 'K',
             'De R$ 7.632,01 até R$ 8.586,00.' : 'L',
             'De R$ 8.586,01 até R$ 9.540,00.' : 'M',
             'De R$ 9.540,01 até, R$ 11.448,00.' : 'N',
             'De R$ 11.448,01 até R$ 14.310,00.' : 'O',
             'De R$ 14.310,01 até R$ 19.080,00.' : 'P',
             'Mais de R$ 19.080,00.' :  'Q'}

Q026_dict = {'Já concluí o Ensino Médio.':'A',
             'Estou cursando e concluirei o Ensino Médio em 2018.':'B',
             'Estou cursando e concluirei o Ensino Médio após 2018.':'C',
             'Não concluí e não estou cursando o Ensino Médio.':'D'}

Q027_dict = {'Somente em escola pública.': 'A',
            'Parte em escola pública e parte em escola privada SEM bolsa de estudo integral.': 'B',
            'Parte em escola pública e parte em escola privada SEM bolsa de estudo integral.': 'C',
            'Somente em escola privada SEM bolsa de estudo integral.': 'D',
            'Somente em escola privada COM bolsa de estudo integral.' : 'E',
            'Não frequentei a escola' : 'F'}

TP_SEXO_dict = {"Masculino" : 'M',
                "Feminino" : 'F'}

TP_ESTADO_CIVIL_dict = {'Solteiro(a)' : 0,
                        'Casado(a)/Mora com companheiro(a)' : 1,
                        'Divorciado(a)/Desquitado(a)/Separado(a)' : 2,
                        'Viúvo(a)' : 3}

TP_COR_RACA_dict = {'Não declarado': 0,
                    'Branca': 1,
                    'Preta': 2,
                    'Parda': 3,
                    'Amarela': 4,
                    'Indígena': 5}

TP_NACIONALIDADE_dict = {'Não informado' : 0,
                         'Brasileiro(a)' : 1,
                         'Brasileiro(a) Naturalizado(a)' : 2,
                         'Estrangeiro(a)' : 3,
                         'Brasileiro(a) Nato(a), nascido(a) no exterior': 4}

TP_ST_CONCLUSAO_dict = {'Já concluí o Ensino Médio': 1,
                        'Estou cursando e concluirei o Ensino Médio em 2018' : 2,
                        'Estou cursando e concluirei o Ensino Médio após 2018' : 3,
                        'Não concluí e não estou cursando o Ensino Médio' : 4}

TP_ANO_CONCLUIU_dict = {'Não informado': 0,
                        '2017': 1,
                        '2016': 2,
                        '2015': 3,
                        '2014': 4,
                        '2013': 5,
                        '2012': 6,
                        '2011': 7,
                        '2010': 8,
                        '2009': 9,
                        '2008': 10,
                        '2007': 11,
                        'Antes de 2007': 12}

TP_ENSINO_dict = {'Ensino Regular' : 1,
                'Educação Especial - Modalidade Substitutiva' : 2,
                'Educação de Jovens e Adultos': 3}



def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value

def get_key(val_my_dict):
    for key, value in my_dict.items():
        if val == key:
            return key
#pergunta 2
def get_value_escola(val):
    for key, value in tipoEscola_dict.items():
        if val == key:
            return value

#pergunta 2
def get_value_simNao(val):
    for key, value in simNao_dict.items():
        if val == key:
            return value

#pergunta 4 e 5
def get_fvalueQ001_Q002(val):
    feature_dict = Q001_Q002_dict
    for key, value in feature_dict.items():
        if val == key:
            return value
#pergunta 6 e 7
def get_fvalueQ003_Q004(val):
    feature_dict = Q003_Q004_dict
    for key, value in feature_dict.items():
        if val == key:
            return value

def get_value_Q007(val):
    for key, value in Q007_dict.items():
        if val == key:
            return value

def get_value_abcde(val):
    for key, value in abcde_dict.items():
        if val == key:
            return value

def get_value_Q006(val):
    for key, value in Q006_dict.items():
        if val == key:
            return value

def get_value_Q026(val):
    for key, value in Q026_dict.items():
        if val == key:
            return value

def get_value_Q027(val):
    for key, value in Q027_dict.items():
        if val == key:
            return value

def get_value_TP_SEXO(val):
    for key, value in TP_SEXO_dict.items():
        if val == key:
            return value

def get_value_TP_ESTADO_CIVIL(val):
    for key, value in TP_ESTADO_CIVIL_dict.items():
        if val == key:
            return value

def get_value_TP_COR_RACA(val):
    for key, value in TP_COR_RACA_dict.items():
        if val == key:
            return  value

def get_value_TP_NACIONALIDADE(val):
    for key, value in TP_NACIONALIDADE_dict.items():
        if val == key:
            return  value

def get_value_TP_ST_CONCLUSAO(val):
    for key, value in TP_ST_CONCLUSAO_dict.items():
        if val == key:
            return  value

def get_value_TP_ANO_CONCLUIU(val):
    for key, value in TP_ANO_CONCLUIU_dict.items():
        if val == key:
            return  value

def get_value_TP_ENSINO(val):
    for key, value in TP_ENSINO_dict.items():
        if val == key:
            return  value

def get_value_IN_TREINEIRO(val):
    for key, value in IN_TREINEIRO_dict.items():
        if val == key:
            return  value

def rodarModelo():
    df=pd.read_csv('dadosPipelineFinal100.csv')
    df=df.drop(['NOTA'], axis=1)
    model = joblib.load('RandomForestJoblib')
    
    df.loc[-1] = feature_list
    #df.loc[-1] =usuario
    df = pd.get_dummies(df, columns=['TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA', 'TP_NACIONALIDADE', 'TP_ST_CONCLUSAO', 'Q001', 'Q002', 'Q003', 'Q004', 'Q006',
       'Q007', 'Q008', 'Q009', 'Q010', 'Q011', 'Q012', 'Q013', 'Q014', 'Q015',
       'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 'Q021', 'Q022', 'Q023', 'Q024',
       'Q025', 'Q026', 'Q027'], drop_first=True)
    dadoModelo = df.loc[-1]
    dadoModelo = np.array(dadoModelo).reshape(1, -1)
    nota = model.predict(dadoModelo)
    return nota
    


#perguntas
idade = st.slider("1. Qual sua idade? ",13, 80)

TP_SEXO = st.radio('31. Qual seu sexo?',
                   tuple(TP_SEXO_dict.keys()))

TP_ESTADO_CIVIL = st.radio('32. Qual seu estado civil?',
                   tuple(TP_ESTADO_CIVIL_dict.keys()))

TP_COR_RACA = st.radio('33. Qual sua cor/raça?',
                   tuple(TP_COR_RACA_dict.keys()))

TP_NACIONALIDADE = st.radio('34. Qual sua nacionalidade?',
                   tuple(TP_NACIONALIDADE_dict.keys()))

TP_ST_CONCLUSAO = st.radio('35. Qual sua situação de conclusão do Ensino Médio?',
                   tuple(TP_ST_CONCLUSAO_dict.keys()))

TP_ANO_CONCLUIU = st.radio('36. Qual o ano de conclusão do seu Ensino Médio?',
                   tuple(TP_ANO_CONCLUIU_dict.keys()))

tipoEscola = st.radio("2. Qual tipo de escola você frequentou:",
                      tuple(tipoEscola_dict.keys()))

TP_ENSINO = st.radio('37. Qual tipo de instituição que concluiu ou concluirá o Ensino Médio?',
                   tuple(TP_ENSINO_dict.keys()))

treineiro = st.radio("3. Você está prestando o ENEM apenas com o intuito de treinar seus conhecimentos?",
                     tuple(IN_TREINEIRO_dict.keys()))

Q001 = st.radio("4. Até que série seu pai, ou o homem responsável por você, estudou?",
                 tuple(Q001_Q002_dict.keys()))

Q002 = st.radio("5. Até que série sua mãe, ou a mulher responsável por você, estudou?",
                 tuple(Q001_Q002_dict.keys()))

Q003 = st.radio("21. A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você. (Se ele não estiver trabalhando, escolha uma ocupação pensando no último trabalho dele).",
                tuple(Q003_Q004_dict.keys()))

Q004 = st.radio("22. A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você. (Se ela não estiver trabalhando, escolha uma ocupação pensando no último trabalho dela).",
                tuple(Q003_Q004_dict.keys()))

Q005 = st.slider("6. Incluindo você, quantas pessoas moram atualmente em sua residência? ", 1,20)

Q006 = st.radio("23. Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)",
                tuple(Q006_dict.keys()))

Q007 = st.radio("7. Em sua residência trabalha empregado(a) doméstico(a)?",
                tuple(Q007_dict.keys()))

Q008 = st.radio("8. Na sua residência tem banheiro?",
                tuple(abcde_dict.keys()))

Q009 = st.radio("9. Na sua residência tem quartos para dormir?",
                tuple(abcde_dict.keys()))

Q010 = st.radio("10. Na sua residência tem carro?",
                tuple(abcde_dict.keys()))

Q011 = st.radio("11. Na sua residência tem motocicleta?",
                tuple(abcde_dict.keys()))

Q012 = st.radio("12. Na sua residência tem geladeira?",
                tuple(abcde_dict.keys()))

Q013 = st.radio("13. Na sua residência tem freezer (independente ou segunda porta da geladeira)?",
                tuple(abcde_dict.keys()))

Q014 = st.radio("14. Na sua residência tem máquina de lavar roupa? (o tanquinho NÃO deve ser considerado)",
                tuple(abcde_dict.keys()))

Q015 = st.radio("15. Na sua residência tem máquina de secar roupa (independente ou em conjunto com a máquina de lavar roupa)?",
                tuple(abcde_dict.keys()))

Q016 = st.radio("16. Na sua residência tem forno micro-ondas?",
                tuple(abcde_dict.keys()))

Q017 = st.radio("17. Na sua residência tem máquina de lavar louça?",
                tuple(abcde_dict.keys()))

Q018 = st.radio("24. Na sua residência tem aspirador de pó?",
                tuple(simNao_dict.keys()))

Q019 = st.radio("18. Na sua residência tem televisão em cores?",
                tuple(abcde_dict.keys()))

Q020 = st.radio("25. Na sua residência tem aparelho de DVD?",
                tuple(simNao_dict.keys()))

Q021 = st.radio("26. Na sua residência tem TV por assinatura?",
                tuple(simNao_dict.keys()))

Q022 = st.radio("19. Na sua residência tem telefone celular?",
                tuple(abcde_dict.keys()))

Q023 = st.radio("27. Na sua residência tem telefone fixo?",
                tuple(simNao_dict.keys()))

Q024 = st.radio("20. Na sua residência tem computador?",
                tuple(abcde_dict.keys()))

Q025 = st.radio("28. Na sua residência tem internet?",
                tuple(simNao_dict.keys()))

Q026 = st.radio("29. Você já concluiu ou está concluindo o Ensino Médio?",
                tuple(Q026_dict.keys()))

Q027 = st.radio('30. Em que tipo de escola você frequentou o Ensino Médio?',
                tuple(Q027_dict.keys()))


#salvando os dados do usuario
feature_list = [idade,
                get_value_TP_SEXO(TP_SEXO),
                get_value_TP_ESTADO_CIVIL(TP_ESTADO_CIVIL),
                get_value_TP_COR_RACA(TP_COR_RACA),
                get_value_TP_NACIONALIDADE(TP_NACIONALIDADE),
                get_value_TP_ST_CONCLUSAO(TP_ST_CONCLUSAO),
                get_value_TP_ANO_CONCLUIU(TP_ANO_CONCLUIU),
                get_value_escola(tipoEscola),
                get_value_TP_ENSINO(TP_ENSINO),
                get_value_IN_TREINEIRO(treineiro),
                get_fvalueQ001_Q002(Q001),
                get_fvalueQ001_Q002(Q002),
                get_fvalueQ003_Q004(Q003),
                get_fvalueQ003_Q004(Q004),
                Q005,
                get_value_Q006(Q006),
                get_value_Q007(Q007),
                get_value_abcde(Q008),
                get_value_abcde(Q009),
                get_value_abcde(Q010),
                get_value_abcde(Q011),
                get_value_abcde(Q012),
                get_value_abcde(Q013),
                get_value_abcde(Q014),
                get_value_abcde(Q015),
                get_value_abcde(Q016),
                get_value_abcde(Q017),
                get_value_simNao(Q018),
                get_value_abcde(Q019),
                get_value_simNao(Q020),
                get_value_simNao(Q021),
                get_value_abcde(Q022),
                get_value_simNao(Q023),
                get_value_abcde(Q024),
                get_value_simNao(Q025),
                get_value_Q026(Q026),
                get_value_Q027(Q027)]


st.header('Sua nota é:')
st.success(rodarModelo())
