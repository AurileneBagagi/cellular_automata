import random

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

TAMANHO_GRADE = 50
GERACOES = 100
TEMPO_DEGRADACAO = 5  # Quantas gerações um agricultor fica no solo ate de degradá-lo
PROBABILIDADE_REGENERACAO_SOLO = 0.001  # Probabilidade de solo se regenerar por geração (0.1%)

# 0: Solo Fértil (marrom), 1: Agricultor (verde), 2: Solo Degradado (bege)
cores = ['#8B4513', '#228B22', '#D2B48C']
mapa_cores = mcolors.ListedColormap(cores)
limites = [0, 1, 2, 3]
norma = mcolors.BoundaryNorm(limites, mapa_cores.N)

