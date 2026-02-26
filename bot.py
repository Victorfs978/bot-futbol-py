import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1',
    'Referer': 'https://google.com/'
}

def mision_ataque_servidor_oculto():
    # El objetivo real que detectaste
    url_base = "https://teaganm68g.rd3yshvoiceou0gwet.cfd/es/"
    print(f"[*] Atacando servidor oculto: {url_base}")
    lista = []
    try:
        r = requests.get(url_base, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            texto = link.get_text(separator=" ").strip().upper()
            
            # Filtro para capturar Santos, Guaraní y cualquier duelo "VS"
            if any(x in texto for x in ["VS", "SANTOS", "VASCO", "GUARA", "JUVENTUD", "CLUB"]):
                full_link = href if href.startswith('http') else f"https://teaganm68g.rd3yshvoiceou0gwet.cfd{href}"
                
                nombre = " ".join(texto.split())
                if len(nombre) > 10:
                    lista.append(f"STREAM-DIRECTO: {nombre}|{full_link}")
                    print(f"[+] CAPTURADO: {nombre[:45]}...")
    except Exception as e:
        print(f"[!] Error: {e}")
    return lista

def ejecutar_operacion():
    eventos = mision_ataque_servidor_oculto()
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(eventos))
    print(f"\n[!] RESULTADO: {len(eventos)} enlaces extraídos del servidor.")
    # Git local para evitar errores de conexión
    os.system("git add . && git commit -m 'Ataque directo al servidor de stream' || echo 'Commit local listo'")

if __name__ == "__main__":
    ejecutar_operacion()
