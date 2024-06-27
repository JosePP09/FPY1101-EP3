import os
sku_existentes = []
libros = []
prestamos = []
listado_prestamos = []
def registrar():
    try:
        titulo = input("Ingrese el titulo del libro: ").lower()
        autor = input("Ingrese el autor del libro: ").lower()
        año = int(input("Ingrese el año de publicacion del libro: "))
        sku = input("Ingrese el SKU(Ejemplo de SKU es las 6 primeras letras del título del libro – las 3 primeras letras del autor – año de publicación): ").lower()

        libro = {
            'titulo': titulo ,
            'autor' : autor ,
            'año' : año ,
            'sku' : sku ,
        }
        libros.append(libro)
        sku_existentes.append(sku)
    except ValueError:
        ("Opcion ingresada no es valida")

def prestar():
        usuario = input("Ingrese su nombre: ").lower()
        titulo = input("Ingresa el nombre del libro: ").lower()
        skuprestado = input("Ingrese el SKU del libro a prestar: ").lower()
        
        
        if skuprestado in sku_existentes:
            if not skuprestado in prestamos:
                fecha = input("Ingrese la fecha del prestamo: ")
                prestamos.append(skuprestado)
                prestamo = {
                    'usuario' : usuario,
                    'titulo' : titulo,
                    'fecha': fecha
                }
                listado_prestamos.append(prestamo)
                prestamos.append(skuprestado)
                print("Se ha generado tu prestamo")
            else:
                print("El libro ya se presto")
        else:
            print("El libro no existe")


        
def listar():
    print("Titulo\t\tAutor\t\tAño de publicacion\t\tSKU\n")
    for libro in libros:
        print(f"{libro['titulo']}\t\t{libro['autor']}\t\t{libro['año']}\t\t{libro['sku']}\n")

def imprimir():
    
    with open("Reporte_prestamos.txt","w") as archivo:
        archivo.write("Usuario\t\tTitulo\t\tFecha del prestamo\n")
        for prestamo in listado_prestamos:
            archivo.write(f"{prestamo['usuario']}\t\t{prestamo['titulo']}\t\t{prestamo['fecha']}\n")
    print("La Reporte de prestamos se guardo en", os.getcwd())

def menu():
    while True:
        print("---Menu---\n1. Registra libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de prestamos\n5. Salir del programa")
        try:
            op = int(input("Selecciona una opcion: "))
            if op == 1:
                registrar()
            elif op ==2:
                prestar()
            elif op ==3:
                listar()
            elif op ==4:
                imprimir()
            elif op == 5:
                print("Programa finalizado\nDesarrollado por Jose Galvez\nRUN 20.640.577-5")
                break
        except ValueError:
            print("La opcion ingresada no es valida")
    