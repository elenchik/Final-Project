from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['surveyDB']
collection = db['users']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'age': request.form['age'],
            'gender': request.form['gender'],
            'income': float(request.form['income']),
            'expenses': {
                'utilities': float(request.form.get('utilities', 0)),
                'entertainment': float(request.form.get('entertainment', 0)),
                'school_fees': float(request.form.get('school_fees', 0)),
                'shopping': float(request.form.get('shopping', 0)),
                'healthcare': float(request.form.get('healthcare', 0))
            }
        }
        collection.insert_one(data)
        return redirect('/')
    return render_template('html.html')


if __name__ == '__main__':
    app.run(debug=True)
