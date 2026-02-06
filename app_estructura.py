import streamlit as st
import pandas as pd
import time
import plotly.express as px # Para gráficos pro

# CONFIGURACIÓN TÉCNICA
st.set_page_config(page_title="VORTEX ACADEMIC PRO", page_icon="🛡️", layout="wide")

# CSS "ELITE DARK MODE"
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    .main-header { 
        background: linear-gradient(90deg, #0d1117 0%, #161b22 100%);
        padding: 40px; border-radius: 20px; border: 1px solid #30363d;
        text-align: center; margin-bottom: 30px;
    }
    .metric-card {
        background: #161b22; border: 1px solid #30363d;
        padding: 20px; border-radius: 15px; text-align: center;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; background-color: #161b22; border-radius: 10px 10px 0 0;
        color: white; padding: 0 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #58a6ff !important; }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("""
<div class="main-header">
    <h1 style="color:#58a6ff; font-size: 3.5rem; margin:0;">VORTEX <span style="color:white;">ACADEMIC</span></h1>
    <p style="letter-spacing: 5px; opacity:0.7;">SISTEMA OPERATIVO DE ESTUDIO AVANZADO</p>
    <p style="font-style: italic; color: #f1c40f; margin-top:15px;">"No estudies para aprobar, estudia para que no tengan más remedio que darte la plaza." 🛡️</p>
</div>
""", unsafe_allow_html=True)

# --- NAVEGACIÓN PRINCIPAL ---
tab1, tab2, tab3, tab4 = st.tabs(["🎯 EXAMEN PRO", "📚 TEMARIO TÁCTICO", "📊 MI RENDIMIENTO", "⚡ FLASHCARDS"])

# 1. EXAMEN PRO CON CRONÓMETRO
with tab1:
    col_q, col_timer = st.columns([3, 1])
    
    with col_timer:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.write("⏱️ TIEMPO RESTANTE")
        st.header("14:59")
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("")
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.write("📈 PRECISIÓN")
        st.header("88%")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_q:
        # Banco ampliado (Ejemplo)
        preguntas = [
            {"p": "¿Qué mayoría se requiere para la reforma agravada del Art. 168?", "o": ["2/3 de cada Cámara", "3/5 de cada Cámara", "Absoluta"], "r": "2/3 de cada Cámara"},
            {"p": "¿Cuál es la duración del mandato de los miembros del Tribunal Constitucional?", "o": ["5 años", "9 años", "12 años"], "r": "9 años"},
            {"p": "¿Quién autoriza la prórroga de la detención preventiva hasta las 72h?", "o": ["El Juez", "El Fiscal", "La Ley directamente"], "r": "La Ley directamente"}
        ]
        
        if 'idx' not in st.session_state: st.session_state.idx = 0
        
        q = preguntas[st.session_state.idx % len(preguntas)]
        st.markdown(f"### Pregunta {st.session_state.idx + 1}")
        st.info(q["p"])
        ans = st.radio("Selecciona opción:", q["o"])
        
        if st.button("CONFIRMAR RESPUESTA"):
            if ans == q["r"]: st.success("RESPUESTA CORRECTA - Punto sincronizado.")
            else: st.error(f"FALLO - La respuesta era: {q['r']}")
            st.session_state.idx += 1
            time.sleep(1)
            st.rerun()

# 2. TEMARIO TÁCTICO (Completo)
with tab2:
    st.subheader("📚 REPOSITORIO DE INTELIGENCIA")
    c1, c2, c3 = st.columns(3)
    
    bloques = {
        "DERECHO": ["Constitución", "Penal", "Administrativo", "Derechos Humanos"],
        "SOCIAL": ["Sociología", "Globalización", "Drogodependencia"],
        "TÉCNICO": ["Armamento", "Informática", "Topografía", "Ortografía"]
    }
    
    for i, (titulo, temas) in enumerate(bloques.items()):
        with [c1, c2, c3][i]:
            st.markdown(f"#### 📁 {titulo}")
            for tema in temas:
                with st.expander(f"📄 {tema}"):
                    st.write(f"Resumen crítico del bloque de {tema}.")
                    st.button(f"Descargar Guía {tema}", key=tema)

# 3. MI RENDIMIENTO (Gráficos Profesionales)
with tab3:
    st.subheader("📊 ANÁLISIS DE EVOLUCIÓN")
    # Generamos datos falsos para el gráfico
    df_stats = pd.DataFrame({
        'Fecha': pd.date_range(start='2026-01-01', periods=10),
        'Nota': [4.5, 5.2, 5.0, 6.1, 5.8, 7.2, 7.5, 8.1, 7.9, 8.5]
    })
    fig = px.line(df_stats, x='Fecha', y='Nota', title='Evolución de Nota Media', markers=True)
    fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

# 4. FLASHCARDS (Para memorizar rápido)
with tab4:
    st.subheader("⚡ ENTRENAMIENTO DE MEMORIA RÁPIDA")
    st.write("Haz clic para ver la respuesta y memorizar conceptos clave.")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        with st.container():
            st.markdown('<div class="metric-card"><b>¿Qué es el <i>Habeas Corpus</i>?</b></div>', unsafe_allow_html=True)
            if st.button("REVELAR RESPUESTA"):
                st.warning("Procedimiento jurídico para evitar detenciones ilegales. Art. 17.4 CE.")
    with col_f2:
        with st.container():
            st.markdown('<div class="metric-card"><b>¿Cuántos diputados tiene el Congreso?</b></div>', unsafe_allow_html=True)
            if st.button("REVELAR RESPUESTA", key="f2"):
                st.warning("Mínimo 300, máximo 400. Actualmente 350.")
