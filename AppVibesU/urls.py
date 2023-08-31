from django.urls import path
from AppVibesU import views
from AppVibesU.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutMe/', views.aboutMe, name="aboutMe"),
    #Search
    path('searchArtist/', searchArtist, name="searchArtist"),
    path('searchSong/', searchSong, name="searchSong"),
    path('searchAlbum/', searchAlbum, name="searchAlbum"),
    path('searchPodcast/', searchPodcast, name="searchPodcast"),
    
  
    #Artist
    path('artists', artistList.as_view(), name="artists"),
    path('create_artist', artistCreate.as_view(), name="create_artist"),
    path('update_artist/<pk>', artistUpdate.as_view(), name="update_artist"),
    path('delete_artist/<pk>', artistDelete.as_view(), name="delete_artist"),
    path('search_artist', artistSearch.as_view(), name="search_artist"),
    #Song
    path('songs', songList.as_view(), name="songs"),
    path('create_song', songCreate.as_view(), name="create_song"),
    path('update_song/<pk>', songUpdate.as_view(), name="update_song"),
    path('delete_song/<pk>', songDelete.as_view(), name="delete_song"),
    path('search_song', songSearch.as_view(), name="search_song"),
    #Album
    path('albums', albumList.as_view(), name="albums"),
    path('create_album', albumCreate.as_view(), name="create_album"),
    path('update_album/<pk>', albumUpdate.as_view(), name="update_album"),
    path('delete_album/<pk>', albumDelete.as_view(), name="delete_album"),
    path('search_album', albumSearch.as_view(), name="search_album"),
    #Podcast
    path('podcasts', podcastList.as_view(), name="podcasts"),
    path('create_podcast', podcastCreate.as_view(), name="create_podcast"),
    path('update_podcast/<pk>', podcastUpdate.as_view(), name="update_podcast"),
    path('delete_podcast/<pk>', podcastDelete.as_view(), name="delete_podcast"),
    path('search_podcast', podcastSearch.as_view(), name="search_podcast"),

    path('login/', views.login_request, name="login"),
    #logout
    path('logout/', LogoutView.as_view(template_name="AppVibesU/logout.html"), name="logout"),
    #register
    path('register/', views.register, name="register"),
    #edit user
    path('editProfile', views.editProfile, name="editProfile"),
    #add avatar
    path('add_avatar', views.addAvatar, name="add_avatar")
]
