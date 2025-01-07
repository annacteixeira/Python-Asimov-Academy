# Analisador de Currículos com IA
Este é um projeto em Python que utiliza o framework Streamlit para analisar currículos enviados por candidatos. A aplicação processa os currículos, organiza os dados relevantes (como habilidades, educação e idiomas) e apresenta uma interface interativa para exibição e download dos currículos. O objetivo é facilitar a visualização e avaliação de candidatos para uma vaga específica.

## Modelo de IA Utilizado

Este projeto utiliza o modelo **llama-3.3-70b-versatile** para realizar a análise dos currículos enviados. O modelo é responsável por interpretar e pontuar os currículos de acordo com as informações das vagas cadastradas, como pré-requisitos, atividades principais e diferenciais.

### Principais funcionalidades do modelo:

- **Análise de coerência**: Avalia a compatibilidade entre as informações do currículo e os requisitos da vaga.
- **Classificação e pontuação**: Gera uma pontuação que auxilia na identificação dos candidatos mais alinhados com as vagas disponíveis.
- **Interpretação contextual**: Capaz de considerar educação, experiência e habilidades relevantes com base nos critérios definidos.

O uso deste modelo garante precisão e eficiência na avaliação dos candidatos, oferecendo uma experiência otimizada para processos seletivos.

## 🖥️ Funcionalidades

- **Upload de Currículos de uma pasta do Google Drive**: Carrega currículos em formato PDF.
- **Extração Automática de Informações**:
Nome do candidato.
Habilidades.
Formação acadêmica.
Idiomas.
 

- **Exibição de Dados**:
Tabela interativa com detalhes dos candidatos.
Gráfico de barras horizontal exibindo a pontuação de cada candidato.


- **Seleção de Candidatos**:
Checkbox para selecionar um ou mais candidatos.


- **Download de Currículos**: Permite baixar o PDF do currículo diretamente pela interface.
- **Gerenciamento dos Dados**: Opção para excluir análises de currículos de uma vaga.


## 📂 Estrutura do Projeto
Projeto - Analisador de Curriculos com IA/ <br/>

├── models/ <br/>
│   ├── analysis.py        # Estrutura para representar as análises no código <br/>
|   ├── file.py            # Modelo Pydantic que representa o relacionamento entre arquivos e vagas. <br/>
|   ├── job.py             # Modelo Pydantic que representa as informações de uma vaga de emprego <br/>
|   ├── summary.py         # Modelo Pydantic que representa o resumo do currículo, com detalhes como opinião e arquivo associado. <br/>
├── resumes/               # Pasta com os currículos em PDF extraídos do Google Drive <br/>
│   ├── exemplo1.pdf <br/>
│   ├── exemplo2.pdf <br/>
├── .env                   # Configuração de variáveis de ambiente. Incluir a variável GROQ_API_KEY para autenticação na API Groq. <br/>
├── ai.py                  # Gerencia interações com o modelo Groq para análise de currículos, geração de resumo, pontuação e opinião <br/>
├── analise.py             # Processa os currículos, gera resumos, opiniões e pontuações, e insere os resultados no banco de dados. <br/>
├── app.py                 # Script principal para executar o Streamlit <br/>
├── authenticate.py        # Gerencia autenticação com a API do Google Drive usando OAuth, salvando e renovando credenciais. <br/>
├── database.py            # Simulação de banco de dados local <br/>
├── db.json                # Arquivo JSON que simula o banco de dados <br/>
├── download_cv.py         # Conecta-se à API do Google Drive para baixar arquivos de uma pasta específica usando a credencial token.json. <br/>
├── helper.py              # Funções auxiliares (leitura de PDFs e extração de dados) <br/>
├── poetry.lock            # Arquivo gerado automaticamente pelo Poetry para travar versões exatas das dependências do projeto <br/>
├── pyproject.toml         # Arquivo de configuração do Poetry que define as dependências e metadados do projeto <br/>
|── README.md              # Documentação do projeto <br/>
|── requirements.txt       # Lista as dependências do projeto necessárias para instalação e execução no ambiente Python. <br/>
└── token.json             # Arquivo gerado automaticamente após a autenticação na API do Google. <br/>


## 📊 Interface do Usuário
A interface é intuitiva e funcional, permitindo:

- Escolher uma vaga para análise.
- Visualizar os candidatos que se candidataram à vaga selecionada.
- Acompanhar as pontuações através de um gráfico de barras horizontal.
- Selecionar um ou mais candidatos e visualizar informações detalhadas.
- Baixar o currículo de um candidato diretamente.
- Apagar os dados analisados de uma vaga, caso necessário.

## Exemplo de Interface


## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter:

Python 3.8 ou superior instalado.<br/>
Poetry ou gerenciador de pacotes para instalar as dependências.<br/>
Framework Streamlit instalado.<br/>

### 2. Instalar Dependências
No diretório do projeto, execute o seguinte comando para instalar as dependências:
pip install -r requirements.txt


### 3. Executar a Aplicação

1. Crie sua API do Google Drive -> Tutorial: https://www.youtube.com/watch?v=2NuI-6kDq_A

2. Execute o script ```authenticate.py``` para gerar um token.json 

3. Crie sua API da GROQ através do site: https://console.groq.com/

3. Crie uma pasta no Google Drive e faça o upload dos currículos desejados. Ao criar a pasta, a URL irá possuir um ID 
'https://drive.google.com/drive/u/0/folders/aqui-fica-o-ID'. Copie o ID e adicione ao arquivo download_cv.py, na variável ```folder_id```

4. Crie a vaga desejada no arquivo ```create_job.py```

5. Crie uma pasta 'resumes' na raiz do projeto

6. Execute o script ```download_cv.py``` para fazer o download dos currículos da pasta do Google Drive

7. Execute o script ```analise.py``` para que o modelo de IA possa gerar as análises dos currículos e adicioná-las ao banco de dados ```db.json```

8. Inicie o servidor Streamlit com o comando:

```bash
streamlit run app.py
```

O aplicativo será iniciado, e um link será exibido no terminal. Abra este link no navegador para acessar a interface.

---

## **📄 Arquivos Principais**

### **1. app.py**
- Controla a execução principal do projeto.
- Configura a interface do usuário com **Streamlit**.
- Exibe dados, gráficos e gerencia interações.

### **2. helper.py**
- Realiza operações auxiliares, como:
  - Ler currículos no formato PDF.
  - Extrair seções importantes (nome, educação, habilidades, etc.).

### **3. database.py**
- Simula um banco de dados utilizando um arquivo JSON (`db.json`).
- Gerencia informações sobre currículos, análises e candidatos.

### **4. db.json**
- Armazena os dados de vagas, currículos e análises em um formato estruturado.

---

## **📦 Requisitos do Projeto**

As dependências podem ser instaladas com o comando `pip install -r requirements.txt`.


## 🔧 Possíveis Melhorias

- Adicionar um sistema de upload de currículos diretamente pela interface.
- Exportação dos resultados em formatos como Excel ou CSV.
- Adicionar uma seção para que o usuário possa criar uma vaga pela interface.
- Melhorias visuais na interface, como temas personalizados.


## 🛠️ Contribuindo
Sinta-se à vontade para contribuir com o projeto! Clone o repositório, crie uma nova branch e envie um pull request


## 📄 Licença
Este projeto está sob a licença MIT. 

Se precisar de ajuda ou estiver com dúvidas, fique à vontade para abrir uma issue no repositório ou entrar em contato!
