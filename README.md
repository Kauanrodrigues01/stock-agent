# 🤖 Stock GPT - Assistente Inteligente de Estoque

<p align="center">
  <img src="https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/images/projetos/stock-agent/page.png" width="70%">
</p>

<p align="center">
  <strong>Um chatbot inteligente que responde perguntas sobre estoque usando IA e linguagem natural</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img alt="LangChain" src="https://img.shields.io/badge/LangChain-2E86C1?style=for-the-badge&logo=langchain&logoColor=white">
  <img alt="OpenAI" src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white">
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
</p>

---

## 🌟 Sobre o Projeto

O **Stock GPT** é uma aplicação web inteligente que permite aos usuários fazer consultas sobre estoque de produtos utilizando **linguagem natural**. Desenvolvido com **Streamlit** e **LangChain**, o sistema utiliza modelos de IA da OpenAI para interpretar perguntas e fornecer respostas precisas através de consultas SQL automatizadas.

### 🎯 Principais Características

- 🗣️ **Conversação Natural**: Faça perguntas como se estivesse falando com um especialista
- 🧠 **IA Avançada**: Suporte para GPT-3.5, GPT-4 e GPT-4-turbo
- 📊 **Análises Inteligentes**: Relatórios automáticos sobre estoque e produtos
- 🇧🇷 **Interface em Português**: Totalmente localizada para o Brasil
- ⚡ **Respostas Rápidas**: Consultas otimizadas para máxima performance

---

## ✨ Funcionalidades

### 💬 Chat Inteligente
- Interface conversacional intuitiva
- Histórico de conversas durante a sessão
- Respostas contextualmente relevantes

### 🎛️ Controles Avançados
- **Seleção de Modelo**: Escolha entre GPT-3.5, GPT-4 e GPT-4-turbo
- **Controle de Temperature**: Ajuste a criatividade das respostas (0.0 - 2.0)
- **Configuração em Tempo Real**: Mudanças aplicadas instantaneamente

### 📈 Consultas Suportadas
- 📦 Status e quantidade de produtos em estoque
- 💰 Informações de preços e valores
- 🏷️ Consultas por categoria, marca ou fornecedor
- 📊 Relatórios de entrada e saída de produtos
- 🔍 Busca por produtos específicos
- ⚠️ Identificação de produtos com estoque baixo

---

## 🛠️ Tecnologias Utilizadas

### 🧩 Stack Principal

