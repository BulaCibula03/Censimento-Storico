from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from . import funzioni
import os
import pandas as pd

bp = Blueprint('main', __name__)

EXPECTED_COLUMNS = [
    "Titolo", "Nome", "Cognome", "Figlio di", "Eta", "Ruolo", "Residenza"
]

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        try:
            df = pd.read_csv(filepath, encoding='utf-8-sig')
        except Exception:
            flash('Errore nella lettura del file CSV.', 'danger')
            return redirect(url_for('main.index'))

        df.columns = [c.strip().lower() for c in df.columns]
        expected_columns = [c.strip().lower() for c in EXPECTED_COLUMNS]

        if not set(expected_columns) <= set(df.columns):
            flash('Il file CSV non ha il formato corretto. Le colonne devono essere: ' + ', '.join(EXPECTED_COLUMNS), 'danger')
            return redirect(url_for('main.index'))

        df = df[expected_columns]
        funzioni.my_list = funzioni.creaIstanze(df)
        funzioni.my_list = sorted(funzioni.my_list, key=lambda x: x.gruppoFamigliare)
        funzioni.pulisciTitoli(funzioni.my_list)
        #flash('File caricato e analizzato con successo!', 'success')
        return redirect(url_for('main.info'))
    else:
        flash('Carica un file CSV valido.', 'danger')
    return redirect(url_for('main.index'))

@bp.route('/api/abitanti')
def api_abitanti():
    data = funzioni.my_list
    if request.args.get('maschi') == '1' and request.args.get('femmine') != '1':
        data = funzioni.trovaMaschi(data)
    elif request.args.get('femmine') == '1' and request.args.get('maschi') != '1':
        data = funzioni.trovaFemmine(data)
    if request.args.get('padri') == '1':
        data = funzioni.persoPadri(data)
    if request.args.get('quartieri') == '1':
        data = funzioni.suddivisioneQuartieri(data)
    if request.args.get('nomi') == '1':
        classifica_nomi, _ = funzioni.classificaNomi(data)
        nomi_freq = dict(classifica_nomi)
        data = sorted(data, key=lambda p: (-nomi_freq.get(p.nome, 0), p.nome.lower()))
    if request.args.get('cognomi') == '1':
        _, classifica_cognomi = funzioni.classificaNomi(data)
        cognomi_freq = dict(classifica_cognomi)
        data = sorted(data, key=lambda p: (-cognomi_freq.get(p.cognome, 0), p.cognome.lower()))
    if request.args.get('titoli') == '1':
        classifica_titoli = funzioni.classificaTitoli(data)
        titoli_freq = {k.strip().lower(): v for k, v in classifica_titoli}
        data = sorted(
            data,
            key=lambda p: (-titoli_freq.get(p.titolo.strip().lower(), 0), p.titolo.strip().lower())
        )
    data = sorted(data, key=lambda p: p.gruppoFamigliare)
    gruppi_info = funzioni.info_gruppi(data)
    abitanti = [{
        "gruppo_famigliare": p.gruppoFamigliare,
        "nome": p.nome,
        "cognome": p.cognome,
        "titolo": p.titolo,
        "eta": p.eta,
        "padre": p.padre,
        "ruolo": p.ruolo,
        "residenza": p.residenza,
    } for p in data]
    return jsonify({"abitanti": abitanti, "gruppi_info": gruppi_info})

@bp.route('/api/classifiche')
def api_classifiche():
    nomi, cognomi = funzioni.classificaNomi(funzioni.my_list)
    titoli = funzioni.classificaTitoli(funzioni.my_list)
    return jsonify({
        "nomi": nomi,
        "cognomi": cognomi,
        "titoli": titoli
    })
    
@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', dati_caricati = bool(funzioni.my_list))

@bp.route('/creator', methods=['GET'])
def creator():
    return render_template('creator.html', dati_caricati = bool(funzioni.my_list))

@bp.route('/statistiche', methods=['GET'])
def statistiche():
    if not funzioni.my_list:
        funzioni.creaIstanze()
        
    etaGenerale = funzioni.mediaEta(funzioni.my_list)
    etaServitu = funzioni.etaServitu(funzioni.my_list)
    etaGruppi = funzioni.mediaEtaGruppiFamigliari(funzioni.my_list)
    etaMogli = funzioni.etaMediaConiugi(funzioni.my_list)[1]  # Mater familias
    etaMariti = funzioni.etaMediaConiugi(funzioni.my_list)[0] # Capofamiglia
    etaNobili = funzioni.differenzaEtaTraClassi(funzioni.my_list)[0]
    etaBorghesi = funzioni.differenzaEtaTraClassi(funzioni.my_list)[1]
    etaPopolo = funzioni.differenzaEtaTraClassi(funzioni.my_list)[2]
    sopraQuaranta = funzioni.superoEtaLimite(funzioni.my_list)
    sottoSedici = funzioni.minoriEtaMassima(funzioni.my_list)
    f1, m1 = funzioni.quantiEtaMaschiEFemmine(funzioni.my_list)[0][0], funzioni.quantiEtaMaschiEFemmine(funzioni.my_list)[1][0]
    f2, m2 = funzioni.quantiEtaMaschiEFemmine(funzioni.my_list)[0][1], funzioni.quantiEtaMaschiEFemmine(funzioni.my_list)[1][1]
    f3, m3 = funzioni.quantiEtaMaschiEFemmine(funzioni.my_list)[0][2], funzioni.quantiEtaMaschiEFemmine(funzioni.my_list)[1][2]
    f4, m4 = funzioni.quantiEtaMaschiEFemmine(funzioni.my_list)[0][3], funzioni.quantiEtaMaschiEFemmine(funzioni.my_list)[1][3]
    mediaNumeroGruppi = funzioni.mediaNumeroGruppiFamiliari(funzioni.my_list)
    contaMaschi, contaFemmine = funzioni.contaMaschiFemmine(funzioni.my_list)
    etaMaschi = funzioni.mediaEta(funzioni.trovaMaschi(funzioni.my_list))
    etaFemmine = funzioni.mediaEta(funzioni.trovaFemmine(funzioni.my_list))
    return render_template(
        'statistiche.html',
        dati_caricati = bool(funzioni.my_list),
        etaGenerale=etaGenerale,
        etaServitu=etaServitu,
        etaGruppi=etaGruppi,
        etaMogli=etaMogli,
        etaMariti=etaMariti,
        etaNobili=etaNobili,
        etaBorghesi=etaBorghesi,
        etaPopolo=etaPopolo,
        sopraQuaranta=sopraQuaranta,
        sottoSedici=sottoSedici,
        f1=f1, f2=f2, f3=f3, f4=f4,
        m1=m1, m2=m2, m3=m3, m4=m4,
        mediaNumeroGruppi=mediaNumeroGruppi,
        contaMaschi=contaMaschi,
        contaFemmine=contaFemmine,
        etaMaschi=etaMaschi,
        etaFemmine=etaFemmine
    )

@bp.route('/info', methods=['GET'])
def info():
    if not funzioni.my_list:
        flash('Devi prima caricare un file CSV!', 'danger')
        return redirect(url_for('main.index'))
    return render_template('infoGenerali.html', dati_caricati = bool(funzioni.my_list))

@bp.route('/classifiche', methods=['GET'])
def classifiche():
    return render_template('classifiche.html', dati_caricati = bool(funzioni.my_list))

@bp.route('/wiki', methods=['GET'])
def wiki():
    return render_template('wiki.html')