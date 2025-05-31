# Django Started API

API sederhana berbasis Django dan Django REST Framework untuk manajemen data User.

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

## Lisensi
MIT 