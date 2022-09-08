'''
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 06 de septiembre del 2022
Autor: Leonardo Martínez González
Continuación de la práctica 6
'''
import random

import bcrypt

'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes. (5) 10 min.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"Base de Datos",
                "Promedio":85
            },
            {
                "Nombre":"Inteligencia Artificial",
                "Promedio":100
            },
            . . . 
        ],
        "Promedio general": 98.4
   }

4. Regresar una lista de JSON con las materias de un estudiante, el formato es el siguiente:
[
    {"Nombre": "Contabilidad Financiera"},
    {"Nombre": "Dise\u00f1o UX y UI"}, 
    {"Nombre": "Base de datos distribuidas"}, 
    {"Nombre": "Finanzas internacionales IV"}, 
    {"Nombre": "Analisis y dise\u00f1o de sistemas de informacion"}, 
    {"Nombre": "Microservicios"},
    {"Nombre": "Algoritmos inteligentes"}
]


5. Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula 
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )

   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - Encriptar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4

   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada

6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }

   ó

   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }

   ó

    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }


'''

#Lista de Materias
def Estud():
    tupla = set()
    with open("Estudiantes.prn") as archivo:
        for line in archivo:
            tupla.add((line[0:8], line[8:-1]))
    return tupla


def Kardex():
    lista = []
    tupla = set()
    with open("Kardex.txt") as archivo:
        for line in archivo:
            lista = line.split("|")
            tupla.add((int(lista[0]), str(lista[1]), int(lista[2])))
    return tupla
import json
def Regresa_Materias_por_Estudiante(nc):
    promedio = Kardex()
    lista_m = []
    for mat in promedio:
        c,m,p = mat #Destructuro la variable
        if nc == c:
            lista_m.append({"Nombre":m})
    return json.dumps(lista_m)

print(Regresa_Materias_por_Estudiante(18420493))

'''
 Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula 
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )

   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - Cifrar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4

   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada

'''

def generarMayus():
    return chr(random.randint(65,90))

def generarMin():
    return chr(random.randint(97,122))

def generarNums():
    return random.randint(0,9)

def generarEsp():
    listachar = ['@', '#', '$','%','&','_','?','!']
    return listachar[random.randint(0,7)]

def generarContraseña():

    clave = ""
    for i in range(10):
        numero = random.randint(1, 5)
        if numero == 1:
            clave += generarMayus()
        elif numero == 2:
            clave += generarMin()
        elif numero == 3:
            clave += generarEsp()
        elif numero >= 4:
            clave += str(generarNums())
    return clave



#print("Contraseña: ", generarContraseña())

#Cifrar contraseñas con bcrypt

def cifrarContra(contra):
    salt = bcrypt.gensalt() #Por default tiene un valor de 12, lo cifra 12 veces
    contracifrada = bcrypt.hashpw(contra.encode("utf-8"), salt)

    return contracifrada

#c = generarContraseña()
#cf = cifrarContra(c)
#print(c, cf)
#print(bcrypt.checkpw("Yu6x4n3&5E".encode("utf-8"), "$2b$12$ZaiX5E1zzQiWd.T9JbBOnO2JV6VRQEwAQCfpiZGdXd1Wkj1JBSisu".encode("utf-8")))

def generarArchivoUsuarios():

    estudiantes = Estud()
    cont = 0
    with open("Usuarios.txt", "w") as archivo:
        for es in estudiantes:
            c, e = es
            clave = generarContraseña()
            cifrado = cifrarContra(clave)

            registro = c + " " + clave + " " + str(cifrado, "utf-8") + "\n"
            archivo.write(registro)
            cont +=1
    print("Archivo generado", cont)

#generarArchivoUsuarios()

'''
 Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }

   ó

   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }

   ó

    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }
'''

def autenticar_usuario(usuario,contrasena):
    lista = []
    lista_a = []
    auten = {}
    listaEs = Estud()
    bandera = False
    with open("Usuarios.txt") as archivo:
        for line in archivo:
            lista.append(line.split(" "))

    for contra in lista:
        if int(contra[0]) == usuario:
            bandera = True
            for es in listaEs:
                if (usuario == int(es[0])):
                     if(bcrypt.checkpw(contrasena.encode("utf-8"),contra[2].strip("\n").encode("utf-8"))):
                        auten["Bandera"]=True
                        auten["Usuario"]=es[1]
                        auten["Mensaje"]="Bienvenido al Sistema de Autenticación de usuarios"
                        break
                     else:
                         auten["Bandera"] = False
                         auten["Usuario"] = es[1]
                         auten["Mensaje"] = "Contrasena Incorrecta"
                         break

    if(bandera==False):
        auten["Bandera"] = False
        auten["Usuario"] = " "
        auten["Mensaje"] = "No existe el Usuario"
    return json.dumps(auten, indent=4)


print(autenticar_usuario(18420493, "144H!JBqr$"))