import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# 1. CONFIGURACIÓN DEL SISTEMA
st.set_page_config(page_title="VORTEX ACADEMIC | Elite Intelligence", page_icon="🛡️", layout="wide")

# 2. DISEÑO INDUSTRIAL AVANZADO (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;700&display=swap');
    
    .stApp { background-color: #050505; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    
    .vortex-header {
        background: linear-gradient(135deg, #0d1117 0%, #1a1a1a 100%);
        padding: 60px; border-radius: 30px; border: 1px solid #38bdf8;
        text-align: center; box-shadow: 0 0 40px rgba(56, 189, 248, 0.1);
        margin-bottom: 40px;
    }
    
    .vortex-title { font-family: 'Orbitron', sans-serif; color: #38bdf8; font-size: 4.5rem; letter-spacing: 10px; margin: 0; }
    
    .card-pro {
        background: rgba(255, 255, 255, 0.02); border: 1px solid #333;
        padding: 25px; border-radius: 20px; margin-bottom: 20px;
        transition: 0.3s all;
    }
    .card-pro:hover { border-color: #38bdf8; background: rgba(56, 189, 248, 0.05); }
    
    .status-online { color: #00ff41; font-weight: bold; text-shadow: 0 0 10px #00ff41; }
    
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8 0%, #1e40af 100%);
        color: white; border: none; border-radius: 10px; font-weight: bold;
        padding: 15px; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 5px 15px rgba(56, 189, 248, 0.4); }
    </style>
""", unsafe_allow_html=True)

# 3. INICIALIZACIÓN DE VARIABLES (ESTADO DE SESIÓN)
if 'score_total' not in st.session_state: st.session_state.score_total = 0
if 'intentos' not in st.session_state: st.session_state.intentos = 0

# --- CABECERA ---
st.markdown("""
<div class="vortex-header">
    <h1 class="vortex-title">VORTEX</h1>
    <p style="opacity: 0.6; font-size: 1.2rem;">ACADEMIC INTELLIGENCE SYSTEM v10.0</p>
    <p class="status-online">● SYSTEM ONLINE - SECURE CONNECTION</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR PROFESIONAL ---
with st.sidebar:
    st.markdown("### 👤 OPERADOR")
    st.text_input("NOMBRE DE CLAVE", value="JOSÍAS MARTÍNEZ")
    st.markdown("### 🚀 PROGRESO DE NIVEL")
    st.progress(0.75)
    st.caption("Nivel 7: Especialista en Derecho")
    st.divider()
    menu = st.radio("SISTEMA CENTRAL", 
                    ["DASHBOARD", "SIMULADOR EXAMEN", "BIBLIOTECA LEYES", "AGENDA TÁCTICA", "LOGROS"])

# --- MODULO 1: DASHBOARD ---
if menu == "DASHBOARD":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card-pro"><h3>🎯 PRECISIÓN</h3><h1>89.4%</h1><p>+2.1% esta semana</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card-pro"><h3>⏱️ TIEMPO/PREG</h3><h1>42s</h1><p>Meta: 35s</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card-pro"><h3>🔥 RACHA</h3><h1>14 DÍAS</h1><p>¡Nivel Imparable!</p></div>', unsafe_allow_html=True)
    
    st.subheader("📊 MAPA DE DOMINIO TÉCNICO")
    df_radar = pd.DataFrame(dict(
        r=[90, 85, 40, 70, 60],
        theta=['Constitucional', 'Penal', 'Administrativo', 'Social', 'Inglés']))
    fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself', line_color='#38bdf8')
    fig.update_layout(template="plotly_dark", polar=dict(radialaxis=dict(visible=False)))
    st.plotly_chart(fig, use_container_width=True)

# --- MODULO 2: SIMULADOR DE EXAMEN ---
elif menu == "SIMULADOR EXAMEN":
    st.subheader("📝 MODO EXAMEN: CONVOCATORIA 2026")
    
    with st.expander("⚙️ AJUSTES DE SIMULACRO"):
        st.selectbox("Dificultad", ["Oficial", "Extremo", "Solo Falladas"])
        st.checkbox("Penalización por fallo (1/2)", value=True)

    # Base de datos expandida
    preguntas = [
        {"p": "¿Cuántas disposiciones adicionales tiene la Constitución?", "o": ["4", "9", "2"], "r": "4", "h": "Art. Final CE"},
        {"p": "¿Qué Título regula la reforma constitucional?", "o": ["Título IX", "Título X", "Título VIII"], "r": "Título X", "h": "Arts. 166-168"},
        {"p": "¿Quién es el Defensor del Pueblo?", "o": ["Comisionado de las Cortes", "Mando Policial", "Juez Supremo"], "r": "Comisionado de las Cortes", "h": "Art. 54 CE"},
        {"p": "¿Cuál es la mayoría para reformar el Título Preliminar?", "o": ["3/5", "2/3", "Absoluta"], "r": "2/3", "h": "Procedimiento Agravado"},
        {"p": "¿Qué plazo tiene el Rey para sancionar las leyes?", "o": ["10 días", "15 días", "20 días"], "r": "15 días", "h": "Art. 91 CE"}
    ]

    score = 0
    fallos = 0
    with st.form("test_vortex"):
        for i, q in enumerate(preguntas):
            st.write(f"**{i+1}. {q['p']}**")
            choice = st.radio("Respuesta:", q['o'], key=f"p_{i}")
            if choice == q['r']: score += 1
            else: fallos += 1
            st.divider()
        
        if st.form_submit_button("FINALIZAR Y CALCULAR NOTA"):
            nota_final = score - (fallos * 0.5)
            st.session_state.score_total = max(0, nota_final)
            if nota_final >= 2.5:
                st.balloons()
                st.success(f"NOTA: {nota_final}/5 - APTO")
            else:
                st.error(f"NOTA: {nota_final}/5 - NO APTO")

# --- MODULO 3: BIBLIOTECA DE LEYES ---
elif menu == "BIBLIOTECA LEYES":
    st.subheader("📚 REPOSITORIO DE INTELIGENCIA JURÍDICA")
    
    search = st.text_input("🔍 BUSCAR ARTÍCULO O TEMA", placeholder="Ej: Habeas Corpus...")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card-pro"><h4>CONSTITUCIÓN ESPAÑOLA</h4><p>Resúmenes por Títulos y esquemas visuales.</p></div>', unsafe_allow_html=True)
        if st.button("ABRIR TEMA 1"):
            st.info("**Art. 1:** España se constituye en un Estado social y democrático de Derecho...")
    with c2:
        st.markdown('<div class="card-pro"><h4>DERECHO PENAL</h4><p>Código Penal actualizado a 2026.</p></div>', unsafe_allow_html=True)
        if st.button("VER PENAS"):
            st.warning("Prisión permanente revisable: Solo en casos del Art. 140.")

# --- MODULO 4: AGENDA TÁCTICA ---
elif menu == "AGENDA TÁCTICA":
    st.subheader("📅 ORGANIZADOR DE ALTO RENDIMIENTO")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    tareas = ["Constitución", "Derecho Penal", "Psicotécnicos", "Inglés/Ortografía", "Repaso General", "Simulacro", "Descanso"]
    
    agenda = pd.DataFrame({"Día": dias, "Materia Principal": tareas, "Estado": ["Completado", "En proceso", "Pendiente", "Pendiente", "Pendiente", "Pendiente", "Pendiente"]})
    st.table(agenda)

# --- MODULO 5: LOGROS ---
elif menu == "LOGROS":
    st.subheader("🏅 MEDALLERO DE OPERADOR")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("⭐ **EL ERUDITO**")
        st.caption("Has completado 500 preguntas.")
    with c2:
        st.markdown("🔥 **IMPARABLE**")
        st.caption("7 días de racha de estudio.")
    with c3:
        st.markdown("🎯 **PRECISIÓN QUIRÚRGICA**")
        st.caption("Examen con 0 fallos.")

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align:center; opacity:0.5;">VORTEX ACADEMIC © 2026 | Desarrollado por Josías Martínez</p>', unsafe_allow_html=True)
