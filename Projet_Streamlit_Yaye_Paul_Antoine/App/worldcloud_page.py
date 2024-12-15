import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re
import unicodedata
from collections import Counter
import string
from nltk.tokenize import word_tokenize

# Télécharger les données nécessaires pour nltk
nltk.download('stopwords')

# Fonction pour extraire le texte du PDF
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Fonction pour nettoyer et structurer le texte
def clean_text(text):
    # Convertir en minuscule
    text = text.lower()
    # Supprimer la ponctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    #Supprimer les vaaleurs numerique
    text = re.sub(r'\b\d+\b', '', text)
    # Tokenisation
    tokens = word_tokenize(text)
    # Charger les mots vides
    stop_words = set(stopwords.words('english'))
    # Filtrer les mots vides et garder uniquement les mots alphanumériques
    filtered_words = [word for word in tokens if word not in stop_words and word.isalnum()]
    return ' '.join(filtered_words)

# Fonction principale pour afficher la page
def display_wordcloud_page():
    file_path = "Data/data_net/Exploring_the_Trend_of_Commodity_Prices_A_Review_a.txt"

    article_summary = """
    Cet article traite des enjeux contemporains liés au marché des matières premières. 
    Il explore les dynamiques économiques, les fluctuations des prix et leur impact 
    sur les industries mondiales. Une attention particulière est portée à l'analyse 
    des tendances récentes et à l'évolution des politiques commerciales influençant 
    les transactions internationales.
    """

    # Titre de la page
    st.title("Analyse de l'article et Nuage de Mots")
    st.subheader("Lien vers l'article original")
    st.write("https://www.researchgate.net/publication/362473514_Exploring_the_Trend_of_Commodity_Prices_A_Review_and_Bibliometric_Analysis")

    st.subheader("Contenu et Résumé de l'article")
    try:
        # ouvrir et lire le texte
        with open(file_path, 'r', encoding='utf-8') as file:
             raw_text= file.read()
        st.text_area("Contenu brut de l'article (extrait)", raw_text[:1000], height=200)
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
        raw_text = ""

    st.subheader("De quoi parle l'article (Résumé)")
    st.write(article_summary)

    st.subheader("Texte traité")
    if raw_text:
        cleaned_text = clean_text(raw_text)
        st.text_area("Texte nettoyé", cleaned_text[:1000], height=200)
    else:
        st.warning("Aucun texte brut disponible pour le traitement.")

    st.subheader("Nuage de mots")
    if raw_text:
        word_freq = Counter(cleaned_text.split())
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("Le texte traité est vide. Assurez-vous que le fichier contient du texte lisible.")
