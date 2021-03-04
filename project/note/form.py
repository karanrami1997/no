from django.forms import ModelForm
from .models import Document

class Loform(ModelForm):
    class Meta:
        model = Document
        fields = ('title','content')