from django.shortcuts import render, redirect
from .models import Dog, Toy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NapsForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class DogList(ListView):
    model = Dog
    template_name = 'dogs/index.html'

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'

class DogUpdate(UpdateView):
  model = Dog
  fields = ['name', 'breed', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    id_list = dog.toys.all().values_list('id')
    toys_dog_doesnt_have = Toy.objects.exclude(id__in=id_list)
    naps_form = NapsForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'naps_form': naps_form, 'toys': toys_dog_doesnt_have })

def add_naps(request, dog_id):
  form = NapsForm(request.POST)
  if form.is_valid():
    new_naps = form.save(commit=False)
    new_naps.dog_id = dog_id
    new_naps.save()
    return redirect('detail', dog_id=dog_id)

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


def assoc_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.add(toy_id)
  return redirect('detail', dog_id=dog_id)


class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'age']