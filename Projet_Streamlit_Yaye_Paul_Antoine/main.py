import streamlit as st
from App.home import page_home
from App.data_exploration import page_data_exploration
from App.data_analysis import display_data_analysis
from App.worldcloud_page import display_wordcloud_page

# Configuration globale de l'application
st.set_page_config(
    page_title="Analyse des Matières Premières",
    page_icon="📊",
    layout="wide"
)
st.subheader("Lien du jeux de données")
st.write("https://www.kaggle.com/datasets/guillemservera/commodities-futures-collection")

# Menu de navigation
PAGES = {
    "Accueil": page_home,
    "Exploration des Données": page_data_exploration,
    "Analyse des Données": display_data_analysis,
    "WordCloud": display_wordcloud_page
}

st.sidebar.title("Navigation")
choice = st.sidebar.radio("Aller à :", list(PAGES.keys()))
page = PAGES[choice]

# Affichage de la page choisie
page()
