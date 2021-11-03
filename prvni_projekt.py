'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
oddelovac='-'*40
list_slov=[]
r_uzivatele={'bob': '123', 'ann': "pass123", 'mike': 'password123','liz':'pass123'}
user=input("Zadej uživatelské jméno: ")
heslo=input("Zadej heslo: ")
print(oddelovac)

if user in r_uzivatele and r_uzivatele[user]==heslo:
    print(f'Vítej {user}, bude Vám umožněno analyzovat text.')
else:
    print('Špatné heslo nebo uživatelské jméno. Ukončuji.')
    exit()
print(oddelovac)
vyber=input('Zadej cislo textu (od 1 do 3), který text se má analyzovat: ')
if vyber.isnumeric() and int(vyber) in range (1,4):
    print('Výběr v pořádku.')
    vyber=int(vyber)-1
else:
    print('Špatný výběr. Ukončuji')
    exit()
#funguje:
a_text=TEXTS[vyber].split(sep=' ')
for slovo in a_text:
    if slovo:
        list_slov.append(slovo.strip('\n,.'))

#treti pokus na rozdeleni stringu do listu. Proc nefunguje???
#list_slov=[TEXTS[vyber].strip("?@{}&~ˇ^˘°˛`„´˝÷<>* .()#đ\n") for slovo in TEXTS[vyber].split(sep=" ")]

pocet_slov=len(list_slov)
pocet_titlu=0
pocet_kapitalek=0
pocet_malych_slov=0
pocet_cisel=0
suma_cisel=0
nejdelsi=0
nejkratsi=len(list_slov[0])
pocitadlo= {}
for slovo in list_slov:
    if slovo.istitle():
        pocet_titlu+=1
    elif slovo.isupper() and slovo.isalpha():
        pocet_kapitalek += 1
    elif slovo.islower() and slovo.isalpha():
        pocet_malych_slov+=1
    elif slovo.isnumeric():
        pocet_cisel+=1
        suma_cisel+=int(slovo)
    delka = pocitadlo.setdefault(len(slovo), 0)
    pocitadlo.update({len(slovo): delka + 1})

# generovani prazdneho slovniku od nejkratsiho slova po nejdelsi
#    if len(slovo)>nejdelsi:
#        nejdelsi=len(slovo)
#    elif len(slovo)<nejkratsi:
#        nejkratsi=len(slovo)
#for cislo in range(nejkratsi,nejdelsi+1):
#    pocitadlo.setdefault(cislo)

#for slovo in list_slov:
#    delka=pocitadlo.setdefault(len(slovo),0)
#    pocitadlo.update({len(slovo): delka+1})

#finální tisk:
print(f'''{oddelovac}
V textu je {pocet_slov} slov.
V textu je {pocet_titlu} slov začínajících velkým písmenem.
V textu je {pocet_kapitalek} slov psaných velkými písmeny.
V textu je {pocet_malych_slov} slov psaných malými písmeny.
V textu je {pocet_cisel} čísel.
Suma všech čísel je {suma_cisel}
{oddelovac}
DELKA |       ČETNOST       | POČET
{oddelovac}''')

for i in range(min(pocitadlo),max(pocitadlo)+1):
    pocet=pocitadlo.get(i)
    if i<10:
        delka=" "+str(i)
    else:
        delka=str(i)
    if not pocet:
        pocet=0
    graf=pocet * '*' + str((19-pocet) * ' ')
    print(f'  {delka}  | {graf} | {pocet}')



