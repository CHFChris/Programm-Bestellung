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

cur.execute
(
"""
SELECT 
    artikel.Artikelname,  
    artikel.Lagerbestand, 
    lieferant.Lieferantenname
FROM artikel
JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant
"""
)

fenster = tk.Tk()
fenster.title("Bestellungen")
fenster.geometry("800x400")

spalten = ["Artikelname", "Lagerbestand", "Lieferantenname"]

tabelle = ttk.Treeview(fenster, columns=spalten, show="headings")

fenster.mainloop()

cur.close()
conn.close()