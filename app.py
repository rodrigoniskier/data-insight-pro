import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(page_title="Data Insight Pro", page_icon="📊", layout="wide")

# --- Cabeçalho ---
st.title("📊 Data Insight Pro")
st.markdown("""
<style>
.big-font { font-size:20px !important; }
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Transforme seus arquivos Excel/CSV em Dashboards Interativos instantaneamente.</p>', unsafe_allow_html=True)
st.markdown("---")

# --- Barra Lateral ---
with st.sidebar:
    st.header("📂 Configuração")
    st.write("Faça upload dos seus dados para começar.")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["csv", "xlsx"])
    
    st.markdown("---")
    st.caption("Desenvolvido por Rodrigo Niskier | Powered by Python & Streamlit")

# --- Lógica Principal ---
if uploaded_file is not None:
    try:
        # 1. Carregar os dados
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # 2. Visão Geral (Métricas)
        st.subheader("🔎 Visão Geral dos Dados")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total de Linhas", df.shape[0])
        col1.metric("Total de Colunas", df.shape[1])
        # Tenta achar colunas numéricas para somar, se não achar, ignora
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        num_df = df.select_dtypes(include=numerics)
        if not num_df.empty:
            col2.metric("Média Geral (1ª col numérica)", f"{num_df.iloc[:,0].mean():.2f}")
            col3.metric("Soma Total (1ª col numérica)", f"{num_df.iloc[:,0].sum():.2f}")

        # 3. Visualização de Tabela (Expander para não poluir)
        with st.expander("Ver Tabela de Dados Completa"):
            st.dataframe(df)

        st.markdown("---")

        # 4. Criação de Gráficos Dinâmicos
        st.subheader("📈 Gerador de Gráficos")
        
        # O usuário escolhe as colunas
        c1, c2, c3 = st.columns(3)
        with c1:
            x_axis = st.selectbox("Escolha o Eixo X (Categorias)", df.columns)
        with c2:
            y_axis = st.selectbox("Escolha o Eixo Y (Valores)", num_df.columns if not num_df.empty else df.columns)
        with c3:
            graph_type = st.selectbox("Tipo de Gráfico", ["Barras", "Linha", "Pizza", "Dispersão"])

        # Gerar o gráfico baseada na escolha
        if graph_type == "Barras":
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} por {x_axis}")
        elif graph_type == "Linha":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"Evolução de {y_axis}")
        elif graph_type == "Pizza":
            fig = px.pie(df, names=x_axis, values=y_axis, title=f"Distribuição de {y_axis}")
        elif graph_type == "Dispersão":
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Correlação: {x_axis} vs {y_axis}")
        
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

else:
    # --- Estado Zero (Sem Arquivo) ---
    st.info("👆 Utilize a barra lateral para fazer upload de um arquivo CSV ou Excel.")
    
    # Demonstração Visual (Mockup Melhorado)
    st.subheader("Exemplo do que você pode criar:")
    mock_data = pd.DataFrame({
        'Curso': ['Medicina', 'Biomedicina', 'Enfermagem', 'Fisioterapia'],
        'Alunos': [120, 85, 95, 60],
        'Nota Média': [8.5, 8.2, 7.9, 8.0]
    })
    
    c1, c2 = st.columns(2)
    with c1:
        fig1 = px.bar(mock_data, x='Curso', y='Alunos', color='Curso', title="Total de Alunos por Curso")
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        fig2 = px.pie(mock_data, values='Alunos', names='Curso', title="Distribuição Percentual")
        st.plotly_chart(fig2, use_container_width=True)