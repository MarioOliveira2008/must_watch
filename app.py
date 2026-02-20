from flask import Flask, render_template, request, redirect, url_for
from models.desejos import Desejo
from models.database import init_db

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Lista de Desejos')

@app.route('/lista', methods=['GET', 'POST'])
def lista():
    desejos = None

    if request.method == 'POST':
        titulo_desejo = request.form['titulo-desejo']
        tipo_desejo= request.form['tipo-desejo']
        indicado_por = request.form['indicado-por']
        imagem = request.form.get('imagem')


        desejo = Desejo(titulo_desejo, tipo_desejo, indicado_por, imagem=imagem)
        desejo.salvar_lista()

    desejos = Desejo.obter_lista()
    return render_template('lista.html', titulo='Lista de Desejos', desejos=desejos)

@app.route('/delete/<int:idDesejo>') 
def delete(idDesejo):
    desejo = Desejo.id(idDesejo)
    desejo.excluir_desejo()
    # return render_template('agenda.html', titulo="Agenda", tarefas=tarefas)
    return redirect(url_for('lista')) 



@app.route('/update/<int:idDesejo>', methods = ['GET', 'POST'])
def update(idDesejo):
        if request.method == 'POST':
            titulo = request.form['titulo-desejo']
            tipo = request.form['tipo-desejo']
            indicado = request.form['indicado-por']
            imagem = request.form.get('imagem')
            desejo = Desejo(titulo, tipo, indicado, imagem=imagem, id_desejo=idDesejo)

            desejo.atualizar_desejo()
            return redirect(url_for('lista')) #early return
            
        desejos = Desejo.obter_lista()
        desejo_selecionado = Desejo.id(idDesejo) #seleção do desejo que sera editado
        
        return render_template('lista.html', titulo= 'Editar Desejo', desejos=desejos, desejo_selecionado=desejo_selecionado)

        
    

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"