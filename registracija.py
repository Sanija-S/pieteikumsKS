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
    [sg.T("Vecums:"), sg.Radio(key="radio")],

]
#galvenais cikls
#viss... jaizver
logs=sg.Window("Datu reģistrs", layout, resizable=True)