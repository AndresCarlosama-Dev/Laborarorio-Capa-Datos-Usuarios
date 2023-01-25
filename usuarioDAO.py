from conexion import conexion
from usuario import Usuario

class UsuarioDAO(Usuario):
    
    def __init__(self, username=None, password=None, id_usuario=None):
        super().__init__(username, password, id_usuario)
        
    def listar(self) -> list:
        #SQL
        sql = f"""
            SELECT *
            FROM personas
            ORDER BY id_usuario
            """
        #Abrir conexion
        con = conexion()
        #Abir Cursor
        cur = con.cursor()
        #Ejecutar SQL
        cur.execute(sql)
        registros = cur.fetchall()
        con.close()
        
        objPersonas = list()
        for persona in registros:
            objPersonas.append(Usuario(id_usuario = persona[0], username = persona[1], password = persona[2]))
        
        dicPersona = list()
        for persona in objPersonas:
            dicPersona.append(persona.__dict__)
        
        return dicPersona
        
    
    def registrar(self) -> bool:
        #SQL
        sql = f"""
            INSERT INTO personas(username, password)
            VALUES ('{self._username}','{self._password}');
        """
        #Abrir conexion
        con = conexion()
        if con == None:
            raise Exception("No se encuentra conectado a la DB")
        
        #Abrir Cursor
        cur = con.cursor()
        #Ejecutar SQL
        cur.execute(sql)
        con.commit()
        
        registro = cur.rowcount
        con.close()
        return registro == 1
    
    def actualizar(self) -> bool:
        #SQL
        sql = f"""
            UPDATE personas
            SET username = '{self._username}',
                password = '{self._password}'
            WHERE id_usuario = {self._id_usuario};
            """
        #Abrir conexion
        con = conexion()
        #Abrir cursor
        cur = con.cursor()
        #Ejecutar SQL
        cur.execute(sql)
        con.commit()
        actualizacion = cur.rowcount
        con.close()
        
        return actualizacion == 1
    
    def eliminar(self) -> bool:
        #SQL
        sql = f"""
            DELETE
            FROM personas
            WHERE id_usuario = {self._id_usuario};
            """
        #Abrir conexion
        con = conexion()
        #Abrir cursor
        cur = con.cursor()
        #Ejecutar SQL
        cur.execute(sql)
        con.commit()
        eliminacion = cur.rowcount
        con.close()
        
        return eliminacion == 1