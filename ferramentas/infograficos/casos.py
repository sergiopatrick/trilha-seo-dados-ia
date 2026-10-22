"""Gráfico do achado principal de cada caso. Números arredondados dos casos."""

from base import gerar, quebrar

LARGURA = 1000
M = 44


def cabecalho(tela, rotulo, titulo, subtitulo):
    t = tela.t
    tela.texto(M, M + 16, rotulo, 15, t["texto2"], 600, espaco=1.5)
    y = M + 58
    for linha in quebrar(titulo, 32, LARGURA - 2 * M, 700):
        tela.texto(M, y, linha, 32, t["texto"], 700)
        y += 40
    y += tela.paragrafo(M, y + 4, subtitulo, 19, LARGURA - 2 * M, t["texto2"])
    return y + 28


def rodape(tela, y, fonte):
    tela.texto(M, y, fonte, 15, tela.t["texto3"])
    return y + 36


def fmt(n):
    return f"{n:,.0f}".replace(",", ".")


def barras(tela, y, itens, rotulo_w=250, max_v=None, sufixo="", cor=None, h=32, passo=46):
    """Barras horizontais com rótulo à esquerda e valor ao lado."""
    t = tela.t
    max_v = max_v or max(v for _, v, *_ in itens)
    base_x = M + rotulo_w
    escala = (LARGURA - M - base_x - 190) / max_v
    for item in itens:
        rot, val = item[0], item[1]
        c = item[2] if len(item) > 2 else (cor or t["dados"])
        tela.texto(M, y + h / 2 + 7, rot, 18, t["texto2"])
        tela.linha(base_x, y - 6, base_x, y + h + 6, t["grade"], 1)
        tela.rect(base_x, y, max(val * escala, 3), h, c, r=4)
        tela.texto(base_x + max(val * escala, 3) + 12, y + h / 2 + 7, f"{fmt(val)}{sufixo}", 18, t["texto"], 600)
        y += passo
    return y


def caso1(tela):
    t = tela.t
    y = cabecalho(
        tela, "CASO 1 · SEO ESTRATÉGICO E MENSURAÇÃO",
        "A queda de cliques se explica quase toda pelo CTR",
        "Decomposição da variação de cliques em efeito volume (mais ou menos buscas) e efeito CTR (mais ou menos cliques por busca).",
    )
    passos = [("Cliques antes", 10000, None), ("Efeito volume", 200, "+"), ("Efeito CTR", -1700, "−"), ("Cliques agora", 8500, None)]
    topo, alt = y + 20, 300
    escala = alt / 10500
    larg = 150
    gap = (LARGURA - 2 * M - 4 * larg) / 3
    nivel = 0
    base = topo + alt
    tela.linha(M, base, LARGURA - M, base, t["grade"], 1)
    for i, (rot, val, sinal) in enumerate(passos):
        x = M + i * (larg + gap)
        if sinal is None:
            h = val * escala
            tela.rect(x, base - h, larg, h, t["base"], r=4)
            topo_txt = base - h - 12
            nivel = val
            txt = fmt(val)
        else:
            ini, fim = nivel, nivel + val
            y0 = base - max(ini, fim) * escala
            h = abs(val) * escala
            tela.rect(x, y0, larg, max(h, 3), t["dados"] if val > 0 else t["ruim"], r=4)
            topo_txt = y0 - 12
            nivel = fim
            txt = f"{sinal}{fmt(abs(val))}"
        tela.texto(x + larg / 2, topo_txt, txt, 22, t["texto"], 700, "middle")
        tela.texto(x + larg / 2, base + 30, rot, 18, t["texto2"], 400, "middle")
    y = base + 70
    y += tela.paragrafo(M, y, "Posição média e impressões ficaram estáveis. O que mudou foi a página de resultados, que passou a interceptar o clique.", 18, LARGURA - 2 * M, t["texto"]) + 16
    return LARGURA, rodape(tela, y, "Exemplo ilustrativo com números redondos. O caso real está em casos/01-queda-de-leads-que-era-ctr.md")


