import random

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

TAMANHO_GRADE = 50
GERACOES = 100
TEMPO_DEGRADACAO = 5  # Quantas gerações um agricultor fica no solo ate de degradá-lo
PROB_REG_NATURAL = 0.005  # Probabilidade de solo se regenerar por geração (0.1%)
PROB_REG_FATOR_HUMANA = 0.3  # Probabilidade adicional de regeneração por intervenção humana (0%)
FATOR_AUMENTO_ADJACENTE = 0.1  # Fator de aumento da probabilidade de regeneração por vizinho fértil

# 0: Solo Fértil (marrom), 1: Agricultor (verde), 2: Solo Degradado (bege)
cores = ['#8B4513', '#228B22', '#D2B48C']
mapa_cores = mcolors.ListedColormap(cores)
limites = [0, 1, 2, 3]
norma = mcolors.BoundaryNorm(limites, mapa_cores.N)


class AutomatoCelular:
    def __init__(self, tamanho):
        self.grade = np.zeros((tamanho, tamanho), dtype=int)
        self.idade_agrics = np.zeros((tamanho, tamanho), dtype=int)
        self.tamanho = tamanho

    def inicializador_grade(self):
        # Inicializa o solo como 90% fértil e 10% com um agricultor inicial
        num_agrics_inics = int(self.tamanho * self.tamanho * 0.1)
        ind_agrics = random.sample(range(self.tamanho * self.tamanho), num_agrics_inics)

        for ind in ind_agrics:
            linha, coluna = divmod(ind, self.tamanho)
            self.grade[linha, coluna] = 1

    def contar_vizinhos(self, linha, coluna, estado):
        contador = 0
        # Itera sobre os vizinhos, incluindo diagonais (Vizinhança de Moore)
        for i in range(max(0, linha - 1), min(self.tamanho, linha + 2)):
            for j in range(max(0, coluna - 1), min(self.tamanho, coluna + 2)):
                if (i, j) != (linha, coluna) and self.grade[i, j] == estado:
                    contador += 1
        return contador

    def atualizar(self):
        nova_grade = self.grade.copy()

        for i in range(self.tamanho):
            for j in range(self.tamanho):
                estado_atual = self.grade[i, j]

                if estado_atual == 0:  # Solo Fértil
                    vizinhos_agrics = self.contar_vizinhos(i, j, 1)
                    if vizinhos_agrics >= 2:
                        nova_grade[i, j] = 1
            
                elif estado_atual == 1:  # Agricultor
                    self.idade_agrics[i, j] += 1
                    if self.idade_agrics[i, j] >= TEMPO_DEGRADACAO:
                        nova_grade[i, j] = 2
                        self.idade_agrics[i, j] = 0

                elif estado_atual == 2:  # Solo Degradado
                    vizinhos_ferteis = self.contar_vizinhos(i, j, 0)
                    prob_regeneracao = PROB_REG_NATURAL * (1 + FATOR_AUMENTO_ADJACENTE * vizinhos_ferteis)
                    prob_regeneracao += PROB_REG_FATOR_HUMANA  # Acrescenta a probabilidade adicional de regeneração por meio humano
                    prob_regeneracao = min(prob_regeneracao, 1.0)  # Garante que a probabilidade não exceda 1.0
                    if random.random() < prob_regeneracao:
                        nova_grade[i, j] = 0

        self.grade = nova_grade

    def executar_simulacao(self):
        fig, ax = plt.subplots()
        ax.set_title('Simulação de Propagação Agricultores e Degradação do Solo')
        ax.set_xticks([])
        ax.set_yticks([])
        img = ax.imshow(self.grade, cmap=mapa_cores, norm=norma, animated=True)

        # Cria a legenda
        patches = [plt.Rectangle((0, 0), 1, 1, fc=c) for c in cores]
        rotulos = ['Solo Fértil', 'Agricultor', 'Solo\nDegradado']
        
        ax.legend(patches, rotulos, loc='upper left', bbox_to_anchor=(1.02, 0.95), borderaxespad=0)

        leg_geracao = ax.text(1.02, 0.95, '', transform=ax.transAxes, fontsize=10, verticalalignment='bottom')
        
        def atualizar_plot(geracao):
            self.atualizar()
            img.set_array(self.grade)
            # Atualiza o texto da geracao atual
            leg_geracao.set_text(f'Geração: {geracao + 1}/{GERACOES}')
            return img, leg_geracao
        
        # Altere a variavel interval para controlar a velocidade da animação
        animacao = FuncAnimation(fig, atualizar_plot, frames=GERACOES, interval=200, blit=False, repeat=False)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    automato = AutomatoCelular(TAMANHO_GRADE)
    automato.inicializador_grade()
    automato.executar_simulacao()