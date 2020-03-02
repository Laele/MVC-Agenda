from .contact import Contacto
from .cita import Cita

class Model:

    def __init__(self):
        self.contactos = []
        self.citas = []
    
    def esta_id(self,id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True,c
        return False,0
    
    def esta_id_cita(self,id_cita):
        for c in self.citas:
            if c.id_cita == id_cita:
                return True,c
        return False,0


    #Contacto methods
    def agregar_contacto(self, id_contacto, nombre,tel,correo,dir):
        e,c = self.esta_id(id_contacto)
        if not e:
            c = Contacto(id_contacto, nombre,tel,correo,dir)
            self.contactos.append(c)
            return True,c
        return False,c
    
    def leer_contacto(self,id_contacto):
        e,c = self.esta_id(id_contacto)
        if e == True:
            return c
        return False
    
    def actualizar_contacto(self,id_contacto = None,n_nombre = None,n_tel = None,n_correo = None,n_dir = None):
        e,c = self.esta_id(id_contacto)
        if e== True:
            if n_nombre != None:
                c.nombre = n_nombre
            if n_tel != None:
                c.tel = n_tel
            if n_correo != None:
                c.correo = n_correo
            if n_dir != None:
                c.dir = n_dir
            return True
        return False
    
    def borrar_contacto(self,id_contacto):
        e,contacto = self.esta_id(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
        
            for c in lista_temp:
                self.citas.remove(c)
            return True, contacto
        return False, 0

    def buscar_contacto_letra(self,letra):
        list = []
        for i in self.contactos:
            if i.nombre[0] == letra:
                list.append(i.nombre)
        return list
    
    def leer_todos_contactos(self):
        return self.contactos


    #Cita methods
    def agregar_cita(self,id_cita,id_contacto,lugar,fecha,hora,asunto):
        if not self.esta_id_cita(id_cita)[0]:
            if self.esta_id(id_contacto)[0]:
                t = Cita(id_cita,id_contacto,lugar,fecha,hora,asunto)
                self.citas.append(t)
                return True,t
        return False,0
    
    def leer_cita(self,id_cita):
        e,c = self.esta_id_cita(id_cita)
        if e == True:
            return True,c
        return False,0

    def actualizar_cita(self,id_cita = None,n_id_contacto = None,n_lugar = None,n_fecha = None,n_hora = None ,n_asunto = None):
        e,c = self.esta_id_cita(id_cita)
        if e == True:
            if n_id_contacto != None:
                c.id_contacto = n_id_contacto
            if n_lugar  != None:
                c.lugar = n_lugar
            if n_fecha != None:
                c.fecha = n_fecha
            if n_hora != None:
                c.hora = n_hora
            if n_asunto != None:
                c.asunto = n_asunto
            return True
        return False

    def borrar_cita(self,id_cita):
        e,c = self.esta_id_cita(id_cita)
        if e == True:
            self.citas.remove(c)
            return True,c
        return False,0
    
    def buscar_cita_fecha(self,fecha):
        '''list  = []
        for i in self.citas:
            if i.fecha == fecha:
                list.append(i.id_cita)'''
        list = [i for i in self.citas if i.fecha== fecha]
        return list
    
    def leer_todas_citas(self):
        return self.citas

