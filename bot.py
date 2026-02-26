import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://rbtvplus17.baby/',
    'Accept-Language': 'es-ES,es;q=0.9'
}

def mision_agenda_football():
    # Atacamos directamente la sección de fútbol del servidor oculto
    url = "https://teaganm68g.rd3yshvoiceou0gwet.cfd/es/football/"
    print(f"[*] Capturando toda la agenda de Football en: {url}")
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Limpiamos el texto para leer los nombres de los equipos
            texto = " ".join(link.get_text(separator=" ").split()).upper()
            
            # FILTRO DE AGENDA:
            # 1. El link debe pertenecer a la sección de fútbol
            # 2. El texto debe ser largo (más de 12 letras) para que sea un partido y no una categoría
            if "/football/" in href and len(texto) > 12:
                # Excluimos palabras basura que detectamos en tus capturas
                if not any(b in texto for b in ["YOUTUBE", "POLÍTICA", "TELEGRAM", "TÉRMINOS", "FORMULA"]):
                    full_link = href if href.startswith('http') else f"https://teaganm68g.rd3yshvoiceou0gwet.cfd{href}"
                    lista.append(f"FOOTBALL: {texto}|{full_link}")
                    print(f"[+] PARTIDO CAPTURADO: {texto[:50]}")
    except Exception as e:
        print(f"[!] Error en el asalto: {e}")
    return lista

def ejecutar_operacion():
    eventos = mision_agenda_football()
    
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(eventos))
        
    print(f"\n[!] VICTORIA: {len(eventos)} eventos de football en agenda.")
    os.system("git add . && git commit -m 'Captura completa de agenda Football' || echo 'Local ok'")

if __name__ == "__main__":
    ejecutar_operacion()
