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
        rotulos = ['Solo Fértil', 'Agricultor', 'Solo Degradado']
        
        legend_obj = ax.legend(patches, rotulos, loc='upper left', bbox_to_anchor=(1.02, 0.95), borderaxespad=0)
        legend_texts = legend_obj.get_texts()

        leg_geracao = ax.text(1.02, 0.95, '', transform=ax.transAxes, fontsize=10, verticalalignment='bottom')

        historico_fertil = []
        historico_agricultor = []
        historico_degradado = []
        
        def atualizar_plot(geracao):
            self.atualizar()
            img.set_array(self.grade)
            leg_geracao.set_text(f'Geração: {geracao + 1}/{GERACOES}')

            # Calcula as porcentagens
            total_celulas = self.tamanho * self.tamanho
            perc_fertil = (np.sum(self.grade == 0) / total_celulas) * 100
            perc_agricultor = (np.sum(self.grade == 1) / total_celulas) * 100
            perc_degradado = (np.sum(self.grade == 2) / total_celulas) * 100

            legend_texts[0].set_text(f'Solo Fértil:\n{perc_fertil:.0f}%')
            legend_texts[1].set_text(f'Agricultor:\n{perc_agricultor:.0f}%')
            legend_texts[2].set_text(f'Solo\nDegradado:\n{perc_degradado:.0f}%')

            # Exibe o gráfico assim que a última geração ocorre
            historico_fertil.append(np.count_nonzero(self.grade == 0))
            historico_agricultor.append(np.count_nonzero(self.grade == 1))
            historico_degradado.append(np.count_nonzero(self.grade == 2))
            
            if geracao + 1 == GERACOES:
                plt.figure()
                plt.plot(historico_fertil, label='Solo Fértil', color=cores[0])
                plt.plot(historico_agricultor, label='Agricultor', color=cores[1])
                plt.plot(historico_degradado, label='Solo Degradado', color=cores[2])
                plt.xlabel('Geração')
                plt.ylabel('Quantidade de células')
                plt.title('Evolução dos estados ao longo das gerações')
                plt.legend()
                plt.tight_layout()
                plt.show()

            return img, leg_geracao, *legend_texts
      
        # Altere a variavel interval para controlar a velocidade da animação
        animacao = FuncAnimation(fig, atualizar_plot, frames=GERACOES, interval=200, blit=False, repeat=False)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    automato = AutomatoCelular(TAMANHO_GRADE)
    automato.inicializador_grade()
    automato.executar_simulacao()