import re

# Tu lista masiva procesada para extraer dominios reales
raw_data = """
1 camel1.live 2 antenasport.top 3 strumyk.uk 4 daddyhd.com 5 dlhd.link 
9 teledeportes.top 23 tudeporte.pro 26 sosplay.net 31 bolaloca.my 
38 la14hd.com 39 rdtvonline.com 95 pelotalibretv.su 99 vegeta-tv-2.zya.me 
156 ppv.to 189 strmd.link 190 goluchitas.com 197 ntvstream.cx 
198 sportplus.live 201 platinsport.com 203 myfootball.pw 204 liveball.st
206 vipleague.lc 208 calciostream.help 209 rojadirecta.eu 212 vipbox.lc
"""

# Dominios que ya tenemos en el bot
ya_atacados = ['castmedia.click', 'livetv.sx', 'antenasport.top', 'streamtp10.com']

# Extraer y limpiar
encontrados = re.findall(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]', raw_data.lower())
unicos = sorted(list(set([d for d in encontrados if d not in ya_atacados])))

# Inteligencia: ¿Quiénes son 24/7?
fijos_247 = ['daddyhd.com', 'dlhd.link', 'pelotalibretv.su', 'la14hd.com', 'tvporinternet2.com']

print(f"[*] Informe de Inteligencia: {len(unicos)} dominios únicos nuevos.")
print("\n[!] OBJETIVOS PRIORITARIOS (SEÑALES 24/7):")
for dom in unicos:
    if dom in fijos_247:
        print(f"    [ALTA PRIORIDAD] -> {dom}")

print("\n[*] Otros objetivos de eventos:")
for dom in unicos:
    if dom not in fijos_247:
        print(f"    - {dom}")
