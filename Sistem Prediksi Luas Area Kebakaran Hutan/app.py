import streamlit as st
import joblib
import pandas as pd

# Page
st.set_page_config(page_title="Prediksi Kebakaran Hutan", page_icon="🔥", layout="wide")

# CSS 
st.markdown("""
    <style>
    /* Menggunakan Midnight Blue-Black yang lebih hidup daripada abu-abu standar */
    .stApp {
        background-color: #0b0e14 !important; 
        color: #e0e0e0 !important;
    }
    
    /* Sidebar tetap dengan gradasi yang lebih kontras */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #161b22 0%, #0d1117 100%) !important;
        border-right: 1px solid #30363d;
    }
    
    /* Efek Glow/Nyala pada teks saat di-hover */
    h1:hover, h2:hover, h3:hover, p:hover {
        color: #ffa500 !important; /* Warna oranye bara api saat hover */
        text-shadow: 0 0 8px rgba(255, 165, 0, 0.6);
        transition: all 0.3s ease;
    }

    /* Styling Input agar lebih menonjol di atas latar belakang gelap */
    .stNumberInput input {
        background-color: #1c2128 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        border-radius: 8px;
    }

    /* Tombol dengan warna Oranye Api (Ember) yang ikonik */
    .stButton>button {
        background-color: #d9534f !important; /* Warna merah api yang elegan */
        color: #ffffff !important;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #c9302c !important;
        box-shadow: 0 0 15px rgba(217, 83, 79, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("Informasi Proyek")
    with st.expander("ℹ️ Deskripsi"):
        st.write("Aplikasi prediksi luas area terbakar menggunakan model **Random Forest Regressor**.")
    
    with st.expander("🛠️ Detail Model"):
        st.markdown("""
            - **Model:** Random Forest Regressor
            - **Input:** Parameter Klimatologi
            - **Dataset:**
            [Klik untuk Download (ZIP)](https://archive.ics.uci.edu/static/public/162/forest+fires.zip)
            - **URL Referensi:**
            [UCI Forest Fires Repository](https://archive.ics.uci.edu/dataset/162/forest+fires)
            """)
    
    st.divider()
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p style="font-size: 0.8rem; color: #888;">
            © 2026 Dashboard Analisis Kebakaran<br>
            <b>Franco Xander Adu</b><br>
            2581711008
        </p>
        <img src="https://images.seeklogo.com/logo-png/45/1/universitas-udayana-logo-png_seeklogo-451683.png" 
             width="80" style="margin-top: 10px;">
    </div>
""", unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.title("Sistem Prediksi Luas Kebakaran")
st.markdown("Masukkan parameter cuaca untuk estimasi luas area terbakar.")

with st.form("fire_form"):
    st.subheader("📝 Input Parameter Cuaca")
    col1, col2 = st.columns(2)
    
    with col1:
        temp = st.number_input("🌡️ Suhu (°C)", 0.0, 50.0, 25.0)
        rh = st.number_input("💧 Kelembapan (%)", 0.0, 100.0, 40.0)
        wind = st.number_input("🌬️ Kecepatan Angin (km/h)", 0.0, 30.0, 5.0)
        rain = st.number_input("🌧️ Curah Hujan (mm)", 0.0, 10.0, 0.0)
        
    with col2:
        dmc = st.number_input("🌱 DMC (Kelembapan Tanah)", 0.0, 300.0, 50.0)
        dc = st.number_input("🏜️ DC (Indeks Kekeringan)", 0.0, 900.0, 500.0)
        isi = st.number_input("🔥 ISI (Indeks Penyebaran)", 0.0, 30.0, 5.0)
    
    submit = st.form_submit_button("Analisis", use_container_width=True)

# --- LOGIC ---
# --- LOGIC ---
if submit:
    try:
        model = joblib.load("models/fire_model.pkl")
        feature_names = joblib.load("models/feature_names.pkl")
        
        # 1. Tambahkan Logika Validasi (Hard Constraint)
        # Jika semua input cuaca adalah 0, secara logika luas kebakaran adalah 0.
        if temp == 0 and rh == 0 and wind == 0 and rain == 0 and dmc == 0 and dc == 0 and isi == 0:
            prediction = [0.0]
        else:
            # Jika tidak nol, gunakan model untuk memprediksi
            input_data = pd.DataFrame([[temp, rh, wind, rain, dmc, dc, isi]], columns=feature_names)
            prediction = model.predict(input_data)
        
        st.divider()
        st.subheader("📊 Hasil Prediksi")
        st.metric(label="Estimasi Luas Area Terbakar", value=f"{prediction[0]:.2f} Hektar")
        
        # 2. Opsional: Logika tambahan jika prediksi model terlalu kecil tapi tidak 0
        if prediction[0] < 0.1:
            st.success("✅ Status: Risiko Sangat Rendah / Tidak ada kebakaran.")
        elif prediction[0] > 10:
            st.error("⚠️ Status: Risiko Tinggi! Diperlukan tindakan mitigasi segera.")
        else:
            st.warning("⚠️ Status: Risiko Menengah.")
            
    except Exception as e:
        st.error(f"Error: {e}")