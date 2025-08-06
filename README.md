# Proyecto Urban routes
Este proyecto prueba el pedir el servicio de un taxi con tarifa comfort, ingresando datos en el campo desde, hasta,
numero de telefono, metodo de pago, seleccionando manta y pañuelos y dos helados. 
Se compone de los archivos:
- data.py: este archivo contiene todos los valores de pruebas
- GetPhoneCode: este archivo contiene el codigo para obtener el phone code requerido para las pruebas
- UrbanRoutesLocatores: este archivo contiene todos los localizadores usados o requeridos para las pruebas
- UrbanRoutesMethods: este archivo contiene una clase que almacena todos los metodos usados para las pruebas
- main: este es el archivo principal donde se ejecutan todas las pruebas

#  Tecnologías necesarias para ejecutar el proyecto
- Un entorno de desarrollo integrado (IDE)
- Lenguaje de programacion python
- Selenium webdriver
- Pytest packages

# Comandos o metodos de ejecucion para los test
Una vez descarga la libreria Pytest, tenemos ir a las opciones de ejecuccion y edit configuration.
Daremos click en add new configuration, seleccionaremos Pytest, cambiaremos el scrip a custom, aplicamos los cambios.
con estos hecho ya podemos simplemente ejecutar el proyecto ver el resultado de las pruebas.

Tambien se puede hacer uso del comando 'pytest', como la consonala inicia en una carpeta antes podemos realizar los siguientes comandos:
1. 'cd qa-project-Urban_Routes_es' 
2. 'pytest main.py'

O en un solo paso:
1. 'pytest qa-project-Urban_Routes_es/main.py'

# En conclusion
Al ejecutar las pruebas automatizadas se puede verificar que la funcion a probar cumple con los requisitos!

