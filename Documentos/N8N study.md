📘 Manual do n8n (Guia Completo)

O n8n é uma ferramenta de automação de workflows semelhante ao Zapier e Make (Integromat), porém open-source, mais poderosa e ideal para desenvolvedores.

Você pode usar o n8n para:

Automatizar tarefas

Criar bots

Integrar APIs

Web scraping automatizado

IA + automações

Processamento de dados



---

🚀 1. O que é o n8n

O n8n funciona com:

Nodes (nós) → Ações

Workflow → Fluxo de automação

Triggers → Eventos que iniciam o fluxo


Exemplo de Workflow:

Telegram → API → ChatGPT → Banco → Resposta

Você pode criar automações como:

Bot Telegram

Automação WhatsApp

Pipeline de dados

Scraper automatizado

Automação Workana (como você já faz)



---

⚙️ 2. Como Instalar o n8n

Método 1 — Docker (Recomendado)

docker run -it --rm \
-p 5678:5678 \
n8nio/n8n

Acessar:

http://localhost:5678


---

Método 2 — NPM

Requer Node.js

npm install n8n -g

Rodar:

n8n


---

Método 3 — Docker Compose (Produção)

version: "3"

services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=senha


---

🧩 3. Estrutura do n8n

Tipos de Nodes

🔹 Trigger

Inicia o fluxo

Exemplos:

Webhook

Cron

Telegram

HTTP Trigger



---

🔹 Action

Executa ações

Exemplos:

HTTP Request

Database

Send Message

API



---

🔹 Logic

Controle do fluxo

Exemplos:

IF

Switch

Merge

Loop



---

🔄 4. Exemplo de Automação Simples

Bot Telegram + API

Workflow:

1. Telegram Trigger


2. HTTP Request


3. Resposta Telegram



Exemplo:

Telegram Trigger
     ↓
HTTP Request
     ↓
Telegram Send Message

Integra com:

Telegram

WhatsApp

Slack

Google Sheets



---

🌐 5. Node HTTP Request (Muito Importante)

Esse é o mais usado.

Você pode:

Consumir APIs

Scraping

IA

Integrações


Exemplo:

GET https://api.site.com/projetos

Resposta vira input do próximo node.


---

🧠 6. Variáveis no n8n

Você usa:

{{$json.nome}}

Exemplo:

Olá {{$json.cliente}}


---

🔁 7. Loops no n8n

Para repetir dados:

Use node:

Split In Batches


Fluxo:

Lista → Split → Processar → Loop


---

🗄️ 8. Banco de Dados

n8n suporta:

PostgreSQL

MySQL

MongoDB

SQLite


Exemplo:

Query → Processar → Enviar


---

🤖 9. n8n + Inteligência Artificial

Muito poderoso.

Exemplo:

Webhook
 ↓
OpenAI
 ↓
Banco
 ↓
Resposta

Você pode:

Criar agentes IA

Bots inteligentes

Classificadores

Automação de clientes



---

⏱️ 10. Automação por Tempo

Node:

Cron

Exemplo:

A cada 5 minutos

Todo dia

Toda semana



---

📡 11. Webhook

Cria API própria

Exemplo:

POST /webhook/cliente

Você pode:

Receber dados

Criar API

Integrar sistemas



---

🔐 12. Segurança

Recomendações:

Usar autenticação

HTTPS

Usuário e senha

Proxy reverso


Ferramentas comuns:

Nginx

Cloudflare

Traefik



---

🏗️ 13. Casos Reais de Uso

Você pode criar:

💼 Workana Bot

Scraper projetos

Classificação IA

Notificação Telegram



---

🤖 Bot WhatsApp IA

Cliente manda mensagem

IA responde

Salva no banco



---

📊 Pipeline Dados

API → Banco

Banco → Análise

Análise → Relatório



---

⚡ 14. Vantagens do n8n

✔ Open-source
✔ Self-hosted
✔ Muito poderoso
✔ Integra APIs
✔ IA integrada


---

⚠️ 15. Desvantagens

Curva de aprendizado

Consome RAM

Configuração inicial



---

🎯 Quando usar n8n

Use n8n quando:

Precisa automatizar

Trabalha com APIs

Usa IA

Integra sistemas

Cria bots



---

