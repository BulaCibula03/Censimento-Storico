#- nome e cognomi: classifica   //FATTA
#- Quanti maschi e quante femmine   //FATTA
#- Età media generale   //FATTA
#- Suddivisione per titoli: quanti hanno il titolo di ms/mna, quanti sig., quanti nessun titolo…    //FATTA
#- Età dei servi e delle serve, garzoni     //FATTA
#- Età media gruppi familiari   //FATTA
#- Altri dati età: esempio quanti superano i 40 anni?   //FATTA
#- Quante persone minori di 16 anni     //FATTA
#- In base all’età quanti maschi e quante femmine   //FATTA
#- Numero medio componenti gruppi familiari     //FATTA
#- Struttura nuclei familiari   //FATTA
#- Età media della moglie ed età media del marito   //FATTA  
#- Differenza età marito moglie     //FATTA
#- Età primo figlio     //FATTA
#- Differenza età dei nobili e dei borghesi e popolo    //FATTA
#- Possibili genealogie, riunendo vicini tutti quelli con stesso cognome e accanto paternità    //DOPO
#- Quanti hanno già perso il padre? A che età?      //FATTA
#- Suddivisione per quartieri (Contrada della Piazza, Ghirolo ecc.)     //FATTA
from collections import Counter
from . import classi
from collections import defaultdict
my_list = []

def creaIstanze(df):
    for index, row in df.iterrows():
        if row['ruolo'].find("capofamiglia")!=-1 or row['ruolo'].find("mater familias")!=-1 or row['ruolo'].find("vedova")!=-1 or row['ruolo'].find("capofamiglia vedovo")!=-1: classi.nGruppoFamigliare+=1
        eta_str = str(row['eta']).replace(',', '.')
        try:
            eta = float(eta_str)
        except ValueError:
            eta = 0
        p = classi.persona(str(row['titolo']).lower().strip(),str(row['nome']).strip(),str(row['cognome']).strip(),str(row['figlio di']).strip(),eta,str(row['ruolo']).strip(),str(row['residenza']).strip(),classi.nGruppoFamigliare)
        p.stampa()
        my_list.append(p)
    return my_list

def pulisciTitoli(lista):
    for persona in lista:
        persona.titolo = persona.titolo.strip()

#Funzione 1
def classificaNomi(lista):
    nomi = [i.nome for i in lista]
    cognomi = [i.cognome for i in lista]
    classifica_nomi = Counter(nomi).most_common()
    classifica_cognomi = Counter(cognomi).most_common()
    return classifica_nomi, classifica_cognomi

#Funzione 3
def mediaEta(lista):
    tot = 0
    for persona in lista:
        tot += persona.eta
    return int(tot/len(lista))

#Funzione 4
def classificaTitoli(lista):
    titoli = [i.titolo for i in lista]
    classifica = Counter(titoli).most_common()
    return classifica

#Funzione 6
def mediaEtaGruppiFamigliari(lista):
    gruppo = 0
    tot = 0
    n = 0
    medie = {}
    for persona in lista:
        if persona.gruppoFamigliare != gruppo:
            medie[gruppo] = int(tot/n)
            tot=0
            n=0
            gruppo+=1
        tot+=persona.eta
        n+=1
    if n > 0:
        medie[gruppo] = int(tot/n)
    return medie

#Funzione 7
def superoEtaLimite(lista):
    tot=0
    for persona in lista:
        if persona.eta > 40:
            tot+=1
    return tot

#Funzione 8
def minoriEtaMassima(lista):
    tot=0
    for persona in lista:
        if persona.eta < 16:
            tot+=1
    return tot

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
    totMoglie = 0
    nMoglie = 0
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
        elif persona.ruolo == "moglie":
            totMoglie +=persona.eta
            nMoglie += 1
    return [int(totCapofamiglia/nCapofamiglia),int(totMoglie/nMoglie),int(totMaterFamilias/nMaterFamilias),int(totVedova/nVedova),int(totCapofamigliaVedovo/nCapofamigliaVedovo)]

def differenzaEtaConiugi(lista):
    lista = sorted(lista, key=lambda x: x.gruppoFamigliare)
    differenze = {}
    if not lista:
        return differenze
    gruppo_corrente = lista[0].gruppoFamigliare
    marito = None
    moglie = None
    for persona in lista:
        if persona.gruppoFamigliare != gruppo_corrente:
            if marito is not None and moglie is not None:
                differenze[gruppo_corrente] = abs(marito - moglie)
            gruppo_corrente = persona.gruppoFamigliare
            marito = None
            moglie = None
        if persona.ruolo.strip().lower() == "capofamiglia":
            marito = persona.eta
        elif persona.ruolo.strip().lower() == "moglie":
            moglie = persona.eta
    if marito is not None and moglie is not None:
        differenze[gruppo_corrente] = abs(marito - moglie)
    return differenze

