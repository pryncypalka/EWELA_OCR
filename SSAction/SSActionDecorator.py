from SSAction.SSAction import SSAction

class SSActionDecorator(SSAction):
    def __init__(self, decorated_ss_action):
        self.decorated_ss_action = decorated_ss_action

    def get_ss(self, ss_object):
        self.decorated_ss_action.get_ss(ss_object)

    def action(self):
        self.decorated_ss_action.action()