from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Soul_search
souls = db.souls

app = Flask(__name__)

# souls = [
#     { 'name': 'James Brown', 'price': '$100' },
#     { 'name': 'John Coltrain', 'price': '$1000' }
# ]

@app.route('/')
def index():
    """Return homepage"""
    return render_template('index.html', souls=souls.find())

if __name__ == '__main__':
    app.run(debug=True)
