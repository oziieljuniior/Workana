# Sistema Inteligente de Prospecção de Clientes — Workana Bot

## Visão Geral

Desenvolvi um **sistema automatizado de prospecção de clientes** voltado para a plataforma Workana, com objetivo de **identificar oportunidades qualificadas, filtrar clientes relevantes e enviar alertas personalizados via Telegram**.

O projeto foi construído com foco em:

* Automação de prospecção
* Filtragem inteligente de clientes
* Evitar duplicações
* Escalabilidade
* Integração com mensageria

O sistema funciona como um **pipeline de dados completo**, desde a coleta até a notificação.

---

# Arquitetura do Sistema

O sistema foi dividido em módulos independentes:

```
Bot/
 ├── Site/ (Scraping Workana)
 ├── database.py (Banco SQLite)
 ├── filtro.py (Lógica de análise)
 ├── telegram.py (Envio mensagens)
 ├── scheduler.py (Automação)
```

Essa arquitetura modular permite fácil manutenção e escalabilidade.

---

# Pipeline do Sistema

O fluxo de funcionamento:

1. Scraping de projetos na Workana
2. Armazenamento no banco SQLite
3. Filtro de clientes ativos
4. Matching por palavras-chave
5. Envio automático via Telegram
6. Marcação de projetos enviados

---

# Banco de Dados

Foi implementado um banco SQLite com duas tabelas principais:

## Tabela Projetos

Campos:

* id — Identificador único
* titulo — Nome do projeto
* link — URL do projeto
* descricao — Descrição completa
* hash_id — Identificador único para evitar duplicações
* cliente_verificado — Cliente verificado pela plataforma
* cliente_pagamento — Histórico de pagamento
* cliente_historico — Histórico de contratações
* enviado — Controle de envio

Essa estrutura permite **análise de qualidade do cliente antes do envio**.

## Tabela Clientes

Campos:

* id — Identificador do cliente
* nome — Nome do cliente
* telegram_id — ID do Telegram
* palavras_chave — Palavras de interesse
* ativo — Status ativo/inativo

Isso permite **prospecção personalizada para cada cliente**.

Como definido no código do sistema, os clientes ativos são filtrados automaticamente:


```python
SELECT id, nome, telegram_id, palavras_chave
FROM clientes
WHERE ativo = 1
```

---

# Filtro Inteligente

O sistema utiliza:

* Palavras-chave por cliente
* Clientes verificados
* Histórico de pagamento
* Projetos não enviados

Isso cria um **sistema de recomendação de oportunidades**.

---

# Automação

O sistema roda automaticamente utilizando:

* Scheduler (APScheduler)
* Execução periódica
* Pipeline automatizado

Fluxo automático:

```
Scheduler
    ↓
Scraper
    ↓
Database
    ↓
Filtro
    ↓
Telegram
```

---

# Tecnologias Utilizadas

* Python 3.13
* SQLite
* Selenium
* APScheduler
* Telegram Bot API
* Pandas (análise de dados)

---

# Principais Funcionalidades

✔ Scraping automático da Workana
✔ Filtro por qualidade de cliente
✔ Matching por palavras-chave
✔ Banco de dados estruturado
✔ Evitar duplicação de projetos
✔ Notificação automática Telegram
✔ Sistema escalável

---

# Diferenciais Técnicos

* Arquitetura modular
* Pipeline de dados automatizado
* Filtro inteligente por cliente
* Sistema de prospecção ativo
* Preparado para múltiplos clientes

---

# Resultado

O sistema transforma a prospecção manual em:

* Automática
* Inteligente
* Escalável
* Personalizada

Reduzindo significativamente o tempo de busca por oportunidades qualificadas.

---

# Possíveis Expansões

* Machine Learning para ranking de projetos
* Dashboard analítico
* Integração com CRM
* Sistema SaaS multi-usuário

---

# Tipo de Projeto

Automação | Data Engineering | Web Scraping | Bots | SaaS

---
