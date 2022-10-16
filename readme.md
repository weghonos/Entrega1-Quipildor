### ENTREGA1-QUIPILDOR CRISTIAN.

*La base de datos se encuentra vacia, rellenar con un usuario para realizar pruebas *


> #### Direcciones web y sus funciones:
>
>> */home/* 
>> ##### Muestra la pagina principal
>
>>*/ver_usuarios/*
>>##### Visualización y Búsqueda de usuarios dentro de la BD.
>
>>*/crear_usuario/*
>>##### Contiene formulario para la creación de usuarios.
>>##### Una vez creados, devuelve a "/ver_usuarios/"
>
>>*/acerca_de/*
>>##### Informacion acerca del Alumno.

> #### Directorio de proyecto
>
>> - Entrega1-Quipildor  *(Directorio Raiz)
>>      - urls.py (Contiene url admin y home)
>> - home  *(Directorio de Modulo General)
>>      - static (Directorio que contiene CSS )
>>      - templates (Directorio que contiene templates de la app)
>>          - acerca_de.html (Acerca del alumno)
>>          - base.html (Bloques de Herencia de padre)
>>          - crear_usuario.html (form paracrear usuario)
>>          - index.html ( pagina inicial)
>>          - ver_usuarios.html (Visualiza datos de BD)
>>      - models.py (Contiene clase Usuario con campos de datos requeridos )
>>      - forms.py (Contiene 2 Clases, 1 para Busqueda y otra para creacion de usuarios. )
>>      - urls.py (contiene urls de creacion, visualizacion, index y "acerca de" )
>>      - views.py (Contiene funciones de visualizacion y creacion de usuarios. )
>> - db.sqlite3  (Base de datos vacia, rellenar con usuarios desde crear_usuario)
>> - Requirements.txt  (Requerimientos minimos para iniciar el proyecto)