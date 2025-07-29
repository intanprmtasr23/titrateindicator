import streamlit as st
import base64
import requests

def set_bg_from_drive(file_id):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(url)
    if response.status_code == 200:
        encoded = base64.b64encode(response.content).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Gagal mengambil gambar dari Google Drive.")

# Masukkan file ID di sini:
file_id = "1tq5WqVASGOSqqGKWOziSZNBlUjT3ST0e"
set_bg_from_drive(file_id)


# CSS untuk mempercantik tampilan
st.markdown("""
<style>
div[data-testid="stExpander"] div[role="button"] p {
    font-size: 18px;
    font-weight: bold;
    color: #2a3f5f;
}
.css-1aumxhk {
    background-color: rgba(500,500,500,0.8);
    border-radius: 20px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# Judul aplikasi dengan style
st.markdown("""
<div style="background-color: rgba(200,200,200,0.8); padding: 20px; border-radius: 10px;">
    <h1 style="color: #2a3f5f; text-align: center;">🧪 Aplikasi Pemilihan Indikator Titrasi</h1>
    <p style="text-align: center;">Pilih indikator yang sesuai untuk berbagai jenis titrasi analitik</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .custom-bg {
        background-color: rgba(255, 255, 255, 0.85);  /* putih transparan */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Tab untuk berbagai jenis titrasi
tab1, tab2, tab3, tab4 = st.tabs([
    "Asam-Basa", 
    "Redoks", 
    "Kompleksometri", 
    "Pengendapan"
])

st.markdown("""
    <style>
    .custom-bg {
        background-color: rgba(255, 255, 255, 0.85);  /* putih transparan */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

with tab1:  # Titrasi Asam-Basa
    st.markdown("""
    <style>
    .text-container {
        background-color: rgba(255, 255, 255, 0.9);  /* Putih transparan (0.9 = hampir solid) */
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .text-container h1, .text-container h2, .text-container h3 {
        font-weight: 800;
        color: #000;
        text-align: center;
    }
    .text-container p {
        font-size: 18px;
        font-weight: 600;
        color: #000;
        text-align: justify;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: rgba(200,200,200,0.8); padding: 20px; border-radius: 10px;">
        <h2 style="color: #2a3f5f;">Titrasi Asam-Basa</h2>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    # Database indikator asam-basa
    indikator_ab = {
        "Metil Violet": {"rentang": (0.1, 1.5), "perubahan": "Kuning ke Biru-hijau", "aplikasi": "Titrasi asam sangat kuat"},
        "Timol Biru": {"rentang": (1.2, 2.8), "perubahan": "Merah ke Kuning", "aplikasi": "Titrasi asam kuat"},
        "Metil Kuning": {"rentang": (2.9, 4.0), "perubahan": "Merah ke Kuning", "aplikasi": "Titrasi asam mineral"},
        "Bromfenol Biru": {"rentang": (3.0, 4.6), "perubahan": "Kuning ke Biru-ungu", "aplikasi": "Titrasi asam organik"},
        "Metil Jingga": {"rentang": (3.1, 4.4), "perubahan": "Merah ke Jingga", "aplikasi": "Titrasi asam kuat-basa kuat"},
        "Bromkresol Hijau": {"rentang": (3.8, 5.4), "perubahan": "Kuning ke Biru", "aplikasi": "Titrasi asam lemah"},
        "Metil Merah": {"rentang": (4.2, 6.3), "perubahan": "Merah ke Kuning", "aplikasi": "Titrasi asam karboksilat"},
        "Klorofenol Merah": {"rentang": (5.0, 6.6), "perubahan": "Kuning ke Merah", "aplikasi": "Titrasi buffer biologis"},
        "Bromtimol Biru": {"rentang": (6.0, 7.6), "perubahan": "Kuning ke Biru", "aplikasi": "Titrasi netralisasi"},
        "Fenol Merah": {"rentang": (6.8, 8.4), "perubahan": "Kuning ke Merah", "aplikasi": "Titrasi dalam biokimia"},
        "Kresol Merah": {"rentang": (7.2, 8.8), "perubahan": "Kuning ke Merah", "aplikasi": "Titrasi enzimatik"},
        "Timol Biru": {"rentang": (8.0, 9.6), "perubahan": "Kuning ke Biru", "aplikasi": "Titrasi basa lemah"},
        "Fenolftalein": {"rentang": (8.3, 10.0), "perubahan": "Tak berwarna ke Merah muda", "aplikasi": "Titrasi standar asam-basa"},
        "Timolftalein": {"rentang": (9.3, 10.5), "perubahan": "Tak berwarna ke Biru", "aplikasi": "Titrasi basa kuat"},
        "Alizarin Kuning R": {"rentang": (10.1, 12.0), "perubahan": "Kuning ke Merah", "aplikasi": "Titrasi basa sangat kuat"}
    }
    
    # Rekomendasi indikator
    st.markdown("""
    <style>
    .text-container {
        background-color: rgba(255, 255, 255, 0.9);  /* Putih transparan (0.9 = hampir solid) */
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .text-container h1, .text-container h2, .text-container h3 {
        font-weight: 800;
        color: #000;
        text-align: center;
    }
    .text-container p {
        font-size: 18px;
        font-weight: 600;
        color: #000;
        text-align: justify;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

    st.subheader("Rekomendasi Indikator")
    rec_indicators = []
    
    for name, data in indikator_ab.items():
        low, high = data["rentang"]
        if low <= pH_eq <= high:
            rec_indicators.append((name, low, high, data["perubahan"], data["aplikasi"]))
    
    if rec_indicators:
        st.write(f"Indikator yang sesuai untuk pH titik ekuivalen {pH_eq:.1f}:")
        for name, low, high, change, app in rec_indicators:
            with st.expander(f"{name}: pH {low}-{high} ({change})"):
                st.write(f"Perubahan Warna: {change}")
                st.write(f"Aplikasi Khas: {app}")
                st.write(f"Rentang pH: {low} - {high}")
    else:
        st.error("Tidak ditemukan indikator yang cocok. Pertimbangkan penggunaan pH meter.")
st.markdown("""
    <style>
    .custom-bg {
        background-color: rgba(255, 255, 255, 0.85);  /* putih transparan */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

with tab2:  # Titrasi Redoks
    st.markdown("""
    <div style="background-color: rgba(200,200,200,0.8); padding: 10px; border-radius: 5px;">
        <h2 style="color: #2a3f5f;">Titrasi Redoks</h2>
    </div>
    """, unsafe_allow_html=True)
    
    metode_redoks = st.selectbox(
        "Pilih Metode Titrasi Redoks",
        ["Permanganometri", "Iodometri"],
        key="metode_redoks"
    )
    
    if metode_redoks == "Permanganometri":
        st.markdown("""
        ### Permanganometri (Menggunakan KMnO₄)
        - Indikator: Tidak diperlukan, KMnO₄ berfungsi sebagai indikator sendiri
        - Perubahan warna: 
          - Dari ungu (MnO₄⁻) ke tak berwarna (Mn²⁺) dalam suasana asam
          - Dari ungu ke coklat (MnO₂) dalam suasana netral/basa
        - Kondisi Optimal:
          - Suasana asam kuat (H₂SO₄)
          - Suhu 60-70°C untuk beberapa analit
        - Aplikasi: 
          - Penentuan Fe²⁺ 
          - Analisis H₂O₂
          - Penentuan oksalat
        """)
        
    elif metode_redoks == "Iodometri":
        st.markdown("""
        ### Iodometri/Iodimetri
        - Indikator: Larutan kanji 1%
        - Perubahan warna: 
          - Tak berwarna ke biru tua (kompleks I₂-kanji)
        - Kondisi Optimal:
          - pH netral hingga sedikit asam
          - Hindari cahaya langsung
          - Titrasi pada suhu ruang
        - Aplikasi: 
          - Penentuan Cu²⁺
          - Analisis klorin
          - Penentuan sulfit
        """)
        
st.markdown("""
    <style>
    .custom-bg {
        background-color: rgba(255, 255, 255, 0.85);  /* putih transparan */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

with tab3:  # Titrasi Kompleksometri
    st.markdown("""
    <style>
    .text-container {
        background-color: rgba(255, 255, 255, 0.9);  /* Putih transparan (0.9 = hampir solid) */
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .text-container h1, .text-container h2, .text-container h3 {
        font-weight: 800;
        color: #000;
        text-align: center;
    }
    .text-container p {
        font-size: 18px;
        font-weight: 600;
        color: #000;
        text-align: justify;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: rgba(200,200,200,0.8); padding: 10px; border-radius: 5px;">
        <h2 style="color: #2a3f5f;">Titrasi Kompleksometri</h2>
    </div>
    """, unsafe_allow_html=True)
    
    ion_logam = st.selectbox(
        "Pilih Ion Logam yang Dititrasi",
        ["Ca²⁺/Mg²⁺", "Zn²⁺", "Cu²⁺", "Fe³⁺", "Pb²⁺", "Hg²⁺", "Al³⁺", "Ni²⁺", "Co²⁺"],
        key="ion_logam"
    )
    
    if ion_logam == "Ca²⁺/Mg²⁺":
        st.markdown("""
        ### Penentuan Kesadahan Air (Ca²⁺ dan Mg²⁺)
        - Indikator: 
          1. Eriochrome Black T (EBT)
            - Perubahan warna: Merah anggur ke biru
            - Kondisi: pH 10 (buffer NH₃/NH₄Cl)
          2. Calmagite
            - Perubahan warna: Merah ke biru
            - Kondisi: pH 10, lebih stabil dari EBT
        - Titran: EDTA 0.01 M
        - Aplikasi: Analisis kesadahan air
        """)
        
    elif ion_logam == "Zn²⁺":
        st.markdown("""
        ### Penentuan Zn²⁺
        - Indikator: 
          1. Eriochrome Black T (EBT)
            - Perubahan warna: Merah anggur ke biru
            - Kondisi: pH 10
          2. Xylenol Orange
            - Perubahan warna: Merah ke kuning
            - Kondisi: pH 5-6 (buffer asetat)
        - Aplikasi: Analisis seng dalam preparat farmasi
        """)
        
    elif ion_logam == "Cu²⁺":
        st.markdown("""
        ### Penentuan Cu²⁺
        - Indikator: 
          1. PAN [1-(2-Piridilazo)-2-naftol]
            - Perubahan warna: Kuning ke merah
            - Kondisi: pH 2-3 (asam nitrat)
          2. Murexide
            - Perubahan warna: Kuning ke ungu
            - Kondisi: pH 9 (buffer amonia)
        - Aplikasi: Analisis tembaga dalam paduan logam
        """)
        
    elif ion_logam == "Fe³⁺":
        st.markdown("""
        ### Penentuan Fe³⁺
        - Indikator: Sulfosalicylic acid
        - Perubahan warna: Ungu ke kuning
        - Kondisi: pH 1.5-3.0, suhu 50-60°C
        - Aplikasi: Analisis besi dalam bijih mineral
        """)
        
    elif ion_logam in ["Pb²⁺", "Hg²⁺"]:
        st.markdown(f"""
        ### Penentuan {ion_logam}
        - Indikator utama: 
          1. Xylenol Orange
            - Perubahan warna: Merah ke kuning
            - Kondisi: pH 3-6 (buffer asetat)
          2. Dithizone (untuk Hg²⁺)
            - Perubahan warna: Hijau ke merah
            - Kondisi: pH <2 (asam kuat)
        - Aplikasi: Analisis logam berat dalam sampel lingkungan
        """)
        
    else:  # Al³⁺, Ni²⁺, Co²⁺
        st.markdown(f"""
        ### Penentuan {ion_logam}
        - Indikator umum: 
          1. Pyrocatechol Violet
            - Perubahan warna: Biru ke kuning
            - Kondisi: pH 4-6
          2. Eriochrome Cyanine R
            - Perubahan warna: Merah ke biru
            - Kondisi: pH 6-8
        - Aplikasi: Analisis logam dalam paduan dan mineral
        """)
st.markdown("""
    <style>
    .custom-bg {
        background-color: rgba(255, 255, 255, 0.85);  /* putih transparan */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

with tab4:  # Titrasi Pengendapan
    st.markdown("""
    <div style="background-color: rgba(200,200,200,0.8); padding: 10px; border-radius: 5px;">
        <h2 style="color: #2a3f5f;">Titrasi Pengendapan</h2>
    </div>
    """, unsafe_allow_html=True)
    
    metode_pengendapan = st.selectbox(
        "Pilih Metode Titrasi Pengendapan",
        ["Argentometri (Mohr)", "Argentometri (Volhard)", "Argentometri (Fajans)"],
        key="metode_pengendapan"
    )
    
    if metode_pengendapan == "Argentometri (Mohr)":
        st.markdown("""
        ### Metode Mohr (Penentuan Klorida)
        - Indikator: Ion kromat (CrO₄²⁻) 5%
        - Perubahan warna: Kuning ke merah bata (Ag₂CrO₄)
        - Kondisi Optimal:
          - pH netral/sedikit basa (6.5-9.0)
          - Tidak boleh ada amonia
          - Suhu ruang
        - Aplikasi: 
          - Penentuan Cl⁻ dalam air minum
          - Analisis Br⁻ (tidak untuk I⁻ atau SCN⁻)
        """)
        
    elif metode_pengendapan == "Argentometri (Volhard)":
        st.markdown("""
        ### Metode Volhard (Penentuan Halida Tidak Langsung)
        - Indikator: Ion besi(III) (Fe³⁺) sebagai FeNH₄(SO₄)₂
        - Perubahan warna: Tak berwarna ke merah (FeSCN²⁺)
        - Kondisi Optimal:
          - Suasana asam nitrat pekat
          - Titrasi balik dengan SCN⁻
          - Hindari cahaya langsung
        - Aplikasi: 
          - Penentuan Cl⁻, Br⁻, I⁻, SCN⁻
          - Analisis perak dalam paduan
        """)
        
    elif metode_pengendapan == "Argentometri (Fajans)":
        st.markdown("""
        ### Metode Fajans (Indikator Adsorpsi)
        - Indikator: 
          1. Fluorescein
            - Perubahan warna: Hijau kekuningan ke merah muda
          2. Dichlorofluorescein
            - Perubahan warna: Kuning ke merah muda
        - Kondisi Optimal:
          - pH sesuai indikator (5-9)
          - Partikel koloid harus terbentuk
          - Pengadukan konstan
        - Aplikasi: 
          - Penentuan halida dengan endpoint adsorpsi
          - Analisis dengan presisi tinggi
        """)

# Sidebar dengan informasi tambahan
st.markdown("""
    <style>
    .custom-bg {
        background-color: rgba(255, 255, 255, 0.85);  /* putih transparan */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("""
    <div style="background-color: rgba(200,200,200,0.8); padding: 10px; border-radius: 5px;">
        <h3 style="color: #2a3f5f;">Panduan Penggunaan</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    1. Pilih jenis titrasi dari tab menu
    2. Tentukan parameter analisis
    3. Baca rekomendasi indikator
    4. Perhatikan kondisi optimal untuk setiap metode
    """)
    
    st.markdown("""
    <div style="background-color: rgba(200,200,200,0.8); padding: 10px; border-radius: 10px; margin-top: 5px;">
        <h3 style="color: #2a3f5f;">Tips Penting</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - Kalibrasi larutan titran sebelum digunakan
    - Gunakan indikator secukupnya (terlalu banyak dapat mengganggu)
    - Catat perubahan warna dengan cermat
    - Untuk analisis presisi tinggi, gunakan alat bantu seperti pH meter
    """)
    
    st.markdown("""
    <div style="background-color: rgba(200,200,200,0.8); padding: 10px; border-radius: 10px; margin-top: 5px;">
        <h3 style="color: #2a3f5f;">Tentang Aplikasi</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Developer: Kelompok 8  
    lingkup : Praktikum Kimia Analitik
    """)

import streamlit as st

# Judul aplikasi
st.title("Aplikasi Edukasi Titrasi")
st.write("""
Aplikasi ini dirancang untuk membantu pemahaman konsep dasar titrasi secara interaktif. 
Pengguna dapat mempelajari jenis-jenis titrasi, cara kerja, serta simulasi sederhana melalui antarmuka yang user-friendly.
""")

# (Tambahkan konten atau fitur utama aplikasi di sini jika ada)

# Garis pemisah
st.markdown("---")

    # Aplikasi Edukasi Titrasi
    <div class="custom-bg">
     st.markdown("""

        <h4>Aplikasi Edukasi Titrasi</h4>
        <p>
        Aplikasi ini dirancang untuk membantu pemahaman konsep dasar titrasi secara interaktif. 
        Pengguna dapat mempelajari jenis-jenis titrasi, cara kerja, serta simulasi sederhana melalui antarmuka yang user-friendly.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Kelompok dan anggota
    st.markdown("""
    <div class="custom-bg">
        <h4>Kelompok 8</h4>
        <p><b>Nama Anggota:</b></p>
        <ul>
            <li>Afsha Zahira Riyandi (2460311)</li>
            <li>Intan Permata Sari (2460391)</li>
            <li>Muhammad Rayhan (2460443)</li>
            <li>Ramdan Abdul Azis (2460490)</li>
            <li>Yohanna Angelica Lumbanbatu (246....)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab1:  # Titrasi Asam-Basa
    # Tambahkan CSS styling agar semua tulisan memiliki latar putih transparan
    st.markdown("""
    <style>
    .custom-bg {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 20px;
        border-radius: 12px;
        color: #111;
        margin-bottom: 20px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .custom-bg h2, .custom-bg h4, .custom-bg p, .custom-bg li {
        color: #111;
        font-size: 16px;
    }
    .custom-bg h2 {
        font-size: 22px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Bungkus konten dalam background putih
    st.markdown("""
    <div class="custom-bg">
        <h2>Titrasi Asam-Basa</h2>
        <p>Pilih jenis titran dan analit untuk melihat rekomendasi indikator titrasi berdasarkan titik ekuivalen.</p>
    </div>
    """, unsafe_allow_html=True)

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

    # Tambahan: rekomendasi indikator
    st.markdown("""
    <div class="custom-bg">
        <h4>Rekomendasi Indikator</h4>
        <ul>
            <li><b>Asam kuat + Basa kuat:</b> Bromtimol Biru (pH 6.0–7.6)</li>
            <li><b>Asam lemah + Basa kuat:</b> Fenolftalein (pH 8.2–10)</li>
            <li><b>Asam kuat + Basa lemah:</b> Metil Oranye (pH 3.1–4.4)</li>
            <li><b>Asam lemah + Basa lemah:</b> Tidak direkomendasikan – gunakan potensiometri</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Tambahan: deskripsi aplikasi
    st.markdown("""
    <div class="custom-bg">
        <h4>Aplikasi Edukasi Titrasi</h4>
        <p>Aplikasi ini bertujuan untuk memberikan edukasi mengenai pemilihan indikator dalam titrasi asam-basa melalui pendekatan visual dan interaktif.</p>
    </div>
    """, unsafe_allow_html=True)

    # Tambahan: nama kelompok
    st.markdown("""
    <div class="custom-bg">
        <h4>Kelompok 8</h4>
        <ul>
            <li>Afsha Zahira Riyandi (2460311)</li>
            <li>Intan Permata Sari (2460391)</li>
            <li>Muhammad Rayhan (2460443)</li>
            <li>Ramdan Abdul Azis (2460490)</li>
            <li>Yohanna Angelica Lumbanbatu (246....)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


   


