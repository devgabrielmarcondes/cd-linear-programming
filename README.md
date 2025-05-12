# Simplex no Python
## Arquivos
- *simplex.py*: Tentativa de fazer do zero a função linprog(method="highs") da biblioteca numpy

- *test.py*: Teste usando a função linprog(method="highs") do numpy


## Requisitos
1. Função objetivo (max ou min)
2. Variáveis básicas e não básicas (0)
3. Restrições >=, <= e =
4. Variáveis de sobra, excesso e artificias


## Algoritmo
1. Colocar as equações na forma correta
2. Colocar os coeficientes na matriz
3. Iniciar o algoritmo com as variáveis de decisão como 0
4. Verificar se na linha da func obj. existe algum número negativo. Se sim, terminar, caso contrário continuar.
3. Escolher a coluna com o maior negativo
4. Escolher, entre as linhas abaixo da func obj. e na coluna selecionada, aquela cujo resultado dividido pelo seu valor da sua linha, for o menor.
5. Tornar o valor do pivô em 1;
6. Fazer linha (operação) pivô, para zerar todos os valores na coluna que estào acima ou abaixo do pivô.
7. Voltar à etapa 3.
