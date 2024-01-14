# SoforAtama Driver Assignment Project

![chrome_1ZO0ULQDM8](src/chrome_1ZO0ULQDM8.png)

Bu proje Karadeniz Teknik Üniversitesi İstatistik Ve Bilgisayar Bilimleri 4. Sınıf Bitirme Tezi ve Seminer 1,2 dersleri kapsamında çalıştım.

![Project Summary](src/project-summary.png)

## Katkı Sağlayanlar

* Ali Eren Ekinci (Proje Sahibi)
* Gülnur Ögür (Proje Sahibi)
* Dr. Öğr. Üyesi Tolga Berber (Danışman)
* Arş. Gör. Beyzanur Siyah (Danışman)

## Özet

Belediye ve işletmelerin çalışanlarına eşit vardiya ataması önemli sorunlardan birisidir.

Bu optimizasyon problemini Hedef Programlama tekniğini kullanarak Python ile Google'nın geliştirdiği OR-TOOLS aracı ile çözümünü yaptım.

## Problem

Bir atama probleminde işlerin makinelere dağıtımı, kişilerin işlere tayini, satış personelinin satış bölgelerine dağıtımı vb. yapılır.

Atama modeli aslında kaynakları işçiler, hedefleri de işler olan özel bir ulaştırma modelidir. Kaynakların sayısının hedeflerin sayısına eşit olması gerekir.

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

Daha sora aşağıdaki fotografalara bakarak serveri ekleyebilirsiniz.
  
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

Vscode daki split özelliğini kullanarak başlatabilirsiniz.

![Tüm Terminaller](src/Code_WMlmJdt4ic.png)