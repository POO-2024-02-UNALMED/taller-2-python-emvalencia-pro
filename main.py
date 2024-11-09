class Asiento:
    def __init__(self,color,precio,registro):
        self.color= color
        self.precio= precio
        self.registro= registro
    
    def cambiarColor(self,c):
        if c=="rojo" or c=="verde" or c=="amarillo" or c=="negro" or c=="blanco":
            color=c

class Motor:
    def __init_(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
        
    def cambiarRegistro(self,r):
        self.registro=r
    
    def asignarTipo(self,t):
        if t=="electrico" or t=="gasolina":
            registro=t

class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    
    def cantidadAsientos(self):
        c=0
        for i in asientos:
            if isinstance(i,Asiento) == True :
                c+=1
        return c
    
    def verificarIntegridad(self):
        for i in self.asientos:
            if isinstance(i,Asiento) == True and (registro != i.registro or i.registro != self.motor.registro):
                return "Las piezas no son originales"
        return "Auto original"
            