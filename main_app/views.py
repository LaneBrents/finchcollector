from io import BufferedReader
from unicodedata import name
from django.shortcuts import render

from django.http import HttpResponse

# Add the class of finch
class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

finches = [
    Finch('Lolo', 'tabby', 'smelly', 2),
    Finch('Moomoo', 'calico', 'angy', 3),
    Finch('Chester', 'black', 'mysterious', 30)
]
# Create your views here.
def home(request):
    return HttpResponse('HELLOOOOO')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})
