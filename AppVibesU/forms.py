from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class ArtistForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    genre = forms.CharField(max_length=50, required=True)
    listeners = forms.IntegerField(required=True)
    is_favorite = forms.BooleanField(required=False)
    is_verified = forms.BooleanField(required=False)
    image = forms.CharField(max_length=250, required=True)

class SongForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    artist = forms.CharField(max_length=50, required=True)
    album = forms.CharField(max_length=50, required=True)
    length = forms.CharField(max_length=10, required=True)
    image = forms.CharField(max_length=250, required=True)
    plays = forms.IntegerField()
    is_favorite = forms.BooleanField(required=False)
   

class AlbumForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    artist = forms.CharField(max_length=50, required=True)
    genre = forms.CharField(max_length=50, required=True)
    release_date = forms.CharField(max_length=4, required=True)
    amount_of_songs = forms.IntegerField(required=True)
    album_duration = forms.CharField(max_length=10, required=True)
    is_favorite = forms.BooleanField(required=False)
    image = forms.CharField(max_length=250, required=True)

class PodcastForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    host = forms.CharField(max_length=50, required=True)
    genre = forms.CharField(max_length=50, required=True)
    release_date = forms.CharField(max_length=4, required=True)
    amount_of_episodes = forms.IntegerField(required=True)
    podcast_duration = forms.CharField(max_length=10, required=True)
    is_favorite = forms.BooleanField(required=False)
    image = forms.CharField(max_length=250, required=True)


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Password", max_length=50, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", max_length=50, required=True, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name', 'last_name' ]

#Edit Profile Form
class UserEditForm(UserCreationForm):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Modify E-mail")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Retype Password", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()


    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

#Edit Avatar Form
class AvatarEditForm(forms.Form):
    image = forms.ImageField(required=True)

