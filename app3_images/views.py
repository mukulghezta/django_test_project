from django.shortcuts import render
from .models import Person
from .forms import CreatePerson

def profile(request):
    person = Person.objects.all()
    return render(request, "app3_images/profiles.html", {person:'person'})

def create_profile(request):
    if request.method == "POST":
        form = CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.save()
    return render(request, "app3_images/create_profile.html")
