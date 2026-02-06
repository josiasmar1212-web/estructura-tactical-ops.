import streamlit as st
import pandas as pd

# CONFIGURACIÓN TÉCNICA Y ESTÉTICA
st.set_page_config(page_title="VORTEX | Academic Intelligence", page_icon="⚖️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .main-title { color: #58a6ff; font-family: 'Impact'; text-align: center; font-size: 50px; letter-spacing: 2px; }
    .quote-card { 
        background: linear-gradient(90deg, #161b22 0%, #0d1117 100%); 
        border-left: 5px solid #58a6ff; padding: 25px; border-radius: 10px; 
        margin: 20px 0; font-style: italic; font-size: 1.2rem;
    }
    .study-content { 
        background: #161b22; border: 1px solid #30363d; padding: 30px; 
        border-radius: 15px; border-top: 4px solid #58a6ff;
    }
    .stButton>button { width: 100%; background-color: #238636; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- BANCO DE DATOS: EXAMEN DE 20 PREGUNTAS (EJEMPLOS REALES) ---
banco_preguntas = [
    {"p": "¿Qué artículo de la CE reconoce el derecho a la vida?", "o": ["Art. 14", "Art. 15", "Art. 16"], "r": "Art. 15", "ex": "Art. 15 CE: Todos tienen derecho a la vida."},
    {"p": "¿Cuál es el tiempo máximo de detención preventiva?", "o": ["48h", "72h", "24h"], "r": "72h", "ex": "Art. 17.2 CE."},
    {"p": "¿Quién nombra al Director General de la Policía?", "o": ["El Rey", "El Consejo de Ministros", "El Ministro del Interior"], "r": "El Consejo de Ministros", "ex": "A propuesta del Ministro del Interior."},
    {"p": "¿Qué mayoría se necesita para una Ley Orgánica?", "o": ["Simple", "Absoluta", "2/3"], "r": "Absoluta", "ex": "Votación final sobre el conjunto del proyecto."},
    {"p": "¿Qué Título trata de la Corona?", "o": ["Título I", "Título II", "Título III"], "r": "Título II", "ex": "Artículos 56 al 65 de la CE."},
    {"p": "¿A quién corresponde la defensa de la integridad territorial?", "o": ["Policía Nacional", "Guardia Civil", "Fuerzas Armadas"], "r": "Fuerzas Armadas", "ex": "Art. 8 de la CE."},
    {"p": "¿Cuál es la capital del Estado?", "o": ["Barcelona", "Madrid", "Sevilla"], "r": "Madrid", "ex": "Art. 5 CE: La capital es la villa de Madrid."},
    {"p": "¿Qué lengua es oficial en todo el Estado?", "o": ["Catalán", "Castellano", "Gallego"], "r": "Castellano", "ex": "Art. 3.1 CE."},
    # ... Aquí puedes seguir pegando hasta completar las 20, 50 o 100 ...
]

# --- INTERFAZ PRINCIPAL ---
st.markdown('<h1 class="main-title">VORTEX ACADEMIC</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="quote-card">
    "No te detengas cuando estés cansado, detente cuando hayas terminado. Tu plaza está al otro lado de este esfuerzo." 🛡️
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.selectbox("MODULOS DE INTELIGENCIA", ["📝 SIMULACRO CONTINUO", "📚 BIBLIOTECA DE REPASO"])

# --- SECCIÓN 1: EXAMEN MEJORADO ---
if menu == "📝 SIMULACRO CONTINUO":
    st.subheader("Simulador de Examen de Alta Intensidad")
    
    if 'index' not in st.session_state:
        st.session_state.index = 0
        st.session_state.score = 0

    if st.session_state.index < len(banco_preguntas):
        progreso = (st.session_state.index + 1) / len(banco_preguntas)
        st.write(f"Pregunta {st.session_state.index + 1} de {len(banco_preguntas)}")
        st.progress(progreso)
        
        q = banco_preguntas[st.session_state.index]
        st.info(f"### {q['p']}")
        
        respuesta = st.radio("Elige la respuesta correcta:", q["o"], key=f"pregunta_{st.session_state.index}")
        
        if st.button("SINCRONIZAR Y CONTINUAR ➡️"):
            if respuesta == q["r"]:
                st.session_state.score += 1
                st.toast("✅ ¡Correcto!")
            else:
                st.toast(f"❌ Fallo: {q['r']}")
            
            st.session_state.index += 1
            st.rerun()
    else:
        st.balloons()
        st.success(f"### ¡MISIÓN COMPLETADA! Puntos: {st.session_state.score}/{len(banco_preguntas)}")
        if st.button("REINICIAR SISTEMA"):
            st.session_state.index = 0
            st.session_state.score = 0
            st.rerun()

# --- SECCIÓN 2: BIBLIOTECA INTERACTIVA ---
elif menu == "📚 BIBLIOTECA DE REPASO":
    st.subheader("Temario Crítico y Esquemas de Memorización")
    
    tab1, tab2 = st.tabs(["⚖️ DERECHO", "🚓 SEGURIDAD"])
    
    with tab1:
        with st.expander("TEMA 1: LA CONSTITUCIÓN ESPAÑOLA (PDF)"):
            st.write("Análisis de la norma suprema del ordenamiento.")
            if st.button("DESBLOQUEAR RESUMEN TÁCTICO"):
                st.markdown("""
                <div class="study-content">
                    <h3>💡 Resumen de Éxito - Tema 1</h3>
                    <ul>
                        <li><b>Estructura:</b> 1 Preámbulo, 169 Artículos, 10 Títulos + Preliminar.</li>
                        <li><b>Valores Superiores:</b> Libertad, Justicia, Igualdad, Pluralismo.</li>
                        <li><b>Reforma:</b> Art. 167 (Ordinaria) y Art. 168 (Agravada).</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        with st.expander("TEMA 2: LEY ORGÁNICA 2/86"):
            st.write("Funciones, principios y organización de las FFCCS.")
            if st.button("DESBLOQUEAR ESQUEMA DE REPASO"):
                st.markdown("""
                <div class="study-content">
                    <h3>👮 Conceptos Clave 2/86</h3>
                    <p><b>Principios de Actuación:</b> Adecuación al ordenamiento jurídico, Relaciones con la comunidad, Tratamiento de detenidos.</p>
                    <p><b>Jerarquía:</b> Dependencia directa del Gobierno de la Nación.</p>
                </div>
                """, unsafe_allow_html=True)
