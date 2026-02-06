import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import time

# 1. CONFIGURACIÓN DE NIVEL EMPRESARIAL
st.set_page_config(page_title="VORTEX | Management Suite", page_icon="🏢", layout="wide")

# 2. CSS PROFESIONAL "VORTEX BUSINESS"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=JetBrains+Mono&display=swap');
    
    .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Inter', sans-serif; }
    
    .admin-card {
        background: #161b22; border: 1px solid #30363d;
        padding: 20px; border-radius: 12px; border-left: 5px solid #238636;
    }
    
    .sidebar-logo {
        text-align: center; padding: 20px; border-bottom: 1px solid #30363d;
    }
    
    .stat-box {
        background: #0d1117; border: 1px solid #30363d;
        padding: 15px; border-radius: 10px; text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("""
<div style="background: linear-gradient(90deg, #161b22 0%, #0d1117 100%); padding: 30px; border-radius: 15px; border-bottom: 2px solid #58a6ff; margin-bottom: 25px;">
    <h1 style="color: #58a6ff; margin: 0;">VORTEX <span style="color:white;">ACADEMIC</span></h1>
    <p style="opacity: 0.7;">CENTRO DE GESTIÓN Y RENDIMIENTO PARA ACADEMIAS</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div class="sidebar-logo"><h3>🛡️ PANEL VORTEX</h3></div>', unsafe_allow_html=True)
    perfil = st.selectbox("TIPO DE ACCESO", ["👨‍🎓 ALUMNO", "🏢 ADMINISTRADOR ACADEMIA"])
    st.divider()
    if perfil == "👨‍🎓 ALUMNO":
        menu = st.radio("NAVEGACIÓN", ["🏠 Inicio", "📝 Test de Examen", "📚 Mis Temas", "📊 Mis Notas"])
    else:
        menu = st.radio("NAVEGACIÓN", ["📈 Dashboard Academia", "👥 Gestión Alumnos", "⚙️ Configuración"])

# --- MODULO ALUMNO ---
if perfil == "👨‍🎓 ALUMNO":
    if menu == "🏠 Inicio":
        st.subheader(f"Bienvenido de nuevo, {st.sidebar.text_input('ID Alumno', 'Josías')}")
        st.markdown("> 'La constancia es la clave del éxito. Hoy es un buen día para avanzar 2 temas.'")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Temas Completados", "12/28", "+1")
        c2.metric("Nota Media", "7.45", "-0.2")
        c3.metric("Posición Ranking", "#14", "+2")

    elif menu == "📝 Test de Examen":
        st.subheader("📝 SIMULADOR DE EXAMEN")
        banco = [
            {"p": "¿A quién corresponde la sanción de las leyes?", "o": ["Rey", "Cortes", "Gobierno"], "r": "Rey"},
            {"p": "¿Qué mayoría se requiere para la investidura en 1ª votación?", "o": ["Simple", "Absoluta", "2/3"], "r": "Absoluta"},
            {"p": "¿Cuál es la capital del Estado?", "o": ["Madrid", "Barcelona", "Toledo"], "r": "Madrid"},
            {"p": "¿Qué lengua es oficial en todo el Estado?", "o": ["Castellano", "Catalán", "Todas"], "r": "Castellano"},
            {"p": "¿Quién preside el Consejo de Ministros?", "o": ["Rey", "Presidente del Gobierno", "Ministro Interior"], "r": "Presidente del Gobierno"}
        ]
        
        score = 0
        with st.form("test_alumno"):
            for i, q in enumerate(banco):
                st.write(f"**{i+1}. {q['p']}**")
                ans = st.radio("Opción:", q['o'], key=f"ans_{i}")
                if ans == q['r']: score += 1
            if st.form_submit_button("Finalizar Test"):
                st.success(f"Test finalizado. Puntuación: {score}/{len(banco)}")
                st.balloons()

    elif menu == "📚 Mis Temas":
        st.subheader("📚 MI BIBLIOTECA")
        temas = ["Constitución Española", "Derecho Penal", "Sociología", "Ortografía"]
        for t in temas:
            with st.expander(f"📖 {t}"):
                st.write(f"Resumen del bloque {t} actualizado a 2026.")
                st.button(f"Descargar PDF {t}", key=t)

    elif menu == "📊 Mis Notas":
        st.subheader("📊 MI RENDIMIENTO")
        df_notas = pd.DataFrame({
            "Semana": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
            "Nota": [5.5, 6.2, 7.8, 7.4]
        })
        fig = px.line(df_notas, x="Semana", y="Nota", title="Evolución Personal", markers=True)
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

# --- MODULO ADMINISTRADOR ---
else:
    if menu == "📈 Dashboard Academia":
        st.subheader("🏢 PANEL DE CONTROL PARA DIRECTORES")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="admin-card"><h4>Alumnos Activos</h4><h1>1,240</h1></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="admin-card"><h4>Media Global</h4><h1>6.82</h1></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="admin-card"><h4>Tasa de Aprobados</h4><h1>78%</h1></div>', unsafe_allow_html=True)

        st.divider()
        st.write("### ⚠️ TEMAS CRÍTICOS (Más fallados por los alumnos)")
        error_data = pd.DataFrame({
            "Tema": ["Derecho Penal", "Unión Europea", "Extranjería", "Ortografía"],
            "Fallos Globales (%)": [65, 58, 42, 30]
        })
        fig_err = px.bar(error_data, x="Tema", y="Fallos Globales (%)", color="Fallos Globales (%)", color_continuous_scale="Reds")
        fig_err.update_layout(template="plotly_dark")
        st.plotly_chart(fig_err, use_container_width=True)
        st.info("💡 Sugerencia para la Academia: Programa una clase de repaso de 'Derecho Penal'.")

    elif menu == "👥 Gestión Alumnos":
        st.subheader("👥 LISTADO DE ASPIRANTES")
        st.write("Busca y supervisa el progreso individual de tus alumnos.")
        df_alumnos = pd.DataFrame({
            "Nombre": ["Josías Martínez", "Ana García", "Carlos López", "Marta Sanz"],
            "Progreso": ["85%", "62%", "45%", "92%"],
            "Última Nota": [8.5, 6.4, 4.2, 9.8],
            "Estado": ["Excelente", "Normal", "Riesgo", "Excelente"]
        })
        st.dataframe(df_alumnos, use_container_width=True)
        if st.button("Descargar Informe de Alumnos (CSV)"):
            st.success("Informe generado correctamente.")

    elif menu == "⚙️ Configuración":
        st.subheader("⚙️ AJUSTES DE LA ACADEMIA")
        st.color_picker("Color corporativo de la App", "#58a6ff")
        st.file_uploader("Subir Logo de la Academia")
        st.text_area("Mensaje de Bienvenida para Alumnos", "¡A por la plaza!")

# --- FOOTER ---
st.markdown("---")
st.caption("VORTEX ACADEMIC v13.0 | Cloud Intelligence | Desarrollado para el éxito empresarial.")
