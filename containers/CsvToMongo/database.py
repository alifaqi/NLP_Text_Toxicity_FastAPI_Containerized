import pymongo

def insert_comments_to_mongodb(comments_df):
    try:
        # Attempt to connect to MongoDB
        mongo_client = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
        mongo_db = mongo_client["dummyjson"]
        mongo_collection = mongo_db["commentaires"]
        
        # Convert DataFrame to dictionary
        comment_docs = comments_df.to_dict(orient='records')
        
        # Insert documents into MongoDB collection
        mongo_collection.insert_many(comment_docs)
        
        print("Successfully inserted comments into MongoDB")
        
    except Exception as e:
        print(f"An error occurred while inserting comments into MongoDB: {e}")