def caso2(tela):
    t = tela.t
    y = cabecalho(
        tela, "CASO 2 · SEO TÉCNICO",
        "O sitemap não tinha 9 em cada 10 páginas com tráfego",
        "Das mil páginas com mais cliques orgânicos no Search Console, quantas estavam no sitemap.",
    )
    y = barras(tela, y + 6, [("Fora do sitemap", 918, t["ruim"]), ("No sitemap", 82, t["base"])], sufixo=" páginas")
    y += 24
    tela.texto(M, y, "Varredura pela união de sitemap e Search Console, sem duplicatas", 21, t["texto"], 700)
    y = barras(tela, y + 22, [("Responderam 200", 1770, t["dados"]), ("Deram 404", 220, t["base"])], sufixo=" endereços")
    return LARGURA, rodape(tela, y + 10, "Números arredondados de um caso real anonimizado. Leia em casos/02-sitemap-que-escondia-o-site.md")


def caso3(tela):
    t = tela.t
    y = cabecalho(
        tela, "CASO 3 · SEO TÉCNICO E GEO",
        "O teste local dizia 403. O log mostrava os robôs de IA entrando",
        "Visitas de robôs de IA registradas em um mês, contando só a parte do log com respostas 404. O total real é maior.",
    )
    tela.rect(M, y, LARGURA - 2 * M, 64, t["cartao"], r=10)
    tela.texto(M + 24, y + 40, "Teste do computador da equipe com user-agent de robô", 18, t["texto2"])
    tela.texto(LARGURA - M - 24, y + 41, "403", 26, t["ruim"], 700, "end")
    y += 96
    itens = [("OAI-SearchBot", 1300), ("ClaudeBot", 640), ("YouBot", 420), ("GPTBot", 90), ("Claude-User", 70), ("ChatGPT-User", 30), ("PerplexityBot", 20)]
    y = barras(tela, y, [(r, v, t["ia"]) for r, v in itens], rotulo_w=200, sufixo=" visitas", h=28, passo=40)
    return LARGURA, rodape(tela, y + 10, "Números arredondados de um caso real anonimizado. Leia em casos/03-bloqueio-de-robos-que-nao-existia.md")


def caso4(tela):
    t = tela.t
    y = cabecalho(
        tela, "CASO 4 · OFÍCIO DO CONSULTOR",
        "9 de 32 itens da auditoria estavam errados, pela mesma causa",
        "Em todos, o estado do site foi inferido a partir de um sinal indireto. Os quatro padrões e o teste que teria evitado cada um.",
    )
    pares = [
        ("Contar dados estruturados com grep", "Extrair os blocos com parser"),
        ("Ausência no relatório da ferramenta", "Pedir a URL e ver o status"),
        ("Estimativa escrita como fato", "Contar ou marcar como estimativa"),
        ("Número que o próprio site declara", "Contar no HTML ou no sitemap"),
    ]
    col = (LARGURA - 2 * M - 70) / 2
    tela.texto(M, y + 4, "SINAL INDIRETO", 15, t["texto2"], 600, espaco=1.5)
    tela.texto(M + col + 70, y + 4, "TESTE DIRETO", 15, t["texto2"], 600, espaco=1.5)
    y += 22
    for errado, certo in pares:
        tela.rect(M, y, col, 64, t["cartao"], r=10)
        tela.circulo(M + 26, y + 32, 9, t["ruim"])
        tela.texto(M + 48, y + 39, errado, 19, t["texto"], 600)
        tela.seta([(M + col + 10, y + 32), (M + col + 60, y + 32)], t["texto3"])
        x2 = M + col + 70
        tela.rect(x2, y, col, 64, t["cartao"], r=10)
        tela.circulo(x2 + 26, y + 32, 9, t["bom"])
        tela.texto(x2 + 48, y + 39, certo, 19, t["texto"], 600)
        y += 78
    y += 10
    y += tela.paragrafo(M, y, "Depois da revisão, cada achado passou a ter a origem da evidência e um status. Confirmado, parcial ou verificação recomendada.", 18, LARGURA - 2 * M, t["texto"]) + 16
    return LARGURA, rodape(tela, y, "Leia em casos/04-nove-afirmacoes-erradas.md")


def caso5(tela):
    """Virada falsa. Barras de leads da terça atual contra o par errado e o par certo."""
    t = tela.t
    y = cabecalho(
        tela, "CASO 5 · MENSURAÇÃO",
        "A mesma terça-feira, comparada com o dia errado e com o dia certo",
        "Comparar pelo dia do mês pôs uma terça contra um domingo. Alinhado pelo dia da semana, a alta virou estabilidade.",
    )
    grupos = [
        ("Comparação pelo dia do mês", "Terça atual", 260, "Domingo do mês anterior", 99, "+162%"),
        ("Comparação pelo dia da semana", "Terça atual", 260, "Terça do mês anterior", 265, "−2%"),
    ]
    for titulo, a_rot, a_val, b_rot, b_val, delta in grupos:
        tela.texto(M, y + 6, titulo, 21, t["texto"], 700)
        tela.texto(LARGURA - M, y + 6, delta, 30, t["texto"], 700, "end")
        y = barras(tela, y + 28, [(b_rot, b_val, t["base"]), (a_rot, a_val, t["dados"])], max_v=280, sufixo=" leads")
        y += 30
    return LARGURA, rodape(tela, y, "Números arredondados de um caso real anonimizado. Leia em casos/05-virada-que-nao-existia.md")


