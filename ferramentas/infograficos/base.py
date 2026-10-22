"""Sistema visual dos infográficos.

Cada infográfico é gerado duas vezes, claro e escuro, e o README escolhe
com <picture> conforme o tema do GitHub. Cores validadas com o validador
da skill de dataviz (categórico de 4 matizes, claro e escuro).
"""

from html import escape
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SAIDA = RAIZ / "imagens"

FONTE = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

TEMAS = {
    "claro": {
        "fundo": "#fcfcfb",
        "cartao": "#f3f2ef",
        "borda": "#dcdad5",
        "texto": "#0b0b0b",
        "texto2": "#52514e",
        "texto3": "#6b6a66",
        "grade": "#e4e2dd",
        # cor de identidade (marca) e cor forte (fundo de número com texto branco)
        "busca": "#2a78d6", "busca_forte": "#1c5cab",
        "dados": "#1baf7a", "dados_forte": "#0b6e4c",
        "ia": "#6250d6", "ia_forte": "#4a3aa7",
        "oficio": "#eb6834", "oficio_forte": "#a8431b",
        "base": "#8a8984", "base_forte": "#52514e",
        "bom": "#0ca30c", "ruim": "#d03b3b",
    },
    "escuro": {
        "fundo": "#1a1a19",
        "cartao": "#242423",
        "borda": "#3a3a37",
        "texto": "#f0efec",
        "texto2": "#c3c2b7",
        "texto3": "#a3a29a",
        "grade": "#33332f",
        "busca": "#3987e5", "busca_forte": "#1c5cab",
        "dados": "#199e70", "dados_forte": "#0b6e4c",
        "ia": "#9085e9", "ia_forte": "#4a3aa7",
        "oficio": "#d95926", "oficio_forte": "#a8431b",
        "base": "#8a8984", "base_forte": "#52514e",
        "bom": "#0ca30c", "ruim": "#e66767",
    },
}

AREAS = {
    "base": "Base",
    "busca": "Busca",
    "dados": "Medição e dados",
    "ia": "IA",
    "oficio": "Ofício",
}

AREA_DA_TRILHA = {
    "00": "base", "01": "busca", "02": "busca", "03": "busca", "04": "busca",
    "05": "dados", "06": "dados", "07": "ia", "08": "oficio",
}


def largura_texto(texto, tamanho, peso=400):
    fator = 0.6 if peso >= 600 else 0.54
    return len(texto) * tamanho * fator


def quebrar(texto, tamanho, largura, peso=400):
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = f"{atual} {palavra}".strip()
        if largura_texto(teste, tamanho, peso) <= largura or not atual:
            atual = teste
        else:
            linhas.append(atual)
            atual = palavra
    if atual:
        linhas.append(atual)
    return linhas


class Tela:
    """Acumula elementos SVG para um tema."""

    def __init__(self, tema):
        self.t = TEMAS[tema]
        self.partes = []

    def add(self, s):
        self.partes.append(s)

    def rect(self, x, y, w, h, cor, r=10, borda=None):
        b = f' stroke="{borda}" stroke-width="1"' if borda else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{cor}"{b}/>')

    def texto(self, x, y, s, tamanho=18, cor=None, peso=400, ancora="start", espaco=0):
        cor = cor or self.t["texto"]
        ls = f' letter-spacing="{espaco}"' if espaco else ""
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" font-size="{tamanho}" font-weight="{peso}" '
            f'fill="{cor}" text-anchor="{ancora}"{ls}>{escape(s)}</text>'
        )

    def paragrafo(self, x, y, s, tamanho, largura, cor=None, peso=400, entrelinha=1.35):
        linhas = quebrar(s, tamanho, largura, peso)
        for i, linha in enumerate(linhas):
            self.texto(x, y + i * tamanho * entrelinha, linha, tamanho, cor, peso)
        return len(linhas) * tamanho * entrelinha

    def linha(self, x1, y1, x2, y2, cor, w=2):
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{cor}" stroke-width="{w}"/>')

    def seta(self, pontos, cor, w=2):
        d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pontos)
        self.add(f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{w}" marker-end="url(#seta)"/>')

    def circulo(self, cx, cy, r, cor):
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{cor}"/>')

    def svg(self, largura, altura, titulo):
        t = self.t
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largura} {altura:.0f}" '
            f'width="{largura}" height="{altura:.0f}" role="img" aria-label="{escape(titulo)}" '
            f'font-family="{FONTE}">\n'
            f'<title>{escape(titulo)}</title>\n'
            f'<defs><marker id="seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{t["texto3"]}"/></marker></defs>\n'
            f'<rect width="100%" height="100%" rx="16" fill="{t["fundo"]}"/>\n'
            + "\n".join(self.partes)
            + "\n</svg>\n"
        )


def gerar(nome, funcao, titulo):
    """Chama funcao(tela) nos dois temas. funcao devolve (largura, altura)."""
    SAIDA.mkdir(exist_ok=True)
    for tema, sufixo in (("claro", ""), ("escuro", "-escuro")):
        tela = Tela(tema)
        largura, altura = funcao(tela)
        (SAIDA / f"{nome}{sufixo}.svg").write_text(tela.svg(largura, altura, titulo), encoding="utf-8")


def picture(caminho_rel, nome, alt):
    """HTML para o README, com troca automática de tema no GitHub."""
    return (
        "<picture>\n"
        f'  <source media="(prefers-color-scheme: dark)" srcset="{caminho_rel}/{nome}-escuro.svg">\n'
        f'  <img src="{caminho_rel}/{nome}.svg" alt="{escape(alt)}" width="100%">\n'
        "</picture>"
    )
