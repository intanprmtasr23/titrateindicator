import streamlit as st

st.write("welcome,*world*")

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
    min_value=10, max_value=200, value=50, step=10
)
initial_concentration_acid = st.sidebar.slider(
    "Konsentrasi Asam Awal (M)",
    min_value=0.01, max_value=1.0, value=0.1, step=0.01, format="%.2f"
)
concentration_base = st.sidebar.slider(
    "Konsentrasi Basa (M)",
    min_value=0.01, max_value=1.0, value=0.1, step=0.01, format="%.2f"
)

st.sidebar.markdown("---")

# --- Input Volume Titran ---
st.header("Tambahkan Titran (Basa)")
volume_base_added = st.slider(
    "Volume Basa yang Ditambahkan (mL)",
    min_value=0.0, max_value=2 * initial_volume_acid * initial_concentration_acid / concentration_base,
    value=0.0, step=0.1
)

# --- Nama Indikator dan Rentang pH ---
st.sidebar.header("Pilih Indikator")
selected_indicator = st.sidebar.selectbox(
    "Indikator Kimia",
    ["Fenolftalein", "Metil Oranye", "Bromtimol Biru"]
)

indicator_info = {
    "Fenolftalein": {"range": (8.2, 10.0), "color_acid": "transparan", "color_base": "merah muda"},
    "Metil Oranye": {"range": (3.1, 4.4), "color_acid": "merah", "color_base": "kuning"},
    "Bromtimol Biru": {"range": (6.0, 7.6), "color_acid": "kuning", "color_base": "biru"}
}

# --- Fungsi Perhitungan pH (Asam Kuat-Basa Kuat) ---
def calculate_ph(vol_acid, conc_acid, vol_base, conc_base):
    moles_acid = vol_acid * conc_acid # mmol
    moles_base = vol_base * conc_base # mmol

    if moles_acid > moles_base:
        # Asam berlebih
        remaining_moles_acid = moles_acid - moles_base
        total_volume = vol_acid + vol_base
        concentration_h_plus = remaining_moles_acid / total_volume
        ph = -np.log10(concentration_h_plus)
    elif moles_base > moles_acid:
        # Basa berlebih
        remaining_moles_base = moles_base - moles_acid
        total_volume = vol_acid + vol_base
        concentration_oh_minus = remaining_moles_base / total_volume
        poh = -np.log10(concentration_oh_minus)
        ph = 14 - poh
    else:
        # Titik ekuivalen (pH 7 untuk asam kuat-basa kuat)
        ph = 7.0
    return ph

# --- Fungsi Menentukan Warna Indikator ---
def get_indicator_display_info(ph, indicator_name):
    info = indicator_info[indicator_name]
    low_ph, high_ph = info["range"]
    color_acid = info["color_acid"]
    color_base = info["color_base"]

    display_color_name = ""
    hex_color_code = ""

    if ph < low_ph:
        display_color_name = color_acid
        # Contoh kode warna hex:
        if indicator_name == "Fenolftalein": hex_color_code = "#FFFFFF" # putih/transparan
        elif indicator_name == "Metil Oranye": hex_color_code = "#FF0000" # merah
        elif indicator_name == "Bromtimol Biru": hex_color_code = "#FFFF00" # kuning
    elif ph >= high_ph:
        display_color_name = color_base
        # Contoh kode warna hex:
        if indicator_name == "Fenolftalein": hex_color_code = "#FFC0CB" # merah muda
        elif indicator_name == "Metil Oranye": hex_color_code = "#FFFF00" # kuning
        elif indicator_name == "Bromtimol Biru": hex_color_code = "#0000FF" # biru
    else:
        # Transisi warna di rentang pH
        display_color_name = f"transisi ({color_acid} ke {color_base})"
        # Untuk gradasi bisa lebih kompleks, ini contoh sederhana
        if indicator_name == "Fenolftalein": hex_color_code = "#FFC0CB" # merah muda (mulai terlihat)
        elif indicator_name == "Metil Oranye": hex_color_code = "#FF8C00" # oranye
        elif indicator_name == "Bromtimol Biru": hex_color_code = "#4169E1" # biru kerajaan
    
    return display_color_name, hex_color_code

# --- Perhitungan dan Tampilan Hasil ---
ph_current = calculate_ph(
    initial_volume_acid, initial_concentration_acid,
    volume_base_added, concentration_base
)

st.header("Hasil Titrasi")
st.write(f"*pH Larutan:* {ph_current:.2f}")

indicator_display_name, indicator_hex_color = get_indicator_display_info(ph_current, selected_indicator)

st.write(f"*Warna {selected_indicator}:* {indicator_display_name}")

# Kotak visualisasi warna
st.markdown(
    f"""
    <div style="
        width: 150px;
        height: 75px;
        background-color: {indicator_hex_color};
        border: 2px solid #ccc;
        border-radius: 8px;
        margin: 10px auto;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    "></div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Informasi Indikator ---
st.subheader("Informasi Indikator Terpilih")
st.write(f"{selected_indicator}:")
st.write(f"- Rentang pH Perubahan Warna: {indicator_info[selected_indicator]['range'][0]} - {indicator_info[selected_indicator]['range'][1]}")
st.write(f"- Warna di pH rendah: {indicator_info[selected_indicator]['color_acid']}")
st.write(f"- Warna di pH tinggi: {indicator_info[selected_indicator]['color_base']}")

st.markdown("---")

st.info("Simulasi ini mengasumsikan titrasi asam kuat-basa kuat. Perhitungan pH untuk asam/basa lemah lebih kompleks.")
st.markdown("Dibuat dengan ❤ dan Streamlit.")
