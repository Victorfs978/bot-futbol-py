import requests
import re
from concurrent.futures import ThreadPoolExecutor

# --- OBJETIVOS ESPECÍFICOS: PARAGUAY ---
# Buscamos nombres de canales y el código de país [PY]
RADAR_PY = ["PARAGUAY", "TIGO SPORTS", "SNT", "TELEFUTURO", "TRECE", "GEN", "NPY", "PARAGUAY TV", "ABC TV", "C9N"]

FUENTES_LATAM = [
    "https://iptv-org.github.io/iptv/countries/py.m3u", # Base específica de Paraguay
    "https://raw.githubusercontent.com/iptv-org/iptv/master/categories/sports.m3u",
    "https://raw.githubusercontent.com/Fmacedo87/iptv/master/Deportes.m3u",
    "https://raw.githubusercontent.com/DeXTeR085/IPTV/main/Global.m3u"
]

def captura_paraguay(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=20)
        # Captura Nombre y URL
        matches = re.findall(r'#EXTINF:.*?,(.*?)\n(http.*?m3u8[^\s]*)', r.text)
        
        botin_py = []
        for nombre, link in matches:
            n_up = nombre.upper()
            # Si el canal es de Paraguay o está en nuestra lista de interés
            if any(p in n_up for p in RADAR_PY) or ";py" in url.lower():
                # Filtro básico anti-basura
                if not any(b in n_up for b in ["RADIO", "XXX"]):
                    botin_py.append(f"{nombre.strip()}|{link.strip()}")
        return botin_py
    except:
        return []

def mision_paraguay():
    print("🇵🇾 Iniciando escaneo de canales paraguayos...")
    lista_py = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        resultados = list(executor.map(captura_paraguay, FUENTES_LATAM))
    
    for r in resultados:
        lista_py.extend(r)

    # Eliminar repetidos
    botin_final = sorted(list(set(lista_py)))

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin_final:
            f.write("\n".join(botin_final))
            print(f"🏁 ¡ÉXITO! Se encontraron {len(botin_final)} canales de Paraguay.")
        else:
            f.write("ERROR|No se encontraron señales de Paraguay en las fuentes.")

if __name__ == "__main__":
    mision_paraguay()
    
