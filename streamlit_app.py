import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def main():
    st.title("Pemilihan Indikator Titrasi")
    st.write("Aplikasi ini membantu memilih indikator yang sesuai untuk berbagai jenis titrasi.")
    
    # Sidebar untuk memilih jenis titrasi
    titrasi_type = st.sidebar.selectbox(
        "Pilih Jenis Titrasi",
        ["Asam-Basa", "Redoks", "Kompleksometri", "Pengendapan"]
    )
    
    if titrasi_type == "Asam-Basa":
        st.header("Titrasi Asam-Basa")
        
        # Input parameter
        col1, col2 = st.columns(2)
        with col1:
            asam_type = st.radio("Jenis Asam", ["Kuat", "Lemah"])
        with col2:
            basa_type = st.radio("Jenis Basa", ["Kuat", "Lemah"])
        
        # Menentukan pH titik ekuivalen
        if asam_type == "Kuat" and basa_type == "Kuat":
            pH_equiv = 7.0
            st.success("Titik ekuivalen pada pH 7.0 (netral)")
        elif asam_type == "Kuat" and basa_type == "Lemah":
            pH_equiv = st.slider("Perkiraan pH titik ekuivalen (asam kuat-basa lemah)", 3.0, 7.0, 5.0)
        elif asam_type == "Lemah" and basa_type == "Kuat":
            pH_equiv = st.slider("Perkiraan pH titik ekuivalen (asam lemah-basa kuat)", 7.0, 11.0, 9.0)
        else:
            pH_equiv = st.slider("Perkiraan pH titik ekuivalen (asam lemah-basa lemah)", 3.0, 11.0, 7.0)
            st.warning("Titrasi asam lemah-basa lemah umumnya tidak direkomendasikan karena titik akhir tidak tajam")
        
        # Daftar indikator asam-basa
        indicators = {
            "Metil Merah": (4.2, 6.3, "Merah ke Kuning"),
            "Bromtimol Biru": (6.0, 7.6, "Kuning ke Biru"),
            "Fenolftalein": (8.3, 10.0, "Tak berwarna ke Merah muda"),
            "Metil Jingga": (3.1, 4.4, "Merah ke Jingga"),
            "Bromkresol Hijau": (3.8, 5.4, "Kuning ke Biru"),
            "Fenol Merah": (6.8, 8.4, "Kuning ke Merah")
        }
        
        # Rekomendasi indikator
        st.subheader("Rekomendasi Indikator")
        recommended = []
        for name, (low, high, color_change) in indicators.items():
            if low <= pH_equiv <= high:
                recommended.append((name, low, high, color_change))
        
        if recommended:
            st.write("Indikator yang sesuai untuk rentang pH titik ekuivalen Anda:")
            for name, low, high, color_change in recommended:
                st.info(f"{name}: pH {low}-{high} ({color_change})")
        else:
            st.error("Tidak ditemukan indikator yang cocok untuk pH titik ekuivalen ini. Pertimbangkan untuk menggunakan pH meter.")
        
        # Visualisasi kurva titrasi dan indikator
        st.subheader("Visualisasi Kurva Titrasi dan Indikator")
        fig, ax = plt.subplots()
        
        # Generate kurva titrasi sederhana
        if asam_type == "Kuat" and basa_type == "Kuat":
            x = np.linspace(0, 14, 100)
            y = np.where(x < 7, 1/(1 + np.exp(-(x-7)*5)), 1/(1 + np.exp(-(x-7)*5)))
            ax.plot(x, y, label="Kurva Titrasi")
            ax.axvline(x=7, color='r', linestyle='--', label='Titik Ekuivalen')
        else:
            x = np.linspace(0, 14, 100)
            if asam_type == "Kuat" and basa_type == "Lemah":
                y = 1/(1 + np.exp(-(x-pH_equiv)*3))
            else:
                y = 1/(1 + np.exp(-(x-pH_equiv)*3))
            ax.plot(x, y, label="Kurva Titrasi")
            ax.axvline(x=pH_equiv, color='r', linestyle='--', label='Titik Ekuivalen')
        
        # Tambahkan rentang indikator
        for name, low, high, _ in indicators.items():
            if name in [ind[0] for ind in recommended]:
                ax.axvspan(low, high, alpha=0.2, color='green')
            else:
                ax.axvspan(low, high, alpha=0.1, color='gray')
        
        ax.set_xlabel("pH")
        ax.set_ylabel("Fraksi Titran")
        ax.set_title("Kurva Titrasi dan Rentang Indikator")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
    elif titrasi_type == "Redoks":
        st.header("Titrasi Redoks")
        st.write("""
        Untuk titrasi redoks, indikator yang digunakan biasanya:
        1. *Indikator spesifik*: Bereaksi dengan salah satu reaktan
        2. *Indikator redoks umum*: Berubah warna tergantung potensial sistem
        """)
        
        redoks_type = st.selectbox(
            "Pilih Jenis Titrasi Redoks",
            ["Permanganometri", "Iodometri", "Dikromatometri", "Serimetri"]
        )
        
        if redoks_type == "Permanganometri":
            st.success("""
            *Indikator*: Tidak diperlukan, KMnO4 berfungsi sebagai indikator sendiri
            *Perubahan warna*: Ungu ke tak berwarna/tak berwarna ke merah muda
            """)
        elif redoks_type == "Iodometri":
            st.success("""
            *Indikator*: Kanji
            *Perubahan warna*: Tak berwarna ke biru tua
            """)
        elif redoks_type == "Dikromatometri":
            st.success("""
            *Indikator*: Difenilamin sulfonat atau Ferroin
            *Perubahan warna*: 
            - Difenilamin sulfonat: Ungu ke hijau
            - Ferroin: Merah ke biru pucat
            """)
        else:
            st.success("""
            *Indikator*: Ferroin
            *Perubahan warna*: Merah ke biru pucat
            """)
        
    elif titrasi_type == "Kompleksometri":
        st.header("Titrasi Kompleksometri")
        st.write("""
        Untuk titrasi kompleksometri (seperti titrasi EDTA), indikator yang umum digunakan adalah:
        """)
        
        metal = st.selectbox(
            "Pilih Ion Logam yang Dititrasi",
            ["Ca²⁺/Mg²⁺ (air sadah)", "Zn²⁺", "Cu²⁺", "Fe³⁺", "Pb²⁺"]
        )
        
        if metal == "Ca²⁺/Mg²⁺ (air sadah)":
            st.success("""
            *Indikator*: Eriochrome Black T (EBT)
            *Perubahan warna*: Merah anggur ke biru
            *Kondisi pH*: 10 (buffer NH₃/NH₄Cl)
            """)
        elif metal == "Zn²⁺":
            st.success("""
            *Indikator*: Eriochrome Black T (EBT) atau Murexide
            *Perubahan warna*: 
            - EBT: Merah anggur ke biru
            - Murexide: Merah ke ungu
            """)
        elif metal == "Cu²⁺":
            st.success("""
            *Indikator*: Murexide atau PAN
            *Perubahan warna*: 
            - Murexide: Kuning ke ungu
            - PAN: Kuning ke merah
            """)
        else:
            st.success("""
            *Indikator*: Bergantung pada logam, umumnya EBT, Murexide, atau Xylenol Orange
            *Kondisi pH*: Sesuai dengan logam yang dititrasi
            """)
        
    else:  # Pengendapan
        st.header("Titrasi Pengendapan")
        st.write("""
        Untuk titrasi pengendapan (seperti argentometri), indikator yang umum digunakan adalah:
        """)
        
        method = st.selectbox(
            "Pilih Metode Argentometri",
            ["Mohr", "Volhard", "Fajans"]
        )
        
        if method == "Mohr":
            st.success("""
            *Indikator*: Kromat (CrO₄²⁻)
            *Perubahan warna*: Kuning ke merah bata (Ag₂CrO₄)
            *Aplikasi*: Penentuan Cl⁻ atau Br⁻ dalam suasana netral/sedikit basa
            """)
        elif method == "Volhard":
            st.success("""
            *Indikator*: Besi(III) (Fe³⁺)
            *Perubahan warna*: Tak berwarna ke merah (FeSCN²⁺)
            *Aplikasi*: Penentuan halida dalam suasana asam
            """)
        else:  # Fajans
            st.success("""
            *Indikator*: Adsorpsi seperti fluorescein atau dichlorofluorescein
            *Perubahan warna*: Hijau kekuningan ke merah muda
            *Aplikasi*: Penentuan halida dengan endpoint adsorpsi
            """)
    
    # Tambahan informasi umum
    st.sidebar.markdown("### Informasi Umum")
    st.sidebar.info("""
    - *Indikator yang baik* memiliki perubahan warna yang tajam di sekitar titik ekuivalen
    - Warna perubahan harus mudah dibedakan
    - Jumlah indikator harus secukupnya (tidak terlalu banyak atau sedikit)
    """)

if _name_ == "_main_":
    main()



