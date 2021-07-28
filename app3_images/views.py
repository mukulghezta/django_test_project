from django.shortcuts import render
from .models import Person

def profile(request):
    person = Person.objects.all()
    return render(request, "app3_images/profiles.html", {person:'person'})
