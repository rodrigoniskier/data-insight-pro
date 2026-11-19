# Data Insight Pro

### CSV/XLSX → análise exploratória e dashboards interativos

**Data Insight Pro** é uma aplicação em Python que transforma planilhas e arquivos tabulares em uma visão exploratória pronta para análise.

O objetivo é reduzir o trabalho manual necessário para abrir um conjunto de dados, identificar indicadores úteis e produzir visualizações interativas.

## Problema, público e resultado

**Problema.** Abrir uma planilha desconhecida e descobrir quais indicadores e padrões ela contém exige trabalho manual repetitivo.

**Para quem.** Analistas, gestores e estudantes que recebem arquivos CSV ou Excel e precisam de uma primeira leitura rápida dos dados (hipótese de desenho, não validada com usuários).

**O que entrega.** Envio de arquivos `.csv` e `.xlsx`, preparação dos dados, detecção de colunas numéricas, indicadores automáticos e gráficos interativos com filtros, tudo processado em memória durante a sessão.

**Tecnologias.** Python, Pandas, Streamlit, Plotly Express, OpenPyXL.

**Qualidade e evidências.** Projeto pequeno e focado; não há testes automatizados nem CI neste repositório.

## Funcionalidades

- upload de arquivos `.csv` e `.xlsx`;
- leitura e preparação dos dados com Pandas;
- detecção de colunas numéricas;
- geração automática de indicadores;
- gráficos interativos;
- filtros e exploração visual;
- processamento em memória;
- interface web com Streamlit.

## Stack

- **Python**
- **Streamlit**
- **Pandas**
- **OpenPyXL**
- **Plotly Express**

## Executar localmente

```bash
git clone https://github.com/rodrigoniskier/data-insight-pro.git
cd data-insight-pro

python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate  # Windows

pip install -r requirements.txt
streamlit run app.py
```

## Fluxo

```text
CSV / Excel
    ↓
Ingestão
    ↓
Preparação dos dados
    ↓
KPIs + estatísticas
    ↓
Visualizações interativas
```

## Privacidade

O desenho da aplicação prioriza processamento durante a sessão, sem exigir uma base de dados permanente para os arquivos enviados.

Para uso com dados sensíveis, a implantação deve ser revisada de acordo com as políticas de segurança e privacidade do ambiente em que estiver hospedada.

## Por que este projeto está no portfólio

Data Insight Pro mostra um fluxo completo e enxuto de **ingestão, transformação, análise e visualização de dados**, transformando tarefas que normalmente exigiriam várias etapas em planilhas em uma interface única.

---

Desenvolvido por [Rodrigo Niskier](https://github.com/rodrigoniskier).
