
#  Modelagem da Propagação de Agricultores e Degradação do Solo baseado em Autômatos Celulares


##  Resumo

Este projeto foi desenvolvido para a disciplina optativa de **Cellular Automata**. O objetivo é simular, através de um autômato celular (bidimensional de N×N células), a dinâmica entre agricultores, solo fértil, solo degradado e regeneração do solo ao longo do tempo.

A simulação representa três estados de célula:

  * **Solo Fértil (Marrom):** Área disponível para cultivo.
  * **Agricultor (Verde):** Área atualmente em cultivo.
  * **Solo Degradado (Bege):** Área que foi exaustivamente cultivada e se tornou infértil.

Ao final da execução, o código:

  * Mostra uma animação com a evolução espacial dos estados do solo.
  * Exibe um gráfico temporal com a quantidade de células em cada estado ao longo das gerações.

## Parâmetros ajustáveis

Os parâmetros abaixo podem ser alterados diretamente no início do código (`simulacao_AC.py`) para criar diferentes cenários:

| Parâmetro | Descrição | Valor padrão | Exemplo de alteração |
|-----------|-----------|--------------|----------------------|
| `TAMANHO_GRADE` | Tamanho da grade (NxN) | `50` | `100` para simulação maior |
| `GERACOES` | Número total de gerações simuladas | `100` | `200` para mais tempo de simulação |
| `TEMPO_DEGRADACAO` | Gerações que um agricultor leva para degradar o solo | `5` | `10` para degradação mais lenta |
| `PROB_REG_NATURAL` | Probabilidade de regeneração natural por geração | `0.005` | `0.01` para regeneração natural mais rápida |
| `PROB_REG_FATOR_HUMANA` | Probabilidade extra de regeneração devido à intervenção humana | `0.3` (30%) | `0.0` para sem intervenção |
| `FATOR_AUMENTO_ADJACENTE` | Aumento da chance de regeneração por vizinho fértil | `0.1` | `0.2` para efeito maior dos vizinhos |

O modelo é probabilístico, então execuções diferentes podem gerar padrões diferentes.

#### Parâmetros da Animação

  * Dentro da função `rodar_simulacao`, você pode alterar o parâmetro `interval` na chamada `FuncAnimation` para diminuir ou aumentar a velocidade da animação.
     

## 📚 Bibliotecas Utilizadas

O código utiliza as seguintes bibliotecas Python:

- [NumPy](https://numpy.org/) – Manipulação de matrizes e operações numéricas.
- [Matplotlib](https://matplotlib.org/) – Visualização de dados e animação.
- [random](https://docs.python.org/3/library/random.html) – Geração de números aleatórios.

### Instalação das bibliotecas
Você pode instalar todas as dependências executando:

```bash
    pip install numpy matplotlib
```

## ▶️ Execução

1.  **Pré-requisitos:**

      * Certifique-se de ter o **Python 3** instalado em seu sistema.

2.  **Instale as dependências:**

      * Abra seu terminal ou prompt de comando e execute o seguinte comando para instalar as bibliotecas necessárias:

    ```bash
    pip install numpy matplotlib
    ```

3.  **Execute o código:**

      * Navegue pelo terminal até a pasta onde o arquivo `simulacao_AC.py` está salvo e execute o comando:

    ```bash
    python simulacao_AC.py
    ```
