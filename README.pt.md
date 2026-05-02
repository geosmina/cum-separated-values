> 🇬🇧 [English version](README.md)

# _Cum‑Separated Values_: A _Alt‑Right_ e o Movimento pela Retenção Seminal

[![DOI](https://zenodo.org/badge/1227319717.svg)](https://doi.org/10.5281/zenodo.19980653)

Este repositório contém o corpus, o relatório do IRaMuTeQ e o script de processamento dos dados utilizados no resumo expandido “_Cum‑Separated Values_: A _Alt‑Right_ e o Movimento pela Retenção Seminal” de Robert de Amorim Pontes e Victor Gabriel de Almeida Pedra.

## Sobre o estudo

O estudo propõe a metáfora psicanalítica dos **Cum‑Separated Values** (Valores Separados por Gozo) para examinar como a tabulação do gozo corporal espelha estratégias neurótico‑obsessivas de controle e ressoa com o discurso de pureza identitária da _alt‑right_.

A hipótese é de que existe uma homologia estrutural entre a economia psíquica do movimento digital de retenção seminal e o discurso de pureza identitária que alimenta a _alt‑right_. O artigo não afirma uma filiação política direta dos membros da comunidade, mas aponta uma lógica compartilhada de separação e controle: a mesma vírgula que separa dados em um arquivo `*.csv` é usada para separar e gerir a energia do corpo, e essa lógica ecoa a retórica de policiamento de fronteiras dos movimentos de extrema‑direita.

## Como os dados sustentam a hipótese

A análise do IRaMuTeQ (método Reinert / CHD) particionou o discurso em quatro classes. As duas classes principais revelam a estrutura central:

- **Classe 3 — Ameaça Externa e Capital Vital (84,7% dos segmentos):** Dominada por termos como *woman* (mulher), *energy* (energia), *power* (poder), *life* (vida), *sperm* (esperma) e *addiction* (vício). Esta classe retrata uma visão de mundo sitiada, onde o feminino, a pornografia e qualquer forma de vazamento ameaçam a essência vital masculina.

- **Classe 4 — Métricas Biológicas (14,5%):** Fortemente caracterizada por *testosterone* (testosterona), *test* (teste), *level* (nível), *increase* (aumento), *lab* (laboratório), *diet* (dieta) e *streak* (sequência). Reflete uma obsessão por quantificar, monitorar e otimizar o corpo – uma verdadeira “planilha de si” que tenta tornar o gozo administrável.

A alta taxa de classificação (94,9% dos segmentos retidos) indica um léxico altamente coeso e repetitivo, consistente com uma comunidade estruturada em torno de um discurso dogmático e autorreferente. O grafo de similitude confirma que termos relacionados ao tempo (*day*, *streak*, *time*) formam a espinha dorsal de estabilidade, enquanto *woman* e *addiction* aparecem como agentes de instabilidade sistêmica.

Esses achados fornecem evidência lexical para a metáfora dos *Cum‑Separated Values*: o corpus se organiza em torno de delimitar o que está dentro (energia acumulada, métricas, disciplina) e o que está fora (mulheres, pornografia, perda). A homologia com o discurso da *alt‑right* é traçada teoricamente — com apoio das referências citadas no artigo – e não por sobreposição direta de usuários ou análise cruzada de comunidades, o que está além do escopo de um resumo expandido.

## Conteúdo do repositório

| Caminho | Descrição |
|---------|-----------|
| `main.py` | Script Python para limpar e compilar as exportações das threads do Reddit. |
| `jsons/` | Exportações JSON brutas dos 10 tópicos mais engajados do r/Semenretention. |
| `corpus_iramuteq.txt` | Corpus textual final formatado para o IRaMuTeQ. |
| `RAPPORT.txt` | Relatório da análise léxica do IRaMuTeQ (método Reinert / CHD). |
| `README.md` | Este arquivo (versão em português). |
| `README.pt.md` | Versão em inglês deste readme. |

## Como os dados foram obtidos

1. **Seleção**: Foram identificados os 10 tópicos com maior engajamento histórico (Top All Time) do **r/Semenretention** (acesso em maio de 2026). Os tópicos selecionados e utilizados foram:
   - [Tópico 1](https://www.reddit.com/r/Semenretention/comments/m1eo4u/the_modern_struggle/)
   - [Tópico 2](https://www.reddit.com/r/Semenretention/comments/frvg29/semen_retention_the_good_the_bad_and_the_ugly/)
   - [Tópico 3](https://www.reddit.com/r/Semenretention/comments/mme87s/cultivating_a_high_sexual_charge/)
   - [Tópico 4](https://www.reddit.com/r/Semenretention/comments/nocbbe/female_attraction_explained/)
   - [Tópico 5](https://www.reddit.com/r/Semenretention/comments/wsu60w/300_day_semen_retention_streak_free_testosterone/)
   - [Tópico 6](https://www.reddit.com/r/Semenretention/comments/n0dcmi/nikola_teslas_attitude_on_sex_1935/)
   - [Tópico 7](https://www.reddit.com/r/Semenretention/comments/hod39f/why_the_elites_want_you_to_keep_ejaculating/)
   - [Tópico 8](https://www.reddit.com/r/Semenretention/comments/jcxr46/mike_tysons_own_words_on_sex/)
   - [Tópico 9](https://www.reddit.com/r/Semenretention/comments/lux0jo/on_a_good_streak_cannot_sit_still_overload_of/)
   - [Tópico 10](https://www.reddit.com/r/Semenretention/comments/l23ire/a_quick_and_easy_explanation_for_the_benefits_of/)
   
2. **Download**: Cada tópico (post original + todos os comentários aninhados) foi exportado como um único arquivo JSON usando a ferramenta gratuita [Reddinbox Download Reddit Thread](https://reddinbox.com/free-tools/download-reddit-thread).  
   - Cole a URL do tópico → clique em **Download** → salve o arquivo `*.json`.  
   - Repita para todos os tópicos.
3. Os arquivos JSON resultantes estão na pasta `jsons/` deste repositório.

## Ambiente e execução

O script requer **Python 3.12** e utiliza apenas a biblioteca padrão (`json`, `re`, `os`).  
Recomendamos o gerenciamento do ambiente com o [**uv**](https://docs.astral.sh/uv/).

### Configuração com uv

```bash
# Instale o uv, se necessário: https://docs.astral.sh/uv/
uv python install 3.12           # garanta o Python 3.12 disponível
```

Em seguida, execute o script:

```bash
uv run python main.py
```

O script lê todos os arquivos `*.json` da pasta `jsons/` e gera `corpus_iramuteq.txt`.
Durante a execução, ele informa o número de arquivos processados e de segmentos de texto.

## Detalhes da análise no IRaMuTeQ

O corpus foi analisado com o [IRaMuTeQ (v0.8 alpha 7)](https://pratinaud.gitpages.huma-num.fr/iramuteq-website/) utilizando os seguintes parâmetros:

- **Tamanho do segmento (ST):** ~20 palavras.
- **Lematização:** dicionário nativo em inglês.
- **Tamanho mínimo de classe na CHD:** 13 segmentos de texto.
- **Visualizações:** dendrograma e grafo de similitude (omitidos do artigo por limite de páginas e limitação quanto ao uso de imagens e/ou tabelas, mas disponíveis na saída interativa do software).

O relatório estatístico completo está em `RAPPORT.txt`. Ele inclui:

- Valores de qui‑quadrado (χ²) para cada termo por classe.
- Tamanhos e proporções das classes.
- Listas completas de termos com contribuições.

O resumo expandido discute apenas as duas classes dominantes (3 e 4) porque as outras duas (1 e 2) continham cerca de 0,7% dos segmentos e eram residuais (vocabulário nutricional, recomendações de livros).

## Como citar este repositório

Ao utilizar este conjunto de dados ou código, cite‑o como:

> Pontes, Robert de Amorim; Pedra, Victor Gabriel de Almeida. **_Cum‑Separated Values_: A _alt‑right_ e o movimento pela retenção seminal** [Conjunto de dados e código]. Zenodo. DOI: 10.5281/zenodo.19980653. Disponível em: [https://doi.org/10.5281/zenodo.19980653](https://doi.org/10.5281/zenodo.19980653).

## Licença

Este trabalho está licenciado sob a Licença Creative Commons - Atribuição - Não Comercial - Compartilhamento pela mesma Licença 4.0 Internacional. Para ver uma cópia desta licença, visite [http://creativecommons.org/licenses/by-nc-sa/4.0/](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## Contato

Dúvidas? Abra uma issue neste repositório ou entre em contato com os autores.
