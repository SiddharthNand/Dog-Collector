from django.db import models
from django.urls import reverse


NAPS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)


class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f"{self.name} - {self.age}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})


class Naps(models.Model):
    date = models.DateField("nap date")
    nap = models.CharField(max_length=1, choices=NAPS, default=NAPS[0][0])
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_nap_display()} on {self.date} for {self.dog}"