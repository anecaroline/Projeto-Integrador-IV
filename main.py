import pandas as pd
import streamlit as st
import plotly.express as px

def main():
    st.title('Dasboard de Trânsito')

    df = pd.read_csv('acidentes2024_todas_causas_tipos.zip', encoding = 'latin-1', sep = ';')

    st.plotly_chart(px.histogram(
        df,
        x='id',
        title='Gráfico dos casos de acidentes geral'
    ))

    st.plotly_chart(px.scatter(
        df,
        x='uf', y='data_inversa',
        color='classificacao_acidente',
        hover_name='idade',
        width=1000,
        title='Gráfico dos meses do ano em relação aos estados e seus acidentes'
    ))

    st.plotly_chart(px.scatter(
        df,
        x='uf', y='data_inversa',
        color='municipio',
        hover_name='idade',
        width=1000,
        title='Gráfico em relação aos municipios e as idades'
    ))

    st.plotly_chart(px.scatter(
        df,
        x='br',y='uf',
        color='km',
        hover_name='idade',
        log_x=True,
        title='Gráfico das rodovias e suas kilometragem'
    ))

if __name__ == "__main__":
    main()