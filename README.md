# 🚀 Otomatik Staj Listesi ve E-posta Bulucu (Summer 2026)

Bu Python betiği, popüler GitHub repo'larından staj ilanlarını otomatik olarak çeker, şirketlerin web sitelerinden domain bilgilerini ayıklar ve **Hunter.io API** kullanarak ilgili iletişim e-postalarını bulup bir Excel dosyası oluşturur.

## ✨ Özellikler

* **Canlı Veri Çekme:** Güncel staj listelerini doğrudan GitHub üzerinden okur.
* **Akıllı Regex:** Markdown linklerini temizleyerek şirket adlarını ve web sitelerini ayıklar.
* **Domain Analizi:** Şirket web sitelerinden otomatik domain tespiti yapar.
* **Excel Çıktısı:** Verileri `Şirket`, `Rol`, `Lokasyon`, `Website` ve `E-posta/Başvuru Linki` sütunlarıyla kaydeder.

## 🛠 Kurulum

1.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install pandas requests openpyxl
    ```

2.  **API Anahtarı:**
    * [Hunter.io](https://hunter.io/) üzerinden aldığınız API anahtarını kodun içindeki `HUNTER_API_KEY` kısmına ekleyin.

## 🚀 Kullanım

Kodu çalıştırmak için terminale şu komutu yazın:

```bash
python internship-scrapper.py