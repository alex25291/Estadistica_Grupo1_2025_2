import streamlit as st 
import pandas as pd

st.title("Análise de Dados com Streamlit")
st.write("Carregue um arquivo CSV para análise.")   

# Carregamento do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dados carregados com sucesso!")
    st.dataframe(df)

    st.write("Estatísticas descritivas:")
    st.write(df.describe())
    st.write("Gráficos:")

    st.line_chart(df)
    st.bar_chart(df)


    # Adicione mais gráficos conforme necessário
    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)
    st.write("Histograma das colunas numéricas:")
    for col in df.select_dtypes(include='number').columns:
        st.write(f"Histograma de {col}:")
        st.hist(df[col], bins=20)
    st.write("Gráfico de dispersão entre as duas primeiras colunas numéricas:")
    if df.select_dtypes(include='number').shape[1] >= 2:
        st.scatter_chart(df)
        
    st.write("Gráficos Interativos:")
    
    # Gráfico de linha interativo
    st.subheader("Gráfico de Linha Interativo")
    if not df.empty:
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) >= 1:
            selected_line_column = st.selectbox("Selecione a coluna para o gráfico de linha:", numeric_cols, key='line_chart_select')
            st.line_chart(df[selected_line_column])
        else:
            st.write("Não há colunas numéricas para o gráfico de linha.")
    
    # Gráfico de barras interativo
    st.subheader("Gráfico de Barras Interativo")
    if not df.empty:
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns
        if len(categorical_cols) >= 1:
            selected_bar_column = st.selectbox("Selecione a coluna para o gráfico de barras:", categorical_cols, key='bar_chart_select')
            st.bar_chart(df[selected_bar_column].value_counts())
        else:
            st.write("Não há colunas categóricas para o gráfico de barras.")

    # Histograma interativo
    st.subheader("Histograma Interativo")
    if not df.empty:
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) >= 1:
            selected_hist_column = st.selectbox("Selecione a coluna para o histograma:", numeric_cols, key='hist_chart_select')
            st.hist(df[selected_hist_column], bins=20)
        else:
            st.write("Não há colunas numéricas para o histograma.")

    # Gráfico de dispersão interativo
    st.subheader("Gráfico de Dispersão Interativo")
    if not df.empty:
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) >= 2:
            col1_scatter = st.selectbox("Selecione a primeira coluna para o gráfico de dispersão:", numeric_cols)