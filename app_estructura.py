import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime

# 1. CONFIGURACIÓN DE ALTO NIVEL
st.set_page_config(page_title="VORTEX ACADEMIC | Elite Suite", page_icon="🛡️", layout="wide")

# 2. ESTILO INDUSTRIAL DEEP-BLUE (CSS PERSONALIZADO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Roboto+Condensed:wght@700&display=swap');
    
    .stApp { background-color: #05070a; color: #e6edf3; font-family: 'JetBrains Mono', monospace; }
    
    .main-header {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
        padding: 50px; border-radius: 20px; border: 2px solid #30363d;
        text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 30px;
    }
    
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: #0d1117; padding: 10px; border-radius: 15px; }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background-color: #161b22; border: 1px solid #30363d;
        color: #8b949e; border-radius: 10px; font-weight: bold;
    }
    .stTabs [aria-selected="true"] { color: #58a6ff !important; border-color: #58a6ff !important; background: #0d1117 !important; }
    
    .info-card {
        background: #0d1117; border-top: 4px solid #f1c40f;
        padding: 20px; border-radius: 10px; margin-bottom: 15px;
    }
    
    .quote-text { color: #f1c40f; font-size: 1.4rem; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZACIÓN DE DATOS (Mantiene la info guardada) ---
if 'ranking' not in st.session_state:
    st.session_state.ranking = pd.DataFrame({"Usuario": ["Admin", "Josías", "User01"], "Puntos": [95, 88, 72]})
if 'respuestas_correctas' not in st.session_state:
    st.session_state.respuestas_correctas = 0

# --- CABECERA DINÁMICA ---
st.markdown("""
<div class="main-header">
    <h1 style="font-family: 'Roboto Condensed', sans-serif; font-size: 4rem; margin:0; color:#58a6ff;">VORTEX <span style="color:#ffffff;">ACADEMIC</span></h1>
    <p style="color:#8b949e; font-size: 1.2rem;">ESTADO DEL SISTEMA: <span style="color:#238636;">FULLY OPERATIONAL</span></p>
    <div style="margin-top:20px;">
        <span class="quote-text">"La victoria ama la preparación."</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- NAVEGACIÓN POR PESTAÑAS ---
tab_home, tab_exams, tab_library, tab_analytics, tab_admin = st.tabs([
    "🏠 INICIO", "📝 EXÁMENES REALES", "📚 TEMARIO 2026", "📊 INTELIGENCIA", "⚙️ CONFIG"
])

# --- PESTAÑA 1: HOME ---
with tab_home:
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.markdown("### 📢 ÚLTIMAS ACTUALIZACIONES")
        st.info("**CONVOCATORIA 2026:** Publicada actualización del Tema 14 (Derecho Penal). Revisa los nuevos baremos.")
        st.success("**NUEVO RECURSO:** Añadido examen oficial de la convocatoria 2025.")
        
        st.markdown("### 🏆 RANKING DE ASPIRANTES (TOP 3)")
        st.table(st.session_state.ranking)
    
    with col_r:
        st.markdown("### 🎯 OBJETIVOS DIARIOS")
        st.checkbox("Completar 50 preguntas de test", value=True)
        st.checkbox("Repasar Título I de la Constitución")
        st.checkbox("Realizar simulacro cronometrado")
        st.divider()
        st.markdown('<div class="info-card"><b>DATO CLAVE:</b> El 80% de los aptos estudiaron una media de 6h diarias los últimos 3 meses.</div>', unsafe_allow_html=True)

# --- PESTAÑA 2: EXÁMENES (BANCO DE PREGUNTAS) ---
with tab_exams:
    st.subheader("📝 MÓDULO DE EVALUACIÓN TÁCTICA")
    
    # Base de datos ampliada
    banco = [
        {"p": "¿A quién corresponde la Jefatura de las Fuerzas Armadas?", "o": ["Ministro de Defensa", "El Rey", "Presidente del Gobierno"], "r": "El Rey"},
        {"p": "¿Qué mayoría se requiere para la aprobación de una Ley Orgánica?", "o": ["Simple", "Tres quintos", "Absoluta"], "r": "Absoluta"},
        {"p": "¿Cuál es la edad mínima para ser elegido Diputado?", "o": ["18 años", "21 años", "25 años"], "r": "18 años"},
        {"p": "¿Qué órgano garantiza la primacía de la Constitución?", "o": ["Tribunal Supremo", "Tribunal Constitucional", "Cortes Generales"], "r": "Tribunal Constitucional"},
        {"p": "¿Quién nombra al Fiscal General del Estado?", "o": ["El Rey", "El Gobierno", "El Congreso"], "r": "El Rey"},
        {"p": "¿Cuál es el máximo de detención preventiva sin intervención judicial?", "o": ["24h", "48h", "72h"], "r": "72h"},
        {"p": "¿Qué Título trata de la Organización Territorial?", "o": ["Título VIII", "Título IX", "Título X"], "r": "Título VIII"},
        {"p": "¿Cuántos miembros componen el Tribunal Constitucional?", "o": ["10", "12", "15"], "r": "12"},
        {"p": "¿Cuál es la duración del mandato de los Diputados?", "o": ["4 años", "5 años", "6 años"], "r": "4 años"},
        {"p": "¿Qué lengua es oficial en todo el territorio?", "o": ["Todas", "Castellano", "Lenguas cooficiales"], "r": "Castellano"}
    ]
    
    # Lógica de examen
    st.write(f"Preguntas cargadas en memoria: **{len(banco)}**")
    score = 0
    with st.form("examen_form"):
        for i, q in enumerate(banco):
            st.markdown(f"**{i+1}. {q['p']}**")
            st.radio("Opciones:", q['o'], key=f"ans_{i}")
            st.write("---")
        
        if st.form_submit_button("CALCULAR RESULTADO FINAL"):
            st.balloons()
            st.write("### ANALIZANDO DATOS...")
            # Aquí iría la lógica de corrección automática...
            st.success("SIMULACRO FINALIZADO. REVISA TUS FALLOS EN EL RECORRIDO.")

# --- PESTAÑA 3: TEMARIO (LA BIBLIOTECA) ---
with tab_library:
    st.subheader("📚 REPOSITORIO DE INTELIGENCIA")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### ⚖️ BLOQUE JURÍDICO")
        with st.expander("TEMA 1: LA CONSTITUCIÓN"):
            st.write("PDF: Resumen esquemático del Título Preliminar al Título X.")
            st.button("DESBLOQUEAR TEMA 1")
        with st.expander("TEMA 3: DERECHO PENAL"):
            st.write("Gráficos de tipos delictivos y penas.")
            st.button("DESBLOQUEAR TEMA 3")
            
    with c2:
        st.markdown("#### 👥 BLOQUE SOCIAL")
        with st.expander("TEMA 15: SOCIOLOGÍA"):
            st.write("Conceptos de masa, sociedad y cultura.")
            st.button("DESBLOQUEAR TEMA 15")
            
    with c3:
        st.markdown("#### 💻 BLOQUE TÉCNICO")
        with st.expander("TEMA 28: CIBERSEGURIDAD"):
            st.write("Protocolos TCP/IP, malware y delitos informáticos.")
            st.button("DESBLOQUEAR TEMA 28")

# --- PESTAÑA 4: ANALYTICS (Gŕaficos) ---
with tab_analytics:
    st.subheader("📊 MAPA DE CALOR DE RENDIMIENTO")
    
    stats_data = pd.DataFrame({
        'Tema': ['Derecho', 'Social', 'Técnico', 'Psicotécnico', 'Ortografía'],
        'Nivel (%)': [85, 60, 45, 90, 75]
    })
    
    fig = px.bar(stats_data, x='Tema', y='Nivel (%)', color='Nivel (%)',
                 color_continuous_scale='Blues', title="Dominio por Bloques")
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **ANÁLISIS VORTEX:** Tu punto más débil es el bloque **TÉCNICO**. Se recomienda dedicar 2h extra los martes y jueves.")

# --- PESTAÑA 5: ADMIN (GUARDAR Y SALIR) ---
with tab_admin:
    st.subheader("⚙️ CONTROL DE DATOS")
    st.write("Desde aquí puedes gestionar tu cuenta y exportar tu progreso.")
    
    if st.button("EXPORTAR PROGRESO A PDF"):
        st.write("Generando documento táctico...")
    
    if st.button("LIMPIAR CACHÉ DE ESTUDIO"):
        st.warning("Esto borrará tus notas actuales.")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("VORTEX ACADEMIC © 2026 | Sistema Propiedad de Josías Martínez")
