import streamlit as st
import matplotlib.pyplot as plt
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
    
    # Visualisasi
    st.subheader("Visualisasi Rentang pH Indikator")
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot garis pH
    ax.axvline(x=pH_eq, color='red', linestyle='--', label=f'pH Ekuivalen ({pH_eq:.1f})')
    
    # Plot rentang indikator
    y_pos = 1
    for name, (low, high, _) in indikator_ab.items():
        if name in [ind[0] for ind in rec_indicators]:
            ax.hlines(y=y_pos, xmin=low, xmax=high, colors='green', linewidth=5, label=name)
        else:
            ax.hlines(y=y_pos, xmin=low, xmax=high, colors='gray', linewidth=3, alpha=0.5)
        ax.text(high+0.2, y_pos, name, va='center')
        y_pos += 1
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, y_pos)
    ax.set_xlabel("pH")
    ax.set_yticks([])
    ax.set_title("Rentang pH Indikator Asam-Basa")
    ax.legend(loc='upper right')
    ax.grid(True, axis='x')
    
    st.pyplot(fig)

with tab2:  # Titrasi Redoks
    st.header("Titrasi Redoks")
    
    metode_redoks = st.selectbox(
        "Pilih Metode Titrasi Redoks",
        ["Permanganometri", "Iodometri", "Dikromatometri", "Serimetri", "Bromatometri"],
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
        
    elif metode_redoks == "Dikromatometri":
        st.markdown("""
        ### Dikromatometri (Menggunakan K₂Cr₂O₇)
        - *Indikator*: 
          1. Difenilamin sulfonat
            - Perubahan warna: Ungu ke hijau
          2. Ferroin (fenaantrolin besi)
            - Perubahan warna: Merah ke biru pucat
        - *Aplikasi*: Penentuan Fe²⁺, COD (Chemical Oxygen Demand)
        """)
        
    elif metode_redoks == "Serimetri":
        st.markdown("""
        ### Serimetri (Menggunakan Ce⁴⁺)
        - *Indikator*: 
          1. Ferroin
            - Perubahan warna: Merah ke biru pucat
          2. N-fenilantranilat
            - Perubahan warna: Ungu ke hijau
        - *Aplikasi*: Penentuan senyawa organik, Fe²⁺
        """)
        
    else:  # Bromatometri
        st.markdown("""
        ### Bromatometri (Menggunakan KBrO₃)
        - *Indikator*: 
          1. Metil merah atau metil jingga
            - Perubahan warna: Merah ke tak berwarna
          2. Reaksi dengan senyawa organik membentuk bromoform
        - *Aplikasi*: Penentuan senyawa organik aromatik
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
        
    elif ion_logam == "Zn²⁺":
        st.markdown("""
        ### Penentuan Zn²⁺
        - *Indikator*: 
          1. Eriochrome Black T (EBT)
            - Perubahan warna: Merah anggur ke biru
          2. Murexide
            - Perubahan warna: Merah ke ungu
        - *Kondisi*: 
          - pH 10 untuk EBT
          - pH 9 untuk Murexide
        """)
        
    elif ion_logam == "Cu²⁺":
        st.markdown("""
        ### Penentuan Cu²⁺
        - *Indikator*: 
          1. Murexide
            - Perubahan warna: Kuning ke ungu
          2. PAN (1-(2-Piridilazo)-2-naftol)
            - Perubahan warna: Kuning ke merah
        - *Kondisi*: 
          - pH 5-6 (buffer asetat)
        """)
        
    elif ion_logam == "Fe³⁺":
        st.markdown("""
        ### Penentuan Fe³⁺
        - *Indikator*: Sulfosalicylic acid
        - *Perubahan warna*: Ungu ke kuning
        - *Kondisi*: 
          - pH 1.5-3.0
          - Suhu 50-60°C
        """)
        
    else:
        st.markdown(f"""
        ### Penentuan {ion_logam}
        - *Indikator umum*: 
          1. Xylenol Orange
            - Perubahan warna: Merah ke kuning
          2. Calmagite
            - Perubahan warna: Merah ke biru
        - *Kondisi*: pH disesuaikan dengan ion logam
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
        
    elif metode_pengendapan == "Argentometri (Volhard)":
        st.markdown("""
        ### Metode Volhard (Penentuan Halida Tidak Langsung)
        - *Indikator*: Ion besi(III) (Fe³⁺)
        - *Perubahan warna*: Tak berwarna ke merah (FeSCN²⁺)
        - *Kondisi*: 
          - Suasana asam nitrat
          - Titrasi balik dengan SCN⁻
        - *Aplikasi*: Penentuan Cl⁻, Br⁻, I⁻, SCN⁻
        """)
        
    elif metode_pengendapan == "Argentometri (Fajans)":
        st.markdown("""
        ### Metode Fajans (Indikator Adsorpsi)
        - *Indikator*: 
          1. Fluorescein
            - Perubahan warna: Hijau kekuningan ke merah muda
          2. Dichlorofluorescein
            - Perubahan warna: Kuning ke merah muda
        - *Kondisi*: 
          - pH sesuai indikator
          - Partikel koloid harus terbentuk
        - *Aplikasi*: Penentuan halida dengan endpoint adsorpsi
        """)
        
    else:
        st.markdown(f"""
        ### {metode_pengendapan}
        - *Prinsip umum*: 
          - Pembentukan endapan yang stoikiometris
          - Penggunaan indikator yang bereaksi dengan kelebihan titran
        - *Contoh aplikasi*: 
          - Penentuan sulfat dengan Ba²⁺
          - Penentuan merkuri dengan tiosianat
        """)

# Informasi tambahan di sidebar
with st.sidebar:
    st.header("Panduan Penggunaan")
    st.markdown("""
    1. Pilih jenis titrasi dari tab yang tersedia
    2. Masukkan parameter reaksi
    3. Aplikasi akan memberikan rekomendasi indikator
    4. Perhatikan kondisi analisis yang disarankan
    """)
    
    st.header("Tips Penting")
    st.markdown("""
    - Pastikan indikator bekerja pada rentang pH titik ekuivalen
    - Gunakan indikator secukupnya (terlalu banyak dapat mengganggu)
    - Untuk titrasi dengan perubahan warna sulit diamati, pertimbangkan pH meter
    - Kalibrasi larutan titran secara berkala
    """)
    
    st.header("Tentang")
    st.markdown("""
    Aplikasi ini dikembangkan untuk membantu praktikum kimia analitik.
    
    *Versi*: 2.0  
    *Developer*: [Nama Anda]  
    *Institut*: [Nama Institusi]
    """)
