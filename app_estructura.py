import streamlit as st
import pandas as pd

# CONFIGURACIÓN TÉCNICA
st.set_page_config(page_title="ESTRUTURA PRO", layout="wide")

# CSS PROFESIONAL (NEÓN INDUSTRIAL)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #f1c40f; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .card {
        background: #111; border: 1px solid #333; padding: 20px;
        border-radius: 10px; margin-bottom: 20px; border-left: 4px solid #f1c40f;
    }
    .goal-text { font-size: 1.2rem; font-weight: bold; color: #fff; }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR: PERFIL Y METAS
with st.sidebar:
    st.title("👤 PERFIL TÁCTICO")
    nombre = st.text_input("Operador", "Josías Martínez")
    meta_puntos = st.slider("Meta de Puntos", 15, 30, 20)
    st.divider()
    st.write("📂 **GESTIÓN DE DATOS**")
    if st.button("Guardar Progreso Local"):
        st.success("Configuración guardada en caché.")

# CUERPO PRINCIPAL
st.markdown('<h1 style="color:#f1c40f;">ESTRUTURA: TACTICAL OPS v2.5</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🎯 METAS Y NOTAS", "📖 MÉTODOS ESTUDIO", "⚙️ CONFIG"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 📥 MARCAS ACTUALES")
        d_reps = st.number_input("Dominadas", 0, 30, 10)
        c_seg = st.number_input("1km Carrera (seg)", 180, 350, 220)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        nota = (d_reps * 0.5) + (10 - (c_seg - 180)//10) # Lógica pro
        progreso = min(nota / meta_puntos, 1.0)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write(f"### 📈 PROGRESO HACIA META ({meta_puntos} pts)")
        st.progress(progreso)
        st.write(f"Nota Actual: **{nota:.1f}**")
        if nota >= meta_puntos:
            st.balloons()
            st.success("¡META ALCANZADA!")
        else:
            st.warning(f"Te faltan **{meta_puntos - nota:.1f}** puntos para tu objetivo.")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.write("### 🧠 MÉTODOS DE ENTRENAMIENTO CIENTÍFICO")
    exp1 = st.expander("🔥 MÉTODO DE PIRÁMIDE (Para Dominadas)")
    exp1.write("Realiza 1 rep, descansa 10s, realiza 2 reps... hasta llegar a tu máximo y luego baja. Ideal para ganar volumen rápido.")
    
    exp2 = st.expander("🏃 MÉTODO FARTLEK (Para 1000m)")
    exp2.write("Corre 200m a tope, trota 200m. Repite 5 veces. Esto rompe tu techo de velocidad.")

with tab3:
    st.write("Configuración del sistema y selección de baremos oficiales.")
