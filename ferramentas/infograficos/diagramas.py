"""Mapa de estudo, cronograma, método de estudo e arquitetura dos projetos."""

from base import AREA_DA_TRILHA, AREAS, gerar, quebrar

LARGURA = 1000
M = 44

NOMES = {
    "00": "Fundamentos da web", "01": "SEO estratégico", "02": "SEO técnico",
    "03": "SEO em escala", "04": "GEO e busca generativa", "05": "Mensuração",
    "06": "Engenharia de dados", "07": "IA aplicada", "08": "Ofício do consultor",
}


def cabecalho(tela, rotulo, titulo, subtitulo=None):
    t = tela.t
    tela.texto(M, M + 16, rotulo, 15, t["texto2"], 600, espaco=1.5)
    y = M + 56
    for linha in quebrar(titulo, 30, LARGURA - 2 * M, 700):
        tela.texto(M, y, linha, 30, t["texto"], 700)
        y += 38
    if subtitulo:
        y += tela.paragrafo(M, y + 2, subtitulo, 19, LARGURA - 2 * M, t["texto2"])
    return y + 24


def no_trilha(tela, x, y, w, h, num):
    t = tela.t
    area = AREA_DA_TRILHA[num]
    tela.rect(x, y, w, h, t["cartao"], r=10, borda=t[area])
    tela.rect(x + 12, y + (h - 34) / 2, 40, 34, t[f"{area}_forte"], r=6)
    tela.texto(x + 32, y + h / 2 + 7, num, 18, "#ffffff", 700, "middle")
    linhas = quebrar(NOMES[num], 17, w - 68, 600)
    y0 = y + h / 2 - (len(linhas) - 1) * 11 + 6
    for i, l in enumerate(linhas):
        tela.texto(x + 62, y0 + i * 22, l, 17, t["texto"], 600)


def legenda(tela, y, areas):
    t = tela.t
    x = M
    for a in areas:
        tela.rect(x, y - 14, 18, 18, t[a], r=4)
        tela.texto(x + 26, y, AREAS[a], 16, t["texto2"])
        x += 40 + len(AREAS[a]) * 9 + 20
    return y + 30


def mapa(tela):
    t = tela.t
    y = cabecalho(tela, "MAPA DE ESTUDO", "Nove trilhas, uma ordem que faz sentido",
                  "As setas indicam o que destrava o quê. Trilhas na mesma coluna podem ser feitas em paralelo.")
    w, h = 160, 64
    cols = [M, M + 184, M + 368, M + 552]
    pos = {
        "00": (cols[0], y + 110),
        "01": (cols[1], y + 30), "05": (cols[1], y + 190),
        "02": (cols[2], y + 30), "06": (cols[2], y + 190),
        "03": (cols[3], y + 0), "04": (cols[3], y + 100), "07": (cols[3], y + 200),
    }
    def borda_d(n):
        x, yy = pos[n]
        return x + w, yy + h / 2
    def borda_e(n):
        x, yy = pos[n]
        return x, yy + h / 2
    arestas = [("00", "01"), ("00", "05"), ("01", "02"), ("05", "06"), ("02", "03"), ("02", "04"), ("06", "07")]
    for a, b in arestas:
        (x1, y1), (x2, y2) = borda_d(a), borda_e(b)
        mx = (x1 + x2) / 2
        tela.seta([(x1, y1), (mx, y1), (mx, y2), (x2 - 2, y2)], t["texto3"])
    # 07 alimenta 04 (vertical)
    x7, y7 = pos["07"]
    tela.seta([(x7 + w / 2, y7), (x7 + w / 2, pos["04"][1] + h + 2)], t["texto3"])
    for n, (x, yy) in pos.items():
        no_trilha(tela, x, yy, w, h, n)
    # projetos
    px = M + 740
    py = y + 20
    tela.rect(px, py, LARGURA - M - px, 244, t["cartao"], r=10, borda=t["texto3"])
    tela.texto(px + 16, py + 34, "Projetos", 18, t["texto"], 700)
    tela.texto(px + 16, py + 56, "integradores", 18, t["texto"], 700)
    for i, l in enumerate(["Warehouse de SEO", "Monitor de IA", "Auditoria", "Conteúdo com IA"]):
        tela.texto(px + 16, py + 100 + i * 34, f"{i + 1}. {l}", 15, t["texto2"])
    for n in ("03", "04", "07"):
        x1, y1 = borda_d(n)
        tela.seta([(x1, y1), (px - 2, y1)], t["texto3"])
    # 08 transversal
    yb = y + 300
    tela.rect(M, yb, LARGURA - 2 * M, 56, t["cartao"], r=10, borda=t["oficio"])
    tela.rect(M + 12, yb + 11, 40, 34, t["oficio_forte"], r=6)
    tela.texto(M + 32, yb + 35, "08", 18, "#ffffff", 700, "middle")
    tela.texto(M + 64, yb + 35, "Ofício do consultor acompanha todas as trilhas, um módulo por mês a partir do mês 3", 17, t["texto"], 600)
    y = legenda(tela, yb + 100, ["base", "busca", "dados", "ia", "oficio"])
    return LARGURA, y + 10


