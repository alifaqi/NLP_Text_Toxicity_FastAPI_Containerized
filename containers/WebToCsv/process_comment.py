import requests
import pandas as pd
import os

def preprocess_comments(comments_df):
    """
    Prétraitez le DataFrame des commentaires.

     Args :
         comments_df (pandas.DataFrame) : DataFrame contenant les données de commentaires.

     Retour:
         pandas.DataFrame : DataFrame prétraité.
    """
    if not comments_df.empty:
        comments_df['user_id'] = comments_df['user'].apply(lambda x: x.get('id', ''))
        comments_df['username'] = comments_df['user'].apply(lambda x: x.get('username', ''))
        comments_df.drop(columns=['user'], inplace=True)
    return comments_df