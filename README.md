# SoforAtama Driver Assignment Project

![Project Summary](src/project-summary.png)

## Özet

Belediye ve işletmelerin çalışanlarına eşit vardiya ataması önemli sorunlardan birisidir.

Bu optimizasyon problemini Hedef Programlama tekniğini kullanarak Python ile Google'nın geliştirdiği OR-TOOLS aracı ile çözümünü yaptım.

## Problem

Bir atama probleminde işlerin makinelere dağıtımı, kişilerin işlere tayini, satış personelinin satış bölgelerine dağıtımı vb. yapılır. 

Atama modeli aslında kaynakları işçiler, hedefleri de işler olan özel bir ulaştırma modelidir. Kaynakların sayısının hedeflerin sayısına eşit olması gerekir.

## Çözüm

Hedef programlama verilen kısıtlayıcılar altında amaç 
ölçütünü doğrudan maksimum veya minimum kılmaktan ziyade hedeflerin kendi içindeki sapmaları minimum kılmaya odaklanan bir tekniktir.

 Atama problemleri için uygun bir yapısı vardır.

## Kurulum

### Gereklilikler

1. Docker
2. Python
3. node.js
4. yarn

### PostgreSQL sunucusunun kurulumu

İlk olarak ana klasörde docker ile veritabanı sunucusunu kurabilmek adına docker ile kurunuz. 

```bash
docker-compose up -d
```

#### Pgadmin ile PostgreSQL tablolarını takip edebilirsiniz

`docker-compose.yml` gözüktüğü gibi pgadmin için oluşturulan email `mail@pgadmin.com` ve şifre olarak ise `123456` oluşturuldu. [http://localhost:82](http://localhost:82) giderek giriş yapınız.

![pgadmin server](src/pgadmin.png)

![pgadmin server](src/pgadmin2.png)

## Back-End Sunucusunun Kurulumu

Yeni sekmede terminal açıp backend için env oluşturup gerekli kütüphaneleri yükleyelim.

```bash
cd backend
python -m venv .backend
.backend/Scripts/activate
pip install -r requirements.txt
```

Eğer değiştirtiyseniz backend/.env dosyasını düzenleyin.

```.env

DB_URL = postgresql://postgres:123456@localhost:5432/postgres

```

Flask SQLAlchemy ile oluşturulan veritabanını oluşturduğumuz sunucuyla eşitle.

```bash
flask db upgrade
```

Back-End sunucunu çalıştıralım.

```bash
flask --app app run
```

## Front-End Sunucusunun Kurulumu

Yeni bir adet daha terminal açıp aşağıdaki komutla gerekli kütüphaneleri kurunuz.

```bash
cd frontend
yarn
```

Front-end sunucusunu çalıştırınız.

```bash
yarn run vite
```

## Optimizasyon Sunucusunun Kurulumu

Aşağıdaki kodlar ile bir adet env oluşturup gerekli kütüphaneleri yükleyin.

```bash
cd optimizationServer
python -m venv .optimization
.optimization/Scripts/activate
pip install -r requirements.txt
```

```bash
python DriverAssignmentServer.py
```
