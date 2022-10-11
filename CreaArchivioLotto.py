#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import datetime   # importo il modulo datetime per calcoloare l'anno corrente
import string
import requests
from bs4 import BeautifulSoup
import csv
import os.path
from tkinter import *
		

canvas3 = ''	
canvas6 = ''	

root = Tk()
prompt = StringVar()
root.title('ARCHIVIO STORICO LOTTO')
root.geometry('500x350')

# first create the canvas
canvas = Canvas(height=500,width=350)
canvas.pack(fill="both", expand=True)

# "highlightthickness=0" assegna al bordo del frame/canvas la dimensione 0
frame0 = Frame(canvas, width = 500, height = 130, highlightthickness=0)
frame0.grid(row=0,columnspan=3)
frame1 = Frame(canvas, width = 110, height = 70, highlightthickness=0)
frame1.grid(row=1,column=0)
frame2 = Frame(canvas, width = 290, height = 70, highlightthickness=0)
frame2.grid(row=1,column=1)
frame3 = Frame(canvas, width = 150, height = 70, highlightthickness=0)
frame3.grid(row=1,column=2)
frame4 = Frame(canvas, width = 110, height = 150, highlightthickness=0)
frame4.grid(row=2,column=0)
frame5 = Frame(canvas, width = 290, height = 150, highlightthickness=0)
frame5.grid(row=2,column=1)
frame6 = Frame(canvas, width = 150, height = 150, highlightthickness=0)
frame6.grid(row=2,column=2)

def esci(event):
	if event.x >= 30 and event.x <= 70:
		if event.y >= 60 and event.y <= 100:
			root.destroy()

def elab(event):
	if event.x >= 50 and event.x <= 240:
		if event.y >= 10 and event.y <= 60:
			image3 = PhotoImage(file = "elabora.gif")
			canvas3.image =image3
			canvas3.create_image(0,0,anchor='nw', image=image3)
			image6 = PhotoImage(file = "tempo.gif")
			canvas6.image =image6
			canvas6.create_image(0,0,anchor='nw', image=image6)
			canvas6.after(10000, archivio)
					
 
def Inizio():
	global canvas3
	global canvas6
	
	canvas1 = Canvas(frame0, width=500, height=130, highlightthickness=0)
	canvas1.delete("all")
	image1 = PhotoImage(file = "1.gif")
	canvas1.image =image1
	obj1 = canvas1.create_image(0,0,anchor='nw', image=image1)	
	canvas1.pack(fill="both", expand=True)	
	
	canvas2 = Canvas(frame1, width=110, height=70, highlightthickness=0)
	canvas2.delete("all")
	image2 = PhotoImage(file = "2.gif")
	canvas2.image =image2
	obj2 = canvas2.create_image(0,0,anchor='nw', image=image2)
	canvas2.pack(fill="both", expand=True)	
	
	canvas3 = Canvas(frame2, width=290, height=70, highlightthickness=0)
	canvas3.delete("all")
	image3 = PhotoImage(file = "archivio.gif")
	canvas3.image =image3
	obj3 = canvas3.create_image(0,0,anchor='nw', image=image3)
	canvas3.tag_bind(obj3, '<1>', elab)
	canvas3.pack(fill="both", expand=True)	
	
	canvas4 = Canvas(frame3, width=100, height=70, highlightthickness=0)
	canvas4.delete("all")
	image4 = PhotoImage(file = "4.gif")
	canvas4.image =image4
	canvas4.create_image(0,0,anchor='nw', image=image4)
	canvas4.pack(fill="both", expand=True)	
	
	canvas5 = Canvas(frame4, width=110, height=150, highlightthickness=0)
	canvas5.delete("all")
	image5 = PhotoImage(file = "5.gif")
	canvas5.image =image5
	obj5 = canvas5.create_image(0,0,anchor='nw', image=image5)
	canvas5.pack(fill="both", expand=True)	
	
	canvas6 = Canvas(frame5, width=290, height=150, highlightthickness=0)
	canvas6.delete("all")
	image6 = PhotoImage(file = "6.gif")
	canvas6.image =image6
	canvas6.create_image(0,0,anchor='nw', image=image6)
	canvas6.pack(fill="both", expand=True)	
	
	canvas7 = Canvas(frame6, width=100, height=150, highlightthickness=0)
	canvas7.delete("all")
	image7 = PhotoImage(file = "exit1.gif")
	canvas7.image =image7
	obj7 = canvas7.create_image(0,0,anchor='nw', image=image7)
	canvas7.tag_bind(obj7, '<1>', esci)
	canvas7.pack(fill="both", expand=True)


def No_aggiornamenti():
	image3 = PhotoImage(file = "noAgg.gif")
	canvas3.image =image3
	obj3 = canvas3.create_image(0,0,anchor='nw', image=image3)
	image6 = PhotoImage(file = "6.gif")
	canvas6.image =image6
	canvas6.create_image(0,0,anchor='nw', image=image6)

def aggiornamenti():
	image3 = PhotoImage(file = "agg.gif")
	canvas3.image =image3
	obj3 = canvas3.create_image(0,0,anchor='nw', image=image3)
	image6 = PhotoImage(file = "6.gif")
	canvas6.image =image6
	canvas6.create_image(0,0,anchor='nw', image=image6)

def creazione():
	image3 = PhotoImage(file = "crea.gif")
	canvas3.image =image3
	obj3 = canvas3.create_image(0,0,anchor='nw', image=image3)
	image6 = PhotoImage(file = "6.gif")
	canvas6.image =image6
	canvas6.create_image(0,0,anchor='nw', image=image6)
	



