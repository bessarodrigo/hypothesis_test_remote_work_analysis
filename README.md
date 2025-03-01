# Testes de Hipóteses - Produtividade dos Funcionários | Home Office x Presencial 
## Média de Duas Populações Pareadas
Estudo realizado com base nos aprendizados do módulo de inferência estatística da [Escola Preditiva](https://www.preditiva.ai/). apliquei o conceito utilizado no Excel e repliquei no Python.

# Problema
Buscando reduzir custos e melhorar a qualidade de vida de seus colaboradores, uma empresa de atendimento decidiu fazer um teste para avaliar se a adoção do home office para os operadores produziria algum efeito negativo na qualidade dos atendimentos.

Para o teste foram selecionados aleatoriamente 30 operadores que tiveram as médias das notas de avaliação (0 a 10) dos clientes registradas nos 2 locais de trabalho.

Com os dados obtidos, como podemos responder a pergunta: "Operadores trabalhando em home office possuem pior avaliação?"

# Hipóteses
- H0: As notas no Escritório são iguais as notas em Home Office, ou: NE = NHO
- H1: As notas no Escritório são maiores que as notas em Home Office, ou: NE > NHO

# Resultado
Como o p-valor de 12% é maior que o nível de significância de 5%, podemos concluir que não existem evidências estatísticas suficientes contra H0 , ou seja, não rejeitamos H0.

Relembrando as hipóteses definidas:
- H0: As notas no Escritório são iguais as notas em Home Office, ou: NE = NHO
- H1: As notas no Escritório são maiores que as notas em Home Office, ou: NE > NHO

E como não rejeitamos H0, podemos dizer que não existem evidências estatísticas de que a média das notas dos operadores no Escritório não seja igual a média das notas dos mesmos operadores em Home Office.
