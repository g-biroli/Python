import streamlit as st 

df_data = st.session_state['data']
df_data

# Filter [Sidebar] to choose the Team and theirs players.
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubes)

df_players = df_data[df_data['Club'] == club]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Player', players)