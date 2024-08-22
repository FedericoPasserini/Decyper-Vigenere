import os
import random
import chardet
import pandas as pd
import matplotlib.pyplot as plt
from unidecode import unidecode


lemmi = [
    "arduo",
    "effimero",
    "sibilo",
    "breve",
    "obsoleto",
    "zefiro",
    "epocale",
    "effervescente",
    "antitesi",
    "lucubrazione",
    "onirico",
    "fiorire",
    "effluvio",
    "discreto",
    "zenit",
    "solare",
    "oltranzista",
    "perlustrare",
    "vorace",
    "quisquilia",
    "discrepanza",
    "epifania",
    "ineffabile",
    "paradigma",
    "dissonante",
    "luminoso",
    "volubile",
    "efflorescenza",
    "furtivo",
    "insipido",
    "zenzero",
    "piccolo",
    "peregrino",
    "ubiquità",
    "lontananza",
    "effluente",
    "epitome",
    "nostalgico",
    "zenzero",
    "aberrante",
    "oligarchia",
    "giovane",
    "vanitoso",
    "sibilare",
    "quintessenza"
]

def RandomKey(lemmi):
    lemmi = [parola.upper() for parola in lemmi]
    chiave = random.choice(lemmi)

    return chiave

def trovaRicorsività(cifra):
    corrente = []
    i = 0
    j = 0
    k = 0
    x = 0
    y = 0
    for i in range (1,(len(cifra)//2)):
        for k in range (0, len(cifra)-i):
            for j in range (k,k+i):
                corrente = []
                corrente.append(cifra[j])

            for x in range (0,len(cifra)-(k+2*i)):
                for y in range (x+k+i,y+k+2*i):
                    confrontato = []
                    confrontato.append(cifra[y])
            if (corrente == confrontato):
                print("trovata corrispondenza della sequenza", corrente,"in posizione", k,"con la sequenza in posizione", x+k+i,"la distanza tra le due è", x+i)






def leggi_contenuto_file_random(cartella):
    elenco_file = [f for f in os.listdir(cartella) if os.path.isfile(os.path.join(cartella, f))]

    if not elenco_file:
        print("La cartella è vuota.")
        return None

    file_scelto = random.choice(elenco_file)
    percorso_file = os.path.join(cartella, file_scelto)

    # Rileva la codifica del file
    with open(percorso_file, 'rb') as rawfile:
        result = chardet.detect(rawfile.read())
        encoding = result['encoding']

    # Apri il file con la codifica rilevata
    with open(percorso_file, 'r', encoding=encoding) as file:
        contenuto = file.read()

    contenuto_pulito = ''.join(char for char in contenuto if char.isalnum()).upper()
    contenuto_pulito = unidecode(contenuto_pulito)

    return contenuto_pulito

def cifratore(testo, chiave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    j = 0
    i = 0
    cifra = []

    for i in range(len(testo)):
        OffSet = ord(chiave[j])-ord('A')
        NewIndex = (OffSet+(ord(testo[i])-ord('A')))%26
        cifra.append(alfabeto[NewIndex])
        i+=1
        j= (j+1)%(len(chiave))

    return "".join(cifra)

def dividi(cifra, num):
    a = 0
    i = 0
    sezioni = [[] for _ in range(num)]

    while a < len(cifra):
        sezioni[i].append(cifra[a])
        i = (i + 1) % num
        a += 1

    return sezioni

def AnalisiFrequenza(sezioni, num):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    risultati = [[0 for _ in range(26)] for _ in range(num)]

    for i in range(num):
        for j in range(26):
            comparsa = sezioni[i].count(alfabeto[j])
            risultati[i][j] = comparsa / len(sezioni[i])

    return risultati

def decifratore(chiave, cifra):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Decifratura = [] 
    j = 0
    i = 0

    for i in range(len(cifra)):
        OffSet = ord(chiave[j])-ord('A')
        NewIndex = (26-(OffSet-(ord(cifra[i])-ord('A'))))%26
        Decifratura.append(alfabeto[NewIndex])
        i+=1
        j= (j+1)%(len(chiave))

    return "".join(Decifratura)


def GraficaFreq(sezioni, risultati):
    for i in range(len(sezioni)):
        print(sezioni[i])

    for i in range(num):
        print("sezione ", i, "\n")
        for j in range(26):
            print(alfabeto[j], risultati[i][j], "\n")

    for i in range(num):
        df_sezione = pd.DataFrame({'Lettera': list(alfabeto), 'Frequenza': risultati[i]})
        df_sezione.plot(kind='bar', x='Lettera', y='Frequenza', title=f'Sezione {i}', legend=False)
        plt.xlabel('Lettera')
        plt.ylabel('Frequenza')
        plt.show()

    return


alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
IsOn=True
print("Decifra messaggi in codice dai\n")

while IsOn==True:
    a = int(input("[1] assegna randomicamente un testo dalla cartella\n[2] ho un testo da decifrare\n"))
 

    while (a!= 1 and a!= 2):
        print("eddai però")
        a = int(input("[1] assegna randomicamente un testo dalla cartella\n[2] ho un testo da decifrare\n"))

    match a:
        case 1:
            percorso_della_cartella = "C:\\Users\\feder\\OneDrive\\Desktop"
            testo = leggi_contenuto_file_random(percorso_della_cartella)
            chiave = RandomKey(lemmi)
            cifra = cifratore(testo, chiave)
            print(cifra)

        case 2:
            cifra = input("Inserisci il tuo testo cifrato:\n")
            cifra_pulita = ''.join(char for char in cifra if char.isalnum()).upper()
            cifra_pulita = unidecode(cifra_pulita)
            print(cifra_pulita)
    

    trovaRicorsività(cifra)

    num = int(input("Numero sezioni:\n"))
    sezioni = dividi(cifra_pulita, num)
    risultati = AnalisiFrequenza(sezioni, num)
    SpettroFreq = [[] for _ in range(num)]

    GraficaFreq(sezioni, risultati)
    
    chiave = input("inserisci la chiave:\n")
    decifratura = decifratore(chiave, cifra_pulita)
    print(decifratura)

    ancora =int(input("altro giro?([1]si,[2]no):\n"))

    while (a!= 1,2):
        print("eddai però")
        ancora =int(input("altro giro?([1]si,[2]no):\n"))

    match a:
        case 1:
            IsOn = True  

        case 2:
            IsOn = False