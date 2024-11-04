# Streamlit
import streamlit as st
from streamlit_option_menu import option_menu              # menu para sidebar do streamlit

# Analise de Dados
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import pickle 

def gerar_grafico(dados, eixoX, eixoY, titulo, cor=None):
    # Condicional para aplicar cor apenas se o parâmetro for fornecido
    if cor:
        Figura = px.bar(
            dados,
            x=eixoX,        # Eixo x
            y=eixoY,        # Eixo y
            color=cor,      # Cor opcional
            title=titulo    # Título do gráfico
        )
    else:
        Figura = px.bar(
            dados,
            x=eixoX,        # Eixo x
            y=eixoY,        # Eixo y
            title=titulo    # Título do gráfico
        )
    
    return Figura

def gerar_grafico_pizza(dados,nomes,valor,titulo):
    Figura = px.pie(
        dados,
        names = nomes,
        values = valor,
        title = titulo
        
    )
    return Figura

with open('pipelineRandomForest.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

total_acidentes = pd.read_parquet('acidentes_todos_estados.parquet')
acidentes_dia_semana = pd.read_parquet('acidentesDiaDaSemana.parquet')
find_semana = pd.read_parquet('fid_semana.parquet')
genero_acidente = pd.read_parquet('generoCondutores.parquet')

# Titulo - subtitulo
st.set_page_config( 
    page_title='Modelo Preditivo',
    page_icon='📊',
    layout='wide'
)

st.sidebar.title('Analytics')

# customizar a sidebar
with st.sidebar:

    # menu de seleção
    selected = option_menu(

        # titulo
        'Menu',

        # opções de navegação
        ['Dashboard', 'Modelo'],

        # Icones para o menu das opções
        icons=['bar-chart-fill', 'bar-chart-fill'],

        # icone do menu principal
        menu_icon='cast',

        # Seleção padrão
        default_index=0,

        # Estilos
        styles={
            'menu-title' : {'font-size' : '18px'}, # Diminui o tamanho da fonte do título
            'menu-icon': {'display': 'none'},  # Remove o ícone do título
            'icon': {'font-size': '12px'},  # Estilo dos ícones
            'nav-link': {
                'font-size': '15px',  # Tamanho da fonte dos itens do menu
                '--hover-color': '#6052d9',  # Cor de fundo ao passar o mouse
            },
            'nav-link-selected': {'background-color': '#157806'},  # Cor de fundo do item selecionado
        }
    )

if selected == 'Modelo':

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

else:
    # Titulo da pagina
    st.title('Análise de acidentes nas rodovias federais brasileiras(BRs)')

    chamar_grafico = gerar_grafico(total_acidentes,'Estado','count','Quantidade de acidentes por estado')
    st.plotly_chart( chamar_grafico )
   

    chamar_grafico2 = gerar_grafico(total_acidentes,'Estado','count','Quantidade de acidentes por estado e BR','BR')
    st.plotly_chart( chamar_grafico2 )

    chamar_grafico3 = gerar_grafico(acidentes_dia_semana,'Dia da semana','count','Quantidade de acidentes por dia da semana')
    st.plotly_chart( chamar_grafico3 )

    chamar_grafico4 = gerar_grafico_pizza(find_semana,'categoria','count','Relação entre quantidade de Acidentes por Final de Semana X Semana')
    st.plotly_chart( chamar_grafico4 )

    chamar_grafico5 = gerar_grafico_pizza(genero_acidente,'Gênero','count','Número de acidentes por gênero')
    st.plotly_chart( chamar_grafico5 )