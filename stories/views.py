import re
from django.shortcuts import redirect, render
from .models import Prompt, Story

from django.forms import formset_factory, modelformset_factory
from .forms import StoriesForm, PromptForm

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
            Story.objects.create_story(form.cleaned_data['title'], form.cleaned_data['story'], form.cleaned_data['author'])
            return redirect("home")
    else: # GET request
        form = StoriesForm()
    my_context = {
        "form": form,
        "site_title": "Create"
    }
    return render(request, "create.html", my_context) # return an html template

def play_story_view(request, storyId, *args, **kwargs):
    story = Story.objects.get(pk = storyId)
    PromptFormSet = modelformset_factory(Prompt, form=PromptForm, extra=0)
    qs = story.prompts.all()
    formset = PromptFormSet(request.POST or None, queryset=qs)
    my_context = {
        "story": story,
        "formset": formset,
        "site_title": "Play"
    }
    return render(request, "play.html", my_context) # return an html template
