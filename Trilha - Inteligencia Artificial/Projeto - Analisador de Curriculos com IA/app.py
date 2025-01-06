import os
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from database import AnalyzeDatabase

database = AnalyzeDatabase()
print("Current Working Directory:", os.getcwd())

st.set_page_config(
    page_title='AI Resume Analyzer',
    page_icon='📊',
    layout='wide'
)

option = st.selectbox(
    'Escolha uma vaga:',
    [job.get('name') for job in database.jobs.all()],
    index=None
)

data = None

if option:
    job = database.get_job_by_name(option)
    data = database.get_analysys_by_job_id(job.get('id'))
    
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
    
    df.rename(
        columns={
            'name':'Nome',
            'education':'Educação',
            'skills':'Habilidades',
            'language':'Línguas',
            'score':'Score',
            'summary_id':'Currículo ID',
            'id':'ID'
        },
        inplace=True
    )
    
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)
    
    if data:
        gb.configure_column('Score', header_name='Score', sort='desc')
        gb.configure_selection(selection_mode='multiple', use_checkbox=True)
        
    grid_options = gb.build()
    
    st.subheader("Pontuação dos Candidatos")
    st.bar_chart(df, x='Name', y='Score', color='Name')
    
    response = AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.COLUMN_CHANGED,
        theme='streamlit'
    )
    
    selected_candidates = response.get('selected_rows', [])
    candidates_df = pd.DataFrame(selected_candidates)
    
    summaries = database.get_summaries_by_job_id(job.get('id'))
    
    def delete_files_resume(summaries):
        for summary in summaries:
            path = summary.get('file')
            if os.path.isfile(path):
                os.remove(path)
    
    
    if st.button('Apagar análise'):
        database.delete_all_summaries_by_job_id(job.get('id'))
        database.delete_all_analysis_by_job_id(job.get('id'))
        database.delete_all_files_by_job_id(job.get('id'))
    
    if not candidates_df.empty:
        cols = st.columns(len(candidates_df))
        for idx, row in enumerate(candidates_df.iterrows()):
            with st.container():
                if summary_data := database.get_summary_by_id(row[1]['Summary ID']):
                    st.markdown(summary_data.get('content'))
                    st.markdown(summary_data.get('opinion'))

                    with open(summary_data.get('file'), 'rb') as file:
                        pdf_data = file.read()
                        
                        st.download_button(
                            label=f'Download do currículo {row[1]["Name"]}',
                            data=pdf_data,
                            file_name=f'{row[1]["Name"]}.pdf',
                            mime='application/pdf'
                        )