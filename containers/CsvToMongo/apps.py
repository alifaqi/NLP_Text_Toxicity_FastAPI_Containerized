from detoxify import Detoxify
import re
import pandas as pd
from database import insert_comments_to_mongodb


def clean_text(text):
    # Remove special characters, links, and emojis
    text = re.sub(r'http\S+', '', text)  # Remove links
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = text.encode('ascii', 'ignore').decode('ascii')  # Remove emojis
    return text

def load_comments(csv_file):
    try:
        comments_df = pd.read_csv(csv_file)
        comments_df['clean_text'] = comments_df['body'].apply(clean_text)
        return comments_df
    except Exception as e:
        print(f"An error occurred while loading comments from '{csv_file}': {e}")
        return None

def read_comments():
    csvfile = "comments_df.csv"
    comments_df = load_comments(csvfile)
    if comments_df is None:
        return {"error": f"Failed to load comments from '{csvfile}'."}
    try:
        model = Detoxify('original')
    except Exception as e:
        print(f"An error occurred while loading the model from Detoxify: {e}")
        return None
    
    toxicity_scores = []
    for text in comments_df['clean_text']:
        result = model.predict(text)
        toxicity_scores.append(result)

    comments_df['toxicity_score'] = toxicity_scores

    comments_df['toxicity'] = comments_df['toxicity_score'].apply(lambda x: x['toxicity'])
    comments_df['severe_toxicity'] = comments_df['toxicity_score'].apply(lambda x: x['severe_toxicity'])
    comments_df['obscene'] = comments_df['toxicity_score'].apply(lambda x: x['obscene'])
    comments_df['threat'] = comments_df['toxicity_score'].apply(lambda x: x['threat'])
    comments_df['insult'] = comments_df['toxicity_score'].apply(lambda x: x['insult'])
    comments_df['identity_attack'] = comments_df['toxicity_score'].apply(lambda x: x['identity_attack'])

    comments_df.drop(columns=['toxicity_score'], inplace=True)
    
    try:
        insert_comments_to_mongodb(comments_df)
        return {"message": f"Data from '{csvfile}' loaded and inserted into MongoDB collection."}
    except Exception as e:
        return {"error": f"An error occurred while inserting data into MongoDB: {e}"}
