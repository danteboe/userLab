class Usuario:
    def __init__(self, id_usuario:int= None, username:str= None, password:str= None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
    
    def __str__(self):
        return f'''
ID: {self._id_usuario} Username: {self._username} Password: {self._password}
        '''

    @property
    def id_usuario(self):
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password

if __name__ == '__main__':
    from logger_base import log
    usuario1 = Usuario(username='jperez', password='1234')
    log.debug(usuario1)
