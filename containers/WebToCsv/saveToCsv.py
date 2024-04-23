import requests
import pandas as pd
import os
def save_comments_to_csv(comments_df, csv_file_path):
    """
    Enregistrez le DataFrame des commentaires dans un fichier CSV.

     Args :
         comments_df (pandas.DataFrame) : DataFrame contenant les données de commentaires.
         csv_file_path (str) : Chemin pour enregistrer le fichier CSV.
    """
    comments_df.to_csv(csv_file_path, index=False)
    print('Comments saved successfully to', csv_file_path)
