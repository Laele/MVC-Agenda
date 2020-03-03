from model.model import Model
from view.view import View

class Controller:

    #Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contacto controllers
    def agregar_contacto(self, id_contacto,nombre,tel,correo,dir):
        b,c = self.model.agregar_contacto(id_contacto,nombre,tel,correo,dir)
        if b:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)
    
    def leer_contacto(self,id_contacto):
        e,c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_exite(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self,id_contacto = None,n_nombre = None,n_tel = None,n_correo = None,n_dir = None):
        e = self.model.actualizar_contacto(id_contacto ,n_nombre,n_tel,n_correo,n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)
        
    def borrar_contacto(self,id_contacto):
        e,c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
    
    def leer_contactos_letra(self,letra):
        c = self.model.buscar_contacto_letra(letra)
        self.view.mostrar_contactos(c)

    #Cita controllers

    def agregar_cita(self,id_cita,id_contacto,lugar,fecha,hora,asunto):
        b,c = self.model.agregar_cita(id_cita,id_contacto,lugar,fecha,hora,asunto)
        if b:
            self.view.agregar_cita(c)
        else:
            self.view.cita_ya_existe(id_cita)
    
    def leer_cita(self,id_cita):
        b,c = self.model.leer_cita(id_cita)
        if b:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_exite(id_cita)
    
    def leer_todas_citas(self):
        c = self.model.leer_todas_citas()
        self.view.mostrar_citas(c)
    
    def actualizar_cita(self,id_cita = None, n_id_contacto = None, n_lugar = None, n_fecha = None, n_hora = None , n_asunto = None):
        e = self.model.actualizar_cita(self,id_cita ,n_id_contacto ,n_lugar ,n_fecha ,n_hora  ,n_asunto)
        if e:
            self.view.modificar_cita(id_cita)
        else:
            self.view.cita_no_exite(id_cita)
    
    def borrar_cita(self,id_cita):
        e,c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)
    
    def leer_cita_fecha(self,fecha):
        c = self.model.leer_cita_fecha(fecha)
        self.view.mostrar_citas(c)
    


    #General methods
    def insertar_contactos(self):
        self.agregar_contacto(1,"Luis Soriano",4641145785,"luis.sorianocrespo@outlook.com","Monte Aragon 221 Primavera 2")
        self.agregar_contacto(2,"Alan Alvarez",4641156784,"alan.alvarezsanchez@outlook.com","Juan Rojas 228 Humanista 1")
    
    def insertar_citas(self):
        pass

    def start(self):
        #Display a welcome message
        self.view.start()
        #Insert data in model
        self.insertar_contactos()
        self.insertar_citas()
        #Show all contacts in DB
        self.leer_todos_contactos()
        self.leer_contactos_letra('a')
    
    def menu(self):
        #Display menu
        self.view.menu()
        o = input('Selecciona una opcion (1-9)')
        if o == '1':
            id_contacto = input("Introduce el id del contacto: ")
            nombre = input("Introduce el nombre del contacto: ")
            tel = input("Introduce el telefono del contacto: ")
            correo = input("Introduce el correo del contacto: ")
            dir = input("Introduce direccion del contacto: ")
            self.agregar_contacto(id_contacto,nombre,tel,correo,dir)
        elif o == '2':
            self.leer_todos_contactos()
        elif o == '3':
            print("Da enter si no quieres sustituir dicho dato.")
            id_contacto = input("Introduce el id del contacto a cambiar: ")
            n_nombre = input("Introduce el nuevo nombre: ")
            n_tel = input("Introduce el nuevo telefono: ")
            n_correo = input("Introduce el nuevo correo: ")
            n_dir = input("Introduce la nueva direccion: ")
            self.actualizar_contacto(int(id_contacto), n_nombre,n_tel,n_correo,n_dir)
        elif o == '4':
            id_contacto = input("Introduce el id del contacto a eliminar: ")
            self.borrar_contacto(int(id_contacto))
        elif o == '5':
            id_cita = input("Introduce el id de la cita: ")
            id_contacto = input("Introduce el id del contacto a citar: ")
            lugar = input("Introduce el Lugar de la cita: ")
            fecha = input("Introduce la fecha de la cita: ")
            hora = input("Introduce la hora de la cita: ")
            asunto = input("Introduce el asunto de la cita: ")

            self.agregar_citaint(int(id_cita),int(id_contacto),lugar,fecha,hora,asunto)
        elif o == '6':
            self.leer_todas_citas()
        elif o == '7':
            print("Da enter si no quieres sustituir dicho dato.")
            id_cita = input("Introduce el id de la cita a cambiar: ") 
            n_id_contacto = input("Introduce el id del nuevo contacto a citar: ")
            n_lugar = input("Introduce el nuevo lugar: ")
            n_fecha  = input("Introduce la nueva fecha: ")
            n_hora = input("Introduce la nueva hora: ")
            n_asunto = input("Introduce el nuevo asunto: ")

            self.actualizar_cita(int(id_cita),int(n_id_contacto),n_lugar,n_fecha,n_hora,n_asunto)
        elif o == '8':
            id_cita = input("Introduce el id de la cita a borrar: ")
            self.borrar_cita(int(id_cita))
        elif o ==  '9':
            self.view.end()
        else:
            self.view.opcion_no_valida()