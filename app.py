import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.set_page_config(page_title='Stock GPT', page_icon='🤖')

st.header('Bem-vindo ao GPT! 🤖')

# Sidebar for model selection and API key input
model_options = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4-turbo',
]
selected_model = st.sidebar.selectbox('Model', model_options)

# Inicializa o histórico de chat
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Exibe o histórico de chat
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.write(message['content'])

# Input do usuário
if user_input := st.chat_input('Pergunte algo sobre o estoque...'):
    # Adiciona a mensagem do usuário ao histórico e exibe
    st.session_state.chat_history.append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.write(user_input)

