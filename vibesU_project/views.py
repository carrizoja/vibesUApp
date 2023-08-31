from django.http import HttpResponse
from django.template import Template, Context
from django.template import  loader
from datetime import datetime
from AppVibesU.models import *


def hello(request):
    return HttpResponse("Hello world")
   

def testTemplate(self):
    name = "Jose"
    lastname = "Carrizo"
    # get the date now 
    datetime_now = datetime.now()
    #store it in a dictionaty variable
    my_dict = {'name': name, 'lastname': lastname, 'datetime_now': datetime_now}
    template = loader.get_template("template1.html")
    document = template.render(my_dict)
  
    return HttpResponse(document)

#Add song def
def add_song(self):
    str__song = "Siete Palabras"
    song = Song(title=str__song, artist="Raly Barrionuevo", album="La niña de los andamios", length="4min 10seg", plays=5, is_favorite=True)
    song.save()
    document =f"<html><h1>Song {str__song} added!</h1></html>"
    return HttpResponse(document)

