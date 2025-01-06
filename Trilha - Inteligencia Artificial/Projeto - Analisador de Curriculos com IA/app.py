import os
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from database import AnalyzeDatabase
import altair as alt

# Inicialização do banco de dados
database = AnalyzeDatabase()
print("Current Working Directory:", os.getcwd())

# Configuração da página
st.set_page_config(
    page_title='AI Resume Analyzer',
    page_icon='📊',
    layout='wide'
)

# Seleção da vaga
option = st.selectbox(
    'Escolha uma vaga:',
    [job.get('name') for job in database.jobs.all()],
    index=None
)

data = None

if option:
    # Obter a vaga selecionada e os dados de análise associados
    job = database.get_job_by_name(option)
    data = database.get_analysys_by_job_id(job.get('id'))

    # Criar dataframe para exibir os dados
    df = pd.DataFrame(
        data if data else {},
        columns=[
            'name',
            'education',
            'skills',
            'language',
            'score',
            'summary_id',
            'id'
        ]
    )

    # Renomear colunas para exibição
    df.rename(
        columns={
            'name': 'Nome',
            'education': 'Educação',
            'skills': 'Habilidades',
            'language': 'Línguas',
            'score': 'Score',
            'summary_id': 'Currículo ID',
            'id': 'ID'
        },
        inplace=True
    )

    # Configurar grid com paginação e seleção
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)

    if data:
        gb.configure_column('Score', header_name='Score', sort='desc')
        gb.configure_selection(selection_mode='multiple', use_checkbox=True)

    grid_options = gb.build()

    # Exibir gráfico de pontuação na horizontal
    st.subheader("Pontuação dos Candidatos")


    bar_chart = alt.Chart(df).mark_bar().encode(
        x='Score:Q',
        y=alt.Y('Nome:N', sort='-x'),  
        color='Nome:N', 
        tooltip=['Nome', 'Score'] 
    ).properties(
        title="Pontuação dos Candidatos",
        width=800,  
        height=400  
    )

    st.altair_chart(bar_chart, use_container_width=True)
    response = AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        theme='streamlit'
    )

    selected_candidates = response.get('selected_rows', [])
    candidates_df = pd.DataFrame(selected_candidates)

    # Obter os resumos associados à vaga selecionada
    summaries = database.get_summaries_by_job_id(job.get('id'))

    # Função para deletar arquivos de currículo
    def delete_files_resume(summaries):
        for summary in summaries:
            path = summary.get('file')
            if os.path.isfile(path):
                os.remove(path)

    # Botão para apagar análise
    if st.button('Apagar análise'):
        database.delete_all_summaries_by_job_id(job.get('id'))
        database.delete_all_analysis_by_job_id(job.get('id'))
        database.delete_all_files_by_job_id(job.get('id'))

    # Exibir dados dos candidatos selecionados
    if not candidates_df.empty:
        cols = st.columns(len(candidates_df))
        for idx, row in candidates_df.iterrows():
            # Obter dados do resumo pelo ID
            if summary_data := database.get_summary_by_id(row['Currículo ID']):
                st.markdown(summary_data.get('content'))
                st.markdown(summary_data.get('opinion'))

                # Verificar e abrir o arquivo do currículo
                file_name = os.path.basename(summary_data.get('file'))  # Extrai apenas o nome do arquivo
                file_path = os.path.join('resumes', file_name)  # Acessa a pasta resumes diretamente

                if not os.path.isfile(file_path):
                    st.error(f"Arquivo não encontrado: {file_path}")
                else:
                    with open(file_path, 'rb') as file:
                        pdf_data = file.read()

                        st.download_button(
                            label=f"Download do currículo {row['Nome']}",
                            data=pdf_data,
                            file_name=f"{row['Nome']}.pdf",
                            mime='application/pdf'
                        )