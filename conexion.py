from logger_base import log
from psycopg2 import pool
import sys

class Conexion:

    #Change the values accordingly. 
    _DATABASE= 'test_db'
    _USER= 'postgres'
    _PASSWORD='admin'
    _DB_PORT= '5432'
    _HOST= '127.0.0.1'

    #Minimum and maximum number of connections in the pool.
    _MIN_CON= 1
    _MAX_CON= 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user= cls._USER,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database= cls._DATABASE)
                log.debug('Creacion del pool exitosa')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al crear el pool: {e}')
        else:
            return cls._pool
    
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool:{conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Retornamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

