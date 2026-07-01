# 🔥 Prediksi Kebakaran Hutan Menggunakan Machine Learning

## 📖 Deskripsi Proyek
Proyek ini bertujuan membangun model **Machine Learning** untuk memprediksi luas area kebakaran hutan (*burned area*) berdasarkan kondisi cuaca dan karakteristik lingkungan. Model dikembangkan menggunakan algoritma **Random Forest Regressor** dan diimplementasikan ke dalam aplikasi web sederhana menggunakan **Streamlit** sehingga pengguna dapat melakukan prediksi secara interaktif.

---

## 🎯 Tujuan
- Membangun model prediksi luas area kebakaran hutan.
- Menerapkan tahapan Data Mining menggunakan metodologi **CRISP-DM**.
- Mengimplementasikan model Machine Learning ke dalam aplikasi web berbasis Streamlit.
- Menyediakan antarmuka yang mudah digunakan untuk melakukan prediksi.

---

## 🌲 Latar Belakang
Kebakaran hutan merupakan salah satu bencana yang dapat menimbulkan kerugian besar terhadap lingkungan, ekonomi, dan kesehatan masyarakat. Dengan memanfaatkan teknik **Data Mining** dan **Machine Learning**, pola dari data historis kebakaran hutan dapat dipelajari sehingga model mampu memperkirakan luas area yang berpotensi terbakar berdasarkan kondisi tertentu.

---

## 📊 Dataset

| Informasi | Keterangan |
|-----------|------------|
| Dataset | Forest Fires Dataset |
| Sumber | https://archive.ics.uci.edu/dataset/162/forest+fires |
| Jumlah Data | 517 data |
| Jumlah Fitur | 9 fitur |
| Target | Area (luas area kebakaran) |

### Fitur yang digunakan
- X
- Y
- FFMC
- DMC
- DC
- ISI
- Temperature
- Relative Humidity (RH)
- Wind
- Rain

---

## ⚙️ Metodologi

Pengembangan sistem mengikuti metodologi **CRISP-DM** yang terdiri dari:

1. **Business Understanding**
   - Menentukan tujuan penelitian dan kebutuhan sistem.

2. **Data Understanding**
   - Memahami karakteristik dataset serta melakukan eksplorasi data.

3. **Data Preparation**
   - Membersihkan data.
   - Encoding data kategorikal.
   - Seleksi fitur.
   - Pembagian data training dan testing.

4. **Modeling**
   - Membangun model menggunakan **Random Forest Regressor**.

5. **Evaluation**
   - Mengevaluasi performa model menggunakan metrik regresi.

6. **Deployment**
   - Mengimplementasikan model ke dalam aplikasi web menggunakan Streamlit.

---

## 🤖 Algoritma Machine Learning

Model yang digunakan adalah **Random Forest Regressor**.

### Alasan Pemilihan
Random Forest Regressor dipilih karena:
- Cocok untuk permasalahan prediksi nilai numerik (regresi).
- Mampu menangani hubungan non-linear antar variabel.
- Mengurangi risiko overfitting melalui kombinasi banyak decision tree.
- Memberikan performa yang stabil pada dataset berukuran kecil hingga menengah.

---

## 📈 Evaluasi Model

Evaluasi model dilakukan menggunakan metrik regresi, seperti:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score (Coefficient of Determination)

> **Catatan:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix, dan ROC-AUC merupakan metrik untuk klasifikasi sehingga tidak digunakan pada proyek regresi ini.

---

## 💻 Implementasi Aplikasi

Aplikasi dikembangkan menggunakan **Streamlit** dengan fitur sebagai berikut:

- Input parameter kondisi cuaca
- Prediksi luas area kebakaran
- Menampilkan hasil prediksi
- Tampilan sederhana dan mudah digunakan

---

## 📁 Struktur Folder

```
project/
│
├── app.py
├── model.pkl
├── preprocessing.pkl
├── requirements.txt
├── dataset.csv
├── README.md
│
└── images/
    ├── home.png
    ├── prediction.png
    └── result.png
```

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/username/nama-repository.git
```

### 2. Masuk ke Folder Project

```bash
cd nama-repository
```

### 3. Buat dan Aktifkan Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Library Joblib

Apabila library **joblib** belum terinstal, jalankan perintah berikut:

```bash
pip install joblib
```

### 6. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan berjalan dan dapat diakses melalui browser pada alamat berikut:

```text
http://localhost:8501
```
## 🖼️ Tampilan Aplikasi

### Halaman Utama

<img width="1917" height="1027" alt="image" src="https://github.com/user-attachments/assets/634da147-e8d2-4f4b-84f3-395266930d06" />

### Halaman Prediksi

<img width="1518" height="621" alt="image" src="https://github.com/user-attachments/assets/ff7e2857-bf28-47ca-9ba9-78b5279b3b4d" />

### Hasil Prediksi

<img width="1917" height="1027" alt="image" src="https://github.com/user-attachments/assets/61ad20af-0425-4ada-a4e4-cf835832905c" />

---

## 🛠️ Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib
- Matplotlib

---

## 👨‍💻 Penulis

**Franco Xander Adu**

NIM : **2581711008**

Program Studi Magister Manajemen Sistem Informasi dan Komputer

Universitas Udayana

Mata Kuliah **Manajemen Data**

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran pada mata kuliah **Manajemen Data**.
