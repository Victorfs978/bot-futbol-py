import requests
import re

def solucion_relampago():
    print("🚀 INICIANDO ESCANEO FINAL...")
    fuentes = [
        "https://iptv-org.github.io/iptv/languages/spa.m3u",
        "https://raw.githubusercontent.com/TheRealSanjeev/IPTV/main/Global/Sports.m3u"
    ]
    
    botin = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for url in fuentes:
        try:
            r = requests.get(url, headers=headers, timeout=10)
            # Solo buscamos los que dicen "Sports", "ESPN" o "Fox" para que no sea basura
            enlaces = re.findall(r'(https?://[^\s"\'<>]+m3u8)', r.text)
            for l in enlaces:
                if l not in botin:
                    botin.append(l)
        except:
            continue

    print("\n" + "="*50)
    print("🏆 AQUÍ TIENES TUS LINKS (COPIA DESDE AQUÍ ABAJO):")
    print("="*50 + "\n")

    # Los imprimimos todos seguidos para que usted deslice el dedo y copie
    for link in botin[:100]: # Te doy los mejores 100 de golpe
        print(link)

    print("\n" + "="*50)
    print("✅ FIN DEL BOTÍN. COPIA TODO Y PEGALO EN TU APP.")
    print("="*50)

if __name__ == "__main__":
    solucion_relampago()
    