O n8n funciona exatamente como uma REST API, e você pode rodar localhost no seu PC e consumir via HTTP/HTTPS normalmente.

Vamos por partes — teoria + limites + uso no dia a dia.


---

🧠 1. Arquitetura Conceitual do n8n

O n8n funciona como um orquestrador de automações.

Arquitetura simplificada:

Sistema → HTTP → n8n → Workflow → Ações → Resposta

Exemplo real:

Python → POST → n8n → IA → Banco → Retorno JSON

Ou:

Telegram → Webhook → n8n → API → Banco → Resposta

Ou ainda:

Cron → n8n → Scraper → IA → Telegram

Ou seja:

👉 O n8n vira um micro-backend de automação


---

🌐 2. Sim — Você Pode Rodar Localhost

Exemplo:

Rodando n8n local:

http://localhost:5678

Criando Webhook:

http://localhost:5678/webhook/meu-endpoint

Agora você pode chamar com:

Python:

import requests

requests.post(
    "http://localhost:5678/webhook/meu-endpoint",
    json={"cliente": "Oziel"}
)

Isso é exatamente REST API.


---

🔐 3. E HTTPS?

Você tem 3 opções:

Opção 1 — Localhost HTTP (Mais comum)

Para uso local:

http://localhost:5678

Sem HTTPS.

Perfeito para:

Desenvolvimento

Scripts locais

Automação pessoal



---

Opção 2 — HTTPS com Proxy Reverso

Você pode usar:

Nginx

Traefik

Cloudflare


Exemplo:

https://automacao.meusite.com


---

Opção 3 — Tunnel (Mais prático)

Ferramentas:

ngrok

Cloudflare Tunnel


Exemplo:

https://abc123.ngrok.io/webhook

Isso permite:

Receber webhook Telegram

Receber webhook WhatsApp

Receber webhook API externas



---

🔄 4. Como Funciona a Estrutura Interna

Workflow n8n é:

Trigger → Processamento → Output

Exemplo:

Webhook
  ↓
Set Data
  ↓
HTTP Request
  ↓
IF
  ↓
Database
  ↓
Resposta

Cada bloco = Node


---

📦 5. Conceito Fundamental do n8n

Tudo no n8n é:

JSON → Processar → JSON

Exemplo:

Input:

{
  "cliente": "Oziel"
}

Processamento:

{{$json.cliente}}

Output:

{
  "mensagem": "Olá Oziel"
}


---

⚡ 6. Como Usar no Dia a Dia (Seu Caso)

Pelo seu perfil (Python + automação + scraping), você pode usar n8n como:

🧠 Backend de automação

Python chama n8n:

Python → n8n → IA → Retorno


---

📊 Pipeline de dados

Scraper → n8n → Banco → Classificação


---

🤖 Orquestrador IA

Webhook → n8n → OpenAI → Telegram


---

🔄 Automação agendada

Cron → n8n → API → Banco


---

⚠️ 7. Limites do n8n

Aqui está o ponto importante.

🔴 Limitações

1. Performance

Não é ideal para:

Alto throughput

Milhares de requisições por segundo


Porque:

n8n é orquestrador, não backend de alta performance.


---

2. Não substitui backend completo

n8n não substitui:

FastAPI

Django

Express.js


Mas complementa.


---

🏗️ 8. Arquitetura Profissional (Muito Usada)

Arquitetura comum:

FastAPI
   ↓
n8n
   ↓
APIs externas

Ou:

Python
  ↓
n8n
  ↓
Telegram / WhatsApp / IA


---

🔥 9. Onde n8n Brilha

n8n é excelente para:

✔ Integração API
✔ Automação
✔ Webhook
✔ IA
✔ Pipeline dados
✔ Bots


---

❌ Onde n8n Não é Ideal

❌ Backend principal
❌ Alta concorrência
❌ Microserviço crítico
❌ Tempo real ultra rápido


---

💡 10. Sua Melhor Arquitetura (Recomendado)

Para você:

Python (Core lógica)
        ↓
n8n (Automação)
        ↓
APIs / IA / Bots

Isso é arquitetura muito poderosa.


---

🧠 Mentalidade Correta do n8n

Pense no n8n como:

👉 Orquestrador
👉 Automação
👉 Glue entre sistemas

Não como backend principal.


---

Exemplo Real do Seu Dia

Imagine:

