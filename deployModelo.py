# Streamlit
import streamlit as st
from streamlit_option_menu import option_menu              # menu para sidebar do streamlit

# Analise de Dados
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import pickle 

with open('pipelineRandomForest.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Titulo - subtitulo
st.set_page_config( 
    page_title='Modelo Preditivo',
    page_icon='📊',
    layout='wide'
)

# Titulo da pagina
st.title('Modelo de predição de acidentes')

st.text('Insira as informações abaixo:')

# Dividindo a página em duas colunas: coluna 1 (vazia) e coluna 2 (com as caixas de texto)
col1, col2 = st.columns(2)

with col1:
    # Inserindo os parâmetros nas caixas de texto na coluna da direita
    def mostrar_selecionado(label, valor):
        if valor != 'Selecione uma das opções abaixo':
            st.write(f"{label} escolhido foi : {valor}")

    dia_semana = st.selectbox(label="Categoria", 
                 options=['Selecione uma das opções abaixo', 'final de semana e feriado', 'semana'])
    mostrar_selecionado("O dia da semana ", dia_semana)

    periodo_dia = st.selectbox(label="Período do dia", 
                 options=['Selecione uma das opções abaixo', 'noite', 'dia'])
    mostrar_selecionado("O período do dia ", periodo_dia)

    condicao_tempo = st.selectbox(label="Condição meteorológica", 
                 options=['Selecione uma das opções abaixo', 'Bom', 'Ruim'])
    mostrar_selecionado("A condição do tempo ", condicao_tempo)

    tipo_pista = st.selectbox(label="Tipo de pista", 
                 options=['Selecione uma das opções abaixo', 'Dupla', 'Simples'])
    mostrar_selecionado("O tipo de pista ", tipo_pista)

    uso_solo = st.selectbox(label="Uso do solo", 
                 options=['Selecione uma das opções abaixo', 'Urbano', 'Rural'])
    mostrar_selecionado("O uso do solo ", uso_solo)
    
    def prediction():
        df_input=pd.DataFrame([{
            "categoria":dia_semana,
            "Periodo do dia":periodo_dia,
            "Condição metereologica":condicao_tempo,
            "Tipo de pista":tipo_pista,
            "uso_solo":uso_solo

        }])
        predict=model.predict(df_input)[0]
        return predict
         
with col2:
    st.markdown("<h2 style='text-align: center;'>Resultado do modelo</h2>", unsafe_allow_html=True)

    # Criando um botão
    if st.button("Obter resposta"):
        previsao = prediction()
        try:
            if previsao == 1:
                # Mensagem em vermelho
                st.markdown("<h3 style='color: red;'>Com essas características, há uma alta probabilidade de ocorrer um acidente de trânsito.</h3>", unsafe_allow_html=True)
            else:
                # Mensagem em verde
                st.markdown("<h3 style='color: green;'>As características fornecidas indicam uma baixa probabilidade de um acidente de trânsito.</h3>", unsafe_allow_html=True)
        except Exception as error:
            st.error(f"Erro em prever {error}")


   