def caso6(tela):
    t = tela.t
    y = cabecalho(
        tela, "CASO 6 · SEO TÉCNICO E MENSURAÇÃO",
        "A correlação parecia forte. Com seis meses de dado, ela cabia em quase qualquer valor",
        "Correlação entre LCP no celular e receita mensal, com intervalo de confiança de 95%.",
    )
    x0, x1 = M + 40, LARGURA - M - 40
    def px(r):
        return x0 + (r + 1) * (x1 - x0)
    eixo = y + 70
    tela.linha(x0, eixo, x1, eixo, t["grade"], 2)
    for r in (-1, -0.75, -0.5, -0.25, 0):
        tela.linha(px(r), eixo - 6, px(r), eixo + 6, t["texto3"], 1)
        tela.texto(px(r), eixo + 32, f"{r:.2f}".replace(".", ",").replace("-", "−"), 16, t["texto2"], 400, "middle")
    tela.rect(px(-0.98), eixo - 14, px(-0.13) - px(-0.98), 28, t["busca"], r=6)
    tela.circulo(px(-0.85), eixo, 12, t["texto"])
    tela.texto(px(-0.85), eixo - 28, "r = −0,85", 20, t["texto"], 700, "middle")
    tela.texto(px(-0.98), eixo + 62, "−0,98", 18, t["texto"], 600, "middle")
    tela.texto(px(-0.13), eixo + 62, "−0,13", 18, t["texto"], 600, "middle")
    tela.texto(px(-0.55), eixo + 62, "intervalo de 95%, n = 6", 18, t["texto2"], 400, "middle")
    y = eixo + 110
    tela.texto(M, y, "Teste de placebo · a mesma queda calculada em cada um dos 12 cortes possíveis", 21, t["texto"], 700)
    y += 30
    tela.texto(M, y, "Do pior para o melhor resultado", 16, t["texto2"])
    y += 36
    passo = (LARGURA - 2 * M) / 12
    for i in range(12):
        cx = M + passo * (i + 0.5)
        cor = t["ruim"] if i == 3 else (t["base"] if i < 3 else t["grade"])
        tela.circulo(cx, y, 16, cor)
        tela.texto(cx, y + 6, f"{i + 1}º", 13, "#ffffff" if i <= 3 else t["texto2"], 700, "middle")
    y += 48
    tela.texto(M + passo * 1.5, y, "3 piores", 16, t["texto2"], 400, "middle")
    tela.texto(M + passo * 1.5, y + 22, "sem evento técnico", 16, t["texto2"], 400, "middle")
    tela.texto(M + passo * 3.5, y, "mês da piora", 16, t["texto"], 600, "start")
    tela.texto(M + passo * 3.5, y + 22, "técnica, só o 4º", 16, t["texto"], 600, "start")
    y += 70
    return LARGURA, rodape(tela, y, "Números de um caso real anonimizado. Leia em casos/06-correlacao-que-nao-servia.md")


