import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def display_data_analysis():
    # Titre principal
    st.title("Analyse du marché des matières premières 📊")

    # Charger les données
    file_path = "Data/data_net/commodities_market.csv"
    data = pd.read_csv(file_path)

    # Convertir la colonne 'date' en datetime pour faciliter les filtres
    data['date'] = pd.to_datetime(data['date'])
    data['year'] = data['date'].dt.year  # Extraire les années pour les analyses temporelles

    # Vérification des colonnes nécessaires
    if {'daily_trend', 'category', 'volume', 'volatility', 'close', 'date', 'commodity'}.issubset(data.columns):
        
        # Section : Résumé des données
        st.header("Résumé des données 📄")
        st.write(f"**Nombre total d'observations :** {data.shape[0]}")
        st.write(f"**Nombre total de variables :** {data.shape[1]}")
        
        # Section : Description des données
        st.subheader("Description des données")
        st.markdown("""
        - **date** : Date des observations
        - **commodity** : Nom de la matière première
        - **category** : Catégorie de la matière première
        - **close** : Prix de clôture
        - **volume** : Volume des transactions
        - **volatility** : Volatilité journalière
        - **daily_trend** : Tendance quotidienne (hausse, baisse, neutre)
        """)

        # Section : Statistiques descriptives
        st.subheader("Statistiques descriptives générales")
        st.dataframe(data.describe())

        # Section : Aperçu des premières lignes
        st.subheader("Aperçu des premières lignes")
        st.dataframe(data.head(5))

        # Section : Distribution des variables
        st.header("Distribution des variables")
        numeric_columns = list(data.select_dtypes(include=['float64', 'int64']).columns)
        cols = st.columns(3)  # Organiser en trois colonnes pour alignement
        for idx, col in enumerate(numeric_columns):
            with cols[idx % 3]:  # Placer dans la bonne colonne
                st.subheader(f"{col}")
                fig, ax = plt.subplots(figsize=(3, 2))
                data[col].hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
                ax.set_title(f"Histogramme de {col}")
                ax.set_xlabel(col)
                ax.set_ylabel("Fréquence")
                st.pyplot(fig)

        # Section : Répartition des tendances par catégorie
        st.header("Répartition des tendances par catégorie")
        categories = ["Vue globale"] + list(data['category'].unique())
        selected_category = st.selectbox("Sélectionnez une catégorie", categories)
        
        if selected_category == "Vue globale":
            filtered_data = data
        else:
            filtered_data = data[data['category'] == selected_category]
        
        trend_counts = filtered_data['daily_trend'].value_counts(normalize=True) * 100
        trend_counts = trend_counts.round(2)
        
        fig, ax = plt.subplots(figsize=(5, 3))
        trend_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax, startangle=90)
        ax.set_ylabel("")
        ax.set_title(f"Tendances pour {selected_category}")
        st.pyplot(fig)

        # Section : Volume moyen des transactions par catégorie
        st.header("Volume moyen des transactions par catégorie")
        avg_volume = data.groupby('category')['volume'].mean().sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(8, 3))
        avg_volume.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title("Volume moyen des transactions")
        ax.set_xlabel("Catégorie")
        ax.set_ylabel("Volume moyen")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)


        # Section : Analyse de la volatilité
        st.header("Analyse de la volatilité")

        # Colonnes pour afficher les graphiques côte à côte
        col1, col2 = st.columns([1, 1])  # Proportions égales pour les colonnes

        # Histogramme de la volatilité
        with col1:
            st.subheader("Distribution de la volatilité journalière")
            fig, ax = plt.subplots(figsize=(6, 4))  # Taille réduite et uniforme
            sns.histplot(data['volatility'], kde=True, bins=30, color='blue', ax=ax)
            ax.set_title("Distribution de la volatilité journalière")
            ax.set_xlabel("Volatilité (%)")
            ax.set_ylabel("Nombre de jours")
            st.pyplot(fig)

        # Boxplot par catégorie
        with col2:
            st.subheader("Volatilité par catégorie")
            fig, ax = plt.subplots(figsize=(7, 4))  # Taille réduite et uniforme
            sns.boxplot(x='category', y='volatility', data=data, ax=ax)
            ax.set_title("Volatilité par catégorie")
            ax.set_xlabel("Catégorie")
            ax.set_ylabel("Volatilité (%)")
            plt.xticks(rotation=45)  # Incliner les étiquettes pour mieux les lire
            st.pyplot(fig)

        # Section : Évolution des prix avec filtres
        st.header("Évolution des prix")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            selected_commodity = st.selectbox("Sélectionnez une commodité", data['commodity'].unique())
        with col2:
            min_year = data['year'].min()
            max_year = data['year'].max()
            year_range = st.slider("Sélectionnez une plage d'années", min_year, max_year, (min_year, max_year))
        
        filtered_data = data[(data['commodity'] == selected_commodity) & (data['year'].between(year_range[0], year_range[1]))]
        
        st.subheader(f"Prix pour {selected_commodity} ({year_range[0]} - {year_range[1]})")
        if not filtered_data.empty:
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(filtered_data['date'], filtered_data['close'], label='Prix de clôture', color='green')
            ax.set_title(f"Prix pour {selected_commodity}")
            ax.set_xlabel("Date")
            ax.set_ylabel("Prix de clôture")
            ax.legend()
            st.pyplot(fig)
        else:
            st.warning("Aucune donnée disponible pour la sélection.")

        # Section : Corrélation entre volume et prix
        st.header("Corrélation entre volume et prix")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(x='volume', y='close', data=data, ax=ax)
        ax.set_title("Corrélation entre le volume et le prix")
        ax.set_xlabel("Volume")
        ax.set_ylabel("Prix de clôture")
        st.pyplot(fig)

        # Section : Matrice de corrélation interactive
        st.header("Matrice de corrélation interactive")
        selected_columns = st.multiselect("Variables pour la matrice de corrélation", numeric_columns, default=numeric_columns)
        if len(selected_columns) > 1:
            correlation_matrix = data[selected_columns].corr()
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
            ax.set_title("Matrice de corrélation")
            st.pyplot(fig)
        else:
            st.warning("Veuillez sélectionner au moins deux variables.")

        

    else:
        st.error("Les colonnes nécessaires ne sont pas présentes dans le fichier.")
