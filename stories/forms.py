from django import forms
from .models import Story, Prompt

class StoriesForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = "__all__"
        widgets =   { 
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'story' : forms.Textarea(attrs={'class': 'form-control'}),

            'author': forms.HiddenInput(),
        }


class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = "__all__"
        widgets =   { 
            'start' : forms.HiddenInput(), 
            'end' : forms.HiddenInput(), 
            'story' : forms.HiddenInput(),

            'answer': forms.TextInput(attrs={'class': 'form-control'}),
            'prompt' : forms.TextInput(attrs={'class': 'form-control-plaintext', "disabled": True, "readonly": True}),
                    }