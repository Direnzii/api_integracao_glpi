from flask import Flask, request, make_response, Blueprint
from flask_cors import CORS
from src_main import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/mid', methods=['GET', ])
def status_ok():
    return make_response({'result': 'mid rodando'}, 200)


ticket = Blueprint('ticket', __name__, url_prefix='/mid/ticket')


@ticket.route('/criar', methods=['POST', ])
def create():
    try:
        body = request.get_data()
        mensagem = json.loads(body)
        titulo = mensagem['titulo']
        descricao = mensagem['descricao']
        prioridade = mensagem['prioridade']
        usertoken = mensagem['usertoken']
        ticket_id = create_ticket(titulo=titulo, descricao=descricao, prioridade=prioridade, usertoken=usertoken)
        response = {"result": "chamado criado com sucesso", "ticket_id": ticket_id}
        return make_response(response, 200)
    except:
        return make_response('fail', 400)


@ticket.route('/interagir', methods=['POST', ])
def interact():
    try:
        body = request.get_data()
        mensagem = json.loads(body)
        message = mensagem['message']
        ticket_id = mensagem['ticket_id']
        usertoken = mensagem['usertoken']
        add_interaction(message=message, ticket_id=ticket_id, usertoken=usertoken)
        return make_response('{"result": "interação realizada com sucesso"}', 200)
    except:
        return make_response('fail', 400)


@ticket.route('/idUsuarioPeloTelefone', methods=['POST', ])
def getIdByMobile():
    try:
        body = request.get_data()
        mensagem = json.loads(body)
        mobile_phone = mensagem['mobile_phone']
        user_id = get_user_by_fone(mobile_phone=mobile_phone)
        response = {"result": "OK", "user_id": user_id}
        return make_response(response, 200)
    except:
        return make_response('fail', 400)


@ticket.route('/idUsuarioPeloNome', methods=['POST', ])
def getIdByUsername():
    try:
        body = request.get_data()
        mensagem = json.loads(body)
        username = mensagem['username']
        user_id = get_user_by_username(username=username)
        response = {"result": "OK", "user_id": user_id}
        return make_response(response, 200)
    except:
        return make_response('fail', 400)


@ticket.route('/allTicketsPeloUsuario', methods=['POST', ])
def getTicketByUsername():
    try:
        body = request.get_data()
        mensagem = json.loads(body)
        username = mensagem['username']
        tickets = get_tickets_by_user(username=username)
        response = {"result": "OK", "tickets": tickets}
        return make_response(response, 200)
    except:
        return make_response('fail', 400)


if __name__ == '__main__':
    app.register_blueprint(ticket)
    app.run(host='0.0.0.0', port=8000)
