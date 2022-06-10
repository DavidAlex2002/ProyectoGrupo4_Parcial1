#La libreria random sirve para generar numeros aleatorios
#los numeros generados seran usados dentro del código

from random import randint,uniform

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
    imprUsuario()
         Método para perdir e imprimir los datos al usuario para su registro
    """

    def imprUsuario():
        
        print ("____________________________________________")
        print ("|          Registro de Usuario             |")
        print ("|------------------------------------------|") 
        print ("| 1. Inicio de sesión                      |")
        print ("| 2. Registro                              |")
        print ("|------------------------------------------|")
        opcionMenu=int(input("Escoja una opción: "))
        usu="grupo4" #Dato asigando como usuario registrado
        contra="2022" #Dato asignado como contraseña registrada

        if opcionMenu == 1: #Estructura if es igual a la opción "inicio de sesión"
            usuRegistrado=str(input("Ingrese su usuario: "))
            contraRegistrado=str(input("Ingrese su contraseña: "))
            if usuRegistrado == usu and contraRegistrado == contra: #Estructura if anidado para comparar el usuario y la contraseña ingresada
                print("Ingreso correcto Bienvenido grupo4")
            else:
                print("Usuario o contraseña incorrectos")
                print(RegUsuario.imprUsuario())#Llamado a la función de la clase RegUsuario para crear un ciclo (recursividad)

        elif opcionMenu == 2: #Estructura elif es igual a la opción "Registro"
            usuario = input("Ingrese un usuario: ")
            contrasena = input("Ingrese una contraseña:")
            confirmarContrasena = input("Repita la contraseña: ")
        
            #Estrcutura de control while para validar la contraseña
            while contrasena != confirmarContrasena:
               print("El Usuario No Se Registro")
               contrasena = input("Ingrese el contraseña nuevamente: ")
               confirmarContrasena = input("Repita contraseña: ")

            print("____________________________________________")
            print("|     Usuario Registrado Con Éxito         |")
            print("| Bienvenido", usuario, " A la Agencia 'Four Travel' |")
        else:
            print("Opción no valida")

class OpcionesMenu():
    """
    Una clase que representa una opción del menu
    ----------------------------------
    métodos
    -----------------------------------
    constructor()
        
    show()
        Muestra los valores ingresados por teclado para la información del usuario
    """
    def __init__(self):
        """
        Construye todos los atributos necesarios para el objeto empleado.
        -----------------------------
        """
        self.nombre =   input("| Ingrese su nombre  : ")
        self.apellido = input("| Ingrese su apellido: ")
        self.edad = int(input("| Ingrese su edad    : "))
        self.celular = int(input("| Ingrese el número de celular: "))
        self.cedula =  int(input("| Ingrese su cédula  : "))

    def show(self):
        #método para mostrar los detalles del usuario
        print ("Nombre   : ", self.nombre)
        print ("Apellido : ", self.apellido)
        print ("Edad     : ", self.edad)
        print ("Celular  : ", self.celular)
        print ("Cédula   : ", self.cedula)
        
        #Lista para ordenar los datos
        self.lista = [self.nombre, self.apellido, self.edad, self.celular, self.cedula] 
        print("Los Datos son: ", self.lista)
     

class OpcionesMenu2():
    """
    Una clase que es una segunda opción del menu
    ----------------------------
    Atributos
    ----------------------------
        horaSalidaMañ : str
            Hora de salida del viaje en horario de la mañana
        horaSalidaTar : str
            Hora de salida del viaje en horario de la tarde
        horaSalidaNoch : str
            Hora de salida del viaje en horario de la noche 
        horaLlegadaMañ : str
            Hora de llegada del viaje en horario de la mañana
        horaLlegadaTar : str
            Hora de llegada del viaje en horario de la tarde
        horaLlegadaNoch : str
            Hora de llegada del viaje en horario de la noche
    -----------------------------
    Métodos
    -----------------------------
    Constructor()
    HoraViaje()
        Imprime las fechas disponibles del horario que escoja el usuario
        
    
    """
    def __init__(self, horaSalidaMañ, horaSalidaTar, horaSalidaNoch, horaLlegadaMañ, horaLlegadaTar, horaLlegadaNoch):
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
        self.horaLlegadaTar = horaLlegadaTar
        self.horaLlegadaNoch = horaLlegadaNoch
    
    
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

"""|---------------------------------------------------------|
   |                     MENU PRINCIPAL                      |
   |---------------------------------------------------------|"""

"""Creamos una clase llamada menu principal, la cual dentro de si misma
   tendrá una funcino, llamada asi mismo, la cual será el menu principal 
   despues del login, la cual tendra las opciones principales del programa."""

class MenuPrincipal(OpcionesMenu, OpcionesMenu2):
    """
    Una clase que es el menú principal || Hereda las clases OpcionesMenu, OpcionesMenu2
    -----------------------------
    Método
    menuPrincipal() 
        Imprime el menú principal junto con las opciones que el usuario elija
    """
    def menuPrincipal():

        #El menu usamos una estructura de control while, la cual es de tipo cíclica, esto para que 
        #nuestro menú principal sea repetitivo, y al momento de ingresar un valor que no corresponda, 
        #sea dirigido al menú principal nuevamente. 

        while (True):
            print ("____________________________________________")
            print ("|             Menú principal               |")
            print ("|------------------------------------------|")
            print ("| 1.Paquetes viajeros                      |")
            print ("| 2.Datos personales del usuario.          |")
            print ("| 3.Fecha de salida y llegada del viaje.   |")
            print ("| 4.Salir                                  |")
            print ("|------------------------------------------|")
            opc = int(input("| Ingrese una opción: "))
            if opc == 1:

                #Dentro de la opcion uno, llamamos a la funcion paquetes
                #la cual contiene toda la informacion de los lugares que el 
                #usuario puede visitar.

                paquetes()

            elif opc == 2:

                # Dentro de la opcion dos, creamos una variable para asignar la clase OpcionesMenu
                # para llamar al método show()
                # e imprime los datos que previamente se escribieron por teclado

                print ("____________________________________________")
                print ("|           Datos del usuario              |")
                print ("|------------------------------------------|")
                OpcionesMenuClase=OpcionesMenu()
                OpcionesMenuClase.show()
                
            elif opc == 3:
                # Dentro de la opcion tres, cramos una variable para poder llamar a la clase OpcionesMenu2
                # la cual contiene Información acerca de las horas de salidas como de llegadas
                # en los tres diferentes horarios

                print ("____________________________________________")
                print ("|            Hora del viaje                |")
                print ("|------------------------------------------|")
                print ("| 1. Horario Matutino                      |")
                print ("| 2. Horario Vespertino                    |")
                print ("| 3. Horario Nocturno                      |")
                print ("|------------------------------------------|")
                #Instancia del objeto OpcionesMenu2
                OpcionesMenu2Clase=OpcionesMenu2("09:00","13:00","20:00","10:30","16:00","21:30")
                OpcionesMenu2Clase.HoraViaje()
            elif opc == 4:
                print("Salio con éxito, Vuelva Pronto")
                break
            else:
                print("Opcion invalida")
                


"""|---------------------------------------------------------|
   |                    FUNCION PAQUETES                     |
   |---------------------------------------------------------|"""

"""La funcion paquetes, es la que tendra toda la informacion de los paquetes de 
viajes o lugares turisticos de la ciudad de Quito, la cual el usuario podrá 
seleccionar la que mas le convenga""" 


def paquetes():

    """Aqui enconrtamos unas variables, las cuales usamos para definir 
    un numero aleatorio, por ello creamos la libreria random mencionada 
    al principio"""

    """De la libreria importamos randint y uniforma"""

    """randint, sirve para generar un numero aleatorio de tipo enteros, el 
    rango de que numero a que numero pueda generar, sera propuesto dentro 
    de parentesis, separa por una coma"""

    """uniform, al igual que randint, nos sirve para generar numeros
    aleatorios, solamente que estos numeros generados serán de tipo
    flotante o decimales"""

    asi1=randint(0,7)
    asi2=randint(8,11)
    asi3=randint(12,22)
    bus=randint(0,30)
    prec=uniform(40,80)

    """Las variables asi1,asi2,asi3, llevan ese nombre, ya que corresponde
    al numero del asiento, que estará disponible para el usuario.
    La variable bus hace refencia al número de la buseta disponible. Y el 
    prec hace referencia al precio de los paquetes."""
    
    """A cada valor aleatorio generado, serán devueltas como resultado en 
    otra variable, por lo que se convertiran en constantes, y seran usadas
    dentro del codigo"""

    a1=asi1
    b2=asi2
    c3=asi3 
    b=bus
    precF=prec

    """A continuación nos encontramos con un menú, donde tendremos los 
    lugares turisticos disponibles para que el usuario pueda visitar"""

    print ("Dentro de los paquetes de viajes disponibles se")
    print ("encuentran los siguientes lugares turísticos:")
    print ("____________________________________________")
    print ("|    1.El Panecillo                        |")
    print ("|    2.La mitad del mundo                  |")
    print ("|    3.Basílica del voto Nacional          |")
    print ("|    4.Teleférico                          |")
    print ("|    5.Volver al Menú Principal            |")
    print ("|------------------------------------------|")

    """Tendra una estructura repetitiva de tipo while, esto por si el usuario
    ingresa un valor no correspondiente, le vuela a mostrar el menú y pueda
    seleccionar otra opción"""

    while (True):
        opcPaque=int(input("Escoja una opción: "))
        if opcPaque==1:
            print ("____________________________________________")
            print ("|              EL PANECILLO                |")
            print ("|------------------------------------------|")

            """Aqui podemos ver informacion del paquete seleccionado, al igual que
            podemos visualizar como funcionan las variables definidas al principio
            de la función"""

            print("Para la visita al sitio turistico, contamos con los siguientes")
            print("asientos disponibles: ",a1,"",b2,"",c3," en la buseta numero: ",bus)
            print("Este paquete, tiene un precio de: ",prec)

            """El usuario podrá elegir el asiento que guste, cuando elija su asiento
            se le imprime un mensaje, el cual muestra la informacion de su viaje el 
            precio, el bus o buseta, y el número de asiento."""

            while (True):
                print("siendo a1:",a1)
                print("       b2:",b2)
                print("       c3:",c3)
                asi=input("Elija un asiento: \n")
                if asi=='a1':
                    print("Su compra se ha registrado, el numero de asiento es el,",a1)
                    print("el numero de bus es el: ",b,"por lo cual debera terminar")
                    print("pagando la cantidad de: ",precF) 
                    break   
                #print(a1, a2, a3)
                elif asi=='b2':
                    print("Su compra se ha registrado, el numero de asiento es el,",b2)
                    print("el numero de bus es el:",b,"por lo cual debera terminar")
                    print("pagando la cantidad de:",precF)
                    break
                elif asi=='c3':
                    print("Su compra se ha registrado, el numero de asiento es el,",c3)
                    print("el numero de bus es el:",b,"por lo cual debera terminar")
                    print("pagando la cantidad de:",precF)
                    break
                else:
                    print("Asiento no disponible")
            break
        elif opcPaque==2:

            """Al igual, en la opcion dos podemos ver informacion del paquete seleccionado
            junto con aqueñña informacion encontramos los numeros de asientos, bus y su 
            debido precio"""

            print ("____________________________________________")
            print ("|            MITAD DEL MUNDO               |")
            print ("|------------------------------------------|")
            print("Para la visita al sitio turistico, contamos con los siguientes")
            print("asientos disponibles: ",a1,"",b2,"",c3," en la buseta numero: ",bus)
            print("Este paquete, tiene un precio de: ",prec)

            """Trabajamos con las mismas variables, ya que siempre se crea un valor 
            aleatorio, y este cambia constantemente"""

            while (True):
                print("siendo a1:",a1)
                print("       b2:",b2)
                print("       c3:",c3)
                asi=input("Elija un asiento: \n")
                if asi=='a1':
                    print("Su compra se ha registrado, el numero de asiento es el, ",a1)
                    print("el numero de bus es el: ",b," lo cual debera terminar")
                    print("pagando la cantidad de: ",precF) 
                    break   
                #print(a1, a2, a3)
                elif asi=='b2':
                    print("Su compra se ha registrado, el numero de asiento es el, ",b2)
                    print("el numero de bus es el: ",b," lo cual debera terminar")
                    print("pagando la cantidad de: ",precF)
                    break
                elif asi=='c3':
                    print("Su compra se ha registrado, el numero de asiento es el, ",c3)
                    print("el numero de bus es el: ",b," lo cual debera terminar")
                    print("pagando la cantidad de: ",precF)
                    break
                else:
                    print("Asiento no disponible")
            break
        elif opcPaque==3:
            print ("____________________________________________")
            print ("|       BASILICA DEL VOTO NACIONAL         |")
            print ("|------------------------------------------|")
            print("Para la visita al sitio turistico, contamos con los siguientes")
            print("asientos disponibles: ",a1,"",b2,"",c3," en la buseta numero: ",bus)
            print("Este paquete, tiene un precio de: ",prec)

            """Trabajamos con las mismas variables, ya que siempre se crea un valor 
            aleatorio, y este cambia constantemente"""

            while (True):
                print("siendo a1:",a1)
                print("       b2:",b2)
                print("       c3:",c3)
                asi=input("Elija un asiento: \n")
                if asi=='a1':
                    print("Su compra se ha registrado, el numero de asiento es el, ",a1)
                    print("el numero de bus es el: ",b," lo cual debera terminar")
                    print("pagando la cantidad de: ",precF) 
                    break   
                #print(a1, a2, a3)
                elif asi=='b2':
                    print("Su compra se ha registrado, el numero de asiento es el, ",b2)
                    print("el numero de bus es el: ",b," lo cual debera terminar")
                    print("pagando la cantidad de: ",precF)
                    break
                elif asi=='c3':
                    print("Su compra se ha registrado, el numero de asiento es el, ",c3)
                    print("el numero de bus es el: ",b," lo cual debera terminar")
                    print("pagando la cantidad de: ",precF)
                    break
                else:
                    print("Asiento no disponible")
            break
        elif opcPaque==4:
            print ("____________________________________________")
            print ("|               TELEFÉRICO                 |")
            print ("|------------------------------------------|")
            print("Para la visita al sitio turistico, contamos con los siguientes")
            print("asientos disponibles: ",a1,"",b2,"",c3," en la buseta numero: ",bus)
            print("Este paquete, tiene un precio de: ",prec)
            while (True):
                print("siendo a1:",a1)
                print("       b2:",b2)
                print("       c3:",c3)

                """Trabajamos con las mismas variables, ya que siempre se crea un valor 
                aleatorio, y este cambia constantemente"""

                asi=input("Elija un asiento: \n")
                if asi=='a1':
                    print("Su compra se ha registrado, el numero de asiento es el, ",a1)
                    print("el numero de bus es el: ",b," lo cual debera terminar")
                    print("pagando la cantidad de: ",precF) 
                    break   
                #print(a1, a2, a3)
                elif asi=='b2':
                    print("Su compra se ha registrado, el numero de asiento es el, ",b2)
                    print("el numero de bus es el: ",b," lo cual debera terminar")
                    print("pagando la cantidad de: ",precF)
                    break
                elif asi=='c3':
                    print("Su compra se ha registrado, el numero de asiento es el, ",c3)
                    print("el numero de bus es el: ",b," lo cual debera terminar")
                    print("pagando la cantidad de: ",precF)
                    break
                else:
                    print("Asiento no disponible")
        elif opcPaque==5:
            break
        else:
             print("Opcion invalida")

#Instancia del objeto RegUsuario
print(RegUsuario.imprUsuario()) # Llamado para la ejecución del programa
print(MenuPrincipal.menuPrincipal())