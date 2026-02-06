import streamlit as st
import pandas as pd

# CONFIGURACIÓN DE ALTA PRECISIÓN
st.set_page_config(page_title="VORTEX | Academic Intelligence", page_icon="📚", layout="wide")

# ESTILO "BIBLIOTECA TÁCTICA" (Elegante y Serio)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    .stApp { background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; }
    
    .main-header {
        background: #1e293b; border-bottom: 2px solid #38bdf8;
        padding: 30px; text-align: left; border-radius: 0 0 15px 15px;
    }
    
    .exam-card {
        background: #1e293b; border: 1px solid #334155;
        padding: 20px; border-radius: 12px; margin-bottom: 15px;
        transition: 0.3s;
    }
    .exam-card:hover { border-color: #38bdf8; background: #0f172a; }
    
    .topic-tag {
        background: #38bdf8; color: #0f172a; padding: 4px 12px;
        border-radius: 20px; font-weight: bold; font-size: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<div class="main-header"><h1>VORTEX <span style="color:#38bdf8;">ACADEMIC</span></h1><p>REPOSITORIO DE INTELIGENCIA PARA OPOSICIONES 2022-2026</p></div>', unsafe_allow_html=True)

# --- NAVEGACIÓN ---
menu = st.sidebar.selectbox("MÓDULO DE ACCESO", ["📂 ARCHIVO DE EXÁMENES", "📖 TEMARIO OFICIAL", "📈 CONTROL DE METAS"])

if menu == "📂 ARCHIVO DE EXÁMENES":
    st.subheader("HISTÓRICO DE EXÁMENES (Últimos 4 años)")
    st.write("Analiza las preguntas reales que han caído en las convocatorias anteriores.")
    
    examenes = [
        {"Año": "2025", "Convocatoria": "Promoción XXXIX", "Dificultad": "Alta", "Temas Clave": "Derecho Penal, Extranjería"},
        {"Año": "2024", "Convocatoria": "Promoción XXXVIII", "Dificultad": "Media-Alta", "Temas Clave": "Constitución, Unión Europea"},
        {"Año": "2023", "Convocatoria": "Promoción XXXVII", "Dificultad": "Media", "Temas Clave": "Derecho Administrativo, Ortografía"},
        {"Año": "2022", "Convocatoria": "Promoción XXXVI", "Dificultad": "Alta", "Temas Clave": "Derechos Humanos, Sociología"},
    ]
    
    for ex in examenes:
        with st.container():
            st.markdown(f"""
            <div class="exam-card">
                <h3>Examen Oficial {ex['Año']} <span class="topic-tag">{ex['Dificultad']}</span></h3>
                <p><b>Convocatoria:</b> {ex['Convocatoria']}</p>
                <p><b>Tendencia:</b> {ex['Temas Clave']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Descargar PDF y Plantilla {ex['Año']}", key=ex['Año']):
                st.info("Generando enlace de descarga segura...")

elif menu == "📖 TEMARIO OFICIAL":
    st.subheader("ESTRUCTURA DEL TEMARIO (Actualizado 2026)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("⚖️ BLOQUE I: CIENCIAS JURÍDICAS"):
            st.checkbox("Tema 1: La Constitución Española")
            st.checkbox("Tema 2: La Unión Europea")
            st.checkbox("Tema 3: Derecho Penal (Parte General)")
            st.checkbox("Tema 4: Derecho Penal (Parte Especial)")
        
        with st.expander("👥 BLOQUE II: CIENCIAS SOCIALES"):
            st.checkbox("Tema 15: Derechos Humanos")
            st.checkbox("Tema 16: Globalización y Antiglobalización")
    
    with col2:
        with st.expander("💻 BLOQUE III: MATERIAS TÉCNICAS"):
            st.checkbox("Tema 25: Armamento y Tiro")
            st.checkbox("Tema 26: Seguridad Informática")
            st.checkbox("Tema 27: Redes Sociales y Delitos")

elif menu == "📈 CONTROL DE METAS":
    st.subheader("SEGUIMIENTO DE OBJETIVOS DE ESTUDIO")
    
    # Sistema de guardado de metas
    if 'metas' not in st.session_state:
        st.session_state.metas = []
        
    with st.form("nueva_meta"):
        meta_text = st.text_input("Define tu objetivo (ej: Estudiar 4h Penal)")
        fecha_meta = st.date_input("Fecha límite")
        if st.form_submit_button("AÑADIR A MI RUTA"):
            st.session_state.metas.append({"Meta": meta_text, "Fecha": fecha_meta, "Estado": "Pendiente"})
            
    if st.session_state.metas:
        st.table(pd.DataFrame(st.session_state.metas))
