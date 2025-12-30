import pandas as pd
import requests
import re
import time
from urllib.parse import urlparse

# AYARLAR
HUNTER_API_KEY = "BURAYA HUNTER API KEYINIZI GIRINIZ."
GITHUB_RAW_URL = "https://raw.githubusercontent.com/vanshb03/Summer2026-Internships/refs/heads/dev/README.md"

def get_domain(url):
    if not url or 'http' not in url: return ""
    try:
        
        clean_url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
        if clean_url:
            parsed = urlparse(clean_url[0])
            return parsed.netloc.replace('www.', '')
        return ""
    except: return ""

def get_emails_from_hunter(domain):
    if not domain or domain == "": return "Domain Yok"
    # Hunter API limitine dikkat!
    api_url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            emails = data.get('data', {}).get('emails', [])
            return ", ".join([e['value'] for e in emails[:2]]) if emails else "E-posta bulunamadı"
        return f"Hata ({response.status_code})"
    except: return "Bağlantı Hatası"

def run_advanced_automation():
    print("Veriler çekiliyor ve işleniyor...")
    res = requests.get(GITHUB_RAW_URL)
    if res.status_code != 200:
        print("GitHub bağlantı hatası!")
        return

    lines = res.text.split('\n')
    extracted_data = []

    for line in lines:
        # Tablo satırı kontrolü
        if line.count('|') >= 4:
            cols = [c.strip() for c in line.split('|')]
            
            # Başlıkları ve ayraçları atla
            if '---' in line or 'Company' in line or 'Role' in line:
                continue

            name_raw = cols[1]
            name = re.sub(r'\[|\]|\(.*\)', '', name_raw).replace('**', '')

            role = cols[2] if len(cols) > 2 else "Belirtilmemiş"

            location = cols[3] if len(cols) > 3 else "Belirtilmemiş"

            links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
            link = links[0] if links else ""
            domain = get_domain(link)

            if name:
                extracted_data.append({
                    "Şirket": name,
                    "Rol": role,
                    "Lokasyon": location,
                    "Website": domain,
                    "Başvuru Linki": link
                })

    df = pd.DataFrame(extracted_data)
    
    print(f"{len(df)} şirket bulundu. E-postalar sorgulanıyor (İşlem uzun sürebilir)...")
    
    df_emails = df.copy() 

    # Kaydet
    df_emails.to_excel("internship-list.xlsx", index=False)
    print("\n'internship-list.xlsx' başarıyla oluşturuldu!")

if __name__ == "__main__":
    run_advanced_automation()