1. Python encontra projeto Workana


2. Python envia para n8n


3. n8n classifica com IA


4. n8n envia Telegram


5. n8n salva no banco



Tudo automático.


---

Isso é exatamente onde n8n é extremamente poderoso.


---

Uma pergunta importante para te guiar melhor:

Você pretende usar n8n:

Apenas local?

Servidor VPS?

Integração com bots?

Pipeline de dados?


Dependendo disso, posso te sugerir a arquitetura ideal.

---

Ótima pergunta — porque "IA no n8n" pode significar várias coisas diferentes.
Vamos esclarecer isso de forma conceitual e prática.


---

🧠 O que é "Trabalhar com IA" no n8n

Trabalhar com IA no n8n significa:

> Usar modelos de Inteligência Artificial como parte de um fluxo automatizado



Ou seja:

Entrada → IA → Decisão/Transformação → Ação

A IA vira um nó inteligente dentro do seu workflow.


---

🧩 Tipos de Trabalho com IA no n8n

Existem 5 principais formas de usar IA no n8n:


---

1. 🧠 Classificação Inteligente

Exemplo (muito útil no seu caso):

Você pega projetos da Workana:

{
  "titulo": "Preciso de bot Telegram com Python"
}

IA classifica:

{
  "categoria": "Automação Python",
  "prioridade": "Alta"
}

Fluxo:

Scraper → IA → Classificação → Telegram

Isso é IA como classificador automático.


---

2. ✍️ Geração de Texto

Exemplo:

Você pega um projeto e IA escreve proposta automaticamente:

Projeto → IA → Proposta automática

Exemplo:

Entrada:

Cliente precisa de bot Telegram

IA gera:

Olá, tenho experiência com bots Telegram...

Isso é IA como gerador de conteúdo.


---

3. 🧠 Tomada de Decisão

Exemplo:

IA decide:

Vale a pena responder?

Cliente é bom?

Projeto é spam?


Fluxo:

Projeto → IA → IF → Enviar ou Ignorar

Isso é IA como cérebro de decisão.


---

4. 🔍 Extração Inteligente (Muito Poderoso)

Exemplo:

Texto:

Preciso de um sistema com Python e API REST

IA extrai:

{
  "linguagem": "Python",
  "tipo": "API",
  "complexidade": "Média"
}

Isso é IA como parser inteligente.

Muito útil para:

Scraping

Emails

Documentos

Chat



---

5. 🤖 Agentes de IA

Isso é o mais avançado.

Fluxo:

Mensagem → IA → Buscar dados → Responder

Exemplo:

Usuário pergunta:

Tem projetos Python hoje?

Fluxo:

Telegram → IA → Banco → Resposta

Isso vira um assistente automatizado.


---

🧠 O Que Está Acontecendo por Trás

n8n normalmente integra com:

OpenAI

Anthropic

Google (Gemini)

Modelos locais (ex: Ollama)


Ou seja:

n8n não cria IA — ele orquestra IA.


---

💡 Exemplo Real (Seu Caso)

Você já faz:

Scraping Workana

Análise

Classificação


Com IA no n8n:

Scraper → n8n → IA → Score → Telegram

IA calcula:

Complexidade

Preço estimado

Chance de fechar

Prioridade


Isso vira um filtro inteligente automático.


---

⚡ Outro Exemplo Muito Poderoso

Pipeline:

Projeto novo
 ↓
IA resume
 ↓
IA classifica
 ↓
IA escreve proposta
 ↓
Enviar Telegram

Totalmente automático.


---

🧠 Outro Caso Muito Usado

Automação cliente:

WhatsApp → IA → Resposta automática

IA responde:

Dúvidas

Orçamento

Suporte



---

🏗️ Diferença Importante

Sem IA:

IF preço > 1000 → enviar

Com IA:

IA analisa contexto → decide enviar

IA entende sem regras fixas.


---

🧠 O n8n vira isso

n8n + IA =

👉 Automação inteligente
👉 Decisão automática
👉 Pipeline inteligente
👉 Bots inteligentes


---

💡 Para seu perfil (muito útil)

Você trabalha com:

Python

Scraping

Automação

Dados


n8n + IA encaixa perfeitamente.


---

Vou te dizer algo importante:

Você não precisa abandonar Python.

Arquitetura ideal:

