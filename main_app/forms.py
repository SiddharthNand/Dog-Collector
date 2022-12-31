from django.forms import ModelForm
from .models import Naps

class NapsForm(ModelForm):
  class Meta:
    model = Naps
    fields = ['date', 'nap']