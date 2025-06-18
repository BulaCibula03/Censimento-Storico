from app import create_app

app = create_app()

#Tailwind css: https://tailwindcss.com
#Siti per i template (mi raccomando, usa un solo sito per mantenere la coerenza tra i template): https://flowbite.com, https://daisyui.com, https://www.preline.co
#ok, ora scegli un sito, usa solo i template di quel sito e incastrali per fare la tua pagina, e se vuoi usa le singole funzioni di tailwind (già integrato di base nei template) per modificare i template, ok?
#un'ultima cosa, dovrai creare una pagina chiamata base.html che conterrà il layout di base per tutte le altre pagine (es. colore dello sfondo, barra di navigazione...)
#anzi meglio, sappi che nel base.html dovrai mettere, oltre che a quello che ti ho detto prima, questo:
#    <main>
#        {% block content %}
#        {% endblock %}
#    </main>
#questo servirà ad inizializzare la pagina base
#mentre nelle altre, per collegarle al base dovrai usare questo:
#{% extends 'base.html' %}

#{% block title %}nome a caso della pagina{% endblock %}

#{% block content %}
#qua ci metti il tuo codice html
#{% endblock %}