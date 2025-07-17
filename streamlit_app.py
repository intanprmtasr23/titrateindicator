import streamlit as st
import base64
import os

# ========================
# Fungsi background lokal
# ========================
def set_background_from_file(image_file):
    try:
        ext = image_file.split('.')[-1]
        with open(image_file, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/{ext};base64,{encoded}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("File gambar tidak ditemukan.")

# ========================
# Fungsi background Google Drive
# ========================
def set_background_from_gdrive(file_id):
    image_url = f"import streamlit as st
import base64
import os

# ========================
# Fungsi background lokal
# ========================
def set_background_from_file(image_file):
    try:
        ext = image_file.split('.')[-1]
        with open(image_file, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/{ext};base64,{encoded}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("File gambar tidak ditemukan.")

# ========================
# Fungsi background Google Drive
# ========================
def set_background_from_gdrive(file_id):
    image_url = f"https://drive.google.com/uc?export=view&id={file_id}"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ========================
# PILIH SUMBER BACKGROUND
# ========================
st.sidebar.title("🔧 Pengaturan Background")
sumber_bg = st.sidebar.radio("Pilih sumber background:", ["File Lokal", "Google Drive"])

if sumber_bg == "File Lokal":
    bg_path = st.sidebar.text_input("Masukkan nama file (contoh: bg.png):", "titration_bg.png")
    if os.path.exists(bg_path):
        set_background_from_file(bg_path)
    else:
        st.sidebar.warning("File tidak ditemukan. Pastikan file ada di direktori yang sama.")
else:
    gdrive_link = st.sidebar.text_input("Masukkan link Google Drive (file gambar):")
    if "drive.google.com" in gdrive_link:
        # Ambil file ID dari URL Google Drive
        try:
            file_id = gdrive_link.split("/d/")[1].split("/")[0]
            set_background_from_gdrive(file_id)
        except:
            st.sidebar.error("Link Google Drive tidak valid.")
    else:
        st.sidebar.info("Masukkan link berbentuk: https://drive.google.com/file/d/FILE_ID/view")

# ========================
# Konten Aplikasi Utama
# ========================
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.85); padding: 20px; border-radius: 10px;">
    <h1 style="text-align: center; color: #2a3f5f;">🧪 Aplikasi Pemilihan Indikator Titrasi</h1>
    <p style="text-align: center;">Pilih jenis titrasi dan lihat rekomendasi indikator yang sesuai</p>
</div>
""", unsafe_allow_html=True)

# Contoh fitur
jenis_titrasi = st.selectbox("Pilih Jenis Titrasi", ["Asam-Basa", "Redoks", "Kompleksometri", "Pengendapan"])

if jenis_titrasi == "Asam-Basa":
    st.success("Gunakan indikator seperti Fenolftalein, Metil Jingga, dll.")
elif jenis_titrasi == "Redoks":
    st.info("Gunakan indikator KMnO₄ atau larutan kanji.")
elif jenis_titrasi == "Kompleksometri":
    st.warning("Gunakan EBT, Calmagite, atau Murexide.")
elif jenis_titrasi == "Pengendapan":
    st.error("Gunakan indikator seperti Kromat, Fe³⁺, fluorescein, dll.")

st.markdown("<br><br><hr><p style='text-align:center;'>Versi 1.0 | Edukasi Kimia Analitik</p>", unsafe_allow_html=True)
={file_id}"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ========================
# PILIH SUMBER BACKGROUND
# ========================
st.sidebar.title("🔧 Pengaturan Background")
sumber_bg = st.sidebar.radio("Pilih sumber background:", ["File Lokal", "Google Drive"])

if sumber_bg == "File Lokal":
    bg_path = st.sidebar.text_input("Masukkan nama file (contoh: bg.png):", "titration_bg.png")
    if os.path.exists(bg_path):
        set_background_from_file(bg_path)
    else:
        st.sidebar.warning("File tidak ditemukan. Pastikan file ada di direktori yang sama.")
else:
    gdrive_link = st.sidebar.text_input("Masukkan link Google Drive (file gambar):")
    if "drive.google.com" in gdrive_link:
        # Ambil file ID dari URL Google Drive
        try:
            file_id = gdrive_link.split("/d/")[1].split("/")[0]
            set_background_from_gdrive(file_id)
        except:
            st.sidebar.error("Link Google Drive tidak valid.")
    else:
        st.sidebar.info("Masukkan link berbentuk: https://drive.google.com/file/d/FILE_ID/view")

# ========================
# Konten Aplikasi Utama
# ========================
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.85); padding: 20px; border-radius: 10px;">
    <h1 style="text-align: center; color: #2a3f5f;">🧪 Aplikasi Pemilihan Indikator Titrasi</h1>
    <p style="text-align: center;">Pilih jenis titrasi dan lihat rekomendasi indikator yang sesuai</p>
</div>
""", unsafe_allow_html=True)

# Contoh fitur
jenis_titrasi = st.selectbox("Pilih Jenis Titrasi", ["Asam-Basa", "Redoks", "Kompleksometri", "Pengendapan"])

if jenis_titrasi == "Asam-Basa":
    st.success("Gunakan indikator seperti Fenolftalein, Metil Jingga, dll.")
elif jenis_titrasi == "Redoks":
    st.info("Gunakan indikator KMnO₄ atau larutan kanji.")
elif jenis_titrasi == "Kompleksometri":
    st.warning("Gunakan EBT, Calmagite, atau Murexide.")
elif jenis_titrasi == "Pengendapan":
    st.error("Gunakan indikator seperti Kromat, Fe³⁺, fluorescein, dll.")

st.markdown("<br><br><hr><p style='text-align:center;'>Versi 1.0 | Edukasi Kimia Analitik</p>", unsafe_allow_html=True)
