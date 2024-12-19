# Introduzindo o Pydantic

# importa a biblioteca da OpenAI
import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

# Sem o pydantic, podemos criar uma estrutura de dados utilizando funções da seguinte forma:

# Cuidado! Podemos setar os atributos com qualquer tipo de dado, pois o Python por padrão não faz checagem de tipos
class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
    
anna = Pessoa('Anna', 20, 60)

# Criando uma estrutura de dados usando Pydantic

# A sintaxe de pydantic acaba sendo bem mais simples para a criação de classes de dados, ao compararmos com a criação de classes comuns de Python.
# Nela, temos que tomar cuidado com a definição do tipo de cada atributo, pois eles serão utilizados para validar se os dados fornecidos estão corretos.

from pydantic import BaseModel

class pydPessoa(BaseModel):
    nome: str
    idade: int
    peso: float

anna = pydPessoa(nome='Anna', idade=20, peso=60)
print(anna)

# Podemos fazer um nesting de classes de pydantic, onde uma classe de dados recebe como input outra classe pydantic

from typing import List

class pydAsimovTeam(BaseModel):
    funcionarios: List[pydPessoa]
    
pydAsimovTeam(funcionarios=[pydPessoa(nome='Luiza', idade=37, peso=75)])

# ===============================================================================================================================
# Adicionando função externa usando LangChain

from langchain.pydantic_v1 import BaseModel, Field
from typing import Optional
from enum import Enum

class UnidadeEnum(str, Enum):
    celsius = 'celsius'
    fahrenheit = 'fahrenheit'
    

class ObterTemperaturaAtual(BaseModel):
    """Obtém a temperatura atual de uma determinada localidade"""
    local: str = Field(description='O nome da cidade', examples=['São Paulo', 'Porto Alegre'])
    unidade: Optional[UnidadeEnum]
    
from langchain_core.utils.function_calling import convert_to_openai_function

tool_temperatura = convert_to_openai_function(ObterTemperaturaAtual)
print(tool_temperatura)

# Agora que já sabemos criar funções para que os modelos de LLM entendam, podemos passar essas funções para os 
# modelos de linguagem através da biblioteca langchain. Para isso temos duas formas, podemos utilizar o parâmetro functions ao chamar
# o método invoke dos chat_models:

from langchain_openai import ChatOpenAI

chat = ChatOpenAI()

resposta = chat.invoke('Qual é a temperatura de Porto Alegre?', functions = [tool_temperatura])

# Ou podemos dar um bind e criar um novo componente de chat_model que terá acesso a função sempre que for chamado o invoke.
# Nestes dois casos, o modelo se comportará com o parâmetro "auto" de chamamento de função, ou seja, ele chamará a função
# quando necessitar, caso contrário se comportará como um modelo de linguagem normal.

chat = ChatOpenAI()
chat_com_func = chat.bind(functions = [tool_temperatura])
resposta = chat.invoke('Qual é a temperatura de Porto Alegre?')
print(resposta)

# Podemos obrigar o modelo a sempre chamar uma função da seguinte forma:

resposta = chat.invoke(
    'Qual é a temperatura de Porto Alegre?',
    functions=[tool_temperatura],
    function_call={'name':'ObterTemperaturaAtual'}
)
resposta

# Adicionando a uma chain

# Podemos adicionar esse modelo com funções a um prompt e criar uma chain

from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável chamado Isaac'),
    ('user', '{input}')
])

chain = prompt | chat.bind(functions=[tool_temperatura])

response = chain.invoke({'input':'Olá'})

print(response.content)