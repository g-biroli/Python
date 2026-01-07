import streamlit as st 
import webbrowser

# Title
st.markdown('# FIFA23 OFFICIAL DATASET! ⚽')
st.sidebar.markdown('Developed by [Gabriel Biroli] (https://www.linkedin.com/in/gabrielbiroli/)')

# Dataset button for sharing with the audience
btn = st.button('Explore the dataset on kaggle 👌')
if btn == True:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    """
    The football player dataset from 2017 to 2023 provides comprehensive information about professional football players.
    The dataset contains a wide range of attributes, including player demographics, physical characteristics, game statistics, contract details, and club affiliations.
    
    With over **17,000 records**, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the football world, 
    as it allows for the study of player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.
    """
    )