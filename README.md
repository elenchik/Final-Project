Overview:
This project is a survey tool built with Flask, MongoDB, and Python for collecting and analyzing healthcare spending data. 
Jupyter Notebook is used for data visualization.

Instructions:
1. Clone repository
2. Install requirements: `pip install -r requirements.txt`
3. Start MongoDB server locally
4. Run Flask app: `python app.py`
5. Data is saved in MongoDB, exported to `data/user_data.csv` using `user.py`

Data Analysis:
- Run `data_analysis.ipynb` after exporting data (to see visualizations)

AWS Deployment:
1. Use an EC2 instance
2. Install Docker or directly run Flask with Gunicorn: `gunicorn app:app`
3. Update MONGO_URI in `app.py` with AWS MongoDB connection string

Output:
- Visualizations will be saved in `data/` folder
