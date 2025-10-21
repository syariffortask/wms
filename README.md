# 🚀 WMS Backend

Backend project untuk **Warehouse Management System (WMS)** yang dibangun menggunakan **FastAPI**, **PostgreSQL**, dan **uv** sebagai package & environment manager.

---

## 🧰 Prasyarat

Sebelum memulai, pastikan kamu sudah menginstal:

1. **Python** (versi 3.10 ke atas direkomendasikan)  
   👉 [Download Python](https://www.python.org/downloads/)
2. **PostgreSQL** (sudah terinstal dan berjalan)  
   👉 [Download PostgreSQL](https://www.postgresql.org/download/)
3. **uv** – alat untuk sinkronisasi dependensi  
   Jalankan perintah berikut:
   ```bash
   pip install uv
   ```


## 🧩 Langkah Instalasi
1. **Clone** Repository  
   ```
   git clone https://github.com/syariffortask/wms.git
   cd wms
   ```
2. **Sync** dependensi  
   ```
   uv sync
   ```
3. **Environment**  konfigurasi
   ```
   cp .env.example .env
   ```
4. **DB_URL**  Sesuaikan
    sesuikan dengan DB yang di buat
   ```
   DB_URL=postgresql://username:password@localhost:5432/mydatabase

   ```
5. **🗄️ Migrasi Database**  database

   ```
   uv run alembic upgrade head

   ```
6. **🌱 Seeder Data Awal**
   ```
   uv run manage.py seed

   ```
7. **🏃 Jalankan Aplikasi**
   ```
   uv run fastapi run

   ```
   aplikasi akan jalan di port 8000

