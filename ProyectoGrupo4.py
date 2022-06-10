from random import randint,uniform
from random import randint

class RegUsuario:
    """
    Una clase para registrar un usuario
    -----------------------
    Atributos
    -----------------------
    Ninguno
    -----------------------
    Métodos
    -----------------------
    constructor(usuRegistrado, contraRegistrado)
    imprUsuario()
         Método para perdir e imprimir los datos al usuario para su registro
    """

    def imprUsuario():
        
        print ("|------------------------------------------|")
        print ("|          Registro de Usuario             |")
        print ("|------------------------------------------|") 
        print ("| 1. Inicio de sesión                      |")
        print ("| 2. Registro                              |")
        print ("|------------------------------------------|")
        opcionMenu=int(input("Escoja una opción: "))
        usu="grupo4"
        contra="2022"
        if opcionMenu == 1:
            usuRegistrado=str(input("Ingrese su usuario: "))
            contraRegistrado=str(input("Ingrese su contraseña: "))
            if usuRegistrado == usu and contraRegistrado == contra:
                print("Ingreso correcto Bienvenido grupo4")
            else:
                print("Usuario o contraseña incorrectos")
                print(RegUsuario.imprUsuario())
        elif opcionMenu == 2:
            usuario = input("Ingrese un usuario: ")
            contrasena = input("Ingrese una contraseña:")
            confirmarContrasena = input("Repita la contraseña: ")
        
            #Condicional while para validar la contraseña
            while contrasena != confirmarContrasena:
               print("Usuario no registrado con éxito")
               contrasena = input("Ingrese el contraseña nuevamente: ")
               confirmarContrasena = input("Repita contraseña: ")

            print("--------------------------------")
            print("Usuario Registrado con éxito")
            print("Bienvenido", usuario)
        else:
            print("Opción no valida")

class OpcionesMenu():

    def __init__(self):
        #data members
        """
        Construye todos los atributos necesarios para el objeto empleado.
        -----------------------------
        Parámetros
        -----------------------------
        nombre : str
            nombre del usuario
        apellido : str
            apellido del usuario
        edad : int
            edad del usuario
        celular : int
            número de celular del usuario
        cedula : int
            cédula del usuario
        """
        self.nombre =   input("Ingrese su nombre  : ")
        self.apellido = input("Ingrese su apellido: ")
        self.edad = int(input("Ingrese su edad    : "))
        self.celular = int(input("Ingrese el número de celular: "))
        self.cedula =  int(input("Ingrese su cédula  : "))

    #método para mostrar los detalles del usuario
    def show(self):
        
        print (" Nombre   : ", self.nombre)
        print (" Apellido : ", self.apellido)
        print (" Edad     : ", self.edad)
        print (" Celular  : ", self.celular)
        print (" Cédula   : ", self.cedula)
 
        self.lista = [self.nombre, self.apellido, self.edad, self.celular, self.cedula]
        print("Los Datos son: ", self.lista)
     

class OpcionesMenu2():

    def __init__(self, horaSalidaMañ, horaSalidaTar, horaSalidaNoch, horaLlegadaMañ, horaLlegadaTar, horaLlegadaNoch):
        #data members
        """
        Construye todos los atributos necesarios para el objeto empleado.
        -----------------------------
        Parámetros
        -----------------------------
        horaSalidaMañ : str
            Hora de salida del viaje (mañana)
        horaSalidaTar : str
            Hora de salida del viaje (tarde)
        horaSalidaNoch : str
            Hora de salida del viaje (noche) 
        horaLlegadaMañ : str
            Hora de salida del viaje (mañana)
        horaLlegadaTar : str
            Hora de salida del viaje (tarde)
        horaLlegadaNoch : str
            Hora de llegada del viaje (noche)
        """
        self.horaSalidaMañ = horaSalidaMañ
        self.horaSalidaTar = horaSalidaTar
        self.horaSalidaNoch = horaSalidaNoch
        self.horaLlegadaMañ = horaLlegadaMañ
        self.horallegadaTar = horaLlegadaTar
        self.horaLlegadaNoch = horaLlegadaNoch


        #método para mostrar los detalles del usuario
    def HoraViaje(self):
        
        opcionHoraViaje = int(input("Escoja una hora de viaje: "))
        
        if opcionHoraViaje == 1:
            print("La Hora de salida esta establecida a las ",self.horaSalidaMañ)
            print("El recorrido tiene una duración de una hora y media")
            print("Por lo que el horario de llegada será a las ",self.horaLlegadaMañ)
        elif opcionHoraViaje == 2:
            print("La Hora de salida esta establecida a las ",self.horaSalidaTar)
            print("El recorrido tiene una duración de dos horas")
            print("Por lo que el horario de llegada será a las ", self.horaLlegadaTar)
        elif opcionHoraViaje == 3:
            print("La Hora de salida esta establecida a las ", self.horaSalidaNoch)
            print("El recorrido tiene una duración de una hora y media")
            print("Por lo que el horario de llegada será a las ", self.horaLlegadaNoch)
        else:
            print("Opcion incorrecta")
            OpcionesMenu2.HoraViaje()

