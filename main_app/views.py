from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def snakes_index(request):
    return render(request, 'snakes/index.html', { 'snakes': snakes})

class Snake:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

snakes = [
  Snake('Bean', 'Black Mamba', 'foul little demon', 3),
  Snake('Kaa', 'Python', 'diluted tortoise shell', 0),
  Snake('Voldemort', 'Viper', '3 legged cat', 4)
]