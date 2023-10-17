from django.db import models
from django.conf import settings
from django.db import models
import re
import ast

# Create your models here.

# NOTE: use Model instance to manage the models
class StoryManager(models.Manager):
    """ On create_story create the corresponding prompts """
    def create_story(self, title, story, author):
        newstory = self.create(title=title, story=story, author=author)
        # Parse the story and create the promts
        matches=re.finditer(r"\[(?:(?:(?!(?<!\\)\]).)*)]", story) # Based off of finding mathcing quotes - https://stackoverflow.com/questions/9519734/python-regex-to-find-a-string-in-double-quotes-within-a-string
        for match in matches:
            Prompt.objects.create(prompt=match.group(), start=match.start(), end=match.end(), story=newstory)
        # to call is use Story.objects.create_story(...)
        return newstory

class Story(models.Model):
    title = models.CharField(max_length=64)
    story = models.TextField(max_length=1024)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Store the users info
    
    objects = StoryManager()

    def __str__(self) -> str:
        return self.author.username + " - " + self.title
    
class Prompt(models.Model):
    start = models.IntegerField() # The start location of the string to be replaced
    end = models.IntegerField() # The end location of the string to be replaced
    prompt = models.TextField(max_length=32) # Store the promts in a json array
    answer = models.TextField(max_length=32, blank=True, default="[Blank]") # Store the user submited value
    # NOTE: Because we changed related name we do not use prompt_set we just use prompts
    story = models.ForeignKey(Story, related_name = 'prompts', on_delete=models.CASCADE)
