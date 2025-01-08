class Usuario:

    __email = 'max@gmail.com'
    __password = '123'

    def __init__(self):
        pass
    
    def set_password(self,password):
        self.__password = password

    def login(self,email,password):
        if (self.__email == email and self.__password == password):
            print(f'Bienvenido {self.__email}')
        else:
            print('datos incorrectos')

print('LOGIN DE USUARIOS')
email = input ('INGRESE EMAIL : ')
password = input ('INGRESE PASSWORD : ')

usuario = Usuario()
usuario.set_password(password)
usuario.login(email,password)

