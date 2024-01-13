from SSAction.SSAction import SSAction

class SSActionDecorator(SSAction):
    def __init__(self, decorated_ss_action):
        self.decorated_ss_action = decorated_ss_action

    def action(self):
        self.decorated_ss_action.action()
