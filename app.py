from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Soul_search')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.soul_search
souls_collection = db.souls

app = Flask(__name__)

# def picture_url_creator(id_lst):
#     souls = []
#     for soul_id in id_lst:
#         soul = 'https://www.google.com/' + soul_id
#         souls.append(soul)
#     return souls

# souls = [
#     { 'name': 'James Brown', 'price': '$100' },
#     { 'name': 'John Coltrain', 'price': '$1000' }
# ]

@app.route('/')
def index():
    """Return homepage"""
    return render_template('index.html', souls=souls_collection.find())

@app.route('/souls/new')
def souls_new():
    """Put a soul up for sale"""
    return render_template('souls_new.html')

@app.route('/souls', methods=['POST'])
def souls_submit():
    """Submit a soul"""
    soul = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),

    }
    souls_collection.insert(soul)
    return redirect('/')

@app.route('/souls/<soul_id>')
def souls_show(soul_id):
    """Show a single soul"""
    soul = souls_collection.find_one({'_id': ObjectId(soul_id)})
    return render_template('souls_show.html', soul=soul)

@app.route('/souls/<soul_id>/edit')
def souls_edit(soul_id):
    """Show a single soul"""
    soul = souls_collection.find_one({'_id': ObjectId(soul_id)})
    return render_template('souls_edit.html', soul=soul)

@app.route('/souls/<soul_id>', methods=['POST'])
def souls_update(soul_id):
    """Submit edited soul"""
    # soul_id = request.form.get('soul_id')

    updated_soul = {
        'name': request.form.get('name'),
        'price': request.form.get('price')
    }

    souls_collection.update_one(
        {'_id': ObjectId(soul_id)},
        {'$set': updated_soul})

    return redirect(url_for('souls_show', soul_id=soul_id))

@app.route('/souls/<soul_id>/delete', methods=['POST'])
def souls_delete(soul_id):
    """Deletes one soul"""
    souls_collection.delete_one({'_id': ObjectId(soul_id)})
    return redirect(url_for('index'))

@app.route('/souls/<soul_id>/buy', methods=['POST'])
def souls_buy(soul_id):
    """Buy this soul"""
    """Here we want to use the button to render an email form that can
    send an email to the current soul holder"""
    soul = souls_collection.find_one({'_id': ObjectId(soul_id)})
    return render_template('souls-buy.html', soul=soul)

'''How can I more randomize the image?'''

'''How do I set up an email interface where the buyer can
send the seller an email from the sellers email that was
put in the database?'''

if __name__ == '__main__':
    app.run(debug=True)
