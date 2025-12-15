import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página (Browser Tab apenas) ---
st.set_page_config(
    page_title="Data Insight Pro",
    page_icon=None, # Remove ícone da aba se possível ou usa padrão
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS: ESTILO "ONYX & GOLD" (High-End Fintech) ---
st.markdown("""
<style>
    /* 1. FUNDO COM GRADIENTE PROFUNDO (Onyx) */
    .stApp {
        background: linear-gradient(to bottom right, #050505, #1a1a1a);
        color: #E0E0E0;
    }
    
    /* 2. TIPOGRAFIA DOURADA COM GRADIENTE (Efeito Ouro Metálico) */
    h1 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
        text-transform: uppercase;
    }
    
    h2, h3 {
        color: #F4CF57 !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    /* 3. BARRA LATERAL (Glassmorphism Escuro) */
    section[data-testid="stSidebar"] {
        background-color: rgba(10, 10, 10, 0.9);
        border-right: 1px solid #333;
    }
    
    /* 4. CARTÕES DE MÉTRICAS (Efeito Glow Discreto) */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1f1f1f 0%, #0f0f0f 100%);
        border: 1px solid #333;
        border-left: 4px solid #D4AF37;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        transition: transform 0.3s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        border-color: #F4CF57;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3); /* Glow dourado ao passar o mouse */
    }
    
    div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 28px !important;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.8);
    }
    
    div[data-testid="stMetricLabel"] {
        color: #888888 !important;
        font-size: 14px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* 5. BOTÕES (Gradiente Dourado Luxuoso) */
    .stButton>button {
        background: linear-gradient(90deg, #d5b038 0%, #fae17d 50%, #d5b038 100%);
        background-size: 200% auto;
        color: #000000;
        border: none;
        border-radius: 5px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.5s;
    }
    .stButton>button:hover {
        background-position: right center; /* Animação sutil de brilho */
        color: #000;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
    }
    
    /* Remove marcas d'água e padding excessivo */
    .css-18e3th9 { padding-top: 0rem; }
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# --- LÓGICA DO APP ---

# Barra Lateral Limpa (Sem Emojis)
with st.sidebar:
    st.markdown("### CONTROL PANEL")
    st.write("input source")
    uploaded_file = st.file_uploader("Upload Data Asset (CSV/XLSX)", type=["csv", "xlsx"])
    
    st.markdown("---")
    st.markdown("### SETTINGS")
    show_preview = st.toggle("Raw Data Inspector", value=True)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.caption("ENTERPRISE EDITION V3.0")
    st.caption("RODRIGO NISKIER SYSTEMS")

# Corpo Principal
st.title("Data Insight Pro")
st.markdown("PREMIUM ANALYTICS SUITE")
st.markdown("---")

if uploaded_file is not None:
    try:
        # Leitura silenciosa
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine='openpyxl')
            
        # --- SEÇÃO DE KPIs (Dashboard) ---
        st.markdown("### EXECUTIVE SUMMARY")
        
        # Grid layout mais espaçado
        col1, col2, col3, col4 = st.columns(4)
        
        numerics = df.select_dtypes(include=['number'])
        
        # Métricas limpas
        col1.metric("RECORDS PROCESSED", f"{df.shape[0]:,}")
        col2.metric("DATA COLUMNS", df.shape[1])
        
        if not numerics.empty:
            # Pega a coluna com maior variância (geralmente a mais importante)
            main_col = numerics.var().idxmax()
            total_val = numerics[main_col].sum()
            col3.metric(f"TOTAL {main_col.upper()}", f"{total_val:,.0f}")
            col4.metric(f"AVG {main_col.upper()}", f"{numerics[main_col].mean():,.0f}")
        else:
            col3.metric("METRIC A", "N/A")
            col4.metric("METRIC B", "N/A")

        st.markdown("<br>", unsafe_allow_html=True)

        # --- ÁREA VISUAL (Sem bordas feias) ---
        
        c1, c2, c3 = st.columns([1, 1, 1])
        with c1:
            x_axis = st.selectbox("X AXIS DIMENSION", df.columns)
        with c2:
            y_axis = st.selectbox("Y AXIS METRIC", numerics.columns if not numerics.empty else df.columns)
        with c3:
            chart_type = st.selectbox("VISUALIZATION TYPE", ["Bar Chart", "Line Chart", "Area Chart"])

        # Configuração de Gráfico Ultra-Clean
        # Cores: Ouro, Prata, Bronze, Carvão
        luxury_palette = ['#D4AF37', '#C0C0C0', '#CD7F32', '#36454F']
        
        if chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=luxury_palette)
        elif chart_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=luxury_palette)
            fig.update_traces(line=dict(width=3)) # Linha mais grossa
        elif chart_type == "Area Chart":
            fig = px.area(df, x=x_axis, y=y_axis, template="plotly_dark", color_discrete_sequence=luxury_palette)

        # Remove backgrounds do Plotly para fundir com o site
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Helvetica Neue", size=12, color="#E0E0E0"),
            xaxis=dict(showgrid=False), # Limpa as grades verticais
            yaxis=dict(showgrid=True, gridcolor='#333333'), # Grades horizontais sutis
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)

        # --- TABELA DE DADOS ---
        if show_preview:
            st.markdown("### DATA INSPECTION")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")

else:
    # --- ZERO STATE (Apenas texto elegante, sem gráficos falsos para não poluir) ---
    st.info("System Ready. Please initialize data upload via Control Panel.")
    
    # Placeholder minimalista (Skeleton Screen)
    st.markdown("""
    <div style="
        border: 2px dashed #333; 
        border-radius: 10px; 
        padding: 50px; 
        text-align: center; 
        color: #666;">
        <h3 style="color: #666 !important;">WAITING FOR INPUT</h3>
        <p>Analytics Engine is Idle</p>
    </div>
    """, unsafe_allow_html=True)