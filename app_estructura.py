import streamlit as st
import pandas as pd

# CONFIGURACIÓN PRO
st.set_page_config(page_title="ESTRUTURA TACTICAL | Academia", layout="wide")

# CSS INDUSTRIAL MILITAR
st.markdown("""
    <style>
    .stApp { background-color: #0b0c10; color: #f1c40f; font-family: 'Courier New'; }
    .stSelectbox, .stNumberInput { background-color: #1f2833 !important; }
    .nota-box { 
        background-color: #f1c40f; color: #000; padding: 15px; 
        border-radius: 10px; text-align: center; font-weight: bold; font-size: 24px;
    }
    .info-card { border-left: 5px solid #f1c40f; padding-left: 15px; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# LÓGICA DE BAREMOS (Simplificada para el ejemplo, pero funcional)
def calcular_nota(valor, tipo_prueba, cuerpo):
    if cuerpo == "Policía Nacional":
        if tipo_prueba == "Dominadas":
            if valor >= 17: return 10
            if valor <= 4: return 0
            return valor - 4
        if tipo_prueba == "1000m":
            if valor <= 189: return 10 # 3:09 min
            if valor >= 229: return 0  # 3:49 min
            return 10 - ((valor - 189) // 4)
    
    elif cuerpo == "Bomberos":
        # Los bomberos suelen pedir más nivel
        if tipo_prueba == "Dominadas":
            if valor >= 22: return 10
            return valor // 2
    return 5 # Nota base

# --- INTERFAZ PRINCIPAL ---
st.markdown('<h1 style="text-align:center;">🛡️ ESTRUTURA: TACTICAL TRAINING v2.0</h1>', unsafe_allow_html=True)
st.write("---")

menu = st.sidebar.radio("MÓDULO DE ACCESO", ["Simulador de Examen", "Biblioteca de Baremos", "Plan de Estudio"])

if menu == "Simulador de Examen":
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("⚙️ Configuración de Prueba")
        cuerpo = st.selectbox("Selecciona Oposición", ["Policía Nacional", "Bomberos"])
        sexo = st.radio("Género", ["Masculino", "Femenino"])
        
        st.divider()
        st.write("**Pruebas Físicas:**")
        domis = st.number_input("Dominadas (reps)", 0, 40, 10)
        carrera_min = st.number_input("Carrera 1km (Minutos)", 2, 6, 3)
        carrera_seg = st.number_input("Carrera 1km (Segundos)", 0, 59, 30)
        
        tiempo_total_seg = (carrera_min * 60) + carrera_seg
        
    with col2:
        st.subheader("📊 Análisis de Resultados")
        
        nota_fuerza = calcular_nota(domis, "Dominadas", cuerpo)
        nota_resistencia = calcular_nota(tiempo_total_seg, "1000m", cuerpo)
        media = (nota_fuerza + nota_resistencia) / 2
        
        st.markdown(f'<div class="nota-box">NOTA MEDIA: {media}</div>', unsafe_allow_html=True)
        
        if media >= 5:
            st.success
