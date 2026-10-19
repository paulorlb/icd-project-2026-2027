# Projeto ICD: publicações GOVCOPP (2020–2026)

Projeto de análise reprodutível das publicações associadas a investigadores do GOVCOPP. O notebook verifica os ficheiros de entrada, constrói a rede de coautoria e descreve as ligações entre grupos formais. A unidade de trabalho é esta pasta; todos os caminhos usados pelo notebook partem da raiz do projeto.

## Estrutura

```text
data/raw/              ficheiros recebidos, sem alterações manuais
data/processed/        dados produzidos por código
notebooks/W06S01_practice.ipynb
notebooks/aulas/       material de apoio da aula
src/icd_project/       funções reutilizáveis
outputs/coauthorship/  tabelas e figuras geradas pelo notebook
outputs/tables/        tabelas de outras análises
outputs/figures/       figuras de outras análises
```

## Preparar o ambiente

Abra esta pasta no VS Code e, num terminal na raiz do projeto, execute:

```powershell
conda env create -f environment.yml
conda activate icd-project
python -m pip install -e .
python -c "import sys; print(sys.executable)"
```

Se o ambiente já existir e `environment.yml` mudar, atualize-o com `conda env update -f environment.yml --prune`. No VS Code, escolha o interpretador e o kernel **icd-project**; confirme no notebook que `sys.executable` aponta para esse ambiente.

## Dados

Os três CSV foram fornecidos com este projeto. A [descrição original](data/raw/README.md) explica o conteúdo, as unidades de observação, os separadores e as limitações. A data de extração e os direitos de redistribuição não foram documentados. Por isso, os CSV permanecem em `data/raw/` localmente, mas são ignorados pelo Git.

Num clone novo, obtenha os ficheiros junto da equipa que forneceu o conjunto de dados e coloque-os, sem os abrir ou guardar novamente, em `data/raw/` com estes nomes:

| Ficheiro | SHA-256 da versão usada aqui |
|---|---|
| `authorship_2020_2026.csv` | `512f30215fe028935fc599667a6632e017f99f6d9f77f2892258e7f555c66338` |
| `publications_2020_2026.csv` | `badca2d7219a3f5b14a2c9f6f7b100a4c094ffe0dcbe6431a966a0471c3b7362` |
| `publications_authors_2020_2026.csv` | `526c9e6e3b3861f14ecaa6528a0eca5baf2c129c252b136df0b2f5dc2dbe538c` |

O notebook W06 usa os dois primeiros ficheiros. Correspondem, respetivamente, a `teaching_authorship_2020_2026_textual.csv` e `teaching_publications_2020_2026_textual.csv` da aula. O terceiro é uma tabela integrada opcional e usa `;` como separador, com uma primeira linha `sep=;`.

Estes CSV contêm um investigador no grupo `PI3`. A solução docente preservada localmente em `notebooks/aulas/` usa uma correção posterior para `PI2`; por isso, os totais gerais coincidem, mas algumas contagens entre grupos não coincidem. Essa solução e os seus resultados incorporados ficam fora do Git. O notebook do projeto usa as impressões digitais e os valores de referência dos ficheiros locais.

## Executar e verificar

1. Abra `notebooks/W06S01_practice.ipynb` com o kernel **icd-project**.
2. Faça **Restart Kernel → Run All**. O notebook encontra `environment.yml` a partir do diretório de trabalho, verifica os dados e os checkpoints, e grava os resultados.
3. Consulte `outputs/coauthorship/` e, se executar a extensão opcional, `outputs/coauthorship_min_weight_2/`. Estes ficheiros são gerados pelo notebook e não devem ser editados manualmente.

O notebook local em `notebooks/aulas/W06S01_practice_solution.ipynb` é a solução original da suite docente, preservada como referência e ignorada pelo Git. Espera ficheiros `teaching_*_textual.csv` e a afiliação corrigida. Num clone limpo, só o notebook adaptado está disponível.

## Limites e decisões

- Os totais de 2026 podem representar um ano incompleto; a data de extração não está disponível.
- `publication_id` identifica publicações; uma linha de autoria representa uma relação publicação–investigador. Um `merge` destas tabelas aumenta o número de linhas e não deve ser lido como número de publicações.
- Os CSV originais não são transformados. `data/processed/` e `outputs/` contêm apenas resultados regeneráveis. O Git regista código, documentação e notebooks, excluindo dados sem direitos de redistribuição estabelecidos, ambientes locais, segredos e saídas geradas.

## Registo de assistência por IA

| Data | Ferramenta e pedido | Efeito esperado | Verificação independente | Decisão |
|---|---|---|---|---|
| 2026-10-19 | Codex; organizar o projeto segundo a aula W05S01 | Caminhos portáveis, leitura uniforme dos CSV e resultados regeneráveis | Conferir SHA-256 dos originais; executar as células em ordem e validar contagens e chaves | Aceite após verificação |
