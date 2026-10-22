"""Visão geral de cada trilha, lida do próprio README da trilha."""

import re

from base import AREA_DA_TRILHA, AREAS, RAIZ, gerar, quebrar

LARGURA = 1000
MARGEM = 44


def ler_trilha(pasta):
    texto = (pasta / "README.md").read_text(encoding="utf-8")
    texto = re.sub(r"<!-- infografico:.*?<!-- /infografico -->\n*", "", texto, flags=re.S)
    numero, nome = re.match(r"# (\d+) · (.+)", texto).groups()
    objetivo = texto.split("\n\n")[1].split(". ")[0] + "."
    carga = re.search(r"\*\*Carga estimada\.\*\* (.+)", texto).group(1).rstrip(".")
    modulos = []
    for bloco in re.split(r"\n### ", texto)[1:]:
        titulo = re.match(r"\d+\. (.+)", bloco).group(1)
        titulo = re.sub(r"\s*\(.*\)$", "", titulo)
        m = re.search(r"\*\*Conceitos-chave\.\*\* (.+)", bloco)
        conceitos = []
        if m:
            for c in m.group(1).split(". "):
                c = re.sub(r"\s*\([^)]*\)", "", c.replace("`", "")).strip().rstrip(".")
                if c and len(c) <= 60:
                    conceitos.append(c)
        modulos.append((titulo, conceitos[:3]))
    return numero, nome, objetivo, carga, modulos


def desenhar(pasta):
    numero, nome, objetivo, carga, modulos = ler_trilha(pasta)
    area = AREA_DA_TRILHA[numero]

    def f(tela):
        t = tela.t
        y = MARGEM
        # cabeçalho
        tela.rect(MARGEM, y, 96, 96, t[f"{area}_forte"], r=14)
        tela.texto(MARGEM + 48, y + 64, numero, 44, "#ffffff", 700, "middle")
        x = MARGEM + 124
        tela.texto(x, y + 22, f"TRILHA {numero} · {AREAS[area].upper()}", 15, t["texto2"], 600, espaco=1.5)
        tela.texto(x, y + 66, nome, 40, t["texto"], 700)
        tela.texto(x, y + 96, f"{len(modulos)} módulos · {carga}", 18, t["texto2"])
        y += 132
        y += tela.paragrafo(MARGEM, y + 8, objetivo, 21, LARGURA - 2 * MARGEM, t["texto"]) + 24

        # grade de módulos em duas colunas
        col = (LARGURA - 2 * MARGEM - 24) / 2
        alturas = []
        for titulo, conceitos in modulos:
            h = 28 + len(quebrar(titulo, 21, col - 92, 700)) * 28
            h += sum(len(quebrar(c, 16, col - 92)) * 22 for c in conceitos) + 20
            alturas.append(max(h, 96))
        for i in range(0, len(modulos), 2):
            h = max(alturas[i:i + 2])
            for j, (titulo, conceitos) in enumerate(modulos[i:i + 2]):
                x0 = MARGEM + j * (col + 24)
                tela.rect(x0, y, col, h, t["cartao"], r=12)
                tela.circulo(x0 + 40, y + 40, 20, t[f"{area}_forte"])
                tela.texto(x0 + 40, y + 47, str(i + j + 1), 19, "#ffffff", 700, "middle")
                yy = y + 46
                for linha in quebrar(titulo, 21, col - 92, 700):
                    tela.texto(x0 + 76, yy, linha, 21, t["texto"], 700)
                    yy += 28
                yy += 4
                for c in conceitos:
                    for linha in quebrar(c, 16, col - 92):
                        tela.texto(x0 + 76, yy, linha, 16, t["texto2"])
                        yy += 22
            y += h + 20
        y += 4
        tela.texto(MARGEM, y + 18, "trilha-seo-dados-ia · roteiro, aulas, vídeos, leituras e exercícios", 15, t["texto3"])
        return LARGURA, y + 48

    gerar(f"trilha-{numero}", f, f"Trilha {numero}, {nome}. Visão geral dos módulos.")
    return numero, nome


def todas():
    return [desenhar(p) for p in sorted((RAIZ / "trilhas").iterdir()) if p.is_dir()]


if __name__ == "__main__":
    import sys
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    pastas = sorted((RAIZ / "trilhas").iterdir())
    for p in pastas:
        if p.is_dir() and (alvo is None or p.name.startswith(alvo)):
            print(desenhar(p))
