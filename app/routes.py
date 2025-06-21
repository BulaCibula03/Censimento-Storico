from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import funzioni
bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/creator', methods=['GET'])
def creator():
    return render_template('creator.html')

@bp.route('/eta', methods=['GET'])
def eta():
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
    return render_template(
        'eta.html',
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
        m1=m1, m2=m2, m3=m3, m4=m4
    )

@bp.route('/gruppo', methods=['GET'])
def gruppo():
    return render_template('gruppoFamigliare.html')

@bp.route('/info', methods=['GET'])
def info():
    return render_template('infoGenerali.html')
