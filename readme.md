### ENTREGA1-QUIPILDOR CRISTIAN.

La base de datos se encuentra vacia, rellenar con un usuario o usar admin para realizar pruebas.

Usuario administrador:  admin

Password: lilo7259    

>Requerimientos antes de iniciar :
>>instalar:
>>django
>>django-ckeditor
>>pillow



> #### Direcciones web y sus funciones:
>
>> */home/* 
>> ##### Muestra la pagina principal
>
>>*/post/lista/*
>>##### Visualización de los posts creados.
>
>>*/posts/*
>>##### Listado y Busqueda de posts dentro de la BD, se activa la edicion solo si se inició sesión
>
>>*/post/crear/*
>>##### Contiene formulario para la creación de posts. (solo visible logueado)
>>##### Una vez creados, devuelve a "/ver_posts/"
>
>>*/iniciar_sesion/*
>>##### pantalla de login, al iniciar sesión se activa "crear post".
>
>>*/cerrar_sesion/*
>>##### cierra la sesión si se está logueado.
>
>>*/registrar/*
>>##### seccion para crear cuentas de usuario, redirige a Index.
>
>>*/acerca_de/*
>>##### Informacion acerca del Alumno.

> #### Directorio de proyecto
>
>> - Entrega1-Quipildor  *(Directorio Raiz)
>>      - urls.py (Contiene url admin y home y cuentas)
>> - cuentas  *(Directorio de Modulo General)
>>      - static (Directorio que contiene CSS de la pagina )
>>      - templates/cuentas (Directorio que contiene templates de la app cuentas)
>>          - cambiar_contrasena.html (formulario para cambiar password de la cuenta)
>>          - cerrar_sesión.html (Pagina de confirmacion de cierre de sesión)
>>          - editar_perfil.html (edicion de informacion de la cuenta)
>>          - iniciar_sesion.html (pantalla de login))
>>          - perfil.html (Muestra la informacion de la cuenta y links para edicion de los datos de la misma)
>>          - registrar.html (form para crear una cuenta nueva)
>>      - forms.py (Contiene clase Registar/Editar/CambiarPassword )
>>      - models.py (Contiene clase ExtensionUsuario ( Avatar y datos de la cuenta) )
>>      - urls.py (contiene urls creacion/edicion/perfil/sesion de la cuenta)
>>      - views.py (Contiene vistas de todo lo referido a la cuenta de usuario (registrar iniciar/cerrar sesion etc.) )
>> - home  *(Directorio de Modulo General)
>>      - static (Directorio que contiene CSS de la pagina )
>>      - templates (Directorio que contiene templates de la app)
>>          - acerca_de.html (Acerca del alumno)
>>          - base.html (Bloques de Herencia de padre)
>>          - buscar_post.html (Lista y busca todos los post creados como tambien leer indivudualmente un post)
>>          - crear_post.html (form para crear un post nuevo)
>>          - editar_post.html (form para editar posts creados)
>>          - eliminar_post.html (Pagina de confirmacion para eliminar post seleccionado)
>>          - index.html ( pagina inicial)
>>          - info_post.html (muestra el contenido indivual de un post en particular)
>>          - ver_posts.html (Visualiza todos los posts)
>>      - models.py (Contiene clase Post con campos de datos requeridos )
>>      - forms.py (Contiene 2 Clases, 1 para Busqueda y otra para creacion de usuarios. )
>>      - urls.py (contiene urls de creacion, visualizacion, index y "acerca de" )
>>      - views.py (Contiene funciones de visualizacion y creacion de usuarios. )
>> - db.sqlite3  (Base de datos vacia, rellenar con post desde crear_post)
>> - Requirements.txt  (Requerimientos minimos para iniciar el proyecto)