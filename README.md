# 🚀 Workana Intelligent Prospecting Bot

Sistema automatizado de prospecção de clientes na plataforma Workana, com filtragem inteligente e envio automático de oportunidades via Telegram.

---

# 📌 Visão Geral

Este projeto foi desenvolvido para automatizar a busca por projetos qualificados na Workana, filtrando oportunidades com base em critérios definidos e enviando alertas personalizados para clientes ativos.

O sistema atua como um pipeline completo de dados:

```
Scraping → Banco de Dados → Filtro Inteligente → Notificação Telegram
```

---

# 🧠 Principais Funcionalidades

* Scraping automático da Workana
* Armazenamento em banco SQLite
* Filtro por qualidade do cliente
* Matching por palavras-chave
* Evitar projetos duplicados
* Envio automático via Telegram
* Sistema escalável e modular

---

# 🏗️ Arquitetura do Projeto

```
Workana/
│
├── Bot/
│   ├── Site/
│   │   └── SBot.py
│   │
│   ├── Telegram/
│   │   └── BurnTheWitch.py
│   │
│   ├── filtro.py
│   ├── database.py
│   └── scheduler.py
│
├── workana.db
└── README.md
```

---

# ⚙️ Como Funciona

## 1. Scraping

O sistema acessa automaticamente a plataforma Workana utilizando Selenium e coleta:

* Título do projeto
* Link
* Descrição
* Cliente verificado
* Histórico de pagamento
* Histórico do cliente

---

## 2. Banco de Dados

O projeto utiliza SQLite com duas tabelas principais:

### Tabela Projetos

| Campo              | Descrição           |
| ------------------ | ------------------- |
| id                 | Identificador único |
| titulo             | Título do projeto   |
| link               | Link do projeto     |
| descricao          | Descrição completa  |
| hash_id            | Identificador único |
| cliente_verificado | Cliente verificado  |
| cliente_pagamento  | Histórico pagamento |
| cliente_historico  | Histórico cliente   |
| enviado            | Controle envio      |

---

### Tabela Clientes

| Campo          | Descrição          |
| -------------- | ------------------ |
| id             | Identificador      |
| nome           | Nome cliente       |
| telegram_id    | ID Telegram        |
| palavras_chave | Palavras interesse |
| ativo          | Cliente ativo      |

---

# 🔍 Filtro Inteligente

O sistema realiza matching baseado em:

* Palavras-chave do cliente
* Cliente verificado
* Histórico de pagamento
* Projetos ainda não enviados

Isso garante envio apenas de oportunidades relevantes.

---

# 🤖 Automação

O sistema roda automaticamente utilizando:

* APScheduler
* Execução periódica
* Pipeline automatizado

Fluxo:

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

# 🛠️ Tecnologias Utilizadas

* Python 3.13
* SQLite
* Selenium
* APScheduler
* Telegram Bot API
* Pandas

---

# 🚀 Instalação

## 1. Clonar repositório

```
git clone https://github.com/seu-usuario/workana-bot.git

cd workana-bot
```

---

## 2. Criar ambiente virtual

```
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Instalar dependências

```
pip install -r requirements.txt
```

---

# ▶️ Executando o Projeto

## Inicializar banco

```
python database.py
```

---

## Rodar Scraper

```
python Bot/Site/SBot.py
```

---

## Rodar Bot Telegram

```
python Bot/Telegram/BurnTheWitch.py
```

---

# 📈 Roadmap

* [ ] Dashboard Web
* [ ] Machine Learning Ranking
* [ ] Sistema SaaS multi-clientes
* [ ] API REST
* [ ] Integração CRM

---

# 🎯 Objetivo do Projeto

Transformar a prospecção manual de clientes em um processo:

* Automatizado
* Inteligente
* Escalável
* Personalizado

---

# 👨‍💻 Autor

Oziel Ramos
Data Science | Automação | Bots | Python

---

# 📄 Licença

MIT License

---

# ⭐ Contribuição

Pull requests são bem-vindos. Para mudanças maiores, abra uma issue primeiro.

---

# 💡 Observação

Este projeto está em evolução contínua e preparado para escalar para um produto SaaS completo.

---

# 🚀 Status do Projeto

🟢 Em desenvolvimento ativo

---

# 📬 Contato

Caso queira conversar sobre automação ou projetos similares, entre em contato.

---

# ⭐ Se este projeto foi útil, deixe uma estrela no repositório

---
