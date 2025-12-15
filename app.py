import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(
    page_title="Data Insight Pro",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS: ESTILO "ONYX & GOLD" (Alto Contraste) ---
st.markdown("""
<style>
    /* 1. FORÇAR TEXTO BRANCO EM TUDO */
    .stApp, .stMarkdown, .stText, p, div, span, label {
        color: #FFFFFF !important;
    }
    
    /* 2. TÍTULOS COM GRADIENTE DOURADO (Legível) */
    h1 {
        background: -webkit-linear-gradient(0deg, #D4AF37, #F4CF57, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    h2, h3 {
        color: #D4AF37 !important;
        font-weight: 600;
        border-bottom: 1px solid #333;
        padding-bottom: 10px;
    }
    
    /* 3. RETIRAR O FUNDO BRANCO DA BARRA SUPERIOR (Toolbar) */
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); /* Transparente */
    }
    
    /* 4. CARTÕES DE MÉTRICAS (Fundo Escuro + Texto Branco) */
    div[data-testid="stMetric"] {
        background-color: #111111;
        border: 1px solid #333;
        border-left: 5px solid #D4AF37;
        padding: 15px;
        border-radius: 8px;
    }
    
    div[data-testid="stMetricValue"] {
        color: #FFFFFF !important; /* Branco Puro para números */
        font-size: 32px !important;
        font-weight: 700;
    }
    
    div[data-testid="stMetricLabel"] {
        color: #F4CF57 !important; /* Dourado Claro para rótulos */
        font-weight: bold;
    }
    
    /* 5. AJUSTES DO UPLOADER (Para garantir que fique escuro) */
    section[data-testid="stFileUploader"] {
        background-color: #111111;
        border: 1px dashed #D4AF37;
        border-radius: 10px;
        padding: 20px;
    }
    
    /* Botões Dourados */
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #F4CF57 100%);
        color: #000000 !important; /* Texto preto no botão dourado para leitura */
        border: none;
        font-weight: bold;
    }
    
    /* Ajustes na Tabela para ser legível */
    div[data-testid="stDataFrame"] {
        border: 1px solid #333;
    }

</style>
""", unsafe_allow_html=True)

# --- LÓGICA DO APP ---

with st.sidebar:
    st.markdown("## ⚙️ CONTROL PANEL")
    uploaded_file = st.file_uploader("UPLOAD DATA ASSET", type=["csv", "xlsx"])
    
    st.markdown("---")
    show_preview = st.toggle("SHOW RAW DATA", value=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("ENTERPRISE EDITION V3.1")

# Corpo Principal
st.title("DATA INSIGHT PRO")
st.markdown("**PREMIUM ANALYTICS SUITE**")
st.markdown("<br>", unsafe_allow_html=True)

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine='openpyxl')
            
        # DASHBOARD HEADER
        st.markdown("### EXECUTIVE SUMMARY")
        col1, col2, col3, col4 = st.columns(4)
        
        numerics = df.select_dtypes(include=['number'])
        
        col1.metric("TOTAL RECORDS", f"{df.shape[0]:,}")
        col2.metric("FEATURES", df.shape[1])
        
        if not numerics.empty:
            main_col = numerics.var().idxmax()
            col3.metric(f"TOTAL {main_col.upper()}", f"{numerics[main_col].sum():,.0f}")
            col4.metric(f"AVG {main_col.upper()}", f"{numerics[main_col].mean():,.0f}")
        else:
            col3.metric("METRIC", "N/A")
            col4.metric("METRIC", "N/A")

        st.markdown("---")

        # VISUALIZATION AREA
        st.markdown("### STRATEGIC VISUALIZATION")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            x_axis = st.selectbox("X AXIS", df.columns)
        with c2:
            y_axis = st.selectbox("Y AXIS", numerics.columns if not numerics.empty else df.columns)
        with c3:
            chart_type = st.selectbox("CHART TYPE", ["Bar Chart", "Line Chart", "Area Chart"])

        # Gráficos Dourados
        color_seq = ['#D4AF37', '#FFFFFF', '#888888']
        
        if chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=color_seq)
        elif chart_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=color_seq)
        elif chart_type == "Area Chart":
            fig = px.area(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=color_seq)

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )
        
        st.plotly_chart(fig, use_container_width=True)

        if show_preview:
            st.markdown("### DATA INSPECTION")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("WAITING FOR DATA UPLOAD...")
    
    # Placeholder Dourado/Escuro
    st.markdown("""
    <div style="border: 1px dashed #D4AF37; padding: 40px; text-align: center; border-radius: 10px;">
        <h3 style="color: #D4AF37 !important;">SYSTEM READY</h3>
        <p style="color: white !important;">Please upload a CSV or Excel file to generate the dashboard.</p>
    </div>
    """, unsafe_allow_html=True)