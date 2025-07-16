import streamlit as st
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Indikator Titrasi", page_icon=":test_tube:", layout="wide")

# Judul aplikasi
st.title(":test_tube: Aplikasi Pemilihan Indikator Titrasi")
st.markdown("""
Aplikasi ini membantu memilih indikator yang sesuai untuk berbagai jenis titrasi berdasarkan parameter reaksi.
""")

# Tab untuk berbagai jenis titrasi
tab1, tab2, tab3, tab4 = st.tabs([
    "Asam-Basa", 
    "Redoks", 
    "Kompleksometri", 
    "Pengendapan"
])

with tab1:  # Titrasi Asam-Basa
    st.header("Titrasi Asam-Basa")
    
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
    
    # Menentukan pH ekuivalen
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
    
    # Database indikator
    indikator_ab = {
        "Metil Violet": (0.1, 1.5, "Kuning ke Biru-hijau"),
        "Timol Biru": (1.2, 2.8, "Merah ke Kuning"),
        "Metil Kuning": (2.9, 4.0, "Merah ke Kuning"),
        "Bromfenol Biru": (3.0, 4.6, "Kuning ke Biru-ungu"),
        "Metil Jingga": (3.1, 4.4, "Merah ke Jingga"),
        "Bromkresol Hijau": (3.8, 5.4, "Kuning ke Biru"),
        "Metil Merah": (4.2, 6.3, "Merah ke Kuning"),
        "Klorofenol Merah": (5.0, 6.6, "Kuning ke Merah"),
        "Bromtimol Biru": (6.0, 7.6, "Kuning ke Biru"),
        "Fenol Merah": (6.8, 8.4, "Kuning ke Merah"),
        "Kresol Merah": (7.2, 8.8, "Kuning ke Merah"),
        "Timol Biru": (8.0, 9.6, "Kuning ke Biru"),
        "Fenolftalein": (8.3, 10.0, "Tak berwarna ke Merah muda"),
        "Timolftalein": (9.3, 10.5, "Tak berwarna ke Biru"),
        "Alizarin Kuning R": (10.1, 12.0, "Kuning ke Merah")
    }
    
    # Rekomendasi indikator
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

with tab2:  # Titrasi Redoks
    st.header("Titrasi Redoks")
    
    metode_redoks = st.selectbox(
        "Pilih Metode Titrasi Redoks",
        ["Permanganometri", "Iodometri"]
        key="metode_redoks"
    )
    
    if metode_redoks == "Permanganometri":
        st.markdown("""
        ### Permanganometri (Menggunakan KMnO₄)
        - *Indikator*: Tidak diperlukan, KMnO₄ berfungsi sebagai indikator sendiri
        - *Perubahan warna*: 
          - Dari ungu (MnO₄⁻) ke tak berwarna (Mn²⁺) dalam suasana asam
          - Dari ungu ke coklat (MnO₂) dalam suasana netral/basa
        - *Aplikasi*: Penentuan Fe²⁺, H₂O₂, oksalat, dll.
        """)
        
    elif metode_redoks == "Iodometri":
        st.markdown("""
        ### Iodometri/Iodimetri
        - *Indikator*: Larutan kanji
        - *Perubahan warna*: 
          - Tak berwarna ke biru tua (kompleks I₂-kanji)
        - *Aplikasi*: Penentuan senyawa pengoksidasi (melalui I⁻) atau zat pereduksi
        """)

with tab3:  # Titrasi Kompleksometri
    st.header("Titrasi Kompleksometri")
    
    ion_logam = st.selectbox(
        "Pilih Ion Logam yang Dititrasi",
        ["Ca²⁺/Mg²⁺", "Zn²⁺", "Cu²⁺", "Fe³⁺", "Pb²⁺", "Hg²⁺", "Al³⁺"],
        key="ion_logam"
    )
    
    if ion_logam == "Ca²⁺/Mg²⁺":
        st.markdown("""
        ### Penentuan Kesadahan Air (Ca²⁺ dan Mg²⁺)
        - *Indikator*: Eriochrome Black T (EBT)
        - *Perubahan warna*: Merah anggur ke biru
        - *Kondisi*: 
          - pH 10 (buffer NH₃/NH₄Cl)
          - Suhu ruang
        - *Titran*: EDTA 0.01 M
        """)

with tab4:  # Titrasi Pengendapan
    st.header("Titrasi Pengendapan")
    
    metode_pengendapan = st.selectbox(
        "Pilih Metode Titrasi Pengendapan",
        ["Argentometri (Mohr)", "Argentometri (Volhard)", "Argentometri (Fajans)", "Tiosianatometri", "Sulfatometri"],
        key="metode_pengendapan"
    )
    
    if metode_pengendapan == "Argentometri (Mohr)":
        st.markdown("""
        ### Metode Mohr (Penentuan Klorida)
        - *Indikator*: Ion kromat (CrO₄²⁻)
        - *Perubahan warna*: Kuning ke merah bata (Ag₂CrO₄)
        - *Kondisi*: 
          - pH netral/sedikit basa (6.5-9.0)
          - Tidak boleh ada amonia
        - *Aplikasi*: Penentuan Cl⁻, Br⁻
        """)

# Informasi tambahan di sidebar
with st.sidebar:
    st.header("Panduan Penggunaan")
    st.markdown("""
    1. Pilih jenis titrasi dari tab yang tersedia
    2. Masukkan parameter reaksi
    3. Aplikasi akan memberikan rekomendasi indikator
    """)
    
    st.header("Cara Mengatasi Error")
    st.markdown("""
    Jika muncul error tentang modul yang tidak ditemukan:
    1. Pastikan semua dependensi terinstall:
    bash
    pip install streamlit numpy
    
    2. Untuk versi lengkap dengan visualisasi:
    bash
    pip install matplotlib
    
    """)
