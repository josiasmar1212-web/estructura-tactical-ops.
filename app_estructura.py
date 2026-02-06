import streamlit as st
import pandas as pd

# CONFIGURACIÓN DE VORTEX
st.set_page_config(page_title="VORTEX | Tactical Path", page_icon="🌀", layout="wide")

# ESTILO "WAR ROOM" (SALA DE GUERRA)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&display=swap');
    
    .stApp { background: radial-gradient(circle, #0d1b2a 0%, #000814 100%); color: #00f2ff; font-family: 'Rajdhani', sans-serif; }
    
    .vortex-header {
        text-align: center; padding: 40px; border: 2px solid #00f2ff;
        border-radius: 20px; background: rgba(0, 242, 255, 0.05);
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.2); margin-bottom: 30px;
    }
    
    .mission-card {
        background: rgba(255, 255, 255, 0.03); border-left: 5px solid #00f2ff;
        padding: 20px; border-radius: 10px; margin: 10px 0;
    }
    
    .status-badge {
        background: #f1c40f; color: #000; padding: 5px 15px;
        border-radius: 20px; font-weight: bold; font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<div class="vortex-header"><h1>VORTEX <span style="color:#f1c40f;">TACTICAL PATH</span></h1><p>SISTEMA DE PREPARACIÓN DE ÉLITE</p></div>', unsafe_allow_html=True)

# --- SISTEMA DE GUARDADO (SESSION STATE) ---
if 'log_entrenamiento' not in st.session_state:
    st.session_state.log_entrenamiento = []

# --- PANEL DE CONTROL ---
col_menu, col_main = st.columns([1, 3])

with col_menu:
    st.markdown("### 🛠️ COMANDOS")
    opcion = st.radio("SECCIÓN", ["PANEL DE CONTROL", "MÉTODOS DE ESTUDIO", "RECOLECTOR DE DATOS"])
    st.divider()
    st.write("📡 **ESTADO:** CONECTADO")
    st.write("🔋 **ENERGÍA:** 85%")

with col_main:
    if opcion == "PANEL DE CONTROL":
        st.subheader("🎯 MISIÓN DEL DÍA")
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown('<div class="mission-card"><h4>FUERZA</h4><p>Meta: 15 Dominadas</p></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="mission-card"><h4>AGILIDAD</h4><p>Meta: Sub-9 seg</p></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="mission-card"><h4>TEORÍA</h4><p>Meta: 2h de Leyes</p></div>', unsafe_allow_html=True)

        st.divider()
        st.write("### 📊 TU RENDIMIENTO EN TIEMPO REAL")
        val_fuerza = st.slider("Nivel de Fatiga Muscular", 0, 100, 30)
        st.progress(val_fuerza / 100)
        st.caption("A menor fatiga, mayor rendimiento en simulacro.")

    elif opcion == "MÉTODOS DE ESTUDIO":
        st.subheader("🧠 PROTOCOLOS DE APRENDIZAJE")
        
        with st.expander("📝 MÉTODO DE CODIFICACIÓN VISUAL"):
            st.write("Convierte leyes aburridas en esquemas de colores. Tu cerebro procesa imágenes 60,000 veces más rápido que el texto.")
            st.image("https://img.freepik.com/vector-premium/esquema-infografia-mapa-mental_23-2148352220.jpg", width=400)
            
        with st.expander("🎧 MÉTODO DE REPASO AUDITIVO"):
            st.write("Graba los temas más difíciles y escúchalos mientras entrenas. Crea conexiones neuronales dobles.")

    elif opcion == "RECOLECTOR DE DATOS":
        st.subheader("💾 REGISTRO DE MARCAS")
        with st.form("registro_vortex"):
            fecha = st.date_input("Fecha del Test")
            prueba = st.selectbox("Prueba", ["Dominadas", "1000m", "Circuito", "Examen Teórico"])
            resultado = st.number_input("Resultado (Puntos/Tiempo)")
            if st.form_submit_button("SINCRONIZAR DATOS"):
                st.session_state.log_entrenamiento.append({"Fecha": fecha, "Prueba": prueba, "Resultado": resultado})
                st.success("Dato almacenado en el núcleo de VORTEX.")

        if st.session_state.log_entrenamiento:
            st.write("### 📋 HISTORIAL RECIENTE")
            st.table(pd.DataFrame(st.session_state.log_entrenamiento))
