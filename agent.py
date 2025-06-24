from decouple import config
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate

OPENAI_API_KEY = config('OPENAI_API_KEY')

def get_answer(model: str, temperature: float, question: str):
    llm = ChatOpenAI(
        model=model,
        temperature=temperature,
        api_key=OPENAI_API_KEY
    )
    
    db = SQLDatabase.from_uri('sqlite:///estoque.db')
    sql_toolkit = SQLDatabaseToolkit(
        db=db,
        llm=llm
    )
    
    system_message = hub.pull('hwchase17/react')
    
    agent = create_react_agent(
        llm=llm,
        tools=sql_toolkit.get_tools(),
        prompt=system_message
    )
    
    agent_executor = AgentExecutor(
        agent=agent,
        tools=sql_toolkit.get_tools(),
        verbose=True,
        handle_parsing_errors=True
    )
    
    prompt = '''
    Use as ferramentas necessárias para responder perguntas relacionadas ao
    estoque de produtos. Você fornecerá insights sobre produtos, preços, 
    reposição de estoque e relatórios conforme solicitado pelo usuário.
    A resposta final deve ter uma formatação amigável de visualização para o usuário.
    Sempre responda em português brasileiro.
    Pergunta: {q}
    '''
    prompt_template = PromptTemplate.from_template(prompt)
    
    formatted_prompt = prompt_template.format(q=question)
    
    response = agent_executor.invoke({'input': formatted_prompt})
    
    return response['output']
