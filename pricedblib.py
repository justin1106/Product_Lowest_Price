from tinydb import TinyDB, Query
db = TinyDB('pricedb.json')

def insert_product(product):
    db.insert(product)

def delete_product(id):
    db.remove(Query().id == id)

def fetch_products():
    return db.all()

def fetch_product_by_id(id):
    users = db.search(Query().id == id)
    if len(users) == 0:
        return []
    else:
        return users.pop()
def get_new_id():
    products = fetch_products()
    new_id = products[-1]['id'] + 1
    return new_id
def update_product(p):
    db.update(p, Query().id == p['id'])