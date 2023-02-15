import streamlit as stst
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Funções auxiliaadoras
def get_dummies(df, features):
    '''
    Transforma as variáveis categóricas em dummy variables.

    Parâmetros:
    df - Pandas DataFrame
    features - list

    Return:
    df - Pandas DataFrame

    '''
    df = pd.get_dummies(df, columns=features)
    return df


def scale_data(df, numerical_features):
    '''
    Escala (transforma) os dados para um mesmo intervalo ([0, 1]).

    Parâmetros:
    df - Pandas DataFrame
    numerical_features - list

    Return:
    df - Pandas DataFrame

    '''

    sc = MinMaxScaler(feature_range=(1, 2))
    scaled_features = sc.fit_transform(df[numerical_features])
    df[numerical_features] = scaled_features
    return df

# Carregamento do modelo
modelo = pickle.load(open('C:/Users/Kayky/Downloads/Python/Smoker_Prediction/src/model/model.pkl', 'rb'))


# Estrutura do web app
stst.title("Modelo de ML: predição de fumante")
stst.markdown("Insira as informações clínicas do paciente a ser analisado.")

stst.subheader("Informações gerais")
age = stst.slider("Idade: ")
height = stst.slider("Altura (cm): ", min_value=100, max_value=300)
weight = stst.number_input("Peso (kg): ")
waist = stst.number_input("Cintura (cm): ")

stst.subheader("Sensoriais")
eyesight_left = stst.number_input("Visão do Olho Esquerdo (graus): ")
eyesight_right = stst.number_input("Visão do Olho Direito (graus): ")
hearing_left = stst.radio("Audição esquerda: ", [1, 2])
hearing_right = stst.radio("Audição direita: ", [1, 2])

stst.subheader("Laboratoriais")
systolic = stst.number_input("Sistolica: ")
relaxation = stst.number_input("Relaxamento: ")
blood_sugar = stst.number_input("Glicemia: ")
cholesterol = stst.number_input("Nível de Colesterol: ")
triglyceride = stst.number_input("Triglicerídeos: ")
hdl = stst.number_input("Nível de HDL: ")
ldl = stst.number_input("Nível de LDL: ")
hemoglobin = stst.number_input("Nível de Hemoglobina: ")
creatinine = stst.number_input("Creatinina: ")
ast = stst.number_input("Nível de AST: ")
alt = stst.number_input("Nível de ALT: ")
gtp = stst.number_input("Nível de GTP: ")

stst.subheader("Outras")
caries = stst.checkbox("Caries dentárias")
urine_protein = stst.radio("Proteina na Urina: ", [1, 2, 3, 4, 5, 6])


# Botão que faz a predição
if stst.button(label="Fazer predição"):

    stst.subheader("Predição")

    b = [age, height, weight, waist, eyesight_left,
         eyesight_right, systolic, relaxation, blood_sugar,
         cholesterol, triglyceride, hdl, ldl, hemoglobin,
         creatinine, ast, alt, gtp, caries, hearing_left,
         hearing_right, urine_protein]


    df = pd.DataFrame(b)
    df = df.T
    df = get_dummies(df=df, features=[19, 20, 21])

    if "19_1" in df.columns:
        df.insert(20, "19_2", 0)
    else:
        df.insert(19, "19_1", 0)

    if "20_1" in df.columns:
        df.insert(22, "20_2", 0)
    else:
        df.insert(21, "20_1", 0)

    if "21_1" in df.columns:
        df.insert(24, "21_2", 0)
        df.insert(25, "21_3", 0)
        df.insert(26, "21_4", 0)
        df.insert(27, "21_5", 0)
        df.insert(28, "21_6", 0)

    elif "21_2" in df.columns:
        df.insert(23, "21_1", 0)
        df.insert(25, "21_3", 0)
        df.insert(26, "21_4", 0)
        df.insert(27, "21_5", 0)
        df.insert(28, "21_6", 0)

    elif "21_3" in df.columns:
        df.insert(23, "21_1", 0)
        df.insert(24, "21_2", 0)
        df.insert(26, "21_4", 0)
        df.insert(27, "21_5", 0)
        df.insert(28, "21_6", 0)

    elif "21_4" in df.columns:
        df.insert(23, "21_1", 0)
        df.insert(24, "21_2", 0)
        df.insert(25, "21_3", 0)
        df.insert(27, "21_5", 0)
        df.insert(28, "21_6", 0)

    elif "21_5" in df.columns:
        df.insert(23, "21_1", 0)
        df.insert(24, "21_2", 0)
        df.insert(25, "21_3", 0)
        df.insert(26, "21_4", 0)
        df.insert(28, "21_6", 0)

    elif "21_6" in df.columns:
        df.insert(23, "21_1", 0)
        df.insert(24, "21_2", 0)
        df.insert(25, "21_3", 0)
        df.insert(26, "21_4", 0)
        df.insert(27, "21_5", 0)


    df_scaled = scale_data(df=df, numerical_features=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
    df_scaled = np.asarray(df_scaled).astype('float32')

    import time

    texto = "Coletando dados e calculando predição..."
    barra = stst.progress(0, text=texto)

    for porcento in range(100):
        time.sleep(0.01)
        barra.progress(porcento + 1, text=texto)

    prediction = modelo.predict(df_scaled)
    num_pred = prediction[0]

    #if num_pred > 0.5:
     #   num_pred = "fumante"
    #else:
     #   num_pred = "não fumante"


    stst.write(f"A predição é {prediction}.")
