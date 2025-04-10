Aufgabe 1:

Schreiben Sie ein Programm "Bestellung"

Das Programm soll vom Benutzer eine Mindeststückzahl abfragen, die noch auf Lager liegt.

Anschließend soll eine Liste aller Artikel, deren Lagerbestand niedriger ist ausgegeben werden.
Die Liste soll die Artikelbezeichnung, den Lagerbestand und den Lieferanten enthalten.
Verwalten Sie die Abfrage in einer Liste, die Objekte enthält. Gestalten Sie eine grafische Oberfläche!


SQL Abfrage:

SELECT 
    artikel.Artikelname,  
    artikel.Lagerbestand, 
    lieferant.Lieferantenname
FROM artikel
JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant;
