import requests


class GlpiApi:
    def __init__(self, user_token, app_token, server):
        self.user_token = user_token
        self.app_token = app_token
        self.server = server

    def init_session(self):
        header = {'Content-Type': 'application/json',
                  'Authorization': 'user_token %s' % self.user_token,
                  'App-Token': '%s' % self.app_token}
        session = requests.get(f'http://{self.server}/apirest.php/initSession/',
                               headers=header, verify=False)
        session_token = session.json()['session_token']
        return session_token

    def kill_session(self):
        header = {'Content-Type': 'application/json',
                  'Session-Token': '%s' % self.init_session(),
                  'App-Token': '%s' % self.app_token}
        session = requests.get(f'http://{self.server}/apirest.php/killSession/',
                               headers=header, verify=False)
        return session.status_code

    def ticket_create(self, title, desc, priority):
        title = title
        description = desc
        priority = priority

        header = {'Content-Type': 'application/json',
                  'Session-Token': '%s' % self.init_session(),
                  'App-Token': '%s' % self.app_token}
        payload = {"input": {"name": "%s" % title,
                             "content": "%s" % description,
                             "priority": "%s" % priority}}
        session = requests.post(f'http://{self.server}/apirest.php/Ticket', headers=header,
                                json=payload, verify=False)
        return session

    def add_interaction(self, message, ticket_id):
        message = message
        header = {'Content-Type': 'application/json',
                  'Session-Token': '%s' % self.init_session(),
                  'App-Token': '%s' % self.app_token}
        payload = {
            "input": {
                "tickets_id": ticket_id,
                "content": message
            }
        }
        session_add = requests.post(f'http://{self.server}/apirest.php/Ticket/{ticket_id}/TicketFollowup',
                                    headers=header,
                                    json=payload, verify=False)
        return session_add

    def get_user_by_mobile(self, mobile_phone):
        header = {'Content-Type': 'application/json',
                  'Session-Token': '%s' % self.init_session(),
                  'App-Token': '%s' % self.app_token}
        url_complete = (f"http://{self.server}/apirest.php/search/User?criteria[0][field]=6"
                        f"&criteria[0][searchtype]=containss&criteria[0][value]={str(mobile_phone)}"
                        f"&forcedisplay[0]=1&forcedisplay[1]=2&forcedisplay[2]=5"
                        f"&forcedisplay[3]=9&forcedisplay[4]=14&forcedisplay[5]=80")
        response = requests.get(url_complete,
                                headers=header,
                                verify=False)
        return response.content

    def get_user_by_username(self, username):
        header = {'Content-Type': 'application/json',
                  'Session-Token': '%s' % self.init_session(),
                  'App-Token': '%s' % self.app_token}
        url_complete = (f"http://{self.server}/apirest.php/search/User?criteria[0][field]=1"
                        f"&criteria[0][searchtype]=containss&criteria[0][value]={str(username)}"
                        f"&forcedisplay[0]=1&forcedisplay[1]=2&forcedisplay[2]=5"
                        f"&forcedisplay[3]=9&forcedisplay[4]=14&forcedisplay[5]=80")
        response = requests.get(url_complete,
                                headers=header,
                                verify=False)
        return response.content

    def get_all_tickets_by_username(self, username):
        header = {'Content-Type': 'application/json',
                  'Session-Token': '%s' % self.init_session(),
                  'App-Token': '%s' % self.app_token}
        url_complete = (f"http://{self.server}/apirest.php/search/Ticket?criteria[0][field]=22"
                        f"&criteria[0][searchtype]=contains&criteria[0][value]={username}")
        response = requests.get(url_complete,
                                headers=header,
                                verify=False)
        return response.content