def etaPrimoFiglio(lista):
    eta_primo_figlio = {}
    gruppo_corrente = None
    eta_figli = []
    for persona in lista:
        if persona.gruppoFamigliare != gruppo_corrente:
            if eta_figli and gruppo_corrente is not None:
                eta_primo_figlio[gruppo_corrente] = max(eta_figli)
            gruppo_corrente = persona.gruppoFamigliare
            eta_figli = []
        if persona.ruolo.strip().lower() in ["figlio", "figlia"]:
            eta_figli.append(persona.eta)
    if eta_figli and gruppo_corrente is not None:
        eta_primo_figlio[gruppo_corrente] = max(eta_figli)
    return eta_primo_figlio
          
def etaServitu(lista):
    eta_servitu = 0
    totServi = 0
    ruoli_servitu = [
        "servo", "serva", "servitore", "servitrice", "garzone", "staffiero",
        "sguattero", "famiglio di stalla", "servi", "serve", "garzoni"
    ]
    for persona in lista:
        if persona.ruolo.strip().lower() in ruoli_servitu:
            eta_servitu += persona.eta
            totServi += 1
    return int(eta_servitu / totServi) if totServi > 0 else 0

def persoPadri(lista):
    return [p for p in lista if p.padre.strip().lower().startswith("q")]
            
def numeroGruppiFamigliari(lista):
    media=[]
    i=0
    n=0
    media.append(0)
    for persona in lista:
        if persona.gruppoFamigliare==i:
            media[i]+=persona.eta
            media[i]=int(media[i])
            n+=1
        else:
            media[i]/=n
            media[i]=int(media[i])
            media.append(persona.eta)
            i+=1
            n=1
    media[i]/=n
    media[i]=int(media[i])
    return media

def differenzaEtaTraClassi(lista):
    eta_nobili = []
    eta_borghesi = []
    eta_popolo = []
    for persona in lista:
        titolo = persona.titolo.strip().lower()

        if any(t in titolo for t in ["signor", "signora", "sig.", "sig", "sig.ra"]):
            eta_nobili.append(persona.eta)

        elif titolo in ["ms", "mna"]:
            eta_borghesi.append(persona.eta)

        elif titolo == "nessuno" or persona.ruolo.strip().lower() in ["servo", "serva", "servitore", "servitrice", "garzone", "staffiero"]:
            eta_popolo.append(persona.eta)

    media_nobili = int(sum(eta_nobili)/len(eta_nobili)) if eta_nobili else 0
    media_borghesi = int(sum(eta_borghesi)/len(eta_borghesi)) if eta_borghesi else 0
    media_popolo = int(sum(eta_popolo)/len(eta_popolo)) if eta_popolo else 0
    return [media_nobili, media_borghesi, media_popolo]

def suddivisioneQuartieri(lista):
    gruppi = {}
    for persona in lista:
        gruppi.setdefault(persona.gruppoFamigliare, []).append(persona)
    gruppi_quartiere = []
    for n_gruppo, membri in gruppi.items():
        quartieri = [p.residenza.strip().lower() for p in membri]
        if quartieri:
            quartiere_prevalente, freq = Counter(quartieri).most_common(1)[0]
        else:
            quartiere_prevalente, freq = "", 0
        gruppi_quartiere.append((n_gruppo, membri, quartiere_prevalente, freq))
    gruppi_quartiere.sort(key=lambda x: (x[2], -x[3], x[0]))
    lista_ordinata = []
    for _, membri, _, _ in gruppi_quartiere:
        lista_ordinata.extend(membri)
    return lista_ordinata

def mediaNumeroGruppiFamiliari(lista):
    gruppi = []
    i=0
    tot=0
    gruppi.append(0)
    for persona in lista:
        if persona.gruppoFamigliare==i:
            gruppi[i] += 1
        else:
            tot+=gruppi[i]
            gruppi.append(1)
            i+=1
    tot += gruppi[i] 
    return int(tot/(i+1))

def contaMaschiFemmine(lista):
    sesso=[0,0]
    for persona in lista:
        ruolo = persona.ruolo.strip().lower()
        titolo = persona.titolo.strip().lower()
        nome = persona.nome.strip().lower()
        if titolo in ["sig", "signor", "ms", "capofamiglia", "monsignore"]:
            sesso[0] += 1
        elif titolo in ["sig.ra", "signora", "vedova", "mater familias", "mna"]:
            sesso[1] += 1
        elif ruolo in ["figlio", "servo", "nipote", "garzone", "famiglio di stalla", "staffiero"]:
            sesso[0] += 1
        elif ruolo in ["figlia", "serva", "nipotina"]:
            sesso[1] += 1
        elif nome.endswith("a"):
            sesso[1] += 1
        else:
            sesso[0] += 1

    return sesso

