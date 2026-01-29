import streamlit as st
import os

# 0. Ubicar la imagen del logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, "Standard_logo.png")

# 1. Configuración de la pagina
st.set_page_config(page_title="Lobby", initial_sidebar_state="collapsed", layout="wide")
st.markdown(
    """
    <style>
        /* Elimina el botón > de la esquina superior izquierda */
        [data-testid="collapsedControl"] {
            display: none !important;
        }

        /* Elimina la barra lateral por completo */
        [data-testid="stSidebar"] {
            display: none !important;
        }
        
        /* Elimina el encabezado superior para que no quede espacio vacío */
        header {
            visibility: hidden !important;
            height: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# 2. Tamaño y orietación del logo y titulo
col_izq, col_centro, col_der = st.columns([0.000000000000000000000000000000001, 0.025, 0.2]) 

if os.path.exists(ruta_logo):
    with col_centro:
        st.image(ruta_logo, width=200)
with col_der:
    st.title("Sistema de Cotización Inteligente")
    st.write("Bienvenido/a. Selecciona una categoría para empezar:")

    st.divider()