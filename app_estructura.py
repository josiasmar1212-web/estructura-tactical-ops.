import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 1. CORE CONFIGURATION
st.set_page_config(page_title="VORTEX ACADEMIC | Enterprise OS", page_icon="🛡️", layout="wide")

# 2. ELITE INTERFACE DESIGN (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&family=Outfit:wght@300;700&display=swap');
    
    .stApp { background-color: #0b0e14; color: #e6edf3; font-family: 'Outfit', sans-serif; }
    
    .vortex-header {
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
        padding: 50px; border-radius: 20px; border: 1px solid #30363d;
        text-align: center; margin-bottom: 40px; box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    
    .content-card {
        background: #161b22; border: 1px solid #30363d;
        padding: 25px; border-radius: 15px; margin-bottom: 20px;
    }
    
    .download-bar {
        background: #21262d; border-left: 5px solid #238636;
        padding: 15px; border-radius: 8px; margin: 10px 0;
        display: flex; justify-content: space-between; align-items: center;
    }
    
    .status-badge {
        padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold;
    }
    
    .stTabs [data-baseweb="tab-list"] { gap: 15px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #161b22; border-radius: 10px 10px 0 0; color: #8b949e;
        height: 50px; padding: 0 30px;
    }
    .stTabs [aria-selected="true"] { background-color: #58a6ff !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("""
<div class="vortex-header">
    <h1 style="font-family: 'JetBrains Mono'; font-size: 4.5rem; color: #58a6ff; margin:0;">VORTEX</h1>
    <p style="letter-spacing: 8px; font-weight: 300; opacity: 0.7;">ACADEMIC MANAGEMENT SYSTEM v17.0</p>
</div>
""", unsafe_allow_html=True)

# --- SISTEMA DE SESIÓN ---
if 'user_role' not in st.session_state: st.session_state.user_role = "ALUMNO"

# --- SIDEBAR AVANZADA ---
with st.sidebar:
    st.markdown("### 🏢 PORTAL DE ACCESO")
    role_select = st.selectbox("IDENTIFICACIÓN", ["👨‍🎓 ALUMNO ELITE", "👑 DIRECTOR ACADEMIA"])
    st.session_state.user_role = role_select
    st.divider()
    
    if st.session_state.user_role == "👨‍🎓 ALUMNO ELITE":
        menu = st.radio("MÓDULOS DE ESTUDIO", ["📊 Mi Panel", "📚 Biblioteca & PDF", "📝 Sala de Examen", "🎥 Videoclases", "💬 Soporte Técnico"])
    else:
        menu = st.radio("CENTRO DE COMANDO", ["📈 Dashboard Global", "👥 Control Alumnos", "📂 Gestor de Contenidos", "💰 Facturación", "⚙️ Configuración"])

# --- VISTA ALUMNO ---
if st.session_state.user_role == "👨‍🎓 ALUMNO ELITE":
    
    if menu == "📊 Mi Panel":
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Progreso Total", "72%", "+3%")
        c2.metric("Nota Media", "8.1", "+0.2")
        c3.metric("Ranking", "12 / 1,450", "▲ 2")
        c4.metric("Días Restantes", "94", "⚠️")
        
        st.subheader("🗓️ Próximas Clases en Directo")
        st.markdown("""
        <div class="content-card">
            <b>MAÑANA 18:00h:</b> Repaso Intensivo Título I - <i>Prof. García</i> <span class="status-badge" style="background:#238636">Confirmado</span>
            <br><small>Link de Zoom disponible 10 min antes.</small>
        </div>
        """, unsafe_allow_html=True)
        
        # Gráfico de Radar de Competencias
        st.subheader("🧠 Mapa de Competencias Tácticas")
        df_radar = pd.DataFrame(dict(r=[90, 85, 40, 70, 95], theta=['Constitución','Penal','Social','Técnico','Ortografía']))
        fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself', line_color='#58a6ff')
        fig.update_layout(template="plotly_dark", polar=dict(radialaxis=dict(visible=False)))
        st.plotly_chart(fig, use_container_width=True)

    elif menu == "📚 Biblioteca & PDF":
        st.header("📂 Repositorio de Materiales")
        tab_a, tab_b, tab_c = st.tabs(["📕 JURÍDICO", "📘 SOCIALES", "📗 TÉCNICO"])
        
        with tab_a:
            temas = [
                {"id": "T1", "t": "La Constitución de 1978", "est": "Completo", "f": "02/02/2026"},
                {"id": "T2", "t": "Derechos y Deberes", "est": "En repaso", "f": "04/02/2026"},
                {"id": "T3", "t": "La Corona y el Rey", "est": "Pendiente", "f": "--"}
            ]
            for t in temas:
                st.markdown(f"""
                <div class="download-bar">
                    <div><b>{t['id']}:</b> {t['t']} <small>({t['est']})</small></div>
                    <button style="background:#58a6ff; border:none; color:white; border-radius:5px; padding:5px 15px; cursor:pointer;">DESCARGAR PDF</button>
                </div>
                """, unsafe_allow_html=True)

    elif menu == "📝 Sala de Examen":
        st.subheader("📝 Simulacro de Examen Oficial")
        st.info("Este examen consta de 20 preguntas con penalización de -0.5 por fallo.")
        
        # Banco Expandido (Fragmento para el código)
        banco = [
            {"p": "¿Qué mayoría se requiere para aprobar una Ley Orgánica?", "o": ["Simple", "Absoluta", "2/3"], "r": "Absoluta"},
            {"p": "¿Cuál es el plazo máximo de detención preventiva?", "o": ["24h", "48h", "72h"], "r": "72h"},
            {"p": "¿A quién pertenece la soberanía nacional?", "o": ["Rey", "Pueblo", "Cortes"], "r": "Pueblo"}
        ]
        
        with st.form("exam_form"):
            for i, q in enumerate(banco):
                st.write(f"**{i+1}. {q['p']}**")
                st.radio("Opciones:", q['o'], key=f"q_{i}")
                st.divider()
            if st.form_submit_button("FINALIZAR EXAMEN"):
                st.success("Resultados guardados. Tu profesor recibirá el informe en 60 segundos.")

# --- VISTA DIRECTOR ---
else:
    if menu == "📈 Dashboard Global":
        st.header("👑 Panel de Control de Dirección")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="content-card"><h4>Matrículas Activas</h4><h1 style="color:#58a6ff">2,450</h1></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="content-card"><h4>Ingresos Mensuales</h4><h1 style="color:#238636">122.400€</h1></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="content-card"><h4>Tasa de Éxito</h4><h1 style="color:#f1c40f">84%</h1></div>', unsafe_allow_html=True)
            
        st.subheader("📊 Rendimiento Global por Temas")
        df_stats = pd.DataFrame({
            "Tema": ["Título I", "Derecho Penal", "Unión Europea", "Armamento", "Sociología"],
            "Aciertos Globales": [85, 42, 55, 30, 72]
        })
        fig_bar = px.bar(df_stats, x="Tema", y="Aciertos Globales", color="Aciertos Globales", color_continuous_scale="RdYlGn")
        st.plotly_chart(fig_bar, use_container_width=True)
        st.error("🚨 ATENCIÓN: El tema 'Armamento' requiere una clase de refuerzo urgente.")

    elif menu == "👥 Control Alumnos":
        st.subheader("Gestión de Alumnado")
        search = st.text_input("🔍 Buscar alumno por nombre o DNI")
        df_alumnos = pd.DataFrame({
            "Alumno": ["Josías Martínez", "Ana Pérez", "Carlos Ruiz"],
            "Progreso": ["92%", "45%", "12%"],
            "Última Nota": [9.4, 5.2, 3.1],
            "Riesgo": ["Bajo", "Medio", "ALTO"]
        })
        st.table(df_alumnos)

# --- FOOTER ---
st.markdown("---")
st.caption("VORTEX ACADEMIC ENTERPRISE v17.0 | Cloud Intelligence for Civil Guard & Police Academies")
