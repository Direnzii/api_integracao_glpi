from glpi import GlpiApi
import json

# ******* SECRETS (.env) *****************
SERVER_IP = '0.0.0.0/glpi'
APPTOKEN = '******'
ADMUSERTOKEN = '******'


# ****************************************


# def connect_db():
#     """my fail try to connect in database"""
#     config = {
#         'user': '*****',
#         'password': '*****',
#         'host': '******',
#         'database': '****'
#     }
#     try:
#         conn = mysql.connector.connect(**config)
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM glpi_users LIMIT 10;")
#         result = cursor.fetchall()
#         for row in result:
#             print(row)
#     except mysql.connector.Error as err:
#         print(f"Erro: {err}")


def create_ticket(titulo, descricao, prioridade, usertoken):
    """here I create a ticket with title, description and priority, to do that, u need to know if the usertoken
     have been generated, to take sure, enter in web-GUI and search the user, in administracao>>usuarios ahd check"""
    try:
        cursor = GlpiApi(user_token=usertoken, app_token=APPTOKEN, server=SERVER_IP)
        response = cursor.ticket_create(title=titulo, desc=descricao, priority=prioridade)
        print(json.loads(response.content))
        return json.loads(response.content)['id']
    except Exception as err:
        print(err)


def add_interaction(message, ticket_id, usertoken):
    """in this function u need to pass a message and ticket_id to interact in ticket, like a human"""
    try:
        cursor = GlpiApi(user_token=usertoken, app_token=APPTOKEN, server=SERVER_IP)
        response = cursor.add_interaction(message=message, ticket_id=ticket_id)
        print(json.loads(response.content))
    except Exception as err:
        print(err)


def get_user_by_fone(mobile_phone):
    """in this case u pass the phone number (form fill by us) to take the informations about the users, but now
    the function return just user_id"""
    cursor = GlpiApi(user_token=ADMUSERTOKEN, app_token=APPTOKEN, server=SERVER_IP)
    response = cursor.get_user_by_mobile(mobile_phone=mobile_phone)
    print(json.loads(response))
    return json.loads(response)["data"][0]["2"]


def get_user_by_username(username):
    """here is the same to above, but using username like teste.01"""
    cursor = GlpiApi(user_token=ADMUSERTOKEN, app_token=APPTOKEN, server=SERVER_IP)
    response = cursor.get_user_by_username(username=username)
    print(json.loads(response))
    return json.loads(response)["data"][0]["2"]


def get_tickets_by_user(username):
    cursor = GlpiApi(user_token=ADMUSERTOKEN, app_token=APPTOKEN, server=SERVER_IP)
    response = cursor.get_all_tickets_by_username(username=username)
    print(json.loads(response))
    return json.loads(response)['data']


# create_ticket(titulo='Chamado teste python user teste 5656', descricao='descricao teste 5656', prioridade='1')
# add_interaction(message='mensagem teste aaa', ticket_id=5872)
# get_user_by_fone(mobile_phone='123456789')
# get_user_by_username(username='teste.01')

"""
Checklist to do:
- Create ticket = ok
- Interact with this ticket = ok
- Locate information about user using phone number = ok
"""
