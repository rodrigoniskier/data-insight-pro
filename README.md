# Data Insight Pro

### CSV/XLSX → análise exploratória e dashboards interativos

**Data Insight Pro** é uma aplicação em Python que transforma planilhas e arquivos tabulares em uma visão exploratória pronta para análise.

O objetivo é reduzir o trabalho manual necessário para abrir um conjunto de dados, identificar indicadores úteis e produzir visualizações interativas.

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
