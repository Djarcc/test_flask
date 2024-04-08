from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""
    - /cliente/get - listar clientes 
    - /cliente/post - criar
    - /cliente/new (get) renderizar  formulario de criar cliente 
    - /cliente/<id> - buscar por id e mostrar os dados do cliente
    - /cliente/<id>/edit - editar um cliente
    - /cliente/update/<id> - atualizar o registro do cliente
    - /cliente/delete/<id> - deletar um cliente
"""

@cliente_route.route('/')
def listar_cliente():
    return render_template('lista_cliente.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json

    novo_usuario = {
        'id': len(CLIENTES) + 1 , 
        'nome': data['nome'],
        'email': data['email'],
    }

    CLIENTES.append(novo_usuario)

    return   render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new' ,methods=['GET'] )
def form_cliente():
    return render_template('form_cliente.html')

@cliente_route.route("/<int:cliente_id>", methods=["GET"])
def detalhe_cliente(cliente_id):
    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return  render_template("detalhes_cliente.html", cliente=cliente)

@cliente_route.route("/<int:cliente_id>/edit")
def  form_edit_cliente(cliente_id):
    cliente = None
    for c in CLIENTES:
        if  c['id'] == cliente_id:
            cliente = c

    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route("/update/<int:cliente_id>", methods=["PUT"] )
def update_cliente(cliente_id):
    cliente_edit = None

    dados = request.json
    
    for c in CLIENTES:
        if c['id'] == cliente_id :
            c['nome'] =  dados['nome']
            c['email'] = dados['email']
            cliente_edit = c

    return render_template('item_cliente.html', cliente=cliente_edit)
    

@cliente_route.route("/<int:cliente_id>delete", methods=['DELETE'])
def deletar_cliente(cliente_id):
    global  CLIENTES

    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id ]

    return {'ok': 'ok'}