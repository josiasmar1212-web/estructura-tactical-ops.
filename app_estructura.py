import streamlit as st
import pandas as pd

# CONFIGURACIÓN TÉCNICA
st.set_page_config(page_title="VORTEX | Plataforma de Inteligencia", page_icon="⚖️", layout="wide")

# CSS PERSONALIZADO (MÁS PROFESIONAL)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .main-title { color: #58a6ff; font-family: 'Arial Black'; text-align: center; font-size: 40px; }
    .quote-card { background: #161b22; border-left: 5px solid #238636; padding: 20px; border-radius: 10px; margin: 20px 0; }
    .study-box { background: #1c2128; border: 1px solid #30363d; padding: 25px; border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DATOS DE EXAMEN (Aquí puedes añadir las 20+ preguntas) ---
banco_preguntas = [
    {"p": "¿Cuál es el plazo máximo de detención preventiva?", "o": ["24h", "48h", "72h"], "r": "72h", "ex": "Art. 17.2 CE"},
    {"p": "¿Quién es el mando superior de las Fuerzas y Cuerpos de Seguridad?", "o": ["El Rey", "El Ministro del Interior", "El Presidente"], "r": "El Ministro del Interior", "ex": "Ley 2/86"},
    {"p": "¿Qué mayoría se requiere para aprobar una Ley Orgánica?", "o": ["Simple", "Absoluta", "Tres quintos"], "r": "Absoluta", "ex": "Art. 81 CE"},
    {"p": "¿Qué título de la Constitución trata de los Derechos Fundamentales?", "o": ["Título I", "Título II", "Título Preliminar"], "r": "Título I", "ex": "Constitución Española"},
    # Añade aquí todas las preguntas que quieras siguiendo el mismo formato...
]

# --- CABECERA ---
st.markdown('<h1 class="main-title">VORTEX ACADEMIC</h1>', unsafe_allow_html=True)
st.markdown("""
<div class="quote-card">
    "El éxito no es el final, el fracaso no es fatal: lo que cuenta es el valor para continuar." 🛡️
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.selectbox("NAVEGACIÓN", ["🎯 EXAMEN DE PRESIÓN", "📚 BIBLIOTECA INTERACTIVA", "📊 MI PROGRESO"])

# --- SECCIÓN 1: EXAMEN CONTINUO ---
if menu == "🎯 EXAMEN DE PRESIÓN":
    st.subheader("Simulador de Examen Oficial")
    
    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = 0
        st.session_state.puntos = 0

    if st.session_state.pregunta_actual < len(banco_preguntas):
        progreso = (st.session_state.pregunta_actual / len(banco_preguntas))
        st.progress(progreso)
        
        q = banco_preguntas[st.session_state.pregunta_actual]
        st.write(f"### Pregunta {st.session_state.pregunta_actual + 1}:")
        st.info(q["p"])
        
        respuesta = st.radio("Selecciona tu respuesta:", q["o"], key=f"q_{st.session_state.pregunta_actual}")
        
        if st.button("CONFIRMAR Y SIGUIENTE ➡️"):
            if respuesta == q["r"]:
                st.session_state.puntos += 1
                st.success(f"¡Correcto! {q['ex']}")
            else:
                st.error(f"Fallo. La respuesta era {q['r']}. {q['ex']}")
            
            st.session_state.pregunta_actual += 1
            st.rerun() # Esto hace que pase a la siguiente inmediatamente
    else:
        st.balloons()
        st.header("¡EXAMEN FINALIZADO!")
        st.metric("Puntuación Final", f"{st.session_state.puntos}/{len(banco_preguntas)}")
        if st.button("REPETIR EXAMEN"):
            st.session_state.pregunta_actual = 0
            st.session_state.puntos = 0
            st.rerun()

# --- SECCIÓN 2: BIBLIOTECA CON REPASOS ---
elif menu == "📚 BIBLIOTECA INTERACTIVA":
    st.subheader("Temario Oficial y Guías de Repaso")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("⚖️ TEMA 1: LA CONSTITUCIÓN"):
            st.write("Estudio profundo de la norma suprema.")
            if st.button("VER RESUMEN DE REPASO"):
                st.markdown("""
                <div class="study-box">
                    <h4>Puntos Clave Tema 1:</h4>
                    <ul>
                        <li><b>Soberanía:</b> Reside en el pueblo español.</li>
                        <li><b>Forma Política:</b> Monarquía Parlamentaria.</li>
                        <li><b>Valores Superiores:</b> Libertad, Justicia, Igualdad y Pluralismo Político.</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        with st.expander("🚓 TEMA 2: FUERZAS DE SEGURIDAD"):
            st.write("Ley Orgánica 2/1986.")
            if st.button("VER ESQUEMA TÁCTICO"):
                st.markdown("""
                <div class="study-box">
                    <h4>Jerarquía de Mando:</h4>
                    1. Ministro del Interior <br>
                    2. Secretarios de Estado <br>
                    3. Directores Generales
                </div>
                """, unsafe_allow_html=True)

# --- SECCIÓN 3: PROGRESO ---
elif menu == "📊 MI PROGRESO":
    st.subheader("Estadísticas de Estudio")
    st.write("Aquí podrás ver cómo evolucionas cada semana.")
    # Datos de ejemplo
    df = pd.DataFrame({"Semana": ["Sem 1", "Sem 2", "Sem 3"], "Aciertos": [10, 15, 18]})
    st.line_chart(df.set_index("Semana"))
