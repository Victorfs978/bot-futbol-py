import urllib.request
import re
import ssl

# Dominio activo detectado en sus capturas
BASE_URL = "https://ganzqowo.ps34buy87z6lothrough.sbs"
AGENDA_URL = f"{BASE_URL}/es/"

def ataque_quirurgico():
    print(f"[*] Perforando seguridad en: {AGENDA_URL}")
    
    # Forzamos que no verifique certificados SSL para evitar bloqueos de seguridad
    context = ssl._create_unverified_context()
    
    # Disfraz de Navegador Premium para evitar el bloqueo de bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'
    }
    
    try:
        req = urllib.request.Request(AGENDA_URL, headers=headers)
        with urllib.request.urlopen(req, context=context) as response:
            html = response.read().decode('utf-8')
            
            # Buscamos los IDs de 7 dígitos y los deportes
            # Este patrón captura: /basketball/nombre-partido-ID/partido.html
            patron = r'href="([^"]+/(?:basketball|football|tennis)/[^"]+(\d{7})/[^"]+\.html)"'
            enlaces = re.findall(patron, html)
            
            partidos_lista = []
            for href, id_evento in enlaces:
                # Armamos el link directo con la llave maestra icg=UFk
                link_final = f"{BASE_URL}{href}?icg=UFk"
                
                # Limpiamos el nombre para que tu App de Sketchware se vea profesional
                nombre_limpio = href.split('/')[-1].replace('.html', '').replace('-', ' ').upper()
                
                partidos_lista.append(f"{nombre_limpio}|{link_final}")

            if partidos_lista:
                # Eliminamos duplicados para no saturar la App
                resultado = list(set(partidos_lista))
                with open("lista_canales.txt", "w", encoding='utf-8') as f:
                    f.write("\n".join(resultado))
                print(f"[!] ATAQUE EXITOSO: {len(resultado)} partidos capturados.")
            else:
                print("[-] La defensa de la web bloqueó la extracción. Intenta de nuevo.")
                
    except Exception as e:
        print(f"[-] ERROR EN LA OPERACIÓN: {e}")

if __name__ == "__main__":
    ataque_quirurgico()
    
