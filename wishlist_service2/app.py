from flask import Flask, render_template, request, redirect, url_for
from models import db, StavkaPopisa, db_session
app = Flask(__name__)

@app.route('/')
def index():
    search_query = request.args.get('search')
    purchase_filter = request.args.get('purchase_filter')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')

    with db_session:
        query = StavkaPopisa.select()

        # Filtriranje po ključnoj riječi
        if search_query:
            query = query.filter(lambda s: search_query.lower() in s.naziv.lower() or search_query.lower() in s.opis.lower())

        # Filtriranje po statusu kupljeno/nekupljeno
        if purchase_filter == 'bought':
            query = query.filter(lambda s: s.kupljeno)
        elif purchase_filter == 'not_bought':
            query = query.filter(lambda s: not s.kupljeno)

        # Filtriranje po cijeni
        if min_price:
            query = query.filter(lambda s: s.cijena >= float(min_price))
        if max_price:
            query = query.filter(lambda s: s.cijena <= float(max_price))

        items = query[:]
        return render_template('index.html', items=items)


@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        naziv = request.form['naziv']
        opis = request.form['opis']
        cijena = float(request.form['cijena'])
        prioritet = int(request.form['prioritet'])
        with db_session:
            StavkaPopisa(naziv=naziv, opis=opis, cijena=cijena, prioritet=prioritet)
        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/stats')
def stats():
    with db_session:
        total_items = StavkaPopisa.select().count()
        bought_items = StavkaPopisa.select(lambda s: s.kupljeno).count()
        total_spent = sum(s.cijena for s in StavkaPopisa.select() if s.kupljeno)
        return render_template(
            'stats.html',
            total_items=total_items,
            bought_items=bought_items,
            total_spent=total_spent
        )

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    with db_session:
        item = StavkaPopisa.get(id=item_id)
        if item:
            item.delete()
    return redirect(url_for('index'))

@app.route('/toggle_purchase/<int:item_id>')
def toggle_purchase(item_id):
    with db_session:
        item = StavkaPopisa.get(id=item_id)
        if item:
            item.kupljeno = not item.kupljeno
    return redirect(url_for('index'))

@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    with db_session:
        item = StavkaPopisa.get(id=item_id)
        if request.method == 'POST':
            # Ažuriranje postojećih podataka
            item.naziv = request.form['naziv']
            item.opis = request.form['opis']
            item.cijena = float(request.form['cijena'])
            item.prioritet = int(request.form['prioritet'])
            item.kupljeno = 'kupljeno' in request.form  # Ako je checkbox označen
            return redirect(url_for('index'))
        return render_template('update_item.html', item=item)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
