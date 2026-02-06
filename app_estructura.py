import streamlit as st
import pandas as pd

st.set_page_config(page_title="ESTRUTURA TACTICAL", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #f1c40f; }
    .header { background-color: #f1c40f; color: black; padding: 20px; text-align: center; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>ESTRUTURA: TACTICAL OPS v1.0</h1></div>', unsafe_allow_html=True)

st.write("### Simulador de Puntos para Opositores")
nombre = st.text_input("Nombre del Aspirante:", "Josías Martínez")
puntos = st.slider("Puntos actuales en simulacro", 0, 30, 15)

if st.button("CALCULAR APTITUD"):
    if puntos >= 15:
        st.success(f"ASPIRANTE {nombre}: APTO")
    else:
        st.error(f"ASPIRANTE {nombre}: NO APTO")

st.info("Desarrollado por Josías Martínez - Tactical Solutions")
