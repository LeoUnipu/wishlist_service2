import os
from pony.orm import Database, Required, Optional, db_session

db = Database()

class StavkaPopisa(db.Entity):
    naziv = Required(str)
    opis = Required(str)
    cijena = Required(float)
    prioritet = Required(int)
    kupljeno = Required(bool, default=False)
    potrošeno = Optional(float, default=0.0)


db_path = os.getenv('DATABASE_URL', 'wishlist.sqlite')
db.bind(provider='sqlite', filename=db_path, create_db=True)
db.generate_mapping(create_tables=True)

@db_session
def dodaj_stavku(naziv, opis, cijena, prioritet):
    StavkaPopisa(naziv=naziv, opis=opis, cijena=cijena, prioritet=prioritet)


if __name__ == "__main__":
    with db_session:
        dodaj_stavku("Laptop", "Gaming laptop", 1200.0, 1)
