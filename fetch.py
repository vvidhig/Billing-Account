import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['billing_database']
collection = db['billing_data']

# Fetch all documents from the collection
cursor = collection.find()

# Convert cursor to DataFrame
df = pd.DataFrame(list(cursor))

# Drop the MongoDB-generated _id column if not needed
df = df.drop('_id', axis=1)

# Display the first few rows
print(df.head())

# Get basic information about the dataset
print(df.info())