# Django Started API

API sederhana berbasis Django dan Django REST Framework untuk manajemen data User.

## Fitur
- CRUD User (Create, Read, Update, Delete)
- Endpoint khusus untuk mengambil user yang aktif
- Response API sudah distandarisasi

## Model User
| Field      | Tipe Data   | Keterangan         |
|------------|-------------|-------------------|
| name       | CharField   | Nama user         |
| email      | EmailField  | Unik, email user  |
| is_active  | Boolean     | Status aktif      |
| created_at | DateTime    | Tanggal dibuat    |

## Endpoint
Semua endpoint diawali dengan `/api/`

| Method | Endpoint                | Keterangan                |
|--------|------------------------|---------------------------|
| GET    | /api/users/            | List semua user           |
| GET    | /api/users/{id}/       | Detail user berdasarkan id|
| POST   | /api/users/            | Membuat user baru         |
| PUT    | /api/users/{id}/       | Update user               |
| DELETE | /api/users/{id}/       | Hapus user                |
| GET    | /api/users/getactive/  | List user yang aktif      |

## Instalasi & Menjalankan
1. **Clone repository**
   ```bash
   git clone https://github.com/qadrima/django-started-api.git
   cd django-started-api
   ```
2. **Buat virtual environment & install dependencies**
   ```bash
   python -m venv env
   source env/bin/activate  # atau .\env\Scripts\activate di Windows
   pip install -r requirements.txt
   ```
3. **Migrasi database**
   ```bash
   python manage.py migrate
   ```
4. **Jalankan server**
   ```bash
   python manage.py runserver
   ```

## Penggunaan Git
```
git remote add origin https://github.com/qadrima/django-started-api.git
git branch -M main
git push -u origin main
```

## Lisensi
MIT 