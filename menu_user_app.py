from logger_base import log
from usuario_dao import UsuarioDao as userDao
from usuario import Usuario as User

def run_app():
    running = True
    while running:
        print('''
Options:
1. List users.
2. Add user.
3. Modify user.
4. Delete user.
5. Exit the app.
        ''')
        option = input('Insert your option (1-5):')
        if option=='1':
            users= userDao.seleccionar()
            for user in users:
                log.debug(user)

        elif option =='2':
            username = input('Insert the username: ')
            password = input('Insert the password: ')
            user1 = User(username= username, password= password)
            inserted_user = userDao.insertar(user1)
            log.debug(f'{inserted_user} user(s) inserted')
        elif option =='3':
            id = input('Insert the user id to update: ')
            username = input('Insert the new username: ')
            password = input('Insert the new password: ')
            user1 = User(username= username, password= password, id_usuario= id)
            upded_user = userDao.actualizar(user1)
            log.debug(f'{upded_user} user(s) updated')
        elif option=='4':
            id = input('Insert the user id to delete: ')
            user1 = User(id_usuario=id)
            deleted_user = userDao.eliminar(user1)
            log.debug(f'{deleted_user} user(s) deleted')
        elif option=='5':
            running = False

run_app()


            