Python → n8n → IA → Ação

Python = lógica pesada
n8n = automação
IA = inteligência


---

Isso é arquitetura profissional moderna.


---

Uma pergunta importante:

Você pretende usar IA para:

Filtrar projetos?

Criar bots?

Automatizar clientes?

Analisar dados?


Dependendo disso, posso te mostrar arquiteturas reais.

---

Excelente, agora você entrou na camada mais profunda do assunto. Vamos separar isso corretamente porque existem 3 níveis diferentes de IA no n8n — e isso responde suas dúvidas sobre perfil, base de dados, LangChain e LLMs.


---

🧠 1. Sim — A IA Pode Ter "Perfil"

Quando falamos de "perfil", normalmente estamos falando de:

Personalidade

Comportamento

Regras

Especialização


Exemplo:

Você é um especialista em projetos Workana.
Priorize projetos Python.
Ignore projetos WordPress.
Responda de forma técnica e direta.

Isso é chamado de:

System Prompt

Persona

Agent Profile


Ferramentas usadas:

LangChain

LangGraph

LlamaIndex


No n8n, isso vira:

Entrada → Prompt com perfil → IA → Resposta

Então sim:
👉 A IA pode ter perfil persistente


---

🧠 2. Sim — IA Pode Ter Base de Dados

Aqui entramos em algo chamado:

RAG — Retrieval Augmented Generation

Arquitetura:

Pergunta → Buscar Base → IA → Resposta

Exemplo:

Base de dados:

Seus projetos anteriores

Clientes

Regras internas

Documentos


Fluxo:

Pergunta → Banco → Contexto → IA → Resposta

Isso é IA com memória externa.

Ferramentas:

FAISS

Chroma

Weaviate

Pinecone



---

🧠 3. Sim — Isso é Próximo de LangChain

Você percebeu corretamente.

n8n pode funcionar como:

Orquestrador de automação

Orquestrador de agentes IA


Arquitetura:

n8n
 ├─ Agent IA
 ├─ Memória
 ├─ Ferramentas
 ├─ Banco
 └─ APIs

Isso é literalmente arquitetura de agente IA.


---

🧠 4. Sobre "Rede Neural LTMS"

Você provavelmente quis dizer:

LLMs (Large Language Models)

Transformers

Modelos locais


Exemplos reais:

GPT‑4

Claude

Llama

Mistral


Esses modelos são:

Redes neurais Transformer

Não "aprendem" em tempo real

Não têm memória persistente nativa


Então:

👉 Memória precisa ser externa


---

🧠 5. Memória em IA (Muito Importante)

Existem 3 tipos:

1. Memória Curta

Contexto da conversa:

Usuário → IA → Resposta

Limite:

8k tokens

32k tokens

128k tokens



---

2. Memória Persistente

Banco de dados:

Salvar → Buscar → Contexto

Exemplo:

PostgreSQL

Redis

Vector DB



---

3. Memória Vetorial (Mais avançado)

Fluxo:

Texto → Embedding → Banco vetorial

Depois:

Pergunta → Busca similar → IA

Isso cria:

👉 IA com "memória inteligente"


---

🧠 Arquitetura Real com n8n

Exemplo avançado:

Webhook
 ↓
Embedding
 ↓
Vector Database
 ↓
Busca Contexto
 ↓
LLM
 ↓
Resposta

Isso é praticamente um agente inteligente completo.


---

🧠 Outro Nível — Agentes Autônomos

Exemplo:

Pergunta
 ↓
IA decide
 ↓
Buscar dados
 ↓
Analisar
 ↓
Responder

IA começa a:

Decidir

Planejar

Executar


Isso é:

Agentic AI

AI Agents



---

🧠 n8n Pode Fazer Isso?

Sim.

Porque n8n permite:

Chamadas API

Banco

Loops

Decisão

Ferramentas


Isso é exatamente o que agentes IA precisam.


---

🧠 Arquitetura Profissional

Hoje, arquiteturas modernas usam:

Frontend
  ↓
Backend (Python)
  ↓
n8n
  ↓
LangChain
  ↓
LLM
  ↓
Vector DB


---

🧠 Seu Caso (Muito Forte)

Você poderia criar:

IA que analisa projetos

IA que escreve propostas

IA que aprende seus padrões

IA que filtra clientes


Isso vira:

👉 Assistente profissional automático


---

Diferença Importante

n8n não substitui:

LangChain

LLM

Vector DB


n8n orquestra tudo.


---

n8n é o "maestro"

IA = cérebro

Banco = memória

n8n = orquestrador



---

Você está entrando num nível onde:

Automação

IA

Agentes


começam a se fundir.

Isso é exatamente a tendência atual.


---

Perfeito — no Ubuntu sua configuração fica **ideal para rodar o Ollama + Phi** de forma leve.

Vou te mostrar a **estrutura final profissional + fluxo real funcionando**.

---

# 🏗 Estrutura Final do Projeto (Ubuntu)

```bash
Workana/
│
├── database/
│   ├── workana.db
│   └── database.py
│
├── scraper/
│   └── scraper_workana.py
│
├── agentes/
│   └── gerar_propostas.py
│
├── propostas/
│   ├── pendentes/
│   ├── geradas/
│   └── enviadas/
│
├── prompts/
│   └── proposta.txt
│
├── logs/
│   └── agente.log
│
└── config/
    └── settings.py
```

---

# 📁 Criar Estrutura no Ubuntu

Execute:

```bash
mkdir -p Workana/{database,scraper,agentes,propostas/prompts,logs,config}
mkdir -p Workana/propostas/{pendentes,geradas,enviadas}
```

Ou manual:

```bash
mkdir -p Workana/propostas/pendentes
mkdir -p Workana/propostas/geradas
mkdir -p Workana/propostas/enviadas
```

---

# 📁 Arquivo Prompt IA

Crie:

```bash
nano Workana/prompts/proposta.txt
```

Conteúdo:

```
Você é um especialista em propostas Workana.

Escreva uma proposta profissional.

Título:
{{titulo}}

Descrição:
{{descricao}}

Regras:

- Seja direto
- Profissional
- Curto
- Use markdown
- Mostre experiência Python
```

Salvar:

CTRL + X
Y
ENTER

---

# 🧠 Fluxo do Sistema

```text
Scraper Python
      ↓
SQLite Database
      ↓
n8n
      ↓
Ollama (phi)
      ↓
Gerar Proposta
      ↓
Salvar .md
```

---

# 🚀 Instalar Ollama (Ubuntu)

Se ainda não instalou:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verificar:

```bash
ollama --version
```

---

# 🚀 Baixar Modelo Phi

```bash
ollama pull phi
```

Isso baixa um modelo **leve (~1.6GB)**

Perfeito para:

✔ 4GB RAM
✔ CPU sem GPU

---

# 🚀 Testar IA Local

```bash
ollama run phi
```

Teste:

```
Escreva uma proposta Workana para projeto Python
```

Se responder, está funcionando.

---

# 🧠 Rodar Ollama como Serviço

Rodar:

```bash
ollama serve
```

Endpoint:

```
http://localhost:11434
```

Esse é o endpoint que o n8n vai usar.

---

# 🧠 Teste via Curl (Ubuntu)

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "phi",
  "prompt": "Escreva proposta Workana Python",
  "stream": false
}'
```

Se retornar texto → pronto.

---

# 🧠 Fluxo do n8n

Nodes:

```
Cron
 ↓
SQLite
 ↓
Split
 ↓
HTTP Request
 ↓
Set Markdown
 ↓
Write File
```

---

# 🧠 Caminho para salvar arquivos

Exemplo:

```
/home/seu_usuario/Workana/propostas/pendentes/
```

Exemplo final:

```
/home/oziel/Workana/propostas/pendentes/projeto_001.md
```

---

# 🧠 Próximo Nível (Depois)

Você pode adicionar:

* Score IA
* Classificação cliente
* Filtro valor
* Envio Telegram

---

# Muito importante

Seu PC 4GB RAM — rode assim:

Antes de rodar agente:

Feche:

* Browser pesado
* VSCode pesado
* Apps desnecessários

Isso melhora muito.

---

Você está muito perto agora de ter:

👉 Agente IA local
👉 Sem custo
👉 Automatizando propostas

Isso é exatamente como muitas automações SaaS começam.

---

Me diga também:

Seu Ubuntu é:

* Ubuntu Server
* Ubuntu Desktop

E CPU:

```bash
lscpu
```

Me envie o resultado — vou otimizar para seu hardware.