def caso7(tela):
    t = tela.t
    y = cabecalho(
        tela, "CASO 7 · MENSURAÇÃO E DADOS",
        "Quanto mais páginas lidas, maior a conversão em matrícula",
        "Taxa de conversão de quem não leu nenhuma página contra quem leu mais de 50, em duas unidades de negócio.",
    )
    xa, xb = M + 260, LARGURA - M - 260
    topo, alt = y + 30, 300
    def py(v):
        return topo + alt - v / 3.0 * alt
    for v in (0, 1, 2, 3):
        tela.linha(xa - 40, py(v), xb + 40, py(v), t["grade"], 1)
    linhas = [("Unidade A", 0.2, 2.6, t["busca"]), ("Unidade B", 0.4, 2.0, t["oficio"])]
    for nome, a, b, cor in linhas:
        tela.add(f'<line x1="{xa}" y1="{py(a):.1f}" x2="{xb}" y2="{py(b):.1f}" stroke="{cor}" stroke-width="3"/>')
        tela.circulo(xa, py(a), 8, cor)
        tela.circulo(xb, py(b), 8, cor)
        tela.texto(xb + 18, py(b) + 6, f"{nome} · {str(b).replace('.', ',')}%", 18, t["texto"], 600)
        tela.texto(xa - 18, py(a) + 6 + (10 if nome.endswith("A") else -8), f"{nome} · {str(a).replace('.', ',')}%", 18, t["texto"], 600, "end")
    tela.texto(xa, topo + alt + 36, "Nenhuma página", 18, t["texto2"], 400, "middle")
    tela.texto(xb, topo + alt + 36, "Mais de 50 páginas", 18, t["texto2"], 400, "middle")
    y = topo + alt + 76
    y += tela.paragrafo(M, y, "Mais da metade da receita aparecia como offline no CRM, e quase todos esses contatos tinham navegação no site.", 18, LARGURA - 2 * M, t["texto"]) + 16
    return LARGURA, rodape(tela, y, "Números arredondados de um caso real anonimizado. Leia em casos/07-metade-da-receita-sem-origem.md")


def caso8(tela):
    t = tela.t
    y = cabecalho(
        tela, "CASO 8 · SEO TÉCNICO",
        "Centenas de URLs ruins, duas causas",
        "Cada grupo de URLs ruins no relatório de Core Web Vitals tinha uma causa só.",
    )
    col = (LARGURA - 2 * M - 24) / 2
    cartoes = [
        ("Celular", "33 URLs ruins", "Todas de um subdomínio de API lento, sem cache e com PHP antigo"),
        ("Desktop", "61 URLs ruins", "Todas são a home, por um elemento que muda de lugar (CLS)"),
    ]
    for i, (disp, num, causa) in enumerate(cartoes):
        x = M + i * (col + 24)
        tela.rect(x, y, col, 170, t["cartao"], r=12)
        tela.texto(x + 24, y + 38, disp.upper(), 15, t["texto2"], 600, espaco=1.5)
        tela.texto(x + 24, y + 80, num, 30, t["texto"], 700)
        tela.paragrafo(x + 24, y + 114, causa, 18, col - 48, t["texto2"])
    y += 210
    tela.texto(M, y, "Tempo de bloqueio da home em laboratório, antes e depois da fase 1", 21, t["texto"], 700)
    y = barras(tela, y + 24, [("Antes", 5300, t["ruim"]), ("Depois", 740, t["dados"])], rotulo_w=120, sufixo=" ms")
    return LARGURA, rodape(tela, y + 10, "Números arredondados de um caso real anonimizado. Leia em casos/08-core-web-vitals-de-causa-unica.md")


CASOS = {
    "caso-01": (caso1, "Caso 1. Exemplo de decomposição. Cliques caem de 10 mil para 8.500. Efeito volume soma 200 e efeito CTR tira 1.700."),
    "caso-02": (caso2, "Caso 2. Das mil páginas com mais tráfego, 918 estavam fora do sitemap. A varredura completa teve cerca de 1.770 endereços com 200 e 220 com 404."),
    "caso-03": (caso3, "Caso 3. Teste local deu 403, mas o log mostrou visitas de robôs de IA, como OAI-SearchBot com cerca de 1.300 e ClaudeBot com 640."),
    "caso-04": (caso4, "Caso 4. Nove de 32 itens errados. Quatro padrões de sinal indireto e o teste direto que corrige cada um."),
    "caso-05": (caso5, "Caso 5. Comparar pelo dia do mês mostrou alta de 162 por cento. Alinhado pelo dia da semana, a variação foi de menos 2 por cento."),
    "caso-06": (caso6, "Caso 6. Correlação de menos 0,85 com intervalo de 95 por cento de menos 0,98 a menos 0,13, com seis meses. No placebo, o mês da piora foi só o 4º pior de 12."),
    "caso-07": (caso7, "Caso 7. Conversão sobe de 0,2 para 2,6 por cento na unidade A e de 0,4 para 2,0 por cento na unidade B, de nenhuma página para mais de 50."),
    "caso-08": (caso8, "Caso 8. 33 URLs ruins no celular com uma causa e 61 no desktop com outra. Tempo de bloqueio da home caiu de 5.300 para 740 milissegundos."),
}

if __name__ == "__main__":
    for nome, (funcao, alt) in CASOS.items():
        gerar(nome, funcao, alt)
        print(nome)
