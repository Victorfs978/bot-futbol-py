import requests
import re

def asalto_final_streamtp():
    print("🧨 INICIANDO ASALTO A LOS SERVIDORES DE STREAMTP...")
    
    # Atacamos directamente los archivos que alimentan la lista
    servidores = [
        "https://streamtp10.com/global1.php",
        "https://streamtp10.com/global2.php",
        "https://streamtp10.com/agenda.php"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
        'Referer': 'https://streamtp10.com/',
        'X-Requested-With': 'XMLHttpRequest'
    }

    botin = []

    for url in servidores:
        try:
            print(f"🛰️ Escaneando servidor: {url}")
            r = requests.get(url, headers=headers, timeout=15)
            
            # Buscamos enlaces de reproductores (clon.php, player.php, embed.html)
            enlaces = re.findall(r'href=["\'](.*?\.php\?id=.*?)["\']', r.text)
            # También buscamos canales directos en el código
            directos = re.findall(r'["\'](https?://.*?\.m3u8.*?)["\']', r.text)
            
            total = enlaces + directos
            for item in total:
                if item not in botin:
                    botin.append(item)
                    print(f"  🎯 ¡OBJETIVO LOCALIZADO!: {item}")
        except:
            continue

    print("\n" + "="*50)
    if botin:
        print(f"🏆 TENEMOS {len(botin)} PECES GORDOS EN LA MIRA")
        print("Copia estos links para tu App (son los reproductores directos):")
        print("="*50)
        for i, link in enumerate(botin[:20]):
            final_url = link if link.startswith('http') else "https://streamtp10.com/" + link
            print(f"⚽ CANAL {i+1}: {final_url}")
    else:
        print("🚨 El sistema detectó el bot. Necesitamos simular un clic manual.")
        print("💡 PRUEBA ESTO: Pásame el link que sale cuando tocas 'ESPN' en tu celular.")
    print("="*50)

if __name__ == "__main__":
    asalto_final_streamtp()
        
