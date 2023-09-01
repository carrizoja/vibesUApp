# VibesU App (English version)

## Description

`VibesU App` is a music streaming webApp in which you could listen to music online and download songs.

## Models
* It has artists, albums, songs and podcasts. 

* Model Song:
    title = CharField(max_length=50)
    artist = CharField(max_length=50)
    album = CharField(max_length=50)
    length = CharField(max_length=10)
    image = CharField(max_length=250)
    mp3_track = CharField(max_length=250, null=True)
    plays = IntegerField()
    is_favorite = BooleanField(default=False)

* Artist:
    name = CharField(max_length=50)
    genre = CharField(max_length=50)
    listeners = IntegerField()
    image = CharField(max_length=250)
    is_favorite = BooleanField(default=False)
    is_verified = BooleanField(default=False)


* Album:
    title = CharField(max_length=50)
    artist = CharField(max_length=50)
    genre = CharField(max_length=50)
    image = CharField(max_length=250)
    release_date = CharField(max_length=4)
    amount_of_songs = IntegerField()
    album_duration = CharField(max_length=10)
    is_favorite = BooleanField(default=False)

* Podcast:
    title = CharField(max_length=50)
    host = CharField(max_length=50)
    genre = .CharField(max_length=50)
    image = .CharField(max_length=250)
    release_date = CharField(max_length=4)
    amount_of_episodes = IntegerField()
    podcast_duration = CharField(max_length=10)
    is_favorite = BooleanField(default=False)
## Default User:
user: koche
password: Sietepalabras155

## Main functions:

* `Play a Song`: you can listen to a song in the Home section. Go to the "Most Played Songs" section and select it.

* `Artist, songs, albums and podcast list` are available using the CRUD options on the navbar.
* `Artist creation`: you have to enter to the CRUDS / Artists option on the navbar. Then, select "add new" and you should complete all the data for a new artist.
* `Album creation`: you have to enter the the CRUDS / Albums option on the navbar. Then, select "add new" and you should complete all the data for a new album.
* `Song creation`: you have to enter the the CRUDS / Songs option on the navbar. Then, select "add new" and you should complete all the data for a new song.
* `Podcast creation`: you have to enter the the CRUDS / Podcasts option on the navbar. Then, select "add new" and you should complete all the data for a new podcast.
* `Artist edition`: you can change the data from an artist going to CRUDs / Artists option. Then, select the edit option of the artist you want to change.
* `Album edition`: you can change the data from an album going to CRUDs / Albums option. Then, select the edit option of the album you want to change.
* `Song edition`: you can change the data from a song going to CRUDs / Songs option. Then, select the edit option of the song you want to change.
* `Podcast edition`: you can change the data from a Podcast going to CRUDs / Podcasts option. Then, select the edit option of the podcast you want to change.
* `Artist removal`: you can delete a selected artist going to CRUDs / Artists option. Then, select the delete option of the artist you want to remove. You have to confirm the removal.
* `Album removal`: you can delete a selected album going to CRUDs / Albums option. Then, select the delete option of the album you want to remove. You have to confirm the removal.
* `Song removal`: you can delete a selected song going to CRUDs / Songs option. Then, select the delete option of the song you want to remove. You have to confirm the removal.
* `Podcast removal`: you can delete a selected podcast going to CRUDs / Podcasts option. Then, select the delete option of the podcast you want to remove. You have to confirm the removal.
* `Search option`: you can use this function on the navbar. Select a Artist, Song, Album or Podcast criteria. 
* `Edit Profile`: you can edit your user data going to your profile name. Then, select "Edit Profile".
* `Add Avatar`:  you can add an avatar for your user going to your profile name. Then, select "Add Avatar".


**Libraries and Technologies used:**

- Front End with **Html, CSS, Javascript y template de Bootstrap**
- Ruteo with **Django**
- Backend with **Python y Django**

## About Me section

* If you want to know more info about me, you can go to the "About Me" section on the navbar ;)

## Site Deployment

https://web-production-dade.up.railway.app/


# Aplicación VibesU (versión en español)

## Descripción

"VibesU App" es una aplicación web de Streaming de música en la que puedes escuchar música en línea y descargar canciones.

## Modelos
*Cuenta con artistas, álbumes, canciones y podcasts.

* Model Song:
    title = CharField(max_length=50)
    artist = CharField(max_length=50)
    album = CharField(max_length=50)
    length = CharField(max_length=10)
    image = CharField(max_length=250)
    mp3_track = CharField(max_length=250, null=True)
    plays = IntegerField()
    is_favorite = BooleanField(default=False)

