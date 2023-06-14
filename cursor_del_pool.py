from conexion import Conexion 
from logger_base import log

class CursorDelPool:
    def __init__(self)->None:
        self._conn = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with enter')
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor
    
    def __exit__(self, type, value, traceback):
        log.debug('Se ejecuta el metodo exit')
        if value:
            self._conn.rollback()
            log.error(f'Ocurrio una excepcion: {value}{type}{traceback}')
        else:
            self._conn.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conn)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())