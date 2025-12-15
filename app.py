import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration (Browser Tab) ---
st.set_page_config(
    page_title="Data Insight Pro | Business Intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Styling (To make it look Professional) ---
st.markdown("""
<style>
    .main {
        background-color: #f5f7f9;
    }
    .stApp > header {
        background-color: transparent;
    }
    .css-18e3th9 {
        padding-top: 1rem; 
    }
    /* Metric Cards Styling */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e6e9ef;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar (Control Panel) ---
with st.sidebar:
    st.title("⚙️ Control Panel")
    st.write("**Data Import**")
    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
    
    st.markdown("---")
    st.write("**Settings**")
    show_data_preview = st.toggle("Show Raw Data", value=True)
    
    st.markdown("---")
    st.caption("v1.2.0 | Built by Rodrigo Niskier")
    st.caption("© 2025 All Rights Reserved")

# --- Main App Logic ---
st.title("📈 Data Insight Pro")
st.markdown("**Enterprise-Grade Data Analysis & Visualization Tool**")

if uploaded_file is not None:
    # Load Data
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        # --- TOP KPI SECTION (Business Value) ---
        st.markdown("### 📊 Executive Summary")
        
        # Calculate dynamic metrics
        total_rows = df.shape[0]
        total_cols = df.shape[1]
        
        # Find numeric columns for smart insights
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        num_df = df.select_dtypes(include=numerics)
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Records", f"{total_rows:,}")
        col1.caption("Rows processed")
        
        col2.metric("Data Dimensions", total_cols)
        col2.caption("Columns analyzed")
        
        if not num_df.empty:
            # Smart Logic: Pick the last numeric column (often 'Total' or 'Profit')
            primary_metric = num_df.columns[-1] 
            total_val = num_df[primary_metric].sum()
            avg_val = num_df[primary_metric].mean()
            
            col3.metric(f"Total {primary_metric}", f"{total_val:,.2f}")
            col4.metric(f"Avg {primary_metric}", f"{avg_val:,.2f}")
        else:
            col3.metric("Numeric Data", "N/A")
            col4.metric("Analysis", "Categorical Only")

        st.markdown("---")

        # --- TABS LAYOUT (Clean Interface) ---
        tab1, tab2, tab3 = st.tabs(["📈 Visualization Hub", "📋 Data Inspection", "📤 Export"])

        with tab1:
            st.subheader("Dynamic Plotting Engine")
            
            c1, c2, c3 = st.columns(3)
            with c1:
                x_axis = st.selectbox("X-Axis (Category)", df.columns, index=0)
            with c2:
                # Try to auto-select a numeric column for Y if possible
                default_y = num_df.columns[0] if not num_df.empty else df.columns[1]
                try:
                    y_index = list(df.columns).index(default_y)
                except:
                    y_index = 0
                y_axis = st.selectbox("Y-Axis (Value)", num_df.columns if not num_df.empty else df.columns, index=0)
            with c3:
                chart_type = st.selectbox("Chart Type", ["Bar Chart", "Line Chart", "Area Chart", "Scatter Plot", "Pie Chart"])

            # Plotting Logic with English Titles
            if chart_type == "Bar Chart":
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}", template="plotly_white")
            elif chart_type == "Line Chart":
                fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} Trend", template="plotly_white")
            elif chart_type == "Area Chart":
                fig = px.area(df, x=x_axis, y=y_axis, title=f"{y_axis} Cumulative View", template="plotly_white")
            elif chart_type == "Scatter Plot":
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Correlation: {x_axis} vs {y_axis}", template="plotly_white")
            elif chart_type == "Pie Chart":
                fig = px.pie(df, names=x_axis, values=y_axis, title=f"Distribution of {y_axis}", template="plotly_white")
            
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            if show_data_preview:
                st.subheader("Raw Data Inspector")
                st.dataframe(df, use_container_width=True)
            else:
                st.info("Data preview is hidden in settings.")

        with tab3:
            st.subheader("Download Reports")
            st.write("Generate a clean CSV file for external reporting.")
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Processed CSV",
                data=csv,
                file_name='processed_data.csv',
                mime='text/csv',
            )

    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    # --- ZERO STATE (Professional Landing Page) ---
    st.info("ℹ️ Please upload a CSV or Excel file from the sidebar to begin analysis.")
    
    st.subheader("Demo Preview")
    st.markdown("Here is a sample of the automated insights generated by the platform:")
    
    # Mock Data for English Demo
    mock_data = pd.DataFrame({
        'Quarter': ['Q1 - 2024', 'Q2 - 2024', 'Q3 - 2024', 'Q4 - 2024'],
        'Revenue ($)': [150000, 230000, 180000, 320000],
        'Growth (%)': [12, 18, -5, 25]
    })
    
    c1, c2 = st.columns([2, 1])
    
    with c1:
        fig_demo = px.bar(mock_data, x='Quarter', y='Revenue ($)', 
                          title="Quarterly Revenue Performance", 
                          template="plotly_white", color='Revenue ($)')
        st.plotly_chart(fig_demo, use_container_width=True)
        
    with c2:
        st.write("#### Key Metrics")
        st.metric("Total Revenue", "$880k", "24% vs last year")
        st.metric("Top Quarter", "Q4 - 2024")