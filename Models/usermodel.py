'''User'''

class User():
    '''
    Class defining user
    '''
    def __init__(self, id, name, email, username, password, isAdmin):
        '''Initialising attributes of class'''
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.isAdmin = isAdmin

    def to_json(self):
        '''Converting to json'''
        return {
            'id' : self.id,
            'name' : self.name,
            'email' : self.email,
            'username' : self.username,
            'password': self.password,
            'isAdmin': self.isAdmin
        }    
