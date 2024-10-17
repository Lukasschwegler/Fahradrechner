from datetime import datetime


# Aktuelle Uhrzeit abrufen
current_time = datetime.now().hour


if 6 <= current_time < 12:
   greeting = "Guten Morgen"
elif 12 <= current_time < 18:
   greeting = "Guten Tag"
elif 18 <= current_time < 22:
   greeting = "Guten Abend"
else:
   greeting = "Gute Nacht"


#Uhrzeit
from datetime import datetime


# Aktuelles Datum und Uhrzeit
aktuelles_datum_und_uhrzeit = datetime.now()


# Formatierte Ausgabe
formatiertes_datum_und_uhrzeit = aktuelles_datum_und_uhrzeit.strftime("%Y-%m-%d %H:%M:%S")


uhrzeit = formatiertes_datum_und_uhrzeit


# Variablen für die Berechnungen


try:
   a = int(input("Basispreis in Euro "))
except ValueError:
   print("Das war keine gültige Zahl!")


try:
   b = int(input("Rabatt in Prozent "))
except ValueError:
   print("Das war keine gültige Zahl!")


#Json
import json


# Python-Datenstruktur erstellen (Dictionary)
data = {
   "a": a,
   "b": b,
   "uhrzeit": uhrzeit,
}


# Speichern der Daten in einer JSON-Datei
with open('input.json', 'w') as json_file:
   json.dump(data, json_file, indent=4)


import json


# Pfad zur JSON-Datei
datei_pfad = 'input.json'


# JSON-Datei öffnen und einlesen
with open(datei_pfad, 'r', encoding='utf-8') as datei:
   daten = json.load(datei)


# Eine Berechnung mit Division und Multiplikation
rabatt = (a /100) * b


# Rabattierter Preis
zuzahlenderPreis = a - rabatt


# Monatsrate
c= int(input("Monatsanzahl "))
d= zuzahlenderPreis / c


#Zahlrunden
zahl = d
gerundete_zahl = round(zahl, 2)


#Preisvergleich


euro = 50
preis = "Preis ist teuer" if euro <= gerundete_zahl else "Preis ist gut"


#import begruessung


# Beispiel-Dictionary


text = "CSV-Datei wurde erfolgreich erstellt!"
farbe = "\033[90m"  # Nur Blau
reset = "\033[0m"   # Zurücksetzen der Farbe

mein_dict = {

  # "Uhrzeit": greeting,
   "Uhrzeit": f"{farbe}{greeting}{reset}",
   "Monatsrate": f"{farbe}{gerundete_zahl}€{reset} ",
   "Laufzeit": f"{farbe}{c} Monate{reset}",
   "Preisempflung": f"{farbe}{preis}{reset}",
   "CSV":f"{farbe}{text}{reset}"
}

# Manuelle Formatierung
for key, value in mein_dict.items():
   print(f"{key}: {value}")

#CSV
import csv
import os

# Pfad zur CSV-Datei
file_name = 'fahrrad.csv'

# Überprüfen, ob die Datei existiert, um zu entscheiden, ob die Kopfzeile geschrieben werden muss
file_exists = os.path.exists(file_name)

# Öffne die CSV-Datei im Append-Modus ('a' steht für Anhängen)
with open(file_name, 'a', newline='') as csv_file:
    fieldnames = ['Uhrzeit', 'Monatsrate', 'Laufzeit', 'Preisempflung']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Wenn die Datei neu erstellt wird, schreibe die Kopfzeile
    if not file_exists:
        writer.writeheader()

    # Schreibe die neuen Daten als neue Zeile
    writer.writerow({'Uhrzeit': greeting, 'Monatsrate':  f"{gerundete_zahl} €",'Laufzeit': f"{c} Monate",'Preisempflung': preis,})



