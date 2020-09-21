import uuid
import boto3

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Snake, Toy, Photo
from .forms import FeedingForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'catcollector-sei-9-sy'

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
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def snakes_index(request):
    snakes = Snake.objects.all()
    return render(request, 'snakes/index.html', { 'snakes': snakes})

def snakes_detail(request, snake_id):
  snake = Snake.objects.get(id=snake_id)
  toys_snake_doesnt_have = Toy.objects.exclude(id__in= snake.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'snakes/detail.html', { 'snake': snake, 'feeding_form': feeding_form, 'toys': toys_snake_doesnt_have})

def add_feeding(request, snake_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.snake_id = snake_id
    new_feeding.save()
  return redirect('detail', snake_id=snake_id)

def assoc_toy(request, snake_id, toy_id):
  snake = Snake.objects.get(id=snake_id)
  snake.toys.add(toy_id)
  return redirect('detail', snake_id=snake_id)

def unassoc_toy(request, snake_id, toy_id):
  snake.objects.get(id=snake_id).toys.remove(toy_id)
  return redirect('detail', snake_id=snake_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def add_photo(request, snake_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, snake_id=snake_id)
    except:
      print('An error occured uploading file to S3')
  return redirect('detail', snake_id=snake_id)