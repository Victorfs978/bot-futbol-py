import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://rbtvplus17.baby/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

def mision_agenda_total():
    # Atacamos la sección donde la web muestra los partidos
    url = "https://teaganm68g.rd3yshvoiceou0gwet.cfd/es/football/"
    print(f"[*] Escaneando agenda completa en: {url}")
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Buscamos en todos los elementos que puedan contener un partido
        for elemento in soup.find_all(['a', 'div', 'li']):
            # Buscamos si hay un link adentro o si el elemento mismo es el link
            href = elemento.get('href') or (elemento.find('a')['href'] if elemento.find('a') else None)
            
            if href and "/football/" in href:
                texto = " ".join(elemento.get_text(separator=" ").split()).upper()
                
                # FILTRO DE PARTIDO: Nombres largos y que no sean basura de menú
                if len(texto) > 15 and not any(b in texto for b in ["YOUTUBE", "POLÍTICA", "TÉRMINOS", "BALONCESTO", "VOLEIBOL"]):
                    full_link = href if href.startswith('http') else f"https://teaganm68g.rd3yshvoiceou0gwet.cfd{href}"
                    
                    # Evitamos duplicados
                    if not any(full_link in item for item in lista):
                        lista.append(f"FUTBOL-VIVO: {texto}|{full_link}")
                        print(f"[+] PARTIDO ENCONTRADO: {texto[:50]}")
    except Exception as e:
        print(f"[!] Fallo en el escaneo: {e}")
    return lista

def ejecutar_operacion():
    eventos = mision_agenda_total()
    
    # Si sigue en 0, es que usan JavaScript para cargar los partidos. 
    # En ese caso, capturaremos el HTML crudo para analizarlo.
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(eventos))
        
    print(f"\n[!] OPERACIÓN: {len(eventos)} partidos capturados de la agenda.")
    os.system("git add . && git commit -m 'Escaneo de agenda por contenedores' || echo 'Local ok'")

if __name__ == "__main__":
    ejecutar_operacion()
