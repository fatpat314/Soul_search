from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Soul_search
souls = db.souls

app = Flask(__name__)

def picture_url_creator(id_lst):
    souls = []
    for soul_id in id_lst:
        soul = 'https://www.google.com/' + soul_id
        souls.append(soul)
    return souls

# souls = [
#     { 'name': 'James Brown', 'price': '$100' },
#     { 'name': 'John Coltrain', 'price': '$1000' }
# ]

@app.route('/')
def index():
    """Return homepage"""
    return render_template('index.html', souls=souls.find())

@app.route('/souls/new')
def souls_new():
    """Put a soul up for sale"""
    return render_template('souls_new.html')

@app.route('/souls', methods=['POST'])
def souls_submit():
    """Submit a soul"""
    soul_ids = request.form.get('soul_ids').split()

    souls = picture_url_creator(soul_ids)

    souls = {
        'name': request.form.get('name'),
        'price': request.form.get('price')
    }
    print(request.form.to_dict())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
