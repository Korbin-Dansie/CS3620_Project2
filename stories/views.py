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
            form.cleaned_data['author'] = request.user # Set to the current logged in user
            # save the info
            Story.objects.create_story(form.cleaned_data['title'], form.cleaned_data['story'], form.cleaned_data['author'])
            return redirect("home")
    else: # GET request
        form = StoriesForm()
        form.initial['author'] = request.user.id # Set to the current logged in user
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
    # If we are posting back to the webpage
    if request.method == 'POST':
        if formset.is_valid():
            story_value = []
            story_splice_start = 0

            for form in formset.forms:
                prompt_value = form.cleaned_data['answer']
                prompt_start = form.cleaned_data['start']
                prompt_end = form.cleaned_data['end']

                # Splice the story with the input answers
                # If the input awnsers are blank just add the prompt value
                if not prompt_value:
                    prompt_value = form.cleaned_data['prompt']
                # story_value = story_value + story.story[story_splice_start:prompt_start] + prompt_value
                story_value.append([story.story[story_splice_start:prompt_start], prompt_value])
                story_splice_start = prompt_end
            # add the rest of the story
            # story_value = story_value + story.story[story_splice_start:]
            story_value.append([story.story[story_splice_start:], ""])

            my_context = {
                "story": story,
                "result_story": story_value,
                "site_title": "Play"
            }
            return render(request, "display.html", my_context) # return an html template

    # Else we are GETing the webpage
    # Set all awnsers to blank on inital
    for form in formset:
        form.initial['answer'] = ""
    my_context = {
            "story": story,
            "formset": formset,
            "site_title": "Play"
    }
    return render(request, "play.html", my_context) # return an html template