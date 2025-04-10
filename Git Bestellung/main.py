import tkinter as tk
from tkinter import simpledialog, ttk
from funktionen import Bestellungen

fenster = tk.Tk()
fenster.title("Bestellung")
fenster.geometry("600x300")

mindest = simpledialog.askinteger("Eingabe", "Mindeststückzahl (Lager):", parent=fenster)