def cronograma(tela):
    t = tela.t
    y = cabecalho(tela, "RITMO REGULAR · 8 HORAS POR SEMANA", "Um ano do primeiro HTTP ao projeto de portfólio")
    linhas = [("00", 1, 1), ("01", 2, 3), ("05", 2, 3), ("02", 4, 5), ("03", 6, 6), ("06", 7, 8),
              ("07", 9, 10), ("04", 11, 11), ("P", 12, 12), ("08", 3, 12)]
    rot_w = 240
    x0 = M + rot_w
    passo = (LARGURA - M - x0) / 12
    for mes in range(12):
        x = x0 + mes * passo
        tela.texto(x + passo / 2, y + 4, str(mes + 1), 15, t["texto2"], 600, "middle")
    tela.texto(M, y + 4, "Mês", 15, t["texto2"], 600)
    y += 22
    for num, ini, fim in linhas:
        if num == "P":
            nome, cor = "Projetos integradores", t["texto3"]
        else:
            nome, cor = f"{num} · {NOMES[num]}", t[AREA_DA_TRILHA[num]]
        tela.texto(M, y + 23, nome, 17, t["texto"], 600 if num != "08" else 400)
        for mes in range(12):
            tela.rect(x0 + mes * passo + 1, y + 4, passo - 2, 28, t["cartao"], r=4)
        tela.rect(x0 + (ini - 1) * passo + 1, y + 4, (fim - ini + 1) * passo - 2, 28,
                  cor if num != "08" else t["oficio"], r=4)
        y += 40
    y += 8
    y += tela.paragrafo(M, y + 10, "Ritmo leve, 5 h por semana, leva de 16 a 18 meses. Intensivo, 15 h por semana, leva cerca de 6 meses.", 17, LARGURA - 2 * M, t["texto2"])
    return LARGURA, y + 34


def como_estudar(tela):
    t = tela.t
    y = cabecalho(tela, "COMO ESTUDAR CADA MÓDULO", "Cinco passos, sempre na mesma ordem")
    passos = [("Roteiro", "README da trilha"), ("Vídeos", "videos.md"), ("Aula", "aulas.md"),
              ("Leituras", "leituras.md"), ("Exercícios", "exercicios.md")]
    gap = 22
    w = (LARGURA - 2 * M - gap * 4) / 5
    for i, (nome, arq) in enumerate(passos):
        x = M + i * (w + gap)
        tela.rect(x, y, w, 120, t["cartao"], r=12)
        tela.circulo(x + 34, y + 36, 18, t["busca_forte"])
        tela.texto(x + 34, y + 43, str(i + 1), 18, "#ffffff", 700, "middle")
        tela.texto(x + 20, y + 84, nome, 20, t["texto"], 700)
        tela.texto(x + 20, y + 106, arq, 15, t["texto2"])
        if i < 4:
            tela.seta([(x + w + 3, y + 60), (x + w + gap - 3, y + 60)], t["texto3"])
    return LARGURA, y + 160


