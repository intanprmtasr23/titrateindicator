import streamlit as st import matplotlib.pyplot as plt import numpy as np

Konfigurasi halaman

st.set_page_config(page_title="Indikator Titrasi", page_icon=":test_tube:", layout="wide")

Judul aplikasi

st.title(":test_tube: Aplikasi Pemilihan Indikator Titrasi") st.markdown(""" Aplikasi ini membantu memilih indikator yang sesuai untuk berbagai jenis titrasi berdasarkan parameter reaksi. """)

Tab untuk berbagai jenis titrasi

tab1, tab2, tab3, tab4 = st.tabs([ "Asam-Basa", "Redoks", "Kompleksometri", "Pengendapan" ])

with tab1: st.header("Titrasi Asam-Basa")

col1, col2 = st.columns(2)
with col1:
    jenis_titran = st.selectbox(
        "Jenis Titran",
        ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"],
        key="titran_ab"
    )
with col2:
    jenis_analit = st.selectbox(
        "Jenis Analit",
        ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"],
        key="analit_ab"
    )

if ("Asam Kuat" in jenis_titran and "Basa Kuat" in jenis_analit) or ("Basa Kuat" in jenis_titran and "Asam Kuat" in jenis_analit):
    pH_eq = 7.0
    st.success("Titik ekuivalen pada pH 7.0 (netral)")
elif ("Asam Kuat" in jenis_titran and "Basa Lemah" in jenis_analit):
    pH_eq = st.slider("Perkiraan pH titik ekuivalen", 3.0, 6.5, 5.0, 0.1)
elif ("Basa Kuat" in jenis_titran and "Asam Lemah" in jenis_analit):
    pH_eq = st.slider("Perkiraan pH titik ekuivalen", 7.5, 11.0, 8.5, 0.1)
else:
    pH_eq = st.slider("Perkiraan pH titik ekuivalen", 3.0, 11.0, 7.0, 0.1)
    st.warning("Titrasi antara asam lemah dan basa lemah umumnya tidak direkomendasikan")

indikator_ab = {
    "Metil Violet": (0.1, 1.5, "Kuning ke Biru-hijau"),
    "Timol Biru": (8.0, 9.6, "Kuning ke Biru"),  # disesuaikan
    "Metil Kuning": (2.9, 4.0, "Merah ke Kuning"),
    "Bromfenol Biru": (3.0, 4.6, "Kuning ke Biru-ungu"),
    "Metil Jingga": (3.1, 4.4, "Merah ke Jingga"),
    "Bromkresol Hijau": (3.8, 5.4, "Kuning ke Biru"),
    "Metil Merah": (4.2, 6.3, "Merah ke Kuning"),
    "Klorofenol Merah": (5.0, 6.6, "Kuning ke Merah"),
    "Bromtimol Biru": (6.0, 7.6, "Kuning ke Biru"),
    "Fenol Merah": (6.8, 8.4, "Kuning ke Merah"),
    "Kresol Merah": (7.2, 8.8, "Kuning ke Merah"),
    "Fenolftalein": (8.3, 10.0, "Tak berwarna ke Merah muda"),
    "Timolftalein": (9.3, 10.5, "Tak berwarna ke Biru"),
    "Alizarin Kuning R": (10.1, 12.0, "Kuning ke Merah")
}

st.subheader("Rekomendasi Indikator")
rec_indicators = []

for name, (low, high, change) in indikator_ab.items():
    if low <= pH_eq <= high:
        rec_indicators.append((name, low, high, change))

if rec_indicators:
    st.write(f"Indikator yang sesuai untuk pH titik ekuivalen {pH_eq:.1f}:")
    for name, low, high, change in rec_indicators:
        st.info(f"{name}: pH {low}-{high} ({change})")
else:
    st.error("Tidak ditemukan indikator yang cocok. Pertimbangkan penggunaan pH meter.")

st.subheader("Visualisasi Rentang pH Indikator")
fig, ax = plt.subplots(figsize=(10, 6))

ax.axvline(x=pH_eq, color='red', linestyle='--', label=f'pH Ekuivalen ({pH_eq:.1f})')

y_pos = 1
for name, (low, high, _) in indikator_ab.items():
    color = 'green' if name in [ind[0] for ind in rec_indicators] else 'gray'
    width = 5 if color == 'green' else 3
    ax.hlines(y=y_pos, xmin=low, xmax
