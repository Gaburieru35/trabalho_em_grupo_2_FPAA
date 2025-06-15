# Projeto Flood Fill com Visualização

Este projeto implementa o algoritmo **Flood Fill** para preenchimento de regiões conectadas em uma grade (grid) binária, com suporte a visualização interativa utilizando `matplotlib`. Também inclui funcionalidades para geração aleatória de grids para testes e um fluxo integrado para execução e visualização do algoritmo.


##  Equipe
- Gabriel Henrique Mota Rodrigues - RA1450612

- José Miguel Quintão Magalhães - RA1396023

- Matheus Vinicius Mota Rodrigues - RA1462287

---

## Introdução ao Problema

Em diversas áreas como processamento de imagens, jogos e análise espacial, é comum a necessidade de identificar regiões conectadas em uma matriz ou grid bidimensional. Essas regiões são formadas por células adjacentes que satisfazem um critério específico, como serem livres de obstáculos.

O algoritmo **Flood Fill** é um método clássico utilizado para este fim. Dado um ponto inicial, ele explora todas as células conectadas navegáveis (por exemplo, células que não sejam obstáculos), marcando e preenchendo-as para diferenciar as regiões.

## Funcionamento do Algoritmo Flood Fill Implementado

O algoritmo funciona da seguinte forma:

1. **Início a partir de uma célula inicial**: Recebe como entrada um grid 2D e coordenadas de uma célula inicial.

2. **Verificação e validação**: Confirma se a célula inicial é navegável (não é obstáculo) e ainda não foi visitada.

3. **Percurso em largura (BFS)**: Utiliza uma fila para explorar as células adjacentes (cima, baixo, esquerda, direita).

4. **Identificação das células conectadas**: A cada passo, verifica se as células adjacentes são válidas — isto é, estão dentro dos limites do grid, não são obstáculos e não foram visitadas ainda.

5. **Preenchimento com cor específica**: As células válidas são marcadas com uma cor (um valor numérico) para indicar que pertencem à mesma região conectada.

6. **Respeito aos obstáculos e limites**: O algoritmo não atravessa obstáculos (células bloqueadas) nem ultrapassa os limites do grid, garantindo que o preenchimento ocorra apenas nas áreas navegáveis conectadas.

7. **Preenchimento completo de todas as regiões**: Além do ponto inicial, o algoritmo percorre todo o grid para identificar e preencher automaticamente outras regiões desconectadas.

---

## Estrutura do Projeto

- `main.py`  
  Script principal que gera uma grade, executa o flood fill a partir de um ponto inicial e exibe os resultados no console e na visualização.

- `flood_fill.py`  
  Contém a implementação do algoritmo Flood Fill, funções auxiliares para o preenchimento de regiões, e impressão da grade.

- `grid_generator.py`  
  Função para gerar grades aleatórias com uma dada proporção de obstáculos.

- `visualizer.py`  
  Funções para exibir a grade no terminal e para mostrar o processo de preenchimento com gráficos via `matplotlib`.

---

## Funcionalidades

- **Flood Fill completo:** Preenchimento de todas as regiões desconectadas de zeros na grade, atribuindo cores diferentes a cada região.
- **Visualização passo a passo:** Mostra o preenchimento em tempo real, destacando o avanço do algoritmo.
- **Geração aleatória de grids:** Cria matrizes 2D com obstáculos distribuídos aleatoriamente.
- **Fluxo integrado:** Interface simples para executar tudo junto e visualizar resultados.

---

## Como usar

### Pré-requisitos

- Python 3.7 ou superior
- Biblioteca matplotlib (para visualização)

Instale o matplotlib via pip se necessário:

```bash
pip install matplotlib
```
## Executando o projeto
Basta rodar:

```bash
python main.py
```

O script irá:

- Gerar uma grade 10x10 com obstáculos (~30% de células bloqueadas).
- Exibir a grade inicial no console.
- Executar o flood fill a partir do ponto (0,0).
- Exibir a visualização animada do preenchimento.
- Imprimir a grade final preenchida no console.

## Detalhes das funções principais
```python
flood_fill_all(grid, start_x, start_y, visualize=False, show_callback=None)
```
- Preenche todas as regiões de zeros da grade com cores únicas.
- Começa no ponto inicial (start_x, start_y) se for válido.

### Parâmetros:

- **grid**: matriz 2D de inteiros (0 para espaço vazio, 1 para obstáculos).
- **start_x, start_y**: coordenadas iniciais.
- **visualize**: ativa visualização passo a passo.
- **show_callback**: função para desenhar a grade durante o preenchimento.

```python
generate_random_grid(n, m, obstacle_ratio)
```
  Gera uma matriz n x m com células bloqueadas distribuídas aleatoriamente segundo obstacle_ratio.

```python
visualize_flood_fill(grid, start_x, start_y, flood_fill_all_fn)
```
Integra a execução do flood fill com a visualização gráfica usando matplotlib.

---

## Considerações Finais
Este projeto demonstra a aplicação do algoritmo Flood Fill para problemas práticos de análise de regiões conectadas em uma matriz. A solução pode ser expandida para usos em áreas como segmentação de imagens, navegação robótica, jogos e simulações.
