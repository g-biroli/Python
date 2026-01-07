import streamlit as st 

df_data = st.session_state['data']

# Filter [Sidebar] to choose the Team and theirs players.
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubes)

df_players = df_data[(df_data['Club'] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox('Player', players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

st.title(player_stats['Name'])
st.markdown(f'**Club:** {player_stats["Club"]}')
st.markdown(f'**Position:** {player_stats["Position"]}')

# Layout created for specific information
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f'**Idade** {player_stats["Age"]}')