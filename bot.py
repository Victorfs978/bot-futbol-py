import requests
from bs4 import BeautifulSoup
import os

# Usamos el disfraz de Chrome Windows para que el servidor nos de el contenido real
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://rbtvplus17.baby/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

def mision_verificar_y_capturar():
    # Atacamos el dominio donde se ocultan los datos de los partidos
    url = "https://teaganm68g.rd3yshvoiceou0gwet.cfd/es/football/"
    print(f"[*] Analizando integridad de la fuente: {url}")
    lista = []
    try:
        # Hacemos la peticion al servidor hijo
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            print("[+] Conexión establecida con el servidor de stream.")
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Buscamos todos los links de la agenda de futbol
            for link in soup.find_all('a', href=True):
                href = link['href']
                texto = " ".join(link.get_text(separator=" ").split()).upper()
                
                # Solo capturamos si es la ruta de futbol y tiene nombre de partido (largo)
                if "/football/" in href and len(texto) > 15:
                    # Filtro para evitar categorias del menu
                    if not any(b in texto for b in ["YOUTUBE", "POLITICA", "TERMINOS", "BALONCESTO", "TENIS"]):
                        full_link = href if href.startswith('http') else f"https://teaganm68g.rd3yshvoiceou0gwet.cfd{href}"
                        lista.append(f"FOOTBALL-VIVO: {texto}|{full_link}")
                        print(f"[+] AGENDA CAPTURADA: {texto[:50]}")
        else:
            print(f"[!] El servidor respondió con error {r.status_code}. Podrían haber rotado el dominio.")
            
    except Exception as e:
        print(f"[!] Error crítico en el asalto: {e}")
    return lista

def ejecutar_operacion():
    eventos = mision_verificar_y_capturar()
    
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(eventos))
        
    print(f"\n[!] OPERACIÓN: {len(eventos)} eventos de la fuente extraídos.")
    os.system("git add . && git commit -m 'Ataque a fuente de stream validada' || echo 'Sync local'")

if __name__ == "__main__":
    ejecutar_operacion()