* Artist:
    name = CharField(max_length=50)
    genre = CharField(max_length=50)
    listeners = IntegerField()
    image = CharField(max_length=250)
    is_favorite = BooleanField(default=False)
    is_verified = BooleanField(default=False)


* Album:
    title = CharField(max_length=50)
    artist = CharField(max_length=50)
    genre = CharField(max_length=50)
    image = CharField(max_length=250)
    release_date = CharField(max_length=4)
    amount_of_songs = IntegerField()
    album_duration = CharField(max_length=10)
    is_favorite = BooleanField(default=False)

* Podcast:
    title = CharField(max_length=50)
    host = CharField(max_length=50)
    genre = .CharField(max_length=50)
    image = .CharField(max_length=250)
    release_date = CharField(max_length=4)
    amount_of_episodes = IntegerField()
    podcast_duration = CharField(max_length=10)
    is_favorite = BooleanField(default=False)

## Usuario predeterminado:
usuario: koche
contraseña: Sietepalabras155

## Funciones principales:

* `Reproducir una canción`: puedes escuchar una canción en la sección Inicio. Ve a la sección "Canciones más reproducidas" y selecciónala.

* La `Lista de artistas, canciones, álbumes y podcasts` están disponibles usando las opciones CRUD en la barra de navegación.
* `Creación de artista`: debes ingresar a la opción CRUDS / Artistas en la barra de navegación. Luego, selecciona "agregar nuevo" y deberás completar todos los datos de un nuevo artista.
* `Creación de álbum`: debes ingresar a la opción CRUDS / Álbumes en la barra de navegación. Luego, selecciona "agregar nuevo" y deberás completar todos los datos para un nuevo álbum.
* `Creación de canciones`: debes ingresar a la opción CRUDS / Canciones en la barra de navegación. Luego, selecciona "agregar nuevo" y deberás completar todos los datos para una nueva canción.
* `Creación de podcast`: debes ingresar a la opción CRUDS / Podcasts en la barra de navegación. Luego, selecciona "agregar nuevo" y deberás completar todos los datos para un nuevo podcast.
* `Edición de artista`: puedes cambiar los datos de un artista yendo a la opción CRUDs / Artistas. Luego, seleccione la opción de edición del artista que desea cambiar.
* `Edición de álbum`: puedes cambiar los datos de un álbum yendo a la opción CRUDs / Álbumes. Luego, seleccione la opción de edición del álbum que desea cambiar.
* `Edición de canción`: puedes cambiar los datos de una canción yendo a la opción CRUDs/Canciones. Luego, seleccione la opción de edición de la canción que desea cambiar.
*`Edición Podcast`: puedes cambiar los datos de un Podcast yendo a la opción CRUDs/Podcasts. Luego, seleccione la opción de edición del podcast que desea cambiar.
* `Eliminación de artista`: puede eliminar un artista seleccionado yendo a la opción CRUDs / Artistas. Luego, seleccione la opción de eliminar del artista que desea eliminar. Tienes que confirmar la eliminación.
* `Eliminación de álbum`: puede eliminar un álbum seleccionado yendo a la opción CRUD/Álbumes. Luego, seleccione la opción de eliminar del álbum que desea eliminar. Tienes que confirmar la eliminación.
* `Eliminación de canciones`: puede eliminar una canción seleccionada yendo a la opción CRUD/Canciones. Luego, seleccione la opción de eliminar de la canción que desea eliminar. Tienes que confirmar la eliminación.
* `Eliminación de podcast`: puede eliminar un podcast seleccionado yendo a la opción CRUDs/Podcasts. Luego, seleccione la opción de eliminar del podcast que desea eliminar. Tienes que confirmar la eliminación.
* `Opción de búsqueda`: puedes usar esta función en la barra de navegación. Seleccione un criterio de artista, canción, álbum o podcast.
* `Editar perfil`: puedes editar tus datos de usuario yendo al nombre de tu perfil. Luego, seleccione "Editar perfil".
* `Agregar Avatar`: puedes agregar un avatar para tu usuario yendo al nombre de tu perfil. Luego, seleccione "Agregar avatar".


**Bibliotecas y tecnologías utilizadas:**

- Front End con **Html, CSS, Javascript y plantilla de Bootstrap**
-Ruteo con **Django**
- Backend con **Python y Django**

## Sección Acerca de mí

* Si quieres saber más información sobre mí, puedes ir a la sección "Acerca de mí" en la barra de navegación ;)# vibesUApp

## Despliegue del sitio

https://web-production-dade.up.railway.app/