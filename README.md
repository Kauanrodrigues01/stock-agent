# 📊 Stock GPT - Agente Inteligente de Estoque

<p align="center">
  <img src="https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/images/projetos/stock-agent/page.png" width="70%">
</p>

Um agente conversacional inteligente que responde perguntas sobre o estoque de produtos utilizando um modelo de linguagem (LLM), consultas SQL e interface interativa com Streamlit.

---

## 🌎 Visão Geral

Este projeto implementa um **Agente de Estoque** com capacidades de raciocínio e interação com banco de dados. O sistema responde perguntas como:

* Quais produtos estão com baixo estoque?
* Qual o preço da placa de vídeo RTX 4080?
* Quais produtos precisam ser repostos?

Utilizando um **LLM (Large Language Model)** aliado ao padrão **ReAct (Reasoning + Acting)**, o agente consegue raciocinar, consultar o banco de dados com SQL e gerar uma resposta amigável ao usuário.

---

## 💡 Tecnologias Utilizadas

| Tecnologia                                  | Finalidade                                               |
| ------------------------------------------- | -------------------------------------------------------- |
| **[LangChain](https://www.langchain.com/)** | Orquestração do agente, ferramentas e execução via ReAct |
| **OpenAI GPT (via LangChain)**              | Modelo de linguagem responsável pelas respostas          |
| **Streamlit**                               | Interface de chat interativa                             |
| **SQLite**                                  | Banco de dados local com os dados do estoque             |
| **LangChain SQLDatabaseToolkit**            | Ferramenta que permite ao agente interagir com SQL       |
| **ReAct Agent**                             | Permite o agente pensar, agir com ferramentas e concluir |

---

## 🔎 Como Funciona

1. O usuário envia uma pergunta via chat no Streamlit.
2. A pergunta é formatada e passada para o agente.
3. O agente raciocina sobre a pergunta, decide qual ferramenta usar (neste caso, SQL).
4. Executa a consulta SQL no banco `estoque.db` via toolkit.
5. O modelo LLM formata a resposta e a apresenta ao usuário em português.

---

## ⚙️ Como Executar Localmente

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/stock-agent.git
cd stock-agent
```

### 2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Configure sua chave da OpenAI:

Crie um arquivo `.env`:

```
OPENAI_API_KEY=sk-sua-chave-aqui
```

### 5. Execute o app:

```bash
streamlit run app.py
```

---

## 🔌 Estrutura de Arquivos

```bash
.
├── app.py              # Interface em Streamlit
├── agent.py            # Lógica do agente (LLM + SQL + ReAct)
├── estoque.db          # Banco de dados SQLite com os produtos
├── requirements.txt    # Dependências
└── .env                # API Key da OpenAI
```
