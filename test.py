from model.contact import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller
'''
c1 = Contacto(1,"Luis Soriano",4641145785,"luis.sorianocrespo@outlook.com","Monte Aragon 221 Primavera 2")
c2 = Contacto(2,"Alan Alvarez",4641156784,"alan.alvarezsanchez@outlook.com","Juan Rojas 228 Humanista 1")

contactos = []
contactos.append(c1)
contactos.append(c2)
'''
#t = Cita(1,1,"Cine","22-08-2020","9:00","Pelicula con amigos")
"""
guess = input("Introduce Nombre: ")

for i in contactos:
    if i.nombre.lower() == guess.lower():
        print("Si está: " + guess)
        break
    else:
        print('No esta: ' + guess)"""

"""print(c.id_contacto)
print(c.nombre)
print(c.tel)
print(c.correo)
print(c.dir)

print(t.id_cita)
print(t.id_contacto)
print(t.lugar)
print(t.fecha)
print(t.hora)
print(t.asunto)"""
'''
m = Model()

m.agregar_contacto(1,"Luis Soriano",4641145785,"luis.sorianocrespo@outlook.com","Monte Aragon 221 Primavera 2")
m.agregar_contacto(2,"Alan Alvarez",4641156784,"alan.alvarezsanchez@outlook.com","Juan Rojas 228 Humanista 1")
m.agregar_cita(1,2,"Cine","22-08-2020","9:00","Pelicula con amigos")
m.agregar_cita(2,2,"Cine","22-08-2021","9:00","Pelicula con amigos")
s = m.leer_contacto(2)
print(s.nombre)

m.actualizar_contacto(2,"Sara Martinez", "1234-1234", "gh@gmail.com","Dicis")
s = m.leer_contacto(2)
print(s.nombre)

s = m.borrar_contacto(1)
print(s)
s = m.borrar_contacto(2)
print(s)

l = m.buscar_contacto_letra("S")
print(l)

f = m.buscar_cita_fecha("22-08-2021")
print(f)

a = m.leer_todos_contactos()
for c in a:
    print(c.nombre, c.tel)

v = View()
s = m.leer_todos_contactos()
v.mostrar_contactos(s)
c = m.leer_contacto(1)
v.mostrar_contacto(c)

f,c = m.borrar_contacto(1)
if f: 
    v.borrar_contacto(c)
else:
    v.contacto_no_existe(1)
'''
cont = Controller()
cont.start()

while (True):
    print("\n")
    cont.menu()
