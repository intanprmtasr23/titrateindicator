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
 
# CSS untuk mempercantik tampilan dan menambahkan latar belakang putih
st.markdown("""
<style>
/* Mengatur warna teks untuk semua elemen */
body, .stApp, .stMarkdown, .stText, .stAlert, .stSelectbox, .stSlider, .stExpander, .stTabs, h1, h2, h3, h4, h5, h6, p, li {
    color: #333333 !important; /* Warna teks lebih gelap untuk kontras */
}

/* Latar belakang putih untuk area utama konten */
.stApp > header {
    background-color: rgba(255, 255, 255, 0.8) !important; /* Latar belakang putih transparan untuk header Streamlit */
    border-radius: 10px;
    margin-bottom: 20px;
}

.stApp > div:first-child > div:nth-child(3) {
    background-color: rgba(255, 255, 255, 0.8); /* Latar belakang putih transparan untuk konten utama */
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
}

/* Latar belakang putih untuk sidebar */
.stSidebar > div:first-child {
    background-color: rgba(255, 255, 255, 0.8); /* Latar belakang putih transparan untuk sidebar */
    padding: 20px;
    border-radius: 10px;
}

/* Memperjelas teks di expander */
div[data-testid="stExpander"] div[role="button"] p {
    font-size: 18px;
    font-weight: bold;
    color: #2a3f5f !important; /* Warna asli untuk judul expander */
}

/* Latar belakang untuk elemen yang sudah ada (misal: kotak judul) */
.css-1aumxhk {
    background-color: rgba(255, 255, 255, 0.8) !important; /* Mengubah warna menjadi putih transparan */
    border-radius: 20px;
    padding: 20px;
}

/* Latar belakang untuk div judul dan tab */
div[style*="background-color: rgba(200,200,200,0.8)"] {
    background-color: rgba(255, 255, 255, 0.8) !important; /* Mengubah warna menjadi putih transparan */
    border-radius: 10px;
    padding: 20px;
}

/* Menyesuaikan warna teks di dalam div dengan latar belakang putih */
div[style*="background-color: rgba(255, 255, 255, 0.8)"] h1,
div[style*="background-color: rgba(255, 255, 255, 0.8)"] h2,
div[style*="background-color: rgba(255, 255, 255, 0.8)"] h3,
div[style*="background-color: rgba(255, 255, 255, 0.8)"] p,
div[style*="background-color: rgba(255, 255, 255, 0.8)"] li {
    color: #2a3f5f !important; /* Warna teks yang jelas untuk judul dan paragraf */
}

/* Memastikan teks di dalam tab juga jelas */
.stTabs [data-testid="stMarkdownContainer"] p {
    color: #333333 !important;
}

/* Memastikan teks pada judul tab menjadi putih dan tebal */
.stTabs [data-testid="stTab"] p {
    color: white !important;
    font-weight: bold !important;
}

/* Memastikan teks pada judul tab yang aktif menjadi putih dan tebal */
.stTabs [data-testid="stTab"] button[aria-selected="true"] p {
    color: white !important;
    font-weight: bold !important;
}

/* Memastikan teks pada label selectbox dan slider menjadi putih dan tebal */
.stSelectbox label, .stSlider label {
    color: white !important;
    font-weight: bold !important;
}

</style>
""", unsafe_allow_html=True)
 
# Judul aplikasi dengan style
st.markdown("""
<div style="background-color: rgba(255,255,255,0.8);
padding: 20px; border-radius: 10px;">
    <h1 style="color: #2a3f5f; text-align: center;">🧪 Aplikasi Pemilihan Indikator Titrasi</h1>
    <p style="text-align: center;">Pilih indikator yang sesuai untuk berbagai jenis titrasi analitik</p>
</div>
""", unsafe_allow_html=True)
 
# Tab untuk berbagai jenis titrasi
tab1, tab2, tab3, tab4 = st.tabs([
    "Asam-Basa", 
    "Redoks", 
    "Kompleksometri", 
    "Pengendapan"
])
 
