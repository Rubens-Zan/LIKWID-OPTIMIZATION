# Projeto de Otimização de Código Serial
Disciplina: Introdução a computação científica CI1164
Rubens Laszlo - GRR20206147

## Testes LIKWID 
É utilizado o script "./teste.sh" para a geração dos testes do likwid.  
Sendo esses salvos na pasta "./log", com o formato "${METRICA}_${TAMANHO}.log"

Para a geração dos resultados dos testes em csv e geração das informações dos arquivos csv plotados, é utilizado o scripts "./generate_results.py".
Sendo que são gerados os arquivos csv na pasta "./Resultados/CSV"
e os gráficos plotados na pasta "./Resultados/IMGS_PLOTS"

## Métricas
São utilizadas as seguintes funções do LIKWID para efetuar as métricas.

Teste de tempo: Tempo médio do cálculo da função, em milisegundos (Runtime (RDTSC));
Banda de Memória: Grupo  L3 do LIKWID (L3 bandwidth [MBytes/s]);
Cache miss L2: Grupo L2CACHE do LIKWID (L2 miss ratio);
Operações aritméticas: Grupo FLOPS_DP do LIKWID (DP MFLOP/s e AVX DP MFLOP/s) 

## Gráficos
Os gráficos gerados quando são de funções otimizadas tem o formato de linhas "--" com marcadores nos pontos das funções no formato de "o", já para as não otimizadas são utilizados "-" e "v".
