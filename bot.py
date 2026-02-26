import requests
from bs4 import BeautifulSoup
import os

# DISFRAZ DE ÉLITE: Ahora fingimos ser Chrome en Windows para evitar bloqueos
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://rbtvplus17.baby/',
    'Accept-Language': 'es-ES,es;q=0.9'
}

def mision_ataque_total():
    # Vamos directo a la carpeta de fútbol del servidor oculto
    url = "https://teaganm68g.rd3yshvoiceou0gwet.cfd/es/football/"
    print(f"[*] Atacando servidor oculto con disfraz de Chrome...")
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            texto = link.get_text(separator=" ").strip().upper()
            
            # Capturamos TODO lo que tenga un nombre de equipo o estructura de partido
            if len(texto) > 6 and ("/" in href or "VS" in texto or "CLUB" in texto):
                # Filtramos basura de menús
                if not any(b in texto for b in ["YOUTUBE", "POLÍTICA", "TERMINOS"]):
                    full_link = href if href.startswith('http') else f"https://teaganm68g.rd3yshvoiceou0gwet.cfd{href}"
                    
                    nombre = " ".join(texto.split())
                    lista.append(f"VIVO: {nombre}|{full_link}")
                    print(f"[+] CAPTURADO: {nombre[:45]}...")
    except Exception as e:
        print(f"[!] Error: {e}")
    return lista

def ejecutar_operacion():
    eventos = mision_ataque_total()
    
    # Guardamos los resultados
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(eventos))
        
    print(f"\n[!] OPERACIÓN: {len(eventos)} partidos asegurados.")
    os.system("git add . && git commit -m 'Ataque con disfraz de Chrome' || echo 'Local ok'")

if __name__ == "__main__":
    ejecutar_operacion()
