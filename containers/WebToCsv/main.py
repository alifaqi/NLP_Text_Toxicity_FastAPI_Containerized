import requests
import pandas as pd
import os
from process_comment import preprocess_comments
from retrieve_comment import retrieve_comments
from saveToCsv import save_comments_to_csv


def main():
    # URL pour récupérer les commentaires
    url = "https://dummyjson.com/comments?limit=0"
    
    # Récupérer les commentaires de l'URL
    comments_df = retrieve_comments(url)
    
    # Prétraiter les commentaires DataFrame
    comments_df = preprocess_comments(comments_df)
    
    # Spécifiez l'emplacement pour enregistrer le fichier CSV
    csv_file_path = 'comments_df.csv'
    
    # Enregistrer les commentaires dans un fichier CSV
    save_comments_to_csv(comments_df, csv_file_path)

if __name__ == "__main__":
    main()