def archivio():	
	listato = []
	estratti = []
	ultimi_estratti = []
	ruote = ['Bari','Cagliari','Firenze','Genova','Milano','Napoli','Palermo','Roma','Torino',\
	'Venezia','Nazionale']
	blak_list = ["Estrazione", "n.", "del", "RUOTA", "1o", "2o", "3o", "4o", "5o", "estr."]
	
	data_attuale = datetime.datetime.now()
	anno = str(data_attuale.year)
	mese = str(data_attuale.month)
	giorno = str(data_attuale.day)
	
	
	percorso = "http://www.estrazionedellotto.it/risultati/archivio-lotto-"
	estensione = ".asp"

	mese_lung = len(mese)
	giorno_lung = len(giorno)

	if mese_lung == 1:
		mese = '0' + mese 
	if giorno_lung == 1:
		giorno = '0' + giorno
		
	oggi = str(anno) + '/' + str(mese) + '/' +  str(giorno)

	fname = 'archivio.csv'
	esiste = os.path.isfile(fname)

	if esiste:
		f = open(fname, 'r')
		lines = f.readlines ()
		f.close()
		
		last_line = lines[len(lines)-1]
		last_line_data = last_line[0:10]
		last_line_data = int(last_line_data.replace('/', ''))
		oggi = int(oggi.replace('/', ''))
		anno_ultimo_aggiornamento = last_line[0:4]
		if (last_line_data == oggi):
			No_aggiornamenti()               ################## def
		if (last_line_data < oggi):				
			ultima = int(anno_ultimo_aggiornamento)
			ad = int(anno)
			if (ultima < ad):		# se è di qualche anno prima
				while ultima < (ad + 1):
					pagina = percorso + str(ultima) + estensione
					page = requests.get(pagina)
					soup = BeautifulSoup(page, 'html.parser')

					divisione = soup.find('div', attrs={'class': 'tabellaLotto-arch'})

					estrazione_num = divisione.text.strip()
					separa_parole = estrazione_num.split()
					lunghezza = len(separa_parole)
					i = 0
					while i in range(lunghezza):		
						if separa_parole[i] not in blak_list:
							if '/' in separa_parole[i]:
								da1 = separa_parole[i]
								da = da1[6:] + '/' + da1[3:5] + '/' + da1[0:2]  
							if separa_parole[i] in ruote:
								ru = separa_parole[i]
								ri = da, ru, separa_parole[i+1], separa_parole[i+2], separa_parole[i+3], \
								separa_parole[i+4], separa_parole[i+5]
								estratti.append(ri)
								i = i + 5	
						i = i + 1
					sortedlist = sorted(estratti, key=lambda column: column[0])
					for i in sortedlist:
						with open('archivio.csv', 'ab') as myfile:
							wr = csv.writer(myfile)
							wr.writerow(i)
					estratti = []
					ultima = ultima + 1	
					aggiornamenti()               ################## def
						
					
					
			else:		 # se è dello stesso anno
				pagina = "http://www.estrazionedellotto.it/risultati/archivio-lotto-" + \
				anno_ultimo_aggiornamento + ".asp" 
				page = requests.get(pagina)
				soup = BeautifulSoup(page, 'html.parser')

				divisione = soup.find('div', attrs={'class': 'tabellaLotto-arch'})

				estrazione_num = divisione.text.strip()
				separa_parole = estrazione_num.split()
				lunghezza = len(separa_parole)
				i = 0
				while i in range(lunghezza):		
					if separa_parole[i] not in blak_list:
						if '/' in separa_parole[i]:
							da1 = separa_parole[i]
							da = da1[6:] + '/' + da1[3:5] + '/' + da1[0:2]
							da2 = int(da.replace('/', '')) 
						if separa_parole[i] in ruote:
							ru = separa_parole[i]
							ri = da, ru, separa_parole[i+1], separa_parole[i+2], separa_parole[i+3], \
							separa_parole[i+4], separa_parole[i+5]
							if (last_line_data < da2):
								ultimi_estratti.append(ri)
							i = i + 5	
					i = i + 1
					
				if len(ultimi_estratti) > 0:
					sortedlist = sorted(ultimi_estratti, key=lambda column: column[0])
					for i in sortedlist:
						with open('archivio.csv', 'a') as myfile:
							wr = csv.writer(myfile)
							wr.writerow(i)
					ultimi_estratti = []
					aggiornamenti()               ################## def
				else:
					No_aggiornamenti()               ################## def
		
	else:
		fine = data_attuale.year
		inizio = 1871

		percorso = "http://www.estrazionedellotto.it/risultati/archivio-lotto-"
		estensione = ".asp"

		while inizio < (fine + 1):
			pagina = percorso + str(inizio) + estensione
			page = requests.get(pagina)
			soup = BeautifulSoup(page, 'html.parser')

			divisione = soup.find('div', attrs={'class': 'tabellaLotto-arch'})

			estrazione_num = divisione.text.strip()
			separa_parole = estrazione_num.split()
			lunghezza = len(separa_parole)
			i = 0
			while i in range(lunghezza):		
				if separa_parole[i] not in blak_list:
					if '/' in separa_parole[i]:
						da1 = separa_parole[i]
						da = da1[6:] + '/' + da1[3:5] + '/' + da1[0:2]  
					if separa_parole[i] in ruote:
						ru = separa_parole[i]
						ri = da, ru, separa_parole[i+1], separa_parole[i+2], separa_parole[i+3], \
						separa_parole[i+4], separa_parole[i+5]
						estratti.append(ri)
						i = i + 5	
				i = i + 1
			sortedlist = sorted(estratti, key=lambda column: column[0])
			for i in sortedlist:
				with open('archivio.csv', 'ab') as myfile:
					wr = csv.writer(myfile)
					wr.writerow(i)
			estratti = []
			inizio = inizio + 1	
			creazione()               ################## def
    
Inizio()

root.mainloop()
	

	
	
