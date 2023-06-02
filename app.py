from flask import Flask, render_template

app = Flask(__name__)

entradas = [
    {
    "titulo": 'primeiro post do blog',
    'texto': 'aqui vem o texto'
},
{
     "titulo": 'primeiro post do blog',
    'texto': 'aqui vem o texto'
}  
]
@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=entradas)