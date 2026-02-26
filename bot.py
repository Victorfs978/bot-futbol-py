from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import re
import time
import os

# Dominio activo de MadPlay77
BASE_URL = "https://ganzqowo.ps34buy87z6lothrough.sbs"
TARGET = f"{BASE_URL}/es/"

def ataque_kali_dios():
    print(f"[*] Escaneando objetivos en {TARGET}...")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Disfraz de iPhone 14 Pro
    ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    options.add_argument(f'user-agent={ua}')

    try:
        service = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(TARGET)
        
        # Espera estratégica para carga de JavaScript
        time.sleep(15) 
        
        html = driver.page_source
        
        # Patrón más agresivo: busca cualquier enlace con un ID de 7 dígitos seguido de .html
        # Esto captura fútbol, basket, tenis y cualquier otro deporte
        patron = r'href="([^"]+\d{7}/[^"]+\.html)"'
        enlaces = re.findall(patron, html)
        
        partidos = []
        for href in enlaces:
            # Limpiamos el enlace para asegurar que sea absoluto
            if not href.startswith("http"):
                href = f"{BASE_URL}{href}" if href.startswith("/") else f"{BASE_URL}/{href}"
            
            # Inyectamos la llave maestra icg=UFk
            link_final = f"{href}?icg=UFk"
            
            # Extraemos un nombre legible del enlace
            nombre = href.split('/')[-1].replace('.html', '').replace('-', ' ').upper()
            partidos.append(f"{nombre}|{link_final}")

        if partidos:
            # Eliminamos duplicados y guardamos el botín
            resultado = list(set(partidos))
            with open("/home/kali/lista_canales.txt", "w", encoding='utf-8') as f:
                f.write("\n".join(resultado))
            print(f"[!] VICTORIA: {len(resultado)} partidos capturados y listos para Sketchware.")
            
            # Sincronización con tu GitHub
            os.system("git add /home/kali/lista_canales.txt")
            os.system("git commit -m 'Actualización de canales MadPlay'")
            os.system("git push")
            print("[+] GitHub sincronizado con éxito.")
        else:
            print("[-] El objetivo está vacío. El dominio ha cambiado o la agenda está cerrada.")
            
    except Exception as e:
        print(f"[-] Error en la infiltración: {e}")
    finally:
        if 'driver' in locals(): driver.quit()

if __name__ == "__main__":
    ataque_kali_dios()
