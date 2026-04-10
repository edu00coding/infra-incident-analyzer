🛡️ Infrastructure Incident Analyzer

Este projeto automatiza o cruzamento de dados de inventário de ativos (CMDB) com logs de eventos de rede e segurança, permitindo a identificação rápida de incidentes críticos em ambientes de TI.
📋 Contexto do Projeto

Em ambientes de infraestrutura, é comum que logs de monitoramento venham de fontes variadas e em formatos complexos (como JSON aninhado). Este script resolve o desafio de consolidar essas informações, enriquecendo os logs com dados de hostname e setor, facilitando a tomada de decisão da equipe de Operações.
🚀 Funcionalidades Técnicas

    JSON Flattening: Uso de pd.json_normalize() para tratar estruturas de dados complexas dentro de logs.

    Data Enrichment: Realiza o merge (JOIN) entre a base de inventário e os eventos de erro usando chaves distintas (left_on e right_on).

    Tratamento de Dados: Identificação de hosts "fantasmas" (fora do inventário) e preenchimento de valores ausentes para hosts sem incidentes.

    Automação de Relatórios: Exportação filtrada de incidentes críticos para formato .csv para integração com ferramentas de ticketing.

🛠️ Tecnologias

    Python 3.12

    Pandas: Biblioteca principal para análise e manipulação.

    Conda/Venv: Gerenciamento de ambientes virtuais.

📊 Exemplo de Fluxo de Dados

    Entrada: Lista de dicionários (Inventário) e JSON estruturado (Logs).

    Processamento: Limpeza, união e filtragem via Pandas.

    Saída: Arquivo incidentes_graves.csv contendo apenas alertas que exigem ação imediata.

    
📖 Como Rodar

    Clone o repositório:
    Bash

git clone https://github.com/edu00coding/infra-incident-analyzer.git

Instale as dependências:
Bash

pip install -r requirements.txt

Execute o script:
Bash

python Troubleshooting_Infra.py
