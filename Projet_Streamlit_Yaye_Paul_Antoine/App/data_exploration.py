import streamlit as st

def page_data_exploration():
    st.title("Exploration des Données")
    
    # Chemin du fichier Markdown
    markdown_file_path = "Data/data_exploration/data_exploration.md"  # Assurez-vous que le fichier est bien dans ce chemin
    
    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        st.markdown(content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Le fichier data_exploration.md est introuvable. Assurez-vous qu'il est dans le dossier `data`.")
