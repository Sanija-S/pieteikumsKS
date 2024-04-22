#pievienotas biblenes

import PySimpleGUI as sg
import sqlite3 
from datetime import datetime

#savienosim ar db

conn=sqlite3.connect("klase.db")
c=conn.cursor()

#izveidosim tabulu
c.execute('''CREATE TABLE IF NOT EXISTS salidojums(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          vards TEXT,
          uzvards TEXT,
          dzimums TEXT,
          vecums INTEGER,
          ierasanas_datums TEXT

)''')

conn.commit()
#loga izkartojums

layout=[
    [sg.T("Vārds:"), sg.InputText(key="vards")],
    [sg.T("Uzvārds:"), sg.InputText(key="uzvards")],
    [sg.T("Dzimums:"), sg.Radio("Vīrietis","dzimums", key="dzimumsV"), sg.Radio("Sieviete","dzimums", key="dzimumsS")], # "dzimums"- jeb izveidotā grupa apvienos visas radio pogas
    [sg.T("Vecums:"), sg.Combo([i for i in range(18,101)], key="vecums")],
    [sg.T("Ierašanās datums:"), sg.CalendarButton("Izvēlēties datumu", target="ierasanas_datums", key="ierasanas_datums")], # poas nosaukums(calander)), ...., atslēga
    [sg.Button("Reģistrēties"), sg.Button("Iziet")]
    ]
logs=sg.Window("Datu reģistrs", layout, resizable=True)

#galvenais cikls

while True:
 event, values=logs.read()
 if event==sg.WIN_CLOSED or event== "Iziet":
  break
 
#datu apstrāde pēc pogas nospiešanas
 
 elif event=="Reģistrēties":
  #jāiegūst dati
  vards=values["vards"]
  uzvards=values["uzvards"]
  dzimums="Vīrietis" if values["dzimumsV"] else "Sieviete" # piskiranas izteiksme kura nosaka kuru radio pogu izvelejas lietotajs
  vecums=int(values["vecums"])
  ier_datums=values["ierasanas_datums"]
   
   # kā saglabāt datus datu bāzē
c.execute("""INSERT INTO salidojums(vards, uzvards, dzimums, vecums, ierasanas_datums)
          VALUES (?,?,?,?,?) 
          """,(vards, uzvards, dzimums, vecums, ier_datums))  #c- objekts, kas strada piesleguma, komanda, kas laus izpildit sql3 komantas- execute, iekavas noradu kurā laukā tiks ievietots, placeholdes(vietas turetaji)- jautajumu zimes, vertibas kas tiks pievienotas velak izmantojot dotos parametrus- pasas beigas jaliek ievavas mainigie

#viss... jaizver

logs.close()


 #vērtību kortesh/ž-