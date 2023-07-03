# Simulador de Delação Premiada

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Grupo 2**: XX<br>
**Paradigma**: SMA<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0108344  |  Rafael Berto Pereira |
| 19/0016663  |  Lucas Pimentel Quintão |
| 19/0044403  |  Victor Souza Dantas Martins Lima |

## Sobre 
Neste projeto, nossa equipe explorou o conceito do "Dilema do Prisioneiro" e desenvolveu uma simulação de delação premiada.<br>

O "Dilema do Prisioneiro" é um problema clássico na teoria dos jogos que examina a cooperação e a traição em situações de interação entre dois indivíduos. No contexto da delação premiada, o dilema surge quando dois suspeitos de um crime são interrogados separadamente e têm a oportunidade de decidir se irão cooperar com o outro suspeito, permanecendo em silêncio, ou trair o outro, delatando-o à polícia, como detalhado abaixo:

"Dois suspeitos, A e B, são presos pela polícia. A polícia tem provas insuficientes para os condenar, mas, separando os prisioneiros, oferece a ambos o mesmo acordo: se um dos prisioneiros, confessando, testemunhar contra o outro e esse outro permanecer em silêncio, o que confessou sai livre enquanto o cúmplice silencioso cumpre 10 anos de sentença. Se ambos ficarem em silêncio, a polícia só pode condená-los a 6 meses de cadeia cada um. Se ambos traírem o comparsa, cada um leva 5 anos de cadeia. Cada prisioneiro faz a sua decisão sem saber que decisão o outro vai tomar, e nenhum tem certeza da decisão do outro. A questão que o dilema propõe é: o que vai acontecer? Como o prisioneiro vai reagir?"

|                         |           Prisioneiro "B" nega           |          Prisioneiro "B" delata          |
|-------------------------|:----------------------------------------:|:----------------------------------------:|
|   Prisioneiro "A" nega  |      Ambos são condenados a 6 meses      | "A" é condenado a 10 anos; "B" sai livre |
| Prisioneiro "A" delata  | "A" sai livre, "B" é condenado a 10 anos |       Ambos são condenados a 5 anos      |

Nosso projeto consiste em uma simulação desse cenário, onde os suspeitos são representados por agentes de software. Os agentes podem tomar decisões de cooperação ou traição.<br>

A simulação começa com metade dos agentes dispostos a trair e metade dispostos a cooperar, chamamos estes de agentes egoístas e altruístas, respectivamente. Então, em cada rodada, cada agente interage uma vez com cada vizinho seu, traindo ou cooperando. Após essa interação, o prisioneiro assume a estratégia(trair ou cooperar) do seu vizinho que está com o menor tempo de cadeia. Por fim, cada agente assume a posição de um de seus vizinhos. Dessa forma, podemos saber qual a estratégia que irá trazer um melhor resultado a longo prazo.

Para auxiliar na visualização da estratégia predominante, adicionamos um gráfico que faz o cálculo em tempo real do "Índice de Altruísmo", que se refere a porcentagem de prisioneiros que optaram por não delatar seus comparsas naquela rodada.



## Screenshots
Adicione 2 ou mais screenshots do projeto em termos de interface e/ou funcionamento.

## Instalação 
**Linguagens**: xxxxxx<br>
**Tecnologias**: xxxxxx<br>
Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários.
Insira um manual ou um script para auxiliar ainda mais.
Gifs animados e outras ilustrações são bem-vindos!

## Uso 
Explique como usar seu projeto.
Procure ilustrar em passos, com apoio de telas do software, seja com base na interface gráfica, seja com base no terminal.
Nessa seção, deve-se revelar de forma clara sobre o funcionamento do software.

## Vídeo
Adicione 1 ou mais vídeos com a execução do projeto.
Procure: 
(i) Introduzir o projeto;
(ii) Mostrar passo a passo o código, explicando-o, e deixando claro o que é de terceiros, e o que é contribuição real da equipe;
(iii) Apresentar particularidades do Paradigma, da Linguagem, e das Tecnologias, e
(iV) Apresentar lições aprendidas, contribuições, pendências, e ideias para trabalhos futuros.
OBS: TODOS DEVEM PARTICIPAR, CONFERINDO PONTOS DE VISTA.
TEMPO: +/- 15min

## Participações
Apresente, brevemente, como cada membro do grupo contribuiu para o projeto.
|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| -- | -- | -- |
| Fulano  |  Programação dos Fatos da Base de Conhecimento Lógica | Boa |

## Outros 
Quaisquer outras informações sobre o projeto podem ser descritas aqui. Não esqueça, entretanto, de informar sobre:
(i) Lições Aprendidas;
(ii) Percepções;
(iii) Contribuições e Fragilidades, e
(iV) Trabalhos Futuros.

## Fontes
Referencie, adequadamente, as referências utilizadas.
Indique ainda sobre fontes de leitura complementares.
