# Kurulum

Postgres

```bash
docker-compose up -d
```

backend

```bash

cd backend
python -m venv .backend
.backend/Scripts/activate

pip install -r requirements.txt
```

backend/.env dosyasını düzenle

```.env

DB_URL = postgresql://postgres:123456@localhost:5432/postgres

```

veritabanını sunucuyla eşitle

```bash
flask db upgrade
```

backendi çalıştıralım

```bash
flask --app app run
```

```bash
cd ..
cd .\frontend
yarn
```

```bash
yarn run vite
```

```bash
cd .. 
cd .\optimizationServer\
python .\DriverAssignmentServer.py
```

Go to [Local Website](localhost:3000).
