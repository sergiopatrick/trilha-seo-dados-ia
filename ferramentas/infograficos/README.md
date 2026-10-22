# Infográficos

Todos os infográficos do repositório saem destes scripts, em SVG, nas versões clara e escura. O README escolhe a versão pelo tema do GitHub com `<picture>`.

| Script | O que gera |
|---|---|
| `trilhas.py` | Visão geral de cada trilha, lida do README da própria trilha |
| `casos.py` | O gráfico do achado de cada caso |
| `diagramas.py` | Mapa de estudo, cronograma, passos de estudo e arquitetura dos projetos |
| `inserir.py` | Coloca cada imagem na sua página, entre marcadores, sem duplicar |

Para gerar tudo de novo, rode da raiz do repositório.

```bash
python3 ferramentas/infograficos/gerar_tudo.py
```

As cores vêm de uma paleta de quatro matizes validada para daltonismo, nos modos claro e escuro. Cada área tem uma cor. Busca em azul, medição e dados em verde-água, IA em violeta e ofício em laranja. A cor nunca carrega sozinha a informação, porque todo elemento tem rótulo.
