# Proyecto Urban routes | Introducción
Este proyecto se desarrollo utilizando Python como lenguaje de programación con Selenium, el código fue escrito siguiendo el patron de diseño POM (Modelo de objetos de página) para llevar acabo las pruebas automatizadas de una pagina web.

# Objetivo
El objetivo de este proyecto es probar la funcionalidad de pedir el servicio de un taxi atravez de la pagina web llamada Urban routes cumpliendo todos los requisitos mínimos establecidos asi como manipulando todos los elementos presentes en el formulario y verificando que los cambios o datos ingresados estuvieran presentes.

#  Tecnologías necesarias para ejecutar el proyecto
- Un entorno de desarrollo integrado (IDE)
- Lenguaje de programacion python
- Selenium webdriver
- Pytest packages

Se compone de los archivos:
- data.py: este archivo contiene todos los valores de pruebas
- GetPhoneCode: este archivo contiene el codigo para obtener el phone code requerido para las pruebas
- UrbanRoutesLocatores: este archivo contiene todos los localizadores usados o requeridos para las pruebas
- UrbanRoutesMethods: este archivo contiene una clase que almacena todos los metodos usados para las pruebas
- main: este es el archivo principal donde se ejecutan todas las pruebas
  
# Comandos o metodos de ejecucion para los test
Una vez descarga la libreria Pytest, tenemos ir a las opciones de ejecuccion y edit configuration.
Daremos click en add new configuration, seleccionaremos Pytest, cambiaremos el scrip a custom, aplicamos los cambios.
con estos hecho ya podemos simplemente ejecutar el proyecto ver el resultado de las pruebas.

Tambien se puede hacer uso del comando 'pytest', como la consonala inicia en una carpeta antes podemos realizar los siguientes comandos:
1. 'cd qa-project-Urban_Routes_es' 
2. 'pytest main.py'

O en un solo paso:
1. 'pytest qa-project-Urban_Routes_es/main.py'

#Hallazgos clave
Al ejecutar la prueba automatizada no se encontron bugs.

# En conclusion
El servicio probado cumplio con los requisitos establecidos, todos los elementos con los que se interactuo funcionaban segun lo establecido en los requisitos, al momento de ser editados guardaban la información ingresada así como mostrar los cambios de valores he iconos al ingresar información y no presentaban errores de diseño. 

