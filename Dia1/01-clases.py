class Automovil:
    ## creamos metodo constructor
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar

 #metodos
    def encender(self):
        print('encender ' + self.marca)

    def avanzar(self):
        print('avanzar ' + self.marca)

    def acelerar(self):
        print('acelerar ' + self.marca)

    def frenar(self):
        print('frenar ' + self.marca)

## creamos objetos

vw = Automovil(1998,'vx8a','rojo','volswagen')
vw.encender()
vw.avanzar()
vw.acelerar()
vw.frenar()

tico = Automovil(2010,'vae098','amarillo','daewo')
tico.encender()
tico.avanzar()
tico.acelerar()
tico.frenar()