#- nome e cognomi: classifica   //FATTA
#- Quanti maschi e quante femmine   //DA FARE
#- Età media generale   //FATTA
#- Suddivisione per titoli: quanti hanno il titolo di ms/mna, quanti sig., quanti nessun titolo…    //FATTA
#- Età dei servi e delle serve, garzoni     //FATTA
#- Età media gruppi familiari   //FATTA
#- Altri dati età: esempio quanti superano i 40 anni?   //FATTA
#- Quante persone minori di 16 anni     //FATTA
#- In base all’età quanti maschi e quante femmine   //DA FARE
#- Numero medio componenti gruppi familiari     //FATTA
#- Struttura nuclei familiari   //DA FARE
#- Età media della moglie ed età media del marito   //FATTA  
#- Differenza età marito moglie     //FATTA
#- Età primo figlio     //FATTA
#- Differenza età dei nobili e dei borghesi e popolo    //FATTA
#- Possibili genealogie, riunendo vicini tutti quelli con stesso cognome e accanto paternità    //DOPO
#- Quanti hanno già perso il padre? A che età?      //FATTA
#- Suddivisione per quartieri (Contrada della Piazza, Ghirolo ecc.)     //FATTA
from collections import Counter
from parsing import parse
import classi
df = parse()
my_list = []

def creaIstanze():
    for index, row in df.iterrows():
        if row['Ruolo'].find("capofamiglia")!=-1 or row['Ruolo'].find("mater familias")!=-1 or row['Ruolo'].find("vedova")!=-1 or row['Ruolo'].find("capofamiglia vedovo")!=-1: classi.nGruppoFamigliare+=1
        eta_str = str(row['Eta']).replace(',', '.')
        try:
            eta = float(eta_str)
        except ValueError:
            eta = 0
        p = classi.persona(str(row['Titolo']),str(row['Nome']),str(row['Cognome']),str(row['Figlio di']),eta,str(row['Ruolo']),str(row['Residenza']),classi.nGruppoFamigliare)
        p.stampa()
        my_list.append(p)
    return my_list

my_list = creaIstanze()
my_list = sorted(my_list, key=lambda x: x.gruppoFamigliare)

def pulisciTitoli(lista):
    for persona in lista:
        persona.titolo = persona.titolo.strip()
        
pulisciTitoli(my_list)

#Funzione 1
def classificaNomi(lista):
    nomi = [i.nome for i in lista]
    cognomi = [i.cognome for i in lista]
    classifica_nomi = Counter(nomi).most_common()
    classifica_cognomi = Counter(cognomi).most_common()
    return classifica_nomi, classifica_cognomi

nomi, cognomi = classificaNomi(my_list)
print("Classifica nomi:", nomi)
print("Classifica cognomi:", cognomi)

#Funzione 3
def mediaEta(lista):
    tot = 0
    for persona in lista:
        tot += persona.eta
    return int(tot/len(lista))

print(mediaEta(my_list))

#Funzione 4
def classificaTitoli(lista):
    titoli = [i.titolo for i in lista]
    classifica = Counter(titoli).most_common()
    return classifica

print(classificaTitoli(my_list))

#Funzione 6
def mediaEtaGruppiFamigliari(lista):
    gruppo = 0
    tot = 0
    n = 0
    medie = []
    for persona in lista:
        if persona.gruppoFamigliare != gruppo:
            medie.append(int(tot/n))
            tot=0
            n=0
            gruppo+=1
        tot+=persona.eta
        n+=1
    return medie

print(mediaEtaGruppiFamigliari(my_list))

#Funzione 7
def superoEtaLimite(lista):
    tot=0
    for persona in lista:
        if persona.eta > 40:
            tot+=1
    return tot

print(superoEtaLimite(my_list))

#Funzione 8
def minoriEtaMassima(lista):
    tot=0
    for persona in lista:
        if persona.eta < 16:
            tot+=1
    return tot

print(minoriEtaMassima(my_list))

#Funzione 12
def etaMediaConiugi(lista):
    totCapofamiglia = 0
    nCapofamiglia = 0
    totMaterFamilias = 0
    nMaterFamilias = 0
    totVedova = 0
    nVedova = 0
    totCapofamigliaVedovo = 0
    nCapofamigliaVedovo = 0
    for persona in lista:
        if persona.ruolo == "capofamiglia":
            totCapofamiglia += persona.eta
            nCapofamiglia += 1
        elif  persona.ruolo == "mater familias":
            totMaterFamilias += persona.eta 
            nMaterFamilias += 1
        elif persona.ruolo == "vedova":
            totVedova += persona.eta
            nVedova += 1
        elif persona.ruolo == "capofamiglia vedovo":
            totCapofamigliaVedovo += persona.eta
            nCapofamigliaVedovo += 1
    return [int(totCapofamiglia/nCapofamiglia),int(totMaterFamilias/nMaterFamilias),int(totVedova/nVedova),int(totCapofamigliaVedovo/nCapofamigliaVedovo)]