with tab1:  # Titrasi Asam-Basa
    # Menambahkan div dengan latar belakang untuk seluruh konten tab
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 20px; border-radius: 10px;">
        <h2 style="color: #2a3f5f;">Titrasi Asam-Basa</h2>
    """, unsafe_allow_html=True) # Start div for tab content
    
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
    if ("Asam Kuat" in jenis_titran and "Basa Kuat" in jenis_analit) or \
       ("Basa Kuat" in jenis_titran and "Asam Kuat" in jenis_analit):
        pH_eq = 7.0
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <p style="color: #333333;">Titik ekuivalen pada pH 7.0 (netral)</p>
        </div>
        """, unsafe_allow_html=True)
    elif ("Asam Kuat" in jenis_titran and "Basa Lemah" in jenis_analit):
        pH_eq = st.slider("Perkiraan pH titik ekuivalen", 3.0, 6.5, 5.0, 0.1)
    elif ("Basa Kuat" in jenis_titran and "Asam Lemah" in jenis_analit):
        pH_eq = st.slider("Perkiraan pH titik ekuivalen", 7.5, 11.0, 8.5, 0.1)
    else:
        pH_eq = st.slider("Perkiraan pH titik ekuivalen", 3.0, 11.0, 7.0, 0.1)
        # Menambahkan latar belakang oranye dan teks tebal hitam untuk peringatan
        st.markdown(f"""
        <div style="background-color: rgba(255, 165, 0, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <p style="color: #000000; font-weight: bold;">Titrasi antara asam lemah dan basa lemah umumnya tidak direkomendasikan</p>
        </div>
        """, unsafe_allow_html=True)
    
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
    <div style="background-color: rgba(255,255,255,0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
        <h3 style="color: #2a3f5f;">Rekomendasi Indikator</h3>
    </div>
    """, unsafe_allow_html=True)
    
    rec_indicators = []
    
    for name, data in indikator_ab.items():
        low, high = data["rentang"]
        if low <= pH_eq <= high:
            rec_indicators.append((name, low, high, data["perubahan"], data["aplikasi"]))
    
    if rec_indicators:
        # Menghapus latar belakang biru muda dari teks "Indikator yang sesuai..."
        st.markdown(f"""
        <div style="padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <p style="color: #333333;">Indikator yang sesuai untuk pH titik ekuivalen {pH_eq:.1f}:</p>
        </div>
        """, unsafe_allow_html=True)
        for name, low, high, change, app in rec_indicators:
            # Menggunakan st.expander untuk setiap indikator
            with st.expander(f"{name}: pH {low}-{high} ({change})"):
                # Konten di dalam expander dengan latar belakang biru muda dan teks jelas
                st.markdown(f"""
                <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px;">
                    <p style="color: #FFFFFF; font-weight: bold;">Perubahan Warna: {change}</p>
                    <p style="color: #FFFFFF; font-weight: bold;">Aplikasi Khas: {app}</p>
                    <p style="color: #FFFFFF; font-weight: bold;">Rentang pH: {low} - {high}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <p style="color: #FF4B4B;">Tidak ditemukan indikator yang cocok. Pertimbangkan penggunaan pH meter.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True) # End div for tab content

