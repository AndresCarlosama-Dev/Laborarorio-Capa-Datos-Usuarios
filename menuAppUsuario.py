from usuario import Usuario
#from usuarioDAO import UsuarioDAO

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
                print("Ocion invalida")
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
    
    def agregarUsuario(self):
        print("===AGREGAR USUARIOS===")
        usuario = input("Ingrese el usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        
        #Guardar en DB
        # usuario = Usuario(username=usuario, password=contraseña)
        usuario = Usuario(usuario, contraseña)
        guardado = usuario.registar()
        
        if guardado:
            print("Registro de usuario exitoso")
        else:
            print("Error al registar el usuario")