def projeto(nome, rotulo, titulo, colunas, nota):
    """colunas é uma lista de (título da coluna, área, [caixas])."""
    def f(tela):
        t = tela.t
        y = cabecalho(tela, rotulo, titulo)
        n = len(colunas)
        gap = 40
        w = (LARGURA - 2 * M - gap * (n - 1)) / n
        alt_caixa = 64
        maior = max(len(c[2]) for c in colunas)
        alt_total = maior * (alt_caixa + 14) - 14
        for i, (tit, area, caixas) in enumerate(colunas):
            x = M + i * (w + gap)
            tela.texto(x, y + 4, tit.upper(), 14, t["texto2"], 600, espaco=1.2)
            y0 = y + 22 + (alt_total - (len(caixas) * (alt_caixa + 14) - 14)) / 2
            for j, cx in enumerate(caixas):
                yy = y0 + j * (alt_caixa + 14)
                tela.rect(x, yy, w, alt_caixa, t["cartao"], r=10, borda=t[area])
                linhas = quebrar(cx, 16, w - 24, 600)
                base = yy + alt_caixa / 2 - (len(linhas) - 1) * 10 + 6
                for k, l in enumerate(linhas):
                    tela.texto(x + w / 2, base + k * 20, l, 16, t["texto"], 600, "middle")
            if i < n - 1:
                ym = y + 22 + alt_total / 2
                tela.seta([(x + w + 4, ym), (x + w + gap - 4, ym)], t["texto3"])
        y += 22 + alt_total + 36
        y += tela.paragrafo(M, y, nota, 17, LARGURA - 2 * M, t["texto2"])
        return LARGURA, y + 30
    return nome, f


PROJETOS = [
    projeto("projeto-01", "PROJETO 1 · TRILHAS 02, 05 E 06", "Data warehouse de SEO", [
        ("Fontes", "busca", ["API do Search Console", "GA4 ou BigQuery", "Crawl próprio"]),
        ("Ingestão", "dados", ["Python incremental e idempotente", "Parquet por data"]),
        ("Transformação", "dados", ["dbt staging", "dbt intermediate", "dbt marts e testes"]),
        ("Uso", "oficio", ["Painel", "Alertas"]),
    ], "Orquestrado por cron ou Kestra, com alerta para falha e para execução que não aconteceu. A URL normalizada é a chave entre as três fontes."),
    projeto("projeto-02", "PROJETO 2 · TRILHAS 04, 06 E 07", "Monitor de visibilidade em IA", [
        ("Entrada", "busca", ["30 a 50 prompts fixos", "Marcas e domínios"]),
        ("Coleta", "ia", ["2 ou mais IAs com busca", "3 execuções por prompt"]),
        ("Extração", "ia", ["Domínios citados", "Menções de marca"]),
        ("Análise", "dados", ["DuckDB por semana", "Painel com faixa de variação"]),
    ], "Cruza citações com robôs de IA no log, referência de IAs no GA4 e o relatório de IA generativa do Search Console."),
    projeto("projeto-03", "PROJETO 3 · TRILHAS 02, 07 E 08", "Auditoria técnica com agente", [
        ("Ferramentas", "busca", ["buscar_url", "extrair_html", "renderizar", "pagespeed"]),
        ("Agente", "ia", ["Crawl e templates", "Hipóteses", "Teste de cada hipótese"]),
        ("Evidência", "oficio", ["Origem e status", "Solução proposta"]),
        ("Entrega", "oficio", ["Resumo de uma página", "Anexo técnico"]),
    ], "Permissão só de leitura. Instrução escrita dentro de página visitada é dado, nunca comando. Você confere uma amostra à mão e mede a precisão."),
    projeto("projeto-04", "PROJETO 4 · TRILHAS 03, 06 E 07", "Pipeline de conteúdo com IA local", [
        ("Pauta", "busca", ["Buscas reais", "Agrupar por intenção"]),
        ("Base", "dados", ["Fontes primárias", "RAG com embeddings"]),
        ("Geração", "ia", ["Rascunho com fonte", "Checagem de fatos", "Regras por script"]),
        ("Publicação", "oficio", ["Revisão humana", "Site estático"]),
    ], "O modelo decide e redige. Os scripts garantem as regras. Afirmação sem fonte não entra, e cada reprovação humana vira caso de teste."),
]

if __name__ == "__main__":
    gerar("mapa", mapa, "Mapa de estudo. Fundamentos destrava SEO estratégico e Mensuração. Daí seguem SEO técnico e Engenharia de dados, depois SEO em escala, GEO e IA aplicada, e por fim os projetos. Ofício do consultor acompanha tudo.")
    gerar("cronograma", cronograma, "Cronograma de 12 meses no ritmo regular de 8 horas por semana.")
    gerar("como-estudar", como_estudar, "Cinco passos por módulo. Roteiro, vídeos, aula, leituras e exercícios.")
    for nome, f in PROJETOS:
        gerar(nome, f, f"Arquitetura do {nome.replace('-', ' ')}")
    print("ok")
