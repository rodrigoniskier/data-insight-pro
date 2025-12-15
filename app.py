import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página (Título e ícone no navegador)
st.set_page_config(page_title="Data Insight Pro", page_icon="📊", layout="wide")

# Cabeçalho
st.title("📊 Data Insight Pro")
st.markdown("---")

# Barra Lateral (Sidebar) para Upload
with st.sidebar:
    st.header("Upload de Dados")
    st.write("Suba seu arquivo Excel ou CSV para gerar insights automáticos.")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["csv", "xlsx"])

# Lógica Principal
if uploaded_file is not None:
    st.success("Arquivo carregado com sucesso! A análise começará em breve.")
    # Aqui é onde a mágica da IA vai entrar depois
    
    # Apenas para mostrar que lemos o arquivo (preview)
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.write("### Visualização dos Dados Brutos")
        st.dataframe(df.head()) # Mostra as primeiras 5 linhas
        
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")

else:
    # Estado inicial (quando não tem arquivo)
    st.info("Aguardando upload de arquivo para iniciar...")
    
    # Exemplo visual (Fake Data) para o portfólio não ficar vazio na primeira impressão
    st.markdown("### Exemplo de como ficará sua análise:")
    
    # Criando dados fictícios só para "decorar" a tela inicial
    mock_data = pd.DataFrame({
        'Categoria': ['Vendas', 'Marketing', 'TI', 'RH'],
        'Valores': [500, 300, 400, 200]
    })
    
    fig = px.bar(mock_data, x='Categoria', y='Valores', title="Exemplo de Gráfico Automático")
    st.plotly_chart(fig, use_container_width=True)