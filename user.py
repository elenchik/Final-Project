import pandas as pd
from pymongo import MongoClient


class User:
    def __init__(self, mongo_uri='mongodb://localhost:27017/', db_name='surveyDB'):
        self.client = MongoClient(mongo_uri)
        self.collection = self.client[db_name]['users']

    def export_to_csv(self, csv_path):
        data = list(self.collection.find({}, {'_id': 0}))
        df = pd.DataFrame(data)
        df.to_csv(csv_path, index=False)