class MenuPrincipal(OpcionesMenu, OpcionesMenu2):
    def menuPrincipal():
        while (True):
            print ("|------------------------------------------|")
            print ("|             Menú principal               |")
            print ("|------------------------------------------|")
            print("1.*Paquetes viajeros*")
            print("2.Datos personales del usuario.")
            print("3.Fecha de salida y llegada del viaje.")
            print("4.Datos del viaje del usuario")
            print("5.Salir")
            print("======================================")
            opc=int(input("INGRESE LA OPCION: \n"))
            if opc==1:
                paquetes()
            elif opc==2:
                print ("|------------------------------------------|")
                print ("|           Datos del usuario              |")
                print ("|------------------------------------------|")
                OpcionesMenuClase=OpcionesMenu()
                OpcionesMenuClase.show()
                
            elif opc==3:
                print ("|------------------------------------------|")
                print ("|            Hora del viaje                |")
                print ("|------------------------------------------|")
                print ("| 1. Horario Matutino                      |")
                print ("| 2. Horario Vespertino                    |")
                print ("| 3. Horario Nocturno                      |")
                print ("|------------------------------------------|")
                OpcionesMenu2Clase=OpcionesMenu2("09:00","13:00","20:00","10:30","16:00","21:30")
                OpcionesMenu2Clase.HoraViaje()
            elif opc==4:
                print ("|------------------------------------------|")
                print ("|            Datos Ingresados              |")
                print ("|------------------------------------------|")
                print ("| Viaje registrado con los siguientes datos|")
                print ("|==========================================|")
                OpcionesMenuClase.show()
                OpcionesMenu2Clase.HoraViaje()
            elif opc==5:
                print("Salio con éxito, Vuelva Pronto")
                break
            else:
                print("Opcion invalida")
        
def paquetes():
    print("|Dentro de los paquetes de viajes disponibles se     |")
    print("|encuentran los siguientes lugares turísticos:       |")
    print("| 1.El Panecillo                2.La Mitad del mundo |")
    print("| 3.Basílica del voto Nacional  4.Teleférico         |")
    print("| 5.Volver al menú principal                         |")
    while (True):
        opcPaque=int(input("INGRESE LA OPCION: \n"))
        if opcPaque==1:
            asi1=randint(0,7)
            asi2=randint(8,11)
            asi3=randint(12,22)
            bus=randint(0,30)
            print("Para la visita al sitio turistico, contamos con los siguientes")
            print("asientos disponibles: ",asi1,"",asi2,"",asi3," en la buseta numero: ",bus)
            print("Este paquete, tiene un precio de: ")
        elif opcPaque==2:
            print("OPCION 2")
        elif opcPaque==3:
            print("OPCION 3")
        elif opcPaque==4:
            print("Opcion 4")
        elif opcPaque==5:
            break
        else:
             print("Opcion invalida")

#Instancia del objeto RegUsuario


print(RegUsuario.imprUsuario())
print(MenuPrincipal.menuPrincipal())

