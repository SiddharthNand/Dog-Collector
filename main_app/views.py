from django.shortcuts import render, redirect
from .models import Dog
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NapsForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def dogs_index(request):
#     dogs = Dog.objects.all()
#     return render(request, 'dogs/index.html', {"dogs": dogs})

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
    naps_form = NapsForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'naps_form': naps_form})

def add_naps(request, dog_id):
  form = NapsForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_naps = form.save(commit=False)
    new_naps.dog_id = dog_id
    new_naps.save()
    return redirect('detail', dog_id=dog_id)