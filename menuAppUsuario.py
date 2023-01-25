from usuario import Usuario
from usuarioDAO import UsuarioDAO

class Menu:
    def mostrarMenu(self):
        while True:
            print("=" * 50)
            print("1. Lista de usuarios")
            print("2. Agregar usuario")
            print("3. Actualizar usuario")
            print("4. Eliminar usuario")
            print("5. Salir")
            opcion = int(input("Ingresa la opcion que deseas realizar: "))
            
            if opcion < 1 and opcion > 5:
                print("Opcion invalida")
                break
            elif opcion == 1:
                self.listarUsuarios()
            elif opcion == 2:
                self.agregarUsuario()
            elif opcion == 3:
                self.actualizarUsuario()
            elif opcion == 4:
                self.eliminarUsuario()
            elif opcion == 5:
                print('Hasta pronto!')
                break
    
    def listarUsuarios(self):
        print("===LISTA DE USUARIOS REGISTRADOS===")
        personas = UsuarioDAO()
        registroUsuarios = personas.listar()
        
        print(registroUsuarios)
    
    def agregarUsuario(self):
        print("===AGREGAR USUARIOS===")
        usuario = input("Ingrese el usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        
        #Guardar en DB
        # usuario = Usuario(username=usuario, password=contraseña)
        #usuario = Usuario(usuario, contraseña)
        usuario = UsuarioDAO(usuario, contraseña)
        guardado = usuario.registrar()
        
        if guardado:
            print("Registro de usuario exitoso")
        else:
            print("Error al registar el usuario")
            
    def actualizarUsuario(self):
        print("===ACTUALIZAR USUARIOS===")
        idUsuario = input("Ingrese el id de usuario: ")
        usuario = input("Ingrese el usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        
        persona = UsuarioDAO(usuario, contraseña, idUsuario)
        actualizado = persona.actualizar()
        
        if actualizado:
            print("Actualizacion de usuario exitoso")
        else:
            print("Error al actualizar el usuario")
        
    def eliminarUsuario(self):
        print("===ELIMINACION DE USUARIOS===")
        idUsuario = input("Ingrese el id de usuario que desea ELIMINAR: ")
        
        persona = UsuarioDAO(id_usuario = idUsuario)
        eliminado = persona.eliminar()
        
        if eliminado:
            print("Eliminacion de usuario exitoso")
        else:
            print("Error al eliminar el usuario")