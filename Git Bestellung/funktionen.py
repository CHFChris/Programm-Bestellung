import mariadb

class Artikel:
    def __init__(self, name, bestand, lieferant):
        self.name = name
        self.bestand = bestand
        self.lieferant = lieferant

def Bestellungen(mindestbestand):
    conn = mariadb.connect(
        user="Raphi",
        password="RaphiH",
        host="localhost",
        port=3306,
        database="schlumpfshop3"
    )
    cur = conn.cursor()

    cur.execute("""
        SELECT artikel.Artikelname, artikel.Lagerbestand, lieferant.Lieferantenname
        FROM artikel
        JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant
        WHERE artikel.Lagerbestand < ?
    """, (mindestbestand,))

    daten = cur.fetchall()

    artikel_liste = []
    for name, bestand, lieferant in daten:
        artikel = Artikel(name, bestand, lieferant)
        artikel_liste.append(artikel)

    cur.close()
    conn.close()

    return artikel_liste
