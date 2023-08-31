from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import * 
from .forms import *
from django.contrib.auth import login, logout, authenticate

#import list views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
#Navbar views

def home(request):
    # One context for Artists, songs, albums and Podcasts
    context = {"artists": Artist.objects.all(), "songs": Song.objects.all(), "albums": Album.objects.all(), "podcasts": Podcast.objects.all()}
    return render(request, 'AppVibesU/home.html', context )


def aboutMe(request):
    return render(request, 'AppVibesU/aboutMe.html')

@login_required
def songs(request):
    context = {"songs": Song.objects.all()}
    return render(request, 'AppVibesU/songs.html', context)

@login_required
def artists(request):
    context = {"artists": Artist.objects.all()}
    return render(request, 'AppVibesU/artists.html', context)

@login_required
def albums(request):
    context = {"albums": Album.objects.all()}
    return render(request, 'AppVibesU/albums.html', context)

@login_required
def podcasts(request):
    context = {"podcasts": Podcast.objects.all()}
    return render(request, 'AppVibesU/podcasts.html', context)

@login_required
def artistForm(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = Artist(name=form.cleaned_data['name'],
                            genre=form.cleaned_data['genre'],
                            listeners=form.cleaned_data['listeners'],
                            is_favorite=form.cleaned_data['is_favorite'],
                            is_verified=form.cleaned_data['is_verified'],
                            image=form.cleaned_data['image'],
                            )
            artist.save()
            return render(request, 'AppVibesU/home.html')
        
    else:
        form = ArtistForm()
    return render(request, 'AppVibesU/artistForm.html', {'form': form})

@login_required
def songForm(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = Song(title=form.cleaned_data['title'],
                            artist=form.cleaned_data['artist'],
                            album=form.cleaned_data['album'],
                            length=form.cleaned_data['length'],
                            image=form.cleaned_data['image'],
                            plays=form.cleaned_data['plays'],
                            is_favorite=form.cleaned_data['is_favorite'],
                            )
            song.save()
            return render(request, 'AppVibesU/home.html')
           
    else:
        form = SongForm()
    return render(request, 'AppVibesU/songForm.html', {'form': form})

@login_required
def albumForm(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = Album(title=form.cleaned_data['title'],
                            artist=form.cleaned_data['artist'],
                            genre=form.cleaned_data['genre'],
                            release_date=form.cleaned_data['release_date'],
                            amount_of_songs=form.cleaned_data['amount_of_songs'],
                            album_duration=form.cleaned_data['album_duration'],
                            is_favorite=form.cleaned_data['is_favorite'],
                            image=form.cleaned_data['image'],
                            )
            album.save()
            return render(request, 'AppVibesU/home.html')
           
    else:
        form = AlbumForm()
    return render(request, 'AppVibesU/albumForm.html', {'form': form})

@login_required
def podcastForm(request):
    if request.method == "POST":
        form = PodcastForm(request.POST)
        if form.is_valid():
            podcast = Podcast(title=form.cleaned_data['title'],
                            host=form.cleaned_data['host'],
                            genre=form.cleaned_data['genre'],
                            release_date=form.cleaned_data['release_date'],
                            amount_of_episodes=form.cleaned_data['amount_of_episodes'],
                            podcast_duration=form.cleaned_data['podcast_duration'],
                            is_favorite=form.cleaned_data['is_favorite'],
                            image=form.cleaned_data['image'],
                            )
            podcast.save()
            return render(request, 'AppVibesU/home.html')
           
    else:
        form = PodcastForm()
    return render(request, 'AppVibesU/podcastForm.html', {'form': form})

#Search
@login_required
def searchArtist(request):
    return render(request, 'AppVibesU/searchArtist.html')

@login_required
def searchSong(request):
    return render(request, 'AppVibesU/searchSong.html')

@login_required
def searchAlbum(request):
    return render(request, 'AppVibesU/searchAlbum.html')

@login_required
def searchPodcast(request):
    return render(request, 'AppVibesU/searchPodcast.html')

@login_required
def searchArtist2(request):
   if request.GET['search']:
        patter = request.GET['search']
        artists = Artist.objects.filter(name__icontains=patter)
        context = {"artists": artists}
        return render(request, 'AppVibesU/artists.html', context)
   return HttpResponse("You don't enter any data")

@login_required
def deleteArtist(request,name):
    artist = Artist.objects.get(name=name)
    artist.delete()
    
    artists = Artist.objects.all()
    context = {"artists": artists}
    return render(request, 'AppVibesU/artists.html', context)

@login_required
def updateArtist(request, id_artist):
    artist = Artist.objects.get(id=id_artist)
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist.name=form.cleaned_data['name']
            artist.genre=form.cleaned_data['genre']
            artist.listeners=form.cleaned_data['listeners']
            artist.is_favorite=form.cleaned_data['is_favorite']
            artist.is_verified=form.cleaned_data['is_verified']
            artist.image=form.cleaned_data['image']
            artist.save()
            return redirect(reverse_lazy('artists'))
    else:
        form = ArtistForm(initial={
            'name': artist.name,
            'genre': artist.genre,
            'listeners': artist.listeners,
            'is_favorite': artist.is_favorite,
            'is_verified': artist.is_verified,
            'image': artist.image,         
        })
    return render(request, 'AppVibesU/artistForm.html', {'form': form})

@login_required
def deleteArtist(request, id_artist):
    artist = Artist.objects.get(id=id_artist)
    artist.delete()
    return redirect(reverse_lazy('artists'))


#class based view
# artistList
class artistList(LoginRequiredMixin, ListView):
    model = Artist

# artist Create
class artistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    fields=['name','genre','listeners','is_favorite','is_verified','image']
    success_url = reverse_lazy('artists')

#artist Update
class artistUpdate(LoginRequiredMixin, UpdateView):
    model = Artist
    fields=['name','genre','listeners','is_favorite','is_verified','image']
    success_url = reverse_lazy('artists')

#artist Delete
class artistDelete(LoginRequiredMixin, DeleteView):
    model = Artist
    success_url = reverse_lazy('artists')

#Artist Search
class artistSearch(LoginRequiredMixin, ListView):
    model = Artist
    template_name = 'AppVibesU/artist_list.html'
    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Artist.objects.filter(name__icontains=query)
        return object_list
    

#Song List
class songList(LoginRequiredMixin, ListView):
    model = Song

#Song Create
class songCreate(LoginRequiredMixin, CreateView):
    model = Song
    fields=['title','artist','album','length','image','mp3_track','plays','is_favorite']
    success_url = reverse_lazy('songs')

#Song Update
class songUpdate(LoginRequiredMixin, UpdateView):
    model = Song
    fields=['title','artist','album','length','image','mp3_track','plays','is_favorite']
    success_url = reverse_lazy('songs')

#Song Delete
class songDelete(LoginRequiredMixin, DeleteView):
    model = Song
    success_url = reverse_lazy('songs')

#Song Search
class songSearch(LoginRequiredMixin, ListView):
    model = Song
    template_name = 'AppVibesU/song_list.html'
    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Song.objects.filter(title__icontains=query)
        return object_list

#Album List
class albumList(LoginRequiredMixin,ListView):
    model = Album

#Album Create
class albumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields=['title','artist','genre','release_date','amount_of_songs','album_duration','is_favorite','image']
    success_url = reverse_lazy('albums')

#Album Update
class albumUpdate(LoginRequiredMixin, UpdateView):
    model = Album
    fields=['title','artist','genre','release_date','amount_of_songs','album_duration','is_favorite','image']
    success_url = reverse_lazy('albums')

#Album Delete
class albumDelete(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('albums')

#Album Search
class albumSearch(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'AppVibesU/album_list.html'
    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Album.objects.filter(title__icontains=query)
        return object_list

#Podcast List
class podcastList(LoginRequiredMixin, ListView):
    model = Podcast

#Podcast Create
class podcastCreate(LoginRequiredMixin, CreateView):
    model = Podcast
    fields=['title','host','genre','release_date','amount_of_episodes','podcast_duration','is_favorite','image']
    success_url = reverse_lazy('podcasts')

#Podcast Update
class podcastUpdate(LoginRequiredMixin, UpdateView):
    model = Podcast
    fields=['title','host','genre','release_date','amount_of_episodes','podcast_duration','is_favorite','image']
    success_url = reverse_lazy('podcasts')

#Podcast Delete
class podcastDelete(LoginRequiredMixin, DeleteView):
    model = Podcast
    success_url = reverse_lazy('podcasts')

#Podcast Search
class podcastSearch(LoginRequiredMixin, ListView):
    model = Podcast
    template_name = 'AppVibesU/podcast_list.html'
    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Podcast.objects.filter(title__icontains=query)
        return object_list
    

#Login module
def login_request(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            #get the username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).image.url
                except:
                    avatar = "/media/avatars/default.jpeg"
                finally:
                    request.session["avatar"] = avatar
                return redirect(reverse_lazy('home'))
            else:
                return render(request, "AppVibesU/login.html", {"form": form, 'message': f'Invalid username or password'})
        else:
            return render(request,"AppVibesU/login.html", {"form": form, 'message': f'Error, wrong form'})
    
    form = UserLoginForm()

    return render(request, "AppVibesU/login.html", {"form": form})

#Register module
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #get the username and password
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, "AppVibesU/home.html")
    else:
        form = UserRegisterForm()
    return render(request, "AppVibesU/register.html", {"form": form})

# Profile funcions


@login_required
def editProfile(request):
    print(request.user.is_authenticated)
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return redirect(reverse_lazy('home'))
        else:
            return render(request, "AppVibesU/editProfile.html", {'form': form, 'user':user}) 
    else:
        form = UserEditForm(instance=user)

    return render(request, 'AppVibesU/editProfile.html',{'form': form, 'user': user})

#Add Avatar 
@login_required
def addAvatar(request):
    if request.method == "POST":
        form = AvatarEditForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            #delete old avatar
            oldAvatar = Avatar.objects.filter(user=u)
            if len(oldAvatar) > 0:
                for i in range(len(oldAvatar)):
                    oldAvatar[i].delete()
            #save new avatar  
            avatar = Avatar(user=u, image=form.cleaned_data['image'])
            avatar.save()
            image = Avatar.objects.get(user=request.user.id).image.url
            request.session["avatar"] = image
            return render(request, "AppVibesU/home.html")
    else:
        form = AvatarEditForm()
    return render(request, "AppVibesU/addAvatar.html", {"form": form})