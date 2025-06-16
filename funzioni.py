#- nome e cognomi: classifica
#- Quanti maschi e quante femmine
#- Età media generale
#- Suddivisione per titoli: quanti hanno il titolo di ms/mna, quanti sig., quanti nessun titolo…
#- Età dei servi e delle serve, garzoni
#- Età media gruppi familiari
#- Altri dati età: esempio quanti superano i 40 anni?
#- Quante persone minori di 16 anni
#- In base all’età quanti maschi e quante femmine
#- Numero medio componenti gruppi familiari
#- Struttura nuclei familiari
#- Età media della moglie ed età media del marito
#- Differenza età marito moglie
#- Età primo figlio
#- Differenza età dei nobili e dei borghesi e popolo
#- Possibili genealogie, riunendo vicini tutti quelli con stesso cognome e accanto paternità
#- Quanti hanno già perso il padre? A che età?
#- Suddivisione per quartieri (Contrada della Piazza, Ghirolo ecc.)
from parsing import parse
import classi
df = parse()
my_list = []

def creaIstanze():
    for index, row in df.iterrows():
        if(row['Ruolo'].find("capofamiglia")!=-1 or row['Ruolo'].find("mater familias")!=-1 or row['Ruolo'].find("vedova")!=-1 or row['Ruolo'].find("capofamiglia vedovo")!=-1):
            classi.nGruppoFamigliare+=1
        p = classi.persona(row['Titolo'],row['Nome'],row['Cognome'],row['Figlio di'],row['Eta'],row['Ruolo'],row['Residenza'],classi.nGruppoFamigliare)
        p.stampa()
        my_list.append(p)
    return my_list

my_list = creaIstanze()