| Tecnologia | Finalidade | Versão |
|------------|------------|---------|
| **[Streamlit](https://streamlit.io/)** | Interface web interativa | 1.46.0 |
| **[LangChain](https://www.langchain.com/)** | Framework para LLM e agentes | latest |
| **[OpenAI](https://openai.com/)** | Modelos de linguagem GPT | API v1 |
| **[SQLite](https://sqlite.org/)** | Banco de dados local | built-in |
| **[Python Decouple](https://pypi.org/project/python-decouple/)** | Gerenciamento de variáveis | 3.8 |

### 🔄 Arquitetura do Sistema

```
Usuário → Streamlit → LangChain Agent → OpenAI GPT → SQL Toolkit → SQLite → Resposta
```

1. **Interface**: Streamlit para chat responsivo
2. **Processamento**: LangChain com padrão ReAct
3. **IA**: Modelos GPT para compreensão e geração
4. **Dados**: SQLite com toolkit automatizado

---

## 📁 Estrutura do Projeto

```
stock-agent/
├── 📄 app.py              # Interface principal do Streamlit
├── 🤖 agent.py            # Lógica do agente de IA e conexão com banco
├── 🗄️ estoque.db          # Banco SQLite com dados de estoque (12 produtos)
├── 📋 requirements.txt    # Dependências do projeto
├── 📚 README.md          # Documentação completa
└── 🔧 .env               # Variáveis de ambiente (criar)
```

### 📊 Estrutura do Banco de Dados

O banco `estoque.db` contém **18 tabelas** com dados completos de estoque:

**Tabelas Principais:**
- **`products_product`**: Catálogo com 12 produtos
- **`categories_category`**: Categorias dos produtos
- **`brands_brand`**: Marcas disponíveis
- **`suppliers_supplier`**: Fornecedores cadastrados
- **`inflows_inflow`**: Histórico de entradas
- **`outflows_outflow`**: Histórico de saídas

**Tabelas de Sistema:**
- Autenticação Django (users, groups, permissions)
- Sistema de migrations e sessões
- Logs administrativos

---

## 🚀 Instalação e Configuração

### 📋 Pré-requisitos

- **Python 3.8+** instalado
- **Chave da API OpenAI** ([Obter aqui](https://platform.openai.com/api-keys))
- **Git** para clonagem do repositório

### 🔧 Instalação Passo a Passo

#### 1️⃣ Clone o repositório
```bash
git clone https://github.com/Kauanrodrigues01/stock-agent.git
cd stock-agent
```

#### 2️⃣ Crie um ambiente virtual
```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

#### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
OPENAI_API_KEY=sua_chave_da_api_openai_aqui
```

#### 5️⃣ Execute a aplicação
```bash
streamlit run app.py
```

🎉 **Pronto!** A aplicação estará disponível em `http://localhost:8501`

---

## 💡 Como Usar

### 🎮 Interface do Usuário

1. **Acesse** `http://localhost:8501` no navegador
2. **Configure** o modelo de IA na barra lateral
3. **Ajuste** a temperatura para controlar criatividade
4. **Digite** sua pergunta no chat
5. **Receba** respostas inteligentes baseadas nos dados

### 🗨️ Exemplos de Perguntas

#### 📊 Consultas Básicas
```
🔍 "Quantos produtos temos em estoque?"
💰 "Qual o produto mais caro?"
📦 "Mostrar produtos com estoque baixo"
🏷️ "Listar produtos por categoria"
```

#### 📈 Consultas Avançadas
```
💵 "Qual o valor total do estoque?"
🔄 "Produtos que precisam ser repostos"
📊 "Relatório de produtos mais vendidos"
🏪 "Produtos do fornecedor específico"
```

#### 🎯 Consultas Específicas
```
🎮 "Informações sobre placas de vídeo"
💾 "Preço das memórias RAM disponíveis"
⚡ "Processadores Intel em estoque"
🖥️ "Produtos da categoria hardware"
```

---

## ⚙️ Configurações Avançadas

### 🧠 Modelos de IA Disponíveis

| Modelo | Velocidade | Qualidade | Custo | Recomendado para |
|--------|------------|-----------|-------|------------------|
| **GPT-3.5-turbo** | ⚡⚡⚡ | ⭐⭐⭐ | 💰 | Consultas rápidas e diretas |
| **GPT-4** | ⚡⚡ | ⭐⭐⭐⭐⭐ | 💰💰💰 | Análises complexas |
| **GPT-4-turbo** | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | 💰💰 | Uso geral (recomendado) |

### 🌡️ Controle de Temperature

- **0.0 - 0.3**: Respostas determinísticas e precisas
- **0.4 - 0.7**: Equilibrio entre precisão e criatividade *(padrão: 0.5)*
- **0.8 - 1.0**: Respostas mais criativas e variadas
- **1.1 - 2.0**: Máxima criatividade (menos precisão)

---

## 🔍 Como Funciona Internamente

### 🔄 Fluxo de Processamento

```
👤 Usuário → 💬 Pergunta → 🤖 Agent ReAct → 🧠 LLM → 🔧 SQL Tools → 🗄️ SQLite → ✨ Resposta
```

### 🧩 Componentes Técnicos

1. **ReAct Agent**: Padrão Reasoning + Acting para tomada de decisões
2. **SQL Database Toolkit**: Converte linguagem natural em SQL
3. **OpenAI LLM**: Processa e formata respostas amigáveis
4. **Streamlit Interface**: Apresentação interativa e responsiva

### 📝 Prompt Engineering

O sistema utiliza um prompt especializado que:
- Instrui o agente a usar ferramentas SQL
- Garante respostas em português brasileiro
- Formata saídas de forma amigável
- Mantém contexto da conversa

---

## 🤝 Contribuição

Contribuições são muito bem-vindas! 🎉

### 🔄 Como Contribuir

1. **Fork** o projeto
2. **Crie** uma branch para sua feature
   ```bash
   git checkout -b feature/MinhaNovaFeature
   ```
3. **Commit** suas mudanças
   ```bash
   git commit -m 'Adiciona MinhaNovaFeature'
   ```
4. **Push** para a branch
   ```bash
   git push origin feature/MinhaNovaFeature
   ```
5. **Abra** um Pull Request

### 🐛 Reportar Issues

Encontrou um problema? [Crie uma issue](https://github.com/Kauanrodrigues01/stock-agent/issues) incluindo:
- Descrição detalhada
- Passos para reproduzir
- Screenshots (se aplicável)
- Informações do ambiente

---

## 📈 Roadmap

### 🎯 Próximas Funcionalidades

- [ ] 📱 Interface mobile responsiva
- [ ] 📊 Dashboard com gráficos e métricas
- [ ] 🔔 Sistema de alertas para estoque baixo
- [ ] 📄 Exportação de relatórios (PDF/Excel)
- [ ] 🔐 Autenticação de usuários
- [ ] 🌐 API REST para integração
- [ ] 📈 Análise preditiva de demanda

### 🔮 Versões Futuras

- **v2.0**: Interface completa com dashboard
- **v3.0**: IA preditiva e análises avançadas
- **v4.0**: Integração com sistemas ERP

---

## 🏆 Reconhecimentos

Agradecimentos especiais para:

- **[OpenAI](https://openai.com/)** pelos modelos GPT excepcionais
- **[LangChain](https://langchain.com/)** pelo framework poderoso e flexível
- **[Streamlit](https://streamlit.io/)** pela simplicidade na criação de interfaces
- **Comunidade Python** pelo ecossistema incrível

---

## 👨‍💻 Autor

**Kauan Rodrigues Lima**

- GitHub: [@Kauanrodrigues01](https://github.com/Kauanrodrigues01)
- LinkedIn: [Kauan Rodrigues](https://www.linkedin.com/in/kauan-rodrigues-lima/)

**🔗 Link do Projeto**: [https://github.com/Kauanrodrigues01/stock-agent](https://github.com/Kauanrodrigues01/stock-agent)
