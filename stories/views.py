from django.shortcuts import redirect, render
from .models import Story

from .forms import StoriesForm

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "stories": Story.objects.all(),
        "site_title": "Home"
    }
    return render(request, "home.html", my_context) # return an html template

def create_story_view(request, *args, **kwargs):
    if request.method == "POST":
        form = StoriesForm(request.POST)
        if form.is_valid():
            # save the info
            Story.objects.create_story(form.cleaned_data['name'], form.cleaned_data['story'], form.cleaned_data['author'])
            return redirect("home")
    else: # GET request
        form = StoriesForm()
    my_context = {
        "form": form,
        "site_title": "Create"
    }
    return render(request, "create.html", my_context) # return an html template
