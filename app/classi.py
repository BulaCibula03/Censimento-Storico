nGruppoFamigliare=0
class persona:
    titolo = ""
    nome = ""
    cognome = ""
    padre=""
    eta = 0.0
    ruolo = ""
    residenza = ""
    gruppoFamigliare = 0
    
    def __init__(self,titolo,nome,cognome,padre,eta,ruolo,residenza,gruppoFamigliare):
        self.nome = nome
        self.cognome = cognome
        self.titolo = titolo
        self.eta = eta
        self.padre = padre
        self.ruolo = ruolo
        self.gruppoFamigliare = gruppoFamigliare
        self.residenza = residenza
        
    def stampa(self):
        print("nome: ",self.nome)
        print("cognome: ",self.cognome)
        print("titolo: ",self.titolo)
        print("eta: ",self.eta)
        print("padre: ",self.padre)
        print("ruolo: ",self.ruolo)
        print("gruppo famigliare: ",self.gruppoFamigliare)
        print("residenza: ",self.residenza)
# 
#aspetta un attimo che risolvo una cosa