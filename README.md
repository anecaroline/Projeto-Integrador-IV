# Análise de Acidentes de Trânsito em Rodovias Federais Brasileiras

Este projeto visa analisar acidentes de trânsito em rodovias federais brasileiras, utilizando técnicas de aprendizado de máquina para identificar padrões e variáveis que contribuem para a gravidade dos acidentes. A análise oferece insights sobre como melhorar a segurança nas estradas e reduzir a frequência e gravidade dos acidentes.

Projeto realizado em grupo para os cursos de Ciências de dados e Engenharia da Computação para a matéria do Projeto Integrador IV. 
**Tema: Desenvolver análise de dados em escala utilizando algum conjunto de dados existentes ou capturados por IoT e aprendizagem de máquina. Preparar uma interface para visualização dos resultados.**

[Acesse o modelo preditivo](https://projeto-integrador-iv-modelo-dash.streamlit.app/)
[Acesse o DashBoard no powerBi]( https://app.powerbi.com/view?r=eyJrIjoiNzQ0Y2JmOTQtYzVhMi00NzBlLTgwZjgtODc2OTNkYjBkMDZmIiwidCI6ImQzMTc1MTVkLTE2MWUtNGEzOS1iYzIyLTlhOTFkMzAwNTRkYSJ9&pageName=99fe28f4a592c07ba39e)

## Motivação

Estudar acidentes de trânsito é fundamental para entender os fatores que contribuem para a segurança nas estradas e, consequentemente, para a criação de políticas e medidas preventivas mais eficazes. O trânsito é uma das principais causas de mortes no mundo, e nas rodovias federais brasileiras, ele representa um desafio significativo para a saúde pública e a segurança. Este projeto ajuda a identificar variáveis associadas a acidentes mais graves e pode auxiliar as autoridades e gestores na criação de estratégias para reduzir o número de acidentes.

## Bibliotecas Utilizadas

Este projeto faz uso das seguintes bibliotecas:

- **Pandas**: Manipulação e análise de dados.
- **NumPy**: Operações matemáticas e computação numérica.
- **Scikit-Learn**: Conjunto de ferramentas para aprendizado de máquina, incluindo o modelo Random Forest.
- **Matplotlib** e **Seaborn**: Visualização de dados para explorar e apresentar os padrões e insights.
- **Plotly Express**: Criação de gráficos interativos.
- **Streamlit**: Ferramenta para criar uma interface interativa e facilitar a apresentação dos resultados.


## Modelo Utilizado: Random Forest

Para prever a gravidade dos acidentes, utilizamos o modelo **Random Forest**, um algoritmo de aprendizado de máquina baseado em uma coleção de árvores de decisão. A seguir, uma breve explicação sobre o funcionamento e as vantagens do Random Forest:

### Como Funciona

O Random Forest é um conjunto de árvores de decisão que trabalham juntas para fazer previsões. Cada árvore individualmente pode fazer previsões diferentes, mas o modelo final é construído combinando os resultados de todas as árvores (geralmente por meio da média ou votação). Esse método torna o Random Forest mais robusto e preciso, pois reduz o risco de overfitting (quando o modelo aprende muito bem os dados de treinamento, mas não generaliza bem para novos dados).

### Vantagens

- **Alta Precisão**: A combinação de várias árvores de decisão tende a aumentar a precisão das previsões.
- **Redução de Overfitting**: O processo de agregação das árvores diminui a chance de que o modelo seja excessivamente ajustado aos dados de treinamento.
- **Versatilidade**: Pode ser usado tanto para problemas de classificação quanto de regressão, adaptando-se a diferentes contextos.
- **Importância das Variáveis**: O Random Forest permite identificar quais variáveis são mais relevantes para a previsão, o que é especialmente útil para entender quais fatores influenciam mais na gravidade dos acidentes.

**Obs: o desemprenho do modelo ficou com acurácia de 0,57 e recall para ambas da classe com um pouco mais que 50% que é a quantidade de acidentes que ele consegue prever de cada categoria. Precisariamos estudar as features disponíveis e até mesmo a possibilidade de usar um outro modelo para obter um resultado melhor.**

## Estrutura do Projeto

- **deployModelo.py**:Interface interativa desenvolvida com Streamlit para visualização dos resultados.
- **ambiente-virtual/**: Diretório contendo o ambiente virtual com todas as dependências instaladas.
- **dados/**: Pasta onde os datasets utilizados no projeto estão armazenados.
- **notebooks/**: Notebooks Jupyter para exploração e análise inicial dos dados.

## Como Executar o Projeto

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
    ```
2. Crie e Ative o Ambiente Virtual
    ```bash
        python -m venv ambiente-virtual
        source ambiente-virtual/bin/activate  # No Windows use: ambiente-virtual\Scripts\activate
    ```
3. Instale as Dependências
    ```bash
        pip install -r requirements.txt
    ```
4. Execute a Aplicação Streamlit
    ```bash
    streamlit run streamlit_app.py
    ```