import tkinter as tk
from tkinter import simpledialog, ttk
from funktionen import Bestellungen

fenster = tk.Tk()
fenster.title("Bestellung")
fenster.geometry("600x300")

mindest = simpledialog.askinteger("Eingabe", "Mindeststückzahl (Lager):", parent=fenster)

if mindest is not None:
    artikel_liste = Bestellungen(mindest)

    spalten = ["Artikelname", "Lagerbestand", "Lieferant"]
    tabelle = ttk.Treeview(fenster, columns=spalten, show="headings")

    for spalte in spalten:
        tabelle.heading(spalte, text=spalte)

    for artikel in artikel_liste:
        tabelle.insert("", tk.END, values=(artikel.name, artikel.bestand, artikel.lieferant))

    tabelle.pack(fill=tk.BOTH, expand=True)

fenster.mainloop()