import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Spotify',
    layout='wide'
)

df = pd.read_csv('01 Spotify.csv')
st.session_state['df_spotify'] = df

df.set_index('Track', inplace=True) # mudando a variável do eixo x

artists = df['Artist'].value_counts().index
artist = st.sidebar.selectbox('Artista', artists)
df_filtered = df[df['Artist'] == artist]

albuns = df_filtered['Album'].value_counts().index
album = st.selectbox('album', albuns)
df_filtered_album = df[df['Album'] == album]

# display = st.checkbox('Display')
# if display:
    # st.bar_chart(df_filtered_album['Stream'])

# Layout - Colunas
col1, col2 = st.columns([0.7, 0.3])
col1.bar_chart(df_filtered_album['Stream'])
col2.line_chart(df_filtered_album['Danceability'])

# Cacheamento e multipages