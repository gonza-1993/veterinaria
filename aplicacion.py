

listaDeAnimales = [
    {
    "nombre_animal":"Perro",
    "descrip" : "El mejor amigo del h",
    },
    {
    "nombre_animal":"Gato",
    "descrip" : "Tira muchos pelos"
    },
    {
    "nombre_animal":"Rhino",
    "descrip" : "Cuidado con el cuerno"
    },
    {
    "nombre_animal":"arania",
    "descrip" : "tiene ocho patas"
    }
]

def agregar_Animales(nombre,descripcion):
    animalNuevo = {
        "nombre_animal" : nombre,
        "descrip" : descripcion
    }
    listaDeAnimales.append(animalNuevo)


def borrar_animal(nombre):
    for animal in listaDeAnimales:
        if(animal["nombre_animal"].lower() == nombre.lower()):
            listaDeAnimales.remove(animal)
            print(f"Animal: {nombre} eliminado con exito")
            return

    print(f"Animal con el nombre {nombre} NO ENCONTRADO")


def editar_animal(nombre):
    for animal in listaDeAnimales:
        if(animal["nombre_animal"].lower() == nombre.lower()):
            nuevoNombre = input(f"Ingrese el nuevo nombre para reemplazar a {nombre}: ")
            nuevaDescripcion = input(f"Ingresa la nueva descripcion para {nombre}: ")
            animal["nombre_animal"] = nuevoNombre
            animal["descrip"] = nuevaDescripcion
            
            print("Descripcion Actualizada con EXITO")
            return
    
    print(f"Animal con el nombre {nombre} no encontrado")



def VerListado():
    for i in listaDeAnimales:
        print(f" {i['nombre_animal']} : {i['descrip']}")
    



def VerOpcionesMenu():
    print("------ PROGRAMA DE ANIMALES ---------")
    print("1) Ver listado de animales")
    print("2) Agregar un animal nuevo")
    print("3) Editar un animal existente")
    print("4) Eliminar un animal de la lista")
    print("5) Salir del programa")



#----ESTRUCTURA PRINCIPAL DEL PROGRAMA-----

ejecutarPrograma = True

while(ejecutarPrograma == True):
    VerOpcionesMenu()
    opcion = int(input("Elegi una opcion: "))
    
    match(opcion):
        case 1:
                VerListado()
        case 2:
                animalNuevo_nombre = input("Ingrese el nombre del nuevo animal: ")
                animalNuevo_descripcion = input("Ingresa la descripción del nuevo animal: ")
                agregar_Animales(animalNuevo_nombre,animalNuevo_descripcion)
                
                print("Animal agregado con EXITO !")
        case 3:
            animal_a_editar = input("Ingrese el nombre del animal a EDITAR: ")
            editar_animal(animal_a_editar)
        case 4:
            animal_a_borrar = input("Ingrese el nombre del animal que quieras borrar: ")
            borrar_animal(animal_a_borrar)
        case 5:
            print("Saliendo del programa")
            ejecutarPrograma = False
        case _:           
            print("Selecciona una opción valida")
           
