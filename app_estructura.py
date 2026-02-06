import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime

# 1. CONFIGURACIÓN DEL SISTEMA
st.set_page_config(page_title="VORTEX ACADEMIC PRO", page_icon="🛡️", layout="wide")

# 2. ESTILO VISUAL "DARK ACADEMY"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Montserrat:wght@700&display=swap');
    
    .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', sans-serif; }
    
    .header-vortex {
        background: linear-gradient(135deg, #161b22 0%, #0d41e1 100%);
        padding: 50px; border-radius: 20px; text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5); border-bottom: 4px solid #58a6ff;
    }
    
    .card-stat {
        background: #161b22; border: 1px solid #30363d;
        padding: 25px; border-radius: 15px; text-align: center;
        transition: 0.3s ease;
    }
    .card-stat:hover { border-color: #58a6ff; transform: scale(1.02); }
    
    .flashcard {
        background: #1f2937; border: 2px solid #3b82f6;
        padding: 30px; border-radius: 20px; text-align: center;
        font-size: 1.2rem; min-height: 150px; display: flex;
        align-items: center; justify-content: center; margin: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("""
<div class="header-vortex">
    <h1 style="font-family: 'Montserrat', sans-serif; font-size: 4rem; margin:0;">VORTEX <span style="color:#ffffff;">PRO</span></h1>
    <p style="font-family: 'Roboto Mono', monospace; letter-spacing: 5px;">PLATAFORMA DE ALTO RENDIMIENTO ACADÉMICO</p>
</div>
""", unsafe_allow_html=True)

# --- FRASE MOTIVADORA ---
st.markdown(f"> **'El dolor del estudio es temporal, el orgullo de la plaza es para siempre.'** - Operador {st.sidebar.text_input('ID', 'Josías')}")

# --- SISTEMA DE NAVEGACIÓN ---
menu = st.sidebar.radio("SISTEMA CENTRAL", 
    ["📊 DASHBOARD", "📝 SIMULACRO 2026", "📚 REPOSITORIO PDF", "⚡ FLASHCARDS", "📅 AGENDA"])

# --- MODULO 1: DASHBOARD ---
if menu == "📊 DASHBOARD":
    st.subheader("📈 ESTADO DE LA PREPARACIÓN")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1: st.markdown('<div class="card-stat"><h3>🔥 RACHA</h3><h1>12 Días</h1></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="card-stat"><h3>✅ TESTS</h3><h1>450</h1></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="card-stat"><h3>🎯 MEDIA</h3><h1>7.8</h1></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="card-stat"><h3>⏳ RESTA</h3><h1>82 Días</h1></div>', unsafe_allow_html=True)

    st.divider()
    
    # GRÁFICO PRO (CORREGIDO)
    df_graf = pd.DataFrame({
        "Materia": ["Derecho", "Sociales", "Técnico", "Inglés", "Ortografía"],
        "Nivel": [90, 65, 45, 80, 70]
    })
    
    fig = px.bar(df_graf, x='Materia', y='Nivel', color='Nivel',
                 title="DOMINIO POR BLOQUE DE ESTUDIO",
                 color_continuous_scale=px.colors.sequential.Blues)
    fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

# --- MODULO 2: SIMULACRO ---
elif menu == "📝 SIMULACRO 2026":
    st.subheader("📝 EXAMEN DE PRESIÓN")
    
    # BANCO DE PREGUNTAS EXTENDIDO
    banco = [
        {"p": "¿Qué artículo trata de la libertad de cátedra?", "o": ["Art. 20", "Art. 27", "Art. 16"], "r": "Art. 20"},
        {"p": "¿Quién nombra al Defensor del Pueblo?", "o": ["El Rey", "Las Cortes", "El Gobierno"], "r": "Las Cortes"},
        {"p": "¿Cuál es el máximo de Senadores por provincia?", "o": ["2", "4", "5"], "r": "4"},
        {"p": "¿Qué Título de la CE trata de la Economía?", "o": ["Título VI", "Título VII", "Título VIII"], "r": "Título VII"},
        {"p": "¿Qué mayoría se requiere para aprobar el Reglamento de una Cámara?", "o": ["Simple", "Absoluta", "2/3"], "r": "Absoluta"},
        # ... Se pueden añadir infinitas aquí
    ]

    if 'idx' not in st.session_state: st.session_state.idx = 0
    
    if st.session_state.idx < len(banco):
        q = banco[st.session_state.idx]
        st.markdown(f"**PREGUNTA {st.session_state.idx + 1} DE {len(banco)}**")
        st.info(q["p"])
        ans = st.radio("Opciones:", q["o"], key=f"q_{st.session_state.idx}")
        
        if st.button("CONFIRMAR Y SIGUIENTE"):
            st.session_state.idx += 1
            st.rerun()
    else:
        st.success("SIMULACRO COMPLETADO")
        if st.button("REINICIAR"):
            st.session_state.idx = 0
            st.rerun()

# --- MODULO 3: REPOSITORIO PDF ---
elif menu == "📚 REPOSITORIO PDF":
    st.subheader("📂 DESCARGA DE TEMARIOS OFICIALES")
    st.write("Selecciona el bloque para obtener el material actualizado.")
    
    temarios = [
        "📕 Bloque I: Derecho Constitucional (2026)",
        "📘 Bloque II: Derecho Penal y Procesal",
        "📙 Bloque III: Ciencias Sociales y Sociología",
        "📗 Bloque IV: Materias Técnicas y Armas"
    ]
    
    for t in temarios:
        with st.container():
            col_a, col_b = st.columns([4, 1])
            col_a.write(f"### {t}")
            if col_b.button("DESCARGAR", key=t):
                st.toast(f"Descargando {t}...")
            st.divider()

# --- MODULO 4: FLASHCARDS ---
elif menu == "⚡ FLASHCARDS":
    st.subheader("⚡ ENTRENAMIENTO DE MEMORIA RÁPIDA")
    
    cards = [
        {"q": "¿Qué es la mayoría absoluta?", "a": "La mitad más uno del total de miembros."},
        {"q": "¿Plazo de sanción real de leyes?", "a": "15 días."},
        {"q": "¿Quién preside el Poder Judicial?", "a": "El Presidente del Tribunal Supremo."}
    ]
    
    for c in cards:
        with st.expander(f"PREGUNTA: {c['q']}"):
            st.markdown(f'<div class="flashcard">{c["a"]}</div>', unsafe_allow_html=True)

# --- MODULO 5: AGENDA ---
elif menu == "📅 AGENDA":
    st.subheader("📅 CALENDARIO DE OPERACIONES")
    
    data_agenda = {
        "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
        "Horas": [6, 8, 6, 8, 4, 10, 0],
        "Tarea": ["Constitucional", "Penal", "Psico", "Leyes", "Repaso", "Simulacro", "Descanso"]
    }
    st.table(pd.DataFrame(data_agenda))
    
    st.info("💡 RECOMENDACIÓN: El sábado es tu día de máxima carga. Asegúrate de descansar bien el viernes.")

# --- FOOTER ---
st.markdown("---")
st.caption("VORTEX ACADEMIC SYSTEM v12.0 | Security Protocol: Active")
