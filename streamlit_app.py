import streamlit as st
import numpy as np

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Simulasi Titrasi Asam Basa",
    layout="centered"
)
# --- Judul Aplikasi ---
st.title("🧪 Simulasi Titrasi Asam Basa")
st.markdown("---")

# --- Pengaturan Awal Titrasi ---
st.sidebar.header("Pengaturan Awal")
initial_volume_acid = st.sidebar.slider(
    "Volume Asam Awal (mL)",
    min_value=10, max_value=10, value=10, step=6
)
initial_concentration_acid = st.sidebar.slider(
    "Konsentrasi Asam Awal (M)",
    min_value=0.01, max_value=1.0, value=0.1, step=0.01, format="%.2f"
)
concentration_base = st.sidebar.slider(
    "Konsentrasi Basa (M)",
    min_value=0.01, max_value=1.0, value=0.1, step=0.01, format="%.2f"
)


