"""Confere os links externos dos arquivos .md do repositório.

Uso
    python ferramentas/checar_links.py            confere tudo
    python ferramentas/checar_links.py trilhas/02-seo-tecnico

Vídeos do YouTube são conferidos pelo oEmbed, que devolve título e canal sem
abrir a página. Os outros links recebem um GET com user-agent descritivo.
O script pausa entre requisições ao mesmo domínio e para de consultar um
domínio no primeiro 429.
"""

import re
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
UA = "trilha-seo-dados-ia link checker (+https://github.com/sergiopatrick/trilha-seo-dados-ia)"
PAUSA = 1.5
LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")


def youtube(url):
    host = urllib.parse.urlparse(url).netloc
    return host.endswith("youtube.com") or host.endswith("youtu.be")


def pedir(url):
    if youtube(url):
        url = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(url, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"erro ({e.__class__.__name__})"


def main():
    alvo = RAIZ / (sys.argv[1] if len(sys.argv) > 1 else "")
    arquivos = [alvo] if alvo.is_file() else sorted(alvo.rglob("*.md"))
    links = defaultdict(set)
    for arq in arquivos:
        for url in LINK.findall(arq.read_text(encoding="utf-8")):
            links[url].add(arq.relative_to(RAIZ).as_posix())

    ultimo = {}
    bloqueados = set()
    falhas = []
    for url in sorted(links):
        dominio = urllib.parse.urlparse(url).netloc
        if dominio in bloqueados:
            falhas.append((url, "não conferido (429 antes)"))
            continue
        espera = PAUSA - (time.time() - ultimo.get(dominio, 0))
        if espera > 0:
            time.sleep(espera)
        status = pedir(url)
        ultimo[dominio] = time.time()
        if status == 429:
            bloqueados.add(dominio)
        if status != 200:
            falhas.append((url, status))

    print(f"{len(links)} links conferidos, {len(falhas)} com problema")
    for url, status in falhas:
        print(f"  {status}  {url}")
        for arq in sorted(links[url]):
            print(f"         em {arq}")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
