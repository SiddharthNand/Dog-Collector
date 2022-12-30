from django.shortcuts import render
from django.http import HttpResponse


class Dog: 
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

dogs = [
  Dog('Comet', 'golden retriever', 3),
  Dog('Chico', 'pitbull', 2),
  Dog('King', 'lab', 4)
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })
