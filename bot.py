import requests
from bs4 import BeautifulSoup
import os

# Cambiamos el Referer para que el servidor hijo nos deje entrar
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://rbtvplus17.baby/',
    'Origin': 'https://rbtvplus17.baby'
}

def mision_asalto_hijo():
    # Atacamos la sección específica de fútbol del servidor oculto
    url = "https://teaganm68g.rd3yshvoiceou0gwet.cfd/es/football/"
    print(f"[*] Perforando servidor hijo: {url}")
    lista = []
    try:
        # Usamos un verificado de SSL falso por si el certificado es rancio
        r = requests.get(url, headers=HEADERS, timeout=15, verify=True)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Buscamos todos los links que tengan nombres de partidos
        for link in soup.find_all('a', href=True):
            href = link['href']
            texto = link.get_text(separator=" ").strip().upper()
            
            # Si el link es un partido real (Santos, Guaraní, vs)
            if any(x in texto for x in ["VS", "SANTOS", "VASCO", "GUARA", "JUVENTUD", "FC"]):
                # Construimos el link final
                full_link = href if href.startswith('http') else f"https://teaganm68g.rd3yshvoiceou0gwet.cfd{href}"
                
                nombre = " ".join(texto.split())
                if len(nombre) > 8:
                    lista.append(f"PARTIDO-VIVO: {nombre}|{full_link}")
                    print(f"[+] ¡DENTRO!: {nombre[:40]}...")
    except Exception as e:
        print(f"[!] Error de asalto: {e}")
    return lista

def ejecutar_operacion():
    eventos = mision_asalto_hijo()
    
    if not eventos:
        print("[!] El servidor hijo sigue bloqueando. Intentando ruta alternativa...")
    
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(eventos))
        
    print(f"\n[!] RESULTADO: {len(eventos)} partidos capturados.")
    os.system("git add . && git commit -m 'Ataque rompe-muros al servidor hijo' || echo 'Local ok'")

if __name__ == "__main__":
    ejecutar_operacion()
