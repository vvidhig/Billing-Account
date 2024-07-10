import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['billing_database']
collection = db['billing_data']

# Load CSV file
df = pd.read_csv('dataset/complex_account_billing_data.csv')

# Convert DataFrame to list of dictionaries
data = df.to_dict('records')

# Insert data into MongoDB
collection.insert_many(data)

print("Data loaded successfully into MongoDB")