import streamlit as st

def page_home():
    st.markdown('<div class="title">Analyse des Commodités - SDA 2025</div>', unsafe_allow_html=True)
    context = """
# Contexte

Les commodités, telles que le pétrole, les céréales, et les métaux précieux, jouent un rôle essentiel dans l'économie mondiale.
Les fluctuations de prix de ces produits peuvent avoir des impacts significatifs sur les marchés financiers, les politiques publiques et la sécurité alimentaire.

Notre projet vise à explorer et analyser les tendances des prix des commodités en utilisant des outils avancés de gestion des données, de visualisation et de text mining. 
Ces analyses permettent de mieux comprendre les facteurs influençant les prix et leur volatilité.

"""
    st.markdown(context)

    project = """
# Objectifs du Projet

Ce projet, dans le cadre de la formation SDA 2024, se concentre sur :

1. **Gestion des données** : 
    - Exploration et nettoyage des données.
    - Création de nouvelles variables pour enrichir l'analyse.

2. **Visualisation des données** :
    - Réalisation de graphiques interactifs pour comprendre les tendances des commodités.
    - Identification des variations de prix et de leur volatilité.

3. **Text Mining** :
    - Analyse d'articles pertinents sur les commodités.
    - Création d'un nuage de mots pour mettre en évidence les thèmes principaux.

"""
    st.markdown(project)

