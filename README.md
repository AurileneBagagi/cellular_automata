
#  Modelagem da Propagação de Assentamentos Agrícolas e Degradação do Solo Através de um Autômato Celular Discreto


##  Resumo

Este projeto foi desenvolvido para a disciplina optativa de **Cellular Automata**. O objetivo é simular, através de um autômato celular (bidimensional de N×N células), como a atividade agrícola se expande e causa o desgaste do solo ao longo do tempo.

A simulação representa três estados de célula:

  * **Solo Fértil (Marrom):** Área disponível para cultivo.
  * **Agricultor (Verde):** Área atualmente em cultivo.
  * **Solo Degradado (Bege):** Área que foi exaustivamente cultivada e se tornou infértil.

## Configuração e Personalização

Você pode alterar os parâmetros da simulação diretamente no início do arquivo `simulacao_AC.py` para observar diferentes resultados.

#### Parâmetros da Simulação

  * `TAMANHO_GRADE`: Altera o tamanho da grade da simulação (padrão: `50`).
  * `GERACOES`: Define o número total de gerações que a simulação irá durar (padrão: `100`).
  * `TEMPO_DEGRADACAO`: Controla quantas gerações um agricultor pode cultivar uma mesma célula antes que ela se degrade (padrão: `5`). Um valor menor acelera o desgaste.
  * `PROBABILIDADE_REGENERACAO_SOLO`: A probabilidade (de 0 a 1) de um solo degradado se tornar fértil a cada geração (padrão: `0.001`, ou 0.1%).

#### Parâmetros da Animação

  * Dentro da função `rodar_simulacao`, você pode alterar o parâmetro `interval` na chamada `FuncAnimation` para diminuir ou aumentar a velocidade da animação.
     

## 📚 Bibliotecas Utilizadas

O projeto depende das seguintes bibliotecas Python:

  * **numpy:** Para manipulação eficiente de arrays e da grade da simulação.
  * **matplotlib:** Para a criação dos gráficos e da animação.

## 🚀 Instalação e Execução

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
