import streamlit as stst
import pickle
import pandas as pd
import numpy as np

modelo = pickle.load(open('C:/Users/Kayky/Downloads/Python/Smoker_Prediction/src/model/model.pkl', 'rb'))

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
urine_protein = stst.radio("Proteina na Urina: ", [1, 2, 3, 4])


if stst.button(label="Fazer predição"):
    a = []
    a.append(alt)
    stst.write(a)
