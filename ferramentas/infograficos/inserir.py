"""Coloca cada infográfico na sua página, entre marcadores, sem duplicar.

Rodar de novo só atualiza o bloco que já existe.
"""

import re

from base import RAIZ, picture

BLOCO = re.compile(r"<!-- infografico:(?P<nome>[\w-]+) -->.*?<!-- /infografico -->\n?", re.S)


def bloco(rel, nome, alt):
    return f"<!-- infografico:{nome} -->\n{picture(rel, nome, alt)}\n<!-- /infografico -->\n"


def colocar(arquivo, nome, alt, depois_de):
    """Insere o bloco logo depois da linha que começa com depois_de."""
    texto = arquivo.read_text(encoding="utf-8")
    rel = "/".join([".."] * (len(arquivo.relative_to(RAIZ).parts) - 1)) or "."
    rel = f"{rel}/imagens" if rel != "." else "imagens"
    novo = bloco(rel, nome, alt)
    existente = [m for m in BLOCO.finditer(texto) if m.group("nome") == nome]
    if existente:
        m = existente[0]
        texto = texto[:m.start()] + novo + texto[m.end():]
    else:
        linhas = texto.split("\n")
        i = next(i for i, l in enumerate(linhas) if l.startswith(depois_de))
        # depois da linha e do parágrafo que ela abre
        j = i + 1
        while j < len(linhas) and linhas[j].strip():
            j += 1
        linhas.insert(j, "\n" + novo.rstrip("\n"))
        texto = "\n".join(linhas)
    arquivo.write_text(texto, encoding="utf-8")


def main():
    r = RAIZ / "README.md"
    colocar(r, "mapa", "Mapa de estudo das nove trilhas e dos projetos integradores", "As setas indicam dependência")
    colocar(r, "como-estudar", "Cinco passos por módulo, do roteiro aos exercícios", "Cada trilha tem um `README.md` com o roteiro")
    colocar(r, "cronograma", "Cronograma de 12 meses no ritmo regular", "| Ritmo | Horas por semana")

    for pasta in sorted((RAIZ / "trilhas").iterdir()):
        if pasta.is_dir():
            num = pasta.name[:2]
            colocar(pasta / "README.md", f"trilha-{num}", f"Visão geral da trilha {num}", "# ")

    for arq in sorted((RAIZ / "casos").glob("0*.md")):
        num = arq.name[:2]
        colocar(arq, f"caso-{num}", f"Gráfico do caso {num}", "**Setor.**")

    for arq in sorted((RAIZ / "projetos").glob("0*.md")):
        num = arq.name[:2]
        colocar(arq, f"projeto-{num}", f"Arquitetura do projeto {num}", "**Carga estimada.**")


if __name__ == "__main__":
    main()
    print("ok")
