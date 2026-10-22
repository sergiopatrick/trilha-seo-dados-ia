"""Gera todos os infográficos e coloca cada um na sua página."""

import runpy
from pathlib import Path

AQUI = Path(__file__).resolve().parent

for script in ("trilhas.py", "casos.py", "diagramas.py", "inserir.py"):
    runpy.run_path(str(AQUI / script), run_name="__main__")
