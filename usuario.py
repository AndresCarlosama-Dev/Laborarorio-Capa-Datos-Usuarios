from conexion import conexion
#from usuarioDAO import UsuarioDAO


class Usuario:
    
    def __init__(self, username, password, id_usuario=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
         
    # Setter and Getter
    def get_id_usuario(self):
        return self._id_usuario
    def set_id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
        
    def get_username(self):
        return self._username
    def set_username(self, username):
        self._username = username
        
    def get_password(self):
        return self._password
    def set_password(self, password):
        self._password = password
        
    
    def __str__(self) -> str:
        return f'Id usuario: {self.get_id_usuario()}, username: {self.get_username()}, password: {self.get_apellido()}, email: {self.get_password()}'
    
    
    # def registar(self) -> bool:
    #     sql = f"""
    #         INSERT INTO personas(username, password)
    #         VALUES ('{self._username}','{self._password}');
    #     """
    #     # Conexion a DB
    #     con = conexion()
    #     if con == None:
    #         raise Exception("No se encuentra conectado a la DB")
        
    #     # Crear cursor
    #     cur = con.cursor()
    #     # Ejecutar SQL
    #     cur.execute(sql)
    #     con.commit()
    #     resultado = cur.rowcount
    #     con.close()
    #     return resultado == 1