def trovaMaschi(lista):
    m = []
    for persona in lista:
        ruolo = persona.ruolo.strip().lower()
        titolo = persona.titolo.strip().lower()
        nome = persona.nome.strip().lower()
        if titolo in ["sig", "signor", "ms", "capofamiglia", "monsignore"]:
            m.append(persona)
        elif ruolo in ["figlio", "servo", "nipote", "garzone", "famiglio di stalla", "staffiero"]:
            m.append(persona)
        elif not nome.endswith("a") and not (
            titolo in ["sig.ra", "signora", "vedova", "mater familias"] or
            ruolo in ["figlia", "serva", "nipotina"]
        ):
            m.append(persona)
    return m

def trovaFemmine(lista):
    f = []
    for persona in lista:
        ruolo = persona.ruolo.strip().lower()
        titolo = persona.titolo.strip().lower()
        nome = persona.nome.strip().lower()
        if titolo in ["sig.ra", "signora", "vedova", "mater familias", "mna"]:
            f.append(persona)
        elif ruolo in ["figlia", "serva", "nipotina"]:
            f.append(persona)
        elif nome.endswith("a") and not (
            titolo in ["sig", "signor", "ms", "mna", "capofamiglia", "monsignore"] or
            ruolo in ["figlio", "servo", "nipote", "garzone", "famiglio di stalla", "staffiero"]
        ):
            f.append(persona)
    return f

def quantiEtaMaschiEFemmine(lista):
    fascioEtaMaschile=[0,0,0,0] # 0= 0-14, 1=15-30, 2=31-45, 3=46
    fascioEtaFemminile=[0,0,0,0] # 0= 0-14, 1=15-30, 2=31-45, 3=46
    femmine=trovaFemmine(lista)
    maschi=trovaMaschi(lista)

    for persona in femmine:
        eta = persona.eta
        if eta < 15:
            fascioEtaFemminile[0] += 1
        elif eta < 31:
            fascioEtaFemminile[1] += 1
        elif eta < 46:
            fascioEtaFemminile[2] += 1
        else:
            fascioEtaFemminile[3] += 1
    for persona in maschi:
        eta = persona.eta
        if eta < 15:
            fascioEtaMaschile[0] += 1
        elif eta < 31:
            fascioEtaMaschile[1] += 1
        elif eta < 46:
            fascioEtaMaschile[2] += 1
        else:
            fascioEtaMaschile[3] += 1

    return fascioEtaFemminile,fascioEtaMaschile

def strutturaFamigliare(lista):
    gruppi = {}
    for persona in lista:
        gruppi.setdefault(persona.gruppoFamigliare, []).append(persona)
    return list(gruppi.values())

def info_gruppi(lista):
    gruppi = {}
    struttura = strutturaFamigliare(lista)
    diff_eta = differenzaEtaConiugi(lista)
    eta_primo = etaPrimoFiglio(lista)
    for idx, gruppo in enumerate(struttura):
        n_gruppo = gruppo[0].gruppoFamigliare
        gruppi[n_gruppo] = {
            "numero": n_gruppo,
            "media_componenti": len(gruppo),
            "diff_eta": diff_eta.get(n_gruppo, ""),
            "eta_primo_figlio": eta_primo.get(n_gruppo, "")
        }
    return gruppi
def etaFiglie(lista):
    figliePerGruppo=defaultdict(list)

    for persona in lista:
        if persona.ruolo.strip().lower()=="figlia":
            figliePerGruppo[persona.gruppoFamigliare].append(persona.eta)
    mediaFiglie = {}
    for gruppo, eta_lista in figliePerGruppo.items():
        media= int(sum(eta_lista)/len(eta_lista)) if eta_lista else 0
        mediaFiglie[gruppo] = media
    return mediaFiglie

def etaFigli(lista):
    figliPerGruppo=defaultdict(list)
    for persona in lista:
        if persona.ruolo.strip().lower()=="figlio":
            figliPerGruppo[persona.gruppoFamigliare].append(persona.eta)
    mediaFigli = {}
    for gruppo, eta_lista in figliPerGruppo.items():
        media= int(sum(eta_lista)/len(eta_lista)) if eta_lista else 0
        mediaFigli[gruppo] = media
    return mediaFigli
def etaFiglietot(lista):
    figlietotal=0
    nFiglie=0
    for persona in lista:
        if persona.ruolo.strip().lower()=="figlia":
            figlietotal+=persona.eta
            nFiglie+=1
    return round(figlietotal/nFiglie) if nFiglie > 0 else 0
def etaFiglitot(lista):
    figlitotal=0
    nFigli=0
    for persona in lista:
        if persona.ruolo.strip().lower()=="figlio":
            figlitotal+=persona.eta
            nFigli+=1
    return round(figlitotal/nFigli) if nFigli > 0 else 0
