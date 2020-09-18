from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Snake
from .forms import FeedingForm

# Add the following import
from django.http import HttpResponse

class SnakeCreate(CreateView):
  model = Snake
  fields = ['name', 'species', 'description', 'age']

class SnakeUpdate(UpdateView):
  model = Snake
  # disallow the renaming of a snake by excluding the name field!
  fields = ['species', 'description', 'age']

class SnakeDelete(DeleteView):
  model = Snake
  success_url = '/snakes/'


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def snakes_index(request):
    snakes = Snake.objects.all()
    return render(request, 'snakes/index.html', { 'snakes': snakes})

def snakes_detail(request, snake_id):
  snake = Snake.objects.get(id=snake_id)
  feeding_form = FeedingForm()
  return render(request, 'snakes/detail.html', { 'snake': snake, 'feeding_form': feeding_form})

def add_feeding(request, snake_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.snake_id = snake_id
    new_feeding.save()
  return redirect('detail', snake_id=snake_id)