import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(
    page_title="Data Insight Pro | Premium Analytics",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS: Estilo "Black & Gold" (Luxo) ---
st.markdown("""
<style>
    /* Fundo Geral - Força o tom Escuro Profundo */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    /* Títulos em Dourado */
    h1, h2, h3 {
        color: #D4AF37 !important; 
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 600;
    }
    
    /* Subtítulos e Texto Secundário em Prata */
    .stMarkdown p, .caption {
        color: #C0C0C0 !important;
    }
    
    /* Cartões de Métricas (KPIs) - Estilo "Cartão Black" */
    div[data-testid="stMetric"] {
        background-color: #161920;
        border: 1px solid #333;
        border-left: 5px solid #D4AF37; /* Detalhe Dourado na borda */
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Valores das Métricas em Branco Brilhante */
    div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 700;
    }
    
    /* Rótulos das Métricas em Dourado Fosco */
    div[data-testid="stMetricLabel"] {
        color: #D4AF37 !important;
    }
    
    /* Botões e Widgets */
    .stButton>button {
        background-color: #D4AF37;
        color: #000000;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #F4CF57;
        color: #000000;
    }
    
    /* Ajuste da Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #11141A;
        border-right: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# --- Barra Lateral ---
with st.sidebar:
    st.title("💎 Control Panel")
    st.markdown("---")
    st.write("**Data Import Strategy**")
    uploaded_file = st.file_uploader("Upload CSV or Excel Asset", type=["csv", "xlsx"])
    
    st.markdown("---")
    st.caption("Enterprise Edition v2.0")
    st.caption("Developed by **Rodrigo Niskier**")

# --- Lógica Principal ---
st.title("DATA INSIGHT PRO")
st.markdown("**Premium Business Intelligence Solution**")
st.markdown("---")

if uploaded_file is not None:
    try:
        # Carregamento Robusto
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            # O engine openpyxl é especificado aqui para garantir
            df = pd.read_excel(uploaded_file, engine='openpyxl')
            
        # --- SEÇÃO DE KPIs (Cartões Pretos e Dourados) ---
        st.subheader("📊 Executive Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        
        # Lógica de Métricas
        total_rows = df.shape[0]
        total_cols = df.shape[1]
        
        col1.metric("Total Records", f"{total_rows:,}")
        col2.metric("Data Features", total_cols)
        
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        num_df = df.select_dtypes(include=numerics)
        
        if not num_df.empty:
            primary_metric = num_df.columns[-1] # Pega a última coluna numérica (geralmente totais)
            total_val = num_df[primary_metric].sum()
            col3.metric(f"Total {primary_metric}", f"{total_val:,.2f}")
            col4.metric(f"Avg {primary_metric}", f"{num_df[primary_metric].mean():,.2f}")
        else:
            col3.metric("Monetary Value", "N/A")
            col4.metric("Growth Rate", "N/A")

        st.markdown("---")

        # --- ÁREA DE ANÁLISE VISUAL ---
        st.subheader("📈 Strategic Visualization")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            x_axis = st.selectbox("Dimension (X-Axis)", df.columns)
        with c2:
            y_axis = st.selectbox("Metric (Y-Axis)", num_df.columns if not num_df.empty else df.columns)
        with c3:
            chart_type = st.selectbox("Visualization Type", ["Bar Chart", "Line Chart", "Area Chart", "Scatter Plot"])

        # Paleta de Cores Personalizada (Dourado e Prata)
        custom_colors = ['#D4AF37', '#C0C0C0', '#A9A9A9', '#8B4513']
        
        # Configuração do Gráfico com Tema Escuro
        if chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=custom_colors)
        elif chart_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=custom_colors)
        elif chart_type == "Area Chart":
            fig = px.area(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=custom_colors)
        elif chart_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=custom_colors)
            
        # Remove fundo do gráfico para mesclar com o site
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        
        st.plotly_chart(fig, use_container_width=True)
        
        # --- TABELA DE DADOS ---
        with st.expander("📂 Inspect Raw Data Source"):
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"System Error: {e}")

else:
    # --- TELA INICIAL (Landing Page de Luxo) ---
    st.info("Waiting for data asset input via sidebar...")
    
    st.subheader("System Preview")
    
    # Mock Data Visualmente Rico
    mock = pd.DataFrame({
        'Asset Class': ['Real Estate', 'Stocks', 'Bonds', 'Crypto'],
        'Return (ROI)': [45000, 32000, 15000, 58000]
    })
    
    fig_mock = px.bar(mock, x='Asset Class', y='Return (ROI)', 
                      template="plotly_dark", 
                      title="Portfolio Performance (Demo)",
                      color_discrete_sequence=['#D4AF37']) # Apenas Dourado
    
    fig_mock.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_mock, use_container_width=True)