with tab2:  # Titrasi Redoks
    # Menambahkan div dengan latar belakang untuk seluruh konten tab
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 20px; border-radius: 10px;">
        <h2 style="color: #2a3f5f;">Titrasi Redoks</h2>
    """, unsafe_allow_html=True) # Start div for tab content
    
    metode_redoks = st.selectbox(
        "Pilih Metode Titrasi Redoks",
        ["Permanganometri", "Iodometri"],
        key="metode_redoks"
    )
    
    if metode_redoks == "Permanganometri":
        st.markdown("""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Permanganometri (Menggunakan KMnO₄)</h3>
            <p style="color: #333333;"><b>- Indikator:</b> Tidak diperlukan, KMnO₄ berfungsi sebagai indikator sendiri</p>
            <p style="color: #333333;"><b>- Perubahan warna:</b></p>
            <ul style="color: #333333;">
              <li>Dari ungu (MnO₄⁻) ke tak berwarna (Mn²⁺) dalam suasana asam</li>
              <li>Dari ungu ke coklat (MnO₂) dalam suasana netral/basa</li>
            </ul>
            <p style="color: #333333;"><b>- Kondisi Optimal:</b></p>
            <ul style="color: #333333;">
              <li>Suasana asam kuat (H₂SO₄)</li>
              <li>Suhu 60-70°C untuk beberapa analit</li>
            </ul>
            <p style="color: #333333;"><b>- Aplikasi:</b></p>
            <ul style="color: #333333;">
              <li>Penentuan Fe²⁺</li>
              <li>Analisis H₂O₂</li>
              <li>Penentuan oksalat</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif metode_redoks == "Iodometri":
        st.markdown("""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Iodometri/Iodimetri</h3>
            <p style="color: #333333;"><b>- Indikator:</b> Larutan kanji 1%</p>
            <p style="color: #333333;"><b>- Perubahan warna:</b></p>
            <ul style="color: #333333;">
              <li>Tak berwarna ke biru tua (kompleks I₂-kanji)</li>
            </ul>
            <p style="color: #333333;"><b>- Kondisi Optimal:</b></p>
            <ul style="color: #333333;">
              <li>pH netral hingga sedikit asam</li>
              <li>Hindari cahaya langsung</li>
              <li>Titrasi pada suhu ruang</li>
            </ul>
            <p style="color: #333333;"><b>- Aplikasi:</b></p>
            <ul style="color: #333333;">
              <li>Penentuan Cu²⁺</li>
              <li>Analisis klorin</li>
              <li>Penentuan sulfit</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True) # End div for tab content

with tab3:  # Titrasi Kompleksometri
    # Menambahkan div dengan latar belakang untuk seluruh konten tab
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 20px; border-radius: 10px;">
        <h2 style="color: #2a3f5f;">Titrasi Kompleksometri</h2>
    """, unsafe_allow_html=True) # Start div for tab content
    
    ion_logam = st.selectbox(
        "Pilih Ion Logam yang Dititrasi",
        ["Ca²⁺/Mg²⁺", "Zn²⁺", "Cu²⁺", "Fe³⁺", "Pb²⁺", "Hg²⁺", "Al³⁺", "Ni²⁺", "Co²⁺"],
        key="ion_logam"
    )
    
    if ion_logam == "Ca²⁺/Mg²⁺":
        st.markdown("""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Penentuan Kesadahan Air (Ca²⁺ dan Mg²⁺)</h3>
            <p style="color: #333333;"><b>- Indikator:</b></p>
            <ul style="color: #333333;">
              <li>1. Eriochrome Black T (EBT)</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Merah anggur ke biru</li>
                <li>Kondisi: pH 10 (buffer NH₃/NH₄Cl)</li>
              </ul>
              <li>2. Calmagite</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Merah ke biru</li>
                <li>Kondisi: pH 10, lebih stabil dari EBT</li>
              </ul>
            </ul>
            <p style="color: #333333;"><b>- Titran:</b> EDTA 0.01 M</p>
            <p style="color: #333333;"><b>- Aplikasi:</b> Analisis kesadahan air</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif ion_logam == "Zn²⁺":
        st.markdown("""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Penentuan Zn²⁺</h3>
            <p style="color: #333333;"><b>- Indikator:</b></p>
            <ul style="color: #333333;">
              <li>1. Eriochrome Black T (EBT)</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Merah anggur ke biru</li>
                <li>Kondisi: pH 10</li>
              </ul>
              <li>2. Xylenol Orange</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Merah ke kuning</li>
                <li>Kondisi: pH 5-6 (buffer asetat)</li>
              </ul>
            </ul>
            <p style="color: #333333;"><b>- Aplikasi:</b> Analisis seng dalam preparat farmasi</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif ion_logam == "Cu²⁺":
        st.markdown("""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Penentuan Cu²⁺</h3>
            <p style="color: #333333;"><b>- Indikator:</b></p>
            <ul style="color: #333333;">
              <li>1. PAN [1-(2-Piridilazo)-2-naftol]</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Kuning ke merah</li>
                <li>Kondisi: pH 2-3 (asam nitrat)</li>
              </ul>
              <li>2. Murexide</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Kuning ke ungu</li>
                <li>Kondisi: pH 9 (buffer amonia)</li>
              </ul>
            </ul>
            <p style="color: #333333;"><b>- Aplikasi:</b> Analisis tembaga dalam paduan logam</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif ion_logam == "Fe³⁺":
        st.markdown("""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Penentuan Fe³⁺</h3>
            <p style="color: #333333;"><b>- Indikator:</b> Sulfosalicylic acid</p>
            <p style="color: #333333;"><b>- Perubahan warna:</b> Ungu ke kuning</p>
            <p style="color: #333333;"><b>- Kondisi:</b> pH 1.5-3.0, suhu 50-60°C</p>
            <p style="color: #333333;"><b>- Aplikasi:</b> Analisis besi dalam bijih mineral</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif ion_logam in ["Pb²⁺", "Hg²⁺"]:
        st.markdown(f"""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Penentuan {ion_logam}</h3>
            <p style="color: #333333;"><b>- Indikator utama:</b></p>
            <ul style="color: #333333;">
              <li>1. Xylenol Orange</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Merah ke kuning</li>
                <li>Kondisi: pH 3-6 (buffer asetat)</li>
              </ul>
              <li>2. Dithizone (untuk Hg²⁺)</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Hijau ke merah</li>
                <li>Kondisi: pH &lt;2 (asam kuat)</li>
              </ul>
            </ul>
            <p style="color: #333333;"><b>- Aplikasi:</b> Analisis logam berat dalam sampel lingkungan</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:  # Al³⁺, Ni²⁺, Co²⁺
        st.markdown(f"""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Penentuan {ion_logam}</h3>
            <p style="color: #333333;"><b>- Indikator umum:</b></p>
            <ul style="color: #333333;">
              <li>1. Pyrocatechol Violet</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Biru ke kuning</li>
                <li>Kondisi: pH 4-6</li>
              </ul>
              <li>2. Eriochrome Cyanine R</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Merah ke biru</li>
                <li>Kondisi: pH 6-8</li>
              </ul>
            </ul>
            <p style="color: #333333;"><b>- Aplikasi:</b> Analisis logam dalam paduan dan mineral</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True) # End div for tab content

with tab4:  # Titrasi Pengendapan
    # Menambahkan div dengan latar belakang untuk seluruh konten tab
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 20px; border-radius: 10px;">
        <h2 style="color: #2a3f5f;">Titrasi Pengendapan</h2>
    """, unsafe_allow_html=True) # Start div for tab content
    
    metode_pengendapan = st.selectbox(
        "Pilih Metode Titrasi Pengendapan",
        ["Argentometri (Mohr)", "Argentometri (Volhard)", "Argentometri (Fajans)"],
        key="metode_pengendapan"
    )
    
    if metode_pengendapan == "Argentometri (Mohr)":
        st.markdown("""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Metode Mohr (Penentuan Klorida)</h3>
            <p style="color: #333333;"><b>- Indikator:</b> Ion kromat (CrO₄²⁻) 5%</p>
            <p style="color: #333333;"><b>- Perubahan warna:</b> Kuning ke merah bata (Ag₂CrO₄)</p>
            <p style="color: #333333;"><b>- Kondisi Optimal:</b></p>
            <ul style="color: #333333;">
              <li>pH netral/sedikit basa (6.5-9.0)</li>
              <li>Tidak boleh ada amonia</li>
              <li>Suhu ruang</li>
            </ul>
            <p style="color: #333333;"><b>- Aplikasi:</b></p>
            <ul style="color: #333333;">
              <li>Penentuan Cl⁻ dalam air minum</li>
              <li>Analisis Br⁻ (tidak untuk I⁻ atau SCN⁻)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif metode_pengendapan == "Argentometri (Volhard)":
        st.markdown("""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Metode Volhard (Penentuan Halida Tidak Langsung)</h3>
            <p style="color: #333333;"><b>- Indikator:</b> Ion besi(III) (Fe³⁺) sebagai FeNH₄(SO₄)₂</p>
            <p style="color: #333333;"><b>- Perubahan warna:</b> Tak berwarna ke merah (FeSCN²⁺)</p>
            <p style="color: #333333;"><b>- Kondisi Optimal:</b></p>
            <ul style="color: #333333;">
              <li>Suasana asam nitrat pekat</li>
              <li>Titrasi balik dengan SCN⁻</li>
              <li>Hindari cahaya langsung</li>
            </ul>
            <p style="color: #333333;"><b>- Aplikasi:</b></p>
            <ul style="color: #333333;">
              <li>Penentuan Cl⁻, Br⁻, I⁻, SCN⁻</li>
              <li>Analisis perak dalam paduan</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif metode_pengendapan == "Argentometri (Fajans)":
        st.markdown("""
        <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="color: #333333;">Metode Fajans (Indikator Adsorpsi)</h3>
            <p style="color: #333333;"><b>- Indikator:</b></p>
            <ul style="color: #333333;">
              <li>1. Fluorescein</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Hijau kekuningan ke merah muda</li>
              </ul>
              <li>2. Dichlorofluorescein</li>
              <ul style="color: #333333;">
                <li>Perubahan warna: Kuning ke merah muda</li>
              </ul>
            </ul>
            <p style="color: #333333;"><b>- Kondisi Optimal:</b></p>
            <ul style="color: #333333;">
              <li>pH sesuai indikator (5-9)</li>
              <li>Partikel koloid harus terbentuk</li>
              <li>Pengadukan konstan</li>
            </ul>
            <p style="color: #333333;"><b>- Aplikasi:</b></p>
            <ul style="color: #333333;">
              <li>Penentuan halida dengan endpoint adsorpsi</li>
              <li>Analisis dengan presisi tinggi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True) # End div for tab content
 
# Sidebar dengan informasi tambahan
with st.sidebar:
    st.markdown("""
    <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 5px;">
        <h3 style="color: #333333;">Panduan Penggunaan</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 10px; border-radius: 5px;">
    <p style="color: #333333;">1. Pilih jenis titrasi dari tab menu</p>
    <p style="color: #333333;">2. Tentukan parameter analisis</p>
    <p style="color: #333333;">3. Baca rekomendasi indikator</p>
    <p style="color: #333333;">4. Perhatikan kondisi optimal untuk setiap metode</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 10px; margin-top: 5px;">
        <h3 style="color: #333333;">Tips Penting</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 10px; border-radius: 5px;">
    <p style="color: #333333;">- Kalibrasi larutan titran sebelum digunakan</p>
    <p style="color: #333333;">- Gunakan indikator secukupnya (terlalu banyak dapat mengganggu)</p>
    <p style="color: #333333;">- Catat perubahan warna dengan cermat</p>
    <p style="color: #333333;">- Untuk analisis presisi tinggi, gunakan alat bantu seperti pH meter</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(173, 216, 230, 0.8); padding: 10px; border-radius: 10px; margin-top: 5px;">
        <h3 style="color: #333333;">Tentang Aplikasi</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="padding: 10px; border-radius: 5px;">
    <p style="color: #333333;">Developer: Kelompok 8</p> 
    <p style="color: #333333;">Lingkup: Praktikum Kimia Analitik</p>
    </div>
    """, unsafe_allow_html=True)
 
# Judul aplikasi di bagian bawah (diperbarui dengan latar belakang putih)
st.markdown("""
<div style="background-color: rgba(255,255,255,0.8); padding: 20px; border-radius: 10px; margin-top: 20px;">
    <h1 style="color: #2a3f5f;">Aplikasi Edukasi Titrasi</h1>
    <p>Aplikasi ini dirancang untuk membantu pemahaman konsep dasar titrasi secara interaktif. Pengguna dapat mempelajari jenis-jenis titrasi, cara kerja, serta simulasi sederhana melalui antarmuka yang user-friendly.</p>
</div>
""", unsafe_allow_html=True)
 
# Garis pemisah
st.markdown("---")
 
# Nama kelompok di bagian bawah (diperbarui dengan latar belakang putih)
st.markdown("""
<div style="background-color: rgba(255,255,255,0.8); padding: 20px; border-radius: 10px; margin-top: 20px;">
    <h2 style="color: #2a3f5f;">Kelompok 8</h2>
    <p><b>Nama Anggota:</b></p>
    <ul>
        <li>Afsha Zahira Riyandi – 2460311</li>
        <li>Intan Permata Sari – 2460391</li>
        <li>Muhammad Rayhan – 2460443</li>
        <li>Ramdan Abdul Azis – 2460490</li>
        <li>Yohana Angelica Lumbanbatu – 2460539</li>
    </ul>
</div>
""", unsafe_allow_html=True)
