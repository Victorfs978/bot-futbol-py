import requests
from bs4 import BeautifulSoup
import os

# Usamos un disfraz de navegador de escritorio robusto
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://www.vipleague.io/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

def mision_asalto_vipleague():
    url = "https://vipleague.io/football-schedule-streaming-links"
    print(f"[*] Atacando nueva posición: {url}")
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # En VipLeague los partidos suelen estar en filas de tablas o divs de clase 'match'
        partidos = soup.find_all(['a', 'div'], class_=['match', 'event']) or soup.find_all('a', href=True)
        
        for item in partidos:
            href = item.get('href') if item.name == 'a' else (item.find('a')['href'] if item.find('a') else None)
            
            if href and "/football/" in href:
                # Extraemos el nombre del partido (ej: Santos vs Vasco)
                texto = " ".join(item.get_text(separator=" ").split()).upper()
                
                # Filtro de agenda: Nombres que representen un partido real
                if len(texto) > 12 and " VS " in texto:
                    full_link = href if href.startswith('http') else f"https://vipleague.io{href}"
                    
                    if not any(full_link in x for x in lista):
                        lista.append(f"VIP-AGENDA: {texto}|{full_link}")
                        print(f"[+] PARTIDO EN AGENDA: {texto[:50]}")
                        
    except Exception as e:
        print(f"[!] Error en el asalto a VipLeague: {e}")
    return lista

def ejecutar_operacion():
    eventos = mision_asalto_vipleague()
    
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(eventos))
        
    print(f"\n[!] VICTORIA: {len(eventos)} eventos capturados de VipLeague.")
    os.system("git add . && git commit -m 'Asalto a VipLeague exitoso' || echo 'Sync local'")

if __name__ == "__main__":
    ejecutar_operacion()
