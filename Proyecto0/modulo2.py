import json

# Defino y Parametrizo la funcion:
BD = {}
def registro(BD):
  # Solicitar ingreso de Datos al usuario:
  username = input("Ingrese el nombre del usuario: ")
  password = input("Ingrese la contraseña: ")
  # Guardamos informacion del diccionario:
  BD.update({username:password})
  
  
# Defino y Parametrizo la funcion:
def leerData(BD):
  # Mostramos la informacion que contiene el diccionario:
  print(f"La info solicitada en la base de datos es: ")
  for key, value in BD.items():
        print(key, value)



# Defino y Parametrizo la funcion:
def guardarArchivo(BD):
  ruta = r"C:\Users\Familia\Desktop\Carpeta VSC\Asignacion3\Proyecto3"
  with open(ruta + "/archivo_diccionario5.txt", "w") as file:
    json.dump(BD, file, indent=4 ) 
        
# Parametrizo la funcion
def login(BD):
  nombre = input("Ingrese su usuario: ")
  # Solicitar al usuario que ingrese su login y password: 
  if nombre in BD.keys():
    clave = input("Ingrese su contraseña: ")
    if BD[nombre] ==clave:
      print("Has iniciado sesion") 
    else: 
        print("Contraseña Incorrecta") 
  else:
      return "No se ha encontrado el usuario"

    


