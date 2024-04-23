import requests
import pandas as pd
import os

def retrieve_comments(url):
    """
    Récupérez les commentaires d'une URL donnée et renvoyez-les sous forme de DataFrame.

     Args :
         url (str) : L'URL à partir de laquelle récupérer les commentaires.

     Retour:
         pandas.DataFrame : DataFrame contenant les données des commentaires.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        comments = data.get("comments", [])
        return pd.DataFrame(comments)
    except requests.RequestException as e:
        print("Error retrieving comments:", e)
        return pd.DataFrame()
