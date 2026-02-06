import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime

# 1. CONFIGURACIÓN DEL SISTEMA CENTRAL
st.set_page_config(page_title="VORTEX | Enterprise Academic", page_icon="🛡️", layout="wide")

# 2. INTERFAZ PROFESIONAL "VORTEX DARK"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=JetBrains+Mono&display=swap');
    
    .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Inter', sans-serif; }
    
    .main-header {
        background: linear-gradient(180deg, #161b22 0%, #0d1117 100%);
        padding: 45px; border-radius: 20px; border-bottom: 2px solid #58a6ff;
        text-align: center; margin-bottom: 30px;
    }
    
    .vortex-card {
        background: #161b22; border: 1px solid #30363d;
        padding: 25px; border-radius: 15px; margin-bottom: 20px;
        transition: transform 0.2s, border-color 0.2s;
    }
    .vortex-card:hover { border-color: #58a6ff; transform: translateY(-2px); }
    
    .download-btn {
        background-color: #238636; color: white; padding: 10px 20px;
        border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block;
    }
    
    .quote-box {
        font-family: 'JetBrains Mono', monospace; color: #f1c40f;
        background: rgba(241, 196, 15, 0.05); padding: 15px;
        border-radius: 10px; border-left: 5px solid #f1c40f;
    }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DATOS AMPLIADA (20 PREGUNTAS CLAVE) ---
banco_preguntas = [
    {"p": "¿Qué artículo define a España como un Estado social y democrático de Derecho?", "o": ["Art. 1", "Art. 2", "Art. 9"], "r": "Art. 1"},
    {"p": "¿Cuál es la forma política del Estado español?", "o": ["República", "Monarquía Parlamentaria", "Monarquía Federal"], "r": "Monarquía Parlamentaria"},
    {"p": "¿A quién pertenece la soberanía nacional?", "o": ["Al Rey", "Al Pueblo Español", "A las Cortes"], "r": "Al Pueblo Español"},
    {"p": "¿Qué mayoría se requiere para aprobar una Ley Orgánica?", "o": ["Simple", "Absoluta", "2/3"], "r": "Absoluta"},
    {"p": "¿Cuál es el plazo de la detención preventiva por delitos de terrorismo (prórroga)?", "o": ["48h", "72h", "48h más"], "r": "48h más"},
    {"p": "¿Qué Título de la CE trata de los derechos y deberes fundamentales?", "o": ["Preliminar", "Título I", "Título II"], "r": "Título I"},
    {"p": "¿Quién nombra a los Ministros?", "o": ["El Rey", "El Presidente", "Las Cortes"], "r": "El Rey"},
    {"p": "¿Qué mayoría se requiere para la reforma agravada (Art. 168)?", "o": ["3/5", "2/3", "Absoluta"], "r": "2/3"},
    {"p": "¿Quién es el Jefe de las Fuerzas Armadas?", "o": ["Presidente", "Ministro Defensa", "El Rey"], "r": "El Rey"},
    {"p": "¿Cuál es la edad mínima para ser Senador?", "o": ["18", "21", "25"], "r": "18"},
    {"p": "¿Qué órgano controla la constitucionalidad de las leyes?", "o": ["Tribunal Supremo", "Tribunal Constitucional", "Fiscalía"], "r": "Tribunal Constitucional"},
    {"p": "¿Cuánto dura el mandato del Defensor del Pueblo?", "o": ["4 años", "5 años", "9 años"], "r": "5 años"},
    {"p": "¿Cuántos diputados componen el Congreso?", "o": ["Entre 300 y 400", "350 fijos", "400 fijos"], "r": "Entre 300 y 400"},
    {"p": "¿Qué lengua es oficial en todo el Estado?", "o": ["Todas", "Castellano", "Gallego"], "r": "Castellano"},
    {"p": "¿A quién corresponde la dirección de la política interior y exterior?", "o": ["Al Rey", "Al Gobierno", "A las Cortes"], "r": "Al Gobierno"},
    {"p": "¿Quién preside el Consejo de Ministros?", "o": ["El Rey", "El Presidente del Gobierno", "El Ministro Portavoz"], "r": "El Presidente del Gobierno"},
    {"p": "¿Qué mayoría se requiere para la moción de censura?", "o": ["Simple", "Absoluta", "2/3"], "r": "Absoluta"},
    {"p": "¿Quién disuelve las Cortes Generales?", "o": ["El Presidente", "El Rey", "El Tribunal Supremo"], "r": "El Rey"},
    {"p": "¿Cuál es la capital del Estado?", "o": ["Madrid", "Barcelona", "Toledo"], "r": "Madrid"},
    {"p": "¿Qué valor superior NO aparece en el Art. 1.1?", "o": ["Libertad", "Justicia", "Fraternidad"], "r": "Fraternidad"}
]

# --- CABECERA ---
st.markdown("""
<div class="main-header">
    <h1 style="font-size: 3.5rem; color: #58a6ff; margin: 0;">VORTEX <span style="color:white;">ACADEMIC</span></h1>
    <p style="letter-spacing: 3px; opacity: 0.8;">SISTEMA DE PREPARACIÓN TÁCTICA PROFESIONAL</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3407/3407024.png", width=100)
    st.markdown("### 👤 PANEL DE CONTROL")
    nombre = st.text_input("ASPIRANTE", "Josías Martínez")
    st.success("Estado: Conectado")
    st.divider()
    menu = st.radio("MÓDULOS", ["🏠 Dashboard", "📝 Examen Real", "📂 Descargas Temarios", "📊 Estadísticas"])

# --- SECCIÓN 1: DASHBOARD ---
if menu == "🏠 Dashboard":
    st.markdown("""
    <div class="quote-box">
        "La disciplina es hacer lo que hay que hacer, incluso cuando no tienes ganas. Tu plaza se gana hoy." 🛡️
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="vortex-card"><h3>📚 Temas Leídos</h3><h1>14 / 28</h1></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="vortex-card"><h3>✅ Tests Hechos</h3><h1>124</h1></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="vortex-card"><h3>🔥 Racha Actual</h3><h1>5 Días</h1></div>', unsafe_allow_html=True)

    st.subheader("📅 Plan Semanal")
    agenda = pd.DataFrame({
        "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
        "Materia": ["Constitucional", "Derecho Penal", "Sociología", "Ortografía", "Simulacro"]
    })
    st.table(agenda)

# --- SECCIÓN 2: EXAMEN REAL ---
elif menu == "📝 Examen Real":
    st.subheader("📝 SIMULADOR DE EXAMEN OFICIAL")
    st.write("Responde a las preguntas. Recuerda que cada fallo resta 0.5 puntos.")
    
    if 'index_p' not in st.session_state:
        st.session_state.index_p = 0
        st.session_state.aciertos = 0
        st.session_state.fallos = 0

    if st.session_state.index_p < len(banco_preguntas):
        q = banco_preguntas[st.session_state.index_p]
        st.progress((st.session_state.index_p + 1) / len(banco_preguntas))
        
        st.markdown(f"#### Pregunta {st.session_state.index_p + 1}:")
        st.info(q["p"])
        
        opcion = st.radio("Selecciona:", q["o"], key=f"p_{st.session_state.index_p}")
        
        if st.button("CONFIRMAR RESPUESTA"):
            if opcion == q["r"]:
                st.session_state.aciertos += 1
                st.toast("✅ Correcto")
            else:
                st.session_state.fallos += 1
                st.toast("❌ Error")
            
            st.session_state.index_p += 1
            st.rerun()
    else:
        st.balloons()
        nota = st.session_state.aciertos - (st.session_state.fallos * 0.5)
        st.markdown(f"""
        <div class="vortex-card" style="text-align:center;">
            <h2>RESULTADO FINAL</h2>
            <h1 style="color:#58a6ff;">{nota} / 20</h1>
            <p>Aciertos: {st.session_state.aciertos} | Fallos: {st.session_state.fallos}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("REINICIAR TEST"):
            st.session_state.index_p = 0
            st.session_state.aciertos = 0
            st.session_state.fallos = 0
            st.rerun()

# --- SECCIÓN 3: DESCARGAS ---
elif menu == "📂 Descargas Temarios":
    st.subheader("📂 REPOSITORIO DE TEMARIOS 2026")
    st.write("Descarga los PDF oficiales resumidos para tu estudio.")
    
    temas = [
        {"nombre": "Bloque I: Derecho Constitucional", "peso": "2.4 MB", "actualizado": "Ene 2026"},
        {"nombre": "Bloque II: Derecho Penal", "peso": "1.8 MB", "actualizado": "Feb 2026"},
        {"nombre": "Bloque III: Ciencias Sociales", "peso": "3.1 MB", "actualizado": "Dic 2025"},
        {"nombre": "Bloque IV: Materias Técnicas", "peso": "4.5 MB", "actualizado": "Feb 2026"}
    ]
    
    for t in temas:
        with st.container():
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown(f"**{t['nombre']}** \n*Tamaño: {t['peso']} | Actualizado: {t['actualizado']}*")
            with col_b:
                if st.button(f"Descargar", key=t['nombre']):
                    st.success("Iniciando descarga...")
            st.divider()

# --- SECCIÓN 4: ESTADÍSTICAS ---
elif menu == "📊 Estadísticas":
    st.subheader("📊 ANÁLISIS DE RENDIMIENTO")
    
    # Gráfico de quesito pro
    df_graf = pd.DataFrame({
        "Área": ["Constitucional", "Penal", "Social", "Técnico"],
        "Nivel": [85, 40, 65, 30]
    })
    
    fig = px.pie(df_graf, values='Nivel', names='Area', title='Dominio de Materias', hole=0.4)
    fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 Consejo de VORTEX: Tu rendimiento en Derecho Penal es bajo. Prioriza los temas 10 al 14 esta semana.")

# --- FOOTER ---
st.markdown("---")
st.caption("VORTEX ACADEMIC © 2026 | Desarrollado para el éxito de Josías.")
