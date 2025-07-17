import streamlit as st

# ======================
# Fungsi: Atur background dari gambar di Google Drive
# ======================
def set_background_from_gdrive():
    # ID gambar dari link Google Drive
    gdrive_file_id = "1VeDJMXcCjt5RNg0oXenfdEYLr_O-swRm"
    image_url = f"https://drive.google.com/uc?export=view&id={gdrive_file_id}"
    
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

# ======================
# Terapkan background
# ======================
set_background_from_gdrive()

# ======================
# Konten Aplikasi
# ======================
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.85); padding: 25px; border-radius: 10px;">
    <h1 style="text-align: center; color: #1e3a5f;">🧪 Aplikasi Edukasi Titrasi</h1>
    <p style="text-align: center;">Silakan pilih jenis titrasi untuk melihat indikator yang sesuai</p>
</div>
""", unsafe_allow_html=True)

# Dropdown pilihan jenis titrasi
jenis_titrasi = st.selectbox(
    "🔍 Pilih Jenis Titrasi",
    ["Asam-Basa", "Redoks", "Kompleksometri", "Pengendapan"]
)

# Menampilkan indikator sesuai pilihan
if jenis_titrasi == "Asam-Basa":
    st.success("✅ Rekomendasi indikator: Fenolftalein, Metil Jingga, Biru Bromtimol")
elif jenis_titrasi == "Redoks":
    st.info("ℹ️ Rekomendasi indikator: Kalium Permanganat (sebagai indikator), Kanji (untuk iodometri)")
elif jenis_titrasi == "Kompleksometri":
    st.warning("⚠️ Rekomendasi indikator: Eriochrome Black T, Murexide, Calmagite")
elif jenis_titrasi == "Pengendapan":
    st.error("🚫 Rekomendasi indikator: Kalium Kromat, Fluorescein")

# Footer Aplikasi
st.markdown("""
<br><hr>
<p style="text-align: center; color: gray;">
    Dibuat oleh Tim Edukasi Kimia | © 2025
</p>
""", unsafe_allow_html=True)
