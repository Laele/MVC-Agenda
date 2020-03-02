class View:
    def mostrar_contacto(self, contacto):
        print('*********** Datos del contacto **********')
        print('Nombre: ', contacto.nombre)
        print('Teléfono: ', contacto.tel)
        print('Correo: ', contacto.correo)
        print('Dirección: ', contacto.dir)
        print('*************************')
    
    def mostrar_contactos(self, contactos):
        print('******** Contactos definidos ********')
        for c in contactos:
            print(c.nombre, c.tel , c.correo, c.dir)
        print('*****************************')

    def agregar_contacto(self,contacto):
        print(contacto.nombre, ' Acaba de nacer en la base de datos')

    def borrar_contacto(self,contacto):
        print(contacto.nombre, ' Ha muerto en la base de datos')
    
    def actualizar_contacto(self,id_contacto):
        print(id_contacto, ' Fue modificado geneticamente de la base de datos')
    
    def contacto_ya_existe(self,id_contacto):
        print(id_contacto, ' Ya existe en la base de datos')

    def contacto_no_existe(self,id_contacto):
        print(id_contacto, ' No existe en la base de datos')
    
    def start(self):
        print('Un Mundo nuevo se acaba de crear!!!!')
    
    def end(self):
        print('El Mundo acaba de destruirse!')
    
    #CITAS VIEW
    def mostrar_cita(self, cita):
        print('*********** Datos del la Cita **********')
        print('Usuario ligado: ', cita.id_contacto)
        print('Lugar: ', cita.lugar)
        print('Fecha: ', cita.fecha)
        print('Hora: ', cita.hora)
        print('Asunto: ', cita.asunto)
        print('*************************')
    
    def mostrar_citas(self, citas):
        print('******** Citas definidas ********')
        for c in citas:
            print(c.id_contacto, c.lugar , c.fecha, c.hora,c.asunto)
        print('*****************************')

    def borrar_cita(self,cita):
        print(cita.id_cita, '  Cita ha expirado en la base de datos')
    
    def modificar_cita(self,cita_o,cita_n):
        print(cita_o.nombre, ' Cita fue modificada de la base de datos')
    
    def cita_ya_existe(self,cita):
        print(cita.id_cita, ' Cita ya existe en la base de datos')

    def cita_no_existe(self,id_cita):
        print(id_cita, ' Cita no existe en la base de datos')
    
    def agregar_cita(self,cita):
        print("Nueva cita: ",cita.asunto, ' agregada compa')
    
    def menu(self):
        print("************MENU**************")
        print('1. Agregar contacto')
        print('2. Mostrar contactos')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Agregar cita')
        print('6. Buscar cita')
        print('7. Actualizar cita')
        print('8. Borrar cita')

