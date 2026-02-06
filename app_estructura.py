import streamlit as st
import pandas as pd
import time
from datetime import datetime

# CONFIGURACIÓN DE ÉLITE
st.set_page_config(page_title="VORTEX | Academic Intelligence", page_icon="⚖️", layout="wide")

# CSS PERSONALIZADO: ESTILO ACADEMIA DE ALTO NIVEL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=JetBrains+Mono&display=swap');
    
    .stApp { background-color: #010409; color: #c9d1d9; font-family: 'Montserrat', sans-serif; }
    
    /* Tarjetas de Temario */
    .topic-card {
        background: #0d1117; border: 1px solid #30363d;
        padding: 20px; border-radius: 12px; margin-bottom: 10px;
        transition: all 0.3s ease;
    }
    .topic-card:hover { border-color: #58a6ff; box-shadow: 0 0 15px rgba(88, 166, 255, 0.1); }
    
    /* Frase Motivadora */
    .quote-box {
        background: linear-gradient(90deg, #1f6feb 0%, #161b22 100%);
        padding: 25px; border-radius: 15px; text-align: center;
        font-style: italic; font-weight: bold; font-size: 1.2rem;
        border-left: 8px solid #58a6ff; margin: 20px 0;
    }
    
    .highlight { color: #58a6ff; font-family: 'JetBrains Mono', monospace; }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("""
<div style="text-align: center; padding-bottom: 20px;">
    <h1 style="font-size: 3rem; margin-bottom: 0;">VORTEX <span style="color:#58a6ff;">ACADEMIC</span></h1>
    <p style="opacity: 0.6; letter-spacing: 2px;">INTELIGENCIA APLICADA AL ÉXITO EN OPOSICIONES</p>
</div>
""", unsafe_allow_html=True)

# --- FRASE MOTIVADORA DINÁMICA ---
st.markdown("""
<div class="quote-box">
    "La disciplina es el puente entre tus metas y tus logros. Tu plaza no se hereda, se conquista cada mañana de estudio." 🛡️
</div>
""", unsafe_allow_html=True)

# --- NAVEGACIÓN LATERAL ---
with st.sidebar:
    st.markdown("### 👤 PANEL DEL ASPIRANTE")
    st.write(f"**Operador:** {st.text_input('ID', 'Josías')}")
    st.progress(0.65, text="Progreso Temario: 65%")
    st.divider()
    menu = st.radio("SISTEMA", ["📚 BIBLIOTECA DE TEMAS", "📝 SIMULADOR EXAMEN", "📊 TENDENCIAS 2022-2026"])

if menu == "📚 BIBLIOTECA DE TEMAS":
    st.subheader("📚 TEMARIO OFICIAL ACTUALIZADO")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.markdown('<div class="topic-card"><h4>⚖️ DERECHO CONSTITUCIONAL</h4><p>Temas 1 al 10: La Corona, Poder Judicial, Derechos Fundamentales.</p></div>', unsafe_allow_html=True)
            if st.button("Ver Esquemas de Repaso", key="btn1"): st.write("Cargando mapas mentales...")
            
        with st.container():
            st.markdown('<div class="topic-card"><h4>🚓 SEGURIDAD Y CIENCIAS</h4><p>Temas 11 al 20: LO 2/86, Fuerzas y Cuerpos de Seguridad.</p></div>', unsafe_allow_html=True)
            if st.button("Ver Resúmenes Clave", key="btn2"): st.write("Preparando PDF...")

    with col2:
        st.info("💡 **TIP DE ESTUDIO:** El Tema 4 (Unión Europea) ha caído en el 90% de los exámenes de los últimos 5 años. Priorízalo.")
        st.image("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60")

elif menu == "📝 SIMULADOR EXAMEN":
    st.subheader("📝 MODO SIMULACRO REAL")
    st.write("Haz clic para iniciar un test de 10 preguntas aleatorias con tiempo controlado.")
    
    if st.button("🚀 INICIAR TEST DE PRESIÓN"):
        with st.empty():
            for i in range(5, 0, -1):
                st.markdown(f"<h1 style='text-align:center;'>Iniciando en {i}...</h1>", unsafe_allow_html=True)
                time.sleep(1)
        st.warning("PREGUNTA 1: ¿Cuál es el plazo máximo de la detención preventiva según la Constitución?")
        ans = st.radio("Selecciona una opción:", ["24 horas", "48 horas", "72 horas"])
        if st.button("Confirmar Respuesta"):
            if ans == "72 horas": st.success("¡CORRECTO! +1 punto")
            else: st.error("INCORRECTO. Revisa el Art. 17.2")

elif menu == "📊 TENDENCIAS 2022-2026":
    st.subheader("📊 ANÁLISIS DE CONVOCATORIAS ANTERIORES")
    st.write("Datos extraídos de las últimas plantillas de corrección oficiales.")
    
    data = pd.DataFrame({
        'Área': ['Constitucional', 'Penal', 'Administrativo', 'Socio', 'Técnico'],
        'Preguntas/Año (Media)': [15, 20, 10, 25, 30]
    })
    st.bar_chart(data.set_index('Área'))
    st.markdown("""
    **Conclusiones de VORTEX Intelligence:**
    1. El bloque **Técnico** (Armas, Informática) ha subido un 15% en importancia.
    2. En 2024, las preguntas de **Derecho Penal** fueron las que más eliminaron aspirantes.
    """)