print(etaMediaConiugi(my_list))

def differenzaEtaConiugi(lista):
    lista = sorted(lista, key=lambda x: x.gruppoFamigliare)
    differenze = []
    if not lista:
        return differenze
    gruppo_corrente = lista[0].gruppoFamigliare
    marito = None
    moglie = None
    for persona in lista:
        if persona.gruppoFamigliare != gruppo_corrente:
            if marito is not None and moglie is not None:
                differenze.append(abs(marito - moglie))
            gruppo_corrente = persona.gruppoFamigliare
            marito = None
            moglie = None
        if persona.ruolo.strip().lower() == "capofamiglia":
            marito = persona.eta
        elif persona.ruolo.strip().lower() == "moglie":
            moglie = persona.eta
    
    if marito is not None and moglie is not None:
        differenze.append(abs(marito - moglie))
    return differenze

print(differenzaEtaConiugi(my_list))

def etaPrimoFiglio(lista):
    eta_primo_figlio = []
    gruppo_corrente = None
    eta_figli = []
    for persona in lista:
        if persona.gruppoFamigliare != gruppo_corrente:
            if eta_figli:
                eta_primo_figlio.append(max(eta_figli))
            gruppo_corrente = persona.gruppoFamigliare
            eta_figli = []
        if persona.ruolo.strip().lower() in ["figlio", "figlia"]:
            eta_figli.append(persona.eta)
    
    if eta_figli:
        eta_primo_figlio.append(max(eta_figli))
    return eta_primo_figlio

print(etaPrimoFiglio(my_list))
#mie funzioni            
def etaServitu(lista):
    eta_servitu = 0
    totServi= 0
    for persona in lista:
        if persona.ruolo.strip().lower() == "servi" or persona.ruolo.strip().lower() == "serve" or persona.ruolo.strip().lower() == "garzoni":
            eta_servitu+=persona.eta
            totServi+=1
    return eta_servitu/totServi if totServi>0 else 0

print(etaServitu(my_list))

def persoPadri(lista):
    tot=0
    trenta=0
    p=[]
    for persona in lista:
        if persona.eta < 30:
            p.append(persona)
            trenta+=1
    for persona in p:
        if persona.padre.strip().lower().startswith("q"):
            tot+=1
    ritorno=[]
    ritorno.append(tot)
    ritorno.append((tot/trenta)*100 if trenta > 0 else 0)
    return ritorno
    
print(persoPadri(my_list))
            
def numeroGruppiFamigliari(lista):
    media=[]
    i=0
    n=0
    media.append(0)
    for persona in lista:
        if persona.gruppoFamigliare==i:
            media[i]+=persona.eta
            n+=1
        else:
            media[i]/=n
            media.append(persona.eta)
            i+=1
            n=1
    media[i]/=n
    return media

print(numeroGruppiFamigliari(my_list))

def differenzaEtaTraClassi(lista):
    differenze=[0,0,0]
    n=0
    p=0
    b=0
    for persona in lista:
        if "signor" in persona.titolo.lower() or "signora" in persona.titolo.lower() or persona.titolo.lower() == "sig" or persona.titolo.lower() == "sig.ra":
            differenze[0]+=persona.eta
            n+=1
        elif persona.titolo.lower()=="ms" or persona.titolo.lower()=="mna":
            differenze[1]+=persona.eta
            b+=1
        elif persona.titolo.lower()=="nessuno":
            differenze[2]+=persona.eta
            p+=1
    differenze[0]/=n if n > 0 else 0
    differenze[1]/=b if b > 0 else 0
    differenze[2]/=p if p > 0 else 0
    return differenze

print(differenzaEtaTraClassi(my_list))

def suddivisioneQuartieri(lista):
    quartieri = {}
    for persona in lista:
        if persona.residenza.strip().lower() in quartieri:
            quartieri[persona.residenza.strip().lower()] += 1
        else:
            quartieri[persona.residenza.strip().lower()] = 1
    return quartieri

print(suddivisioneQuartieri(my_list))


            








