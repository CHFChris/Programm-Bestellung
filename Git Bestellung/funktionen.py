import tkinter as tk
from tkinter import ttk
import mariadb

conn = mariadb.connect(
    user="Raphi",
    password="RaphiH",
    host="localhost",
    port=3306,
    database="schlumpfshop3"
)
cur = conn.cursor()

cur.execute("""
SELECT 
    artikel.Artikelname, 
    artikel.Preis_Netto, 
    artikel.Lagerbestand, 
    lieferant.Lieferantenname
FROM artikel
JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant
""")

alle_artikel = cur.fetchall()

fenster = tk.Tk()
fenster.title("Bestellungen")
fenster.geometry("800x400")

spalten = ["Artikelname", "Preis_Netto", "Lagerbestand", "Lieferantenname"]

tabelle = ttk.Treeview(fenster, columns=spalten, show="headings")

for spalte in spalten:
    tabelle.heading(spalte, text=spalte)

for artikel in alle_artikel:
    tabelle.insert("", tk.END, values=artikel)

tabelle.pack(fill=tk.BOTH, expand=True)

fenster.mainloop()

cur.close()
conn.close()
