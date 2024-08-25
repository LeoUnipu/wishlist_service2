
## Opis Projekta

Ova aplikacija je "Wishlist" aplikacija koja omogućuje korisnicima praćenje popisa želja i njihovih prioriteta. Korisnici mogu dodavati nove stavke na popis, uređivati postojeće, brisati ih, označavati kao kupljene i pregledavati statistike. Aplikacija koristi SQLite bazu podataka za spremanje podataka o stavkama na popisu. 

Aplikacija je osmišljena kako bi se lako mogla integrirati u poslovna okruženja, posebno u sektorima gdje je potrebno praćenje i organizacija želja ili proizvoda, kao što su maloprodaja, e-trgovina ili čak osobna financijska planiranja.

## Funkcionalnosti

- **Dodavanje novih stavki**: Korisnici mogu dodati nove stavke na popis želja, uključujući naziv, opis, cijenu i prioritet.
- **Ažuriranje stavki**: Postojeće stavke mogu se uređivati kako bi se promijenili njihovi podaci.
- **Brisanje stavki**: Stavke se mogu ukloniti s popisa kada više nisu relevantne.
- **Označavanje kao kupljeno**: Korisnici mogu označiti stavke kao kupljene ili nekupljene.
- **Prikaz statistika**: Aplikacija prikazuje ukupni broj stavki, broj kupljenih stavki i ukupnu potrošnju.
- **Pretraga i filtriranje**: Stavke se mogu pretraživati po ključnim riječima, te filtrirati prema statusu kupljeno/nekupljeno i prema rasponu cijena.

## Pokretanje Aplikacije Lokalno

1. **Klona projekta:**
   - Klonirajte ovaj repozitorij na svoje računalo:
     ```bash
     git clone https://github.com/LeoUnipu/wishlist_service2.git
     cd wishlist_service2
     ```

2. **Instalacija ovisnosti:**
   - Instalirajte potrebne ovisnosti koristeći `pip`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Pokretanje aplikacije:**
   - Pokrenite aplikaciju lokalno pomoću sljedeće naredbe:
     ```bash
     python app.py
     ```

4. **Pristup aplikaciji:**
   - Otvorite web preglednik i idite na `http://127.0.0.1:5000` kako biste koristili aplikaciju.

## Korištenje s Dockerom

1. **Build Docker image-a:**
   - Izradite Docker image pomoću:
     ```bash
     docker build -t my-flask-app .
     ```

2. **Pokretanje Docker kontejnera:**
   - Pokrenite aplikaciju unutar Docker kontejnera s trajnim volumenom za bazu podataka:
     ```bash
     docker run -d -p 5000:5000 -v C:\Users\leohr\Desktop\wishlist_service2\data:/app/data my-flask-app
     ```

3. **Pristup aplikaciji:**
   - Otvorite web preglednik i idite na `http://127.0.0.1:5000`.

