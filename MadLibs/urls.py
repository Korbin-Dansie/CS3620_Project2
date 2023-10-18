"""
URL configuration for MadLibs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# Custom views
from stories.views import home_view, create_story_view, play_story_view
urlpatterns = [
    path('', home_view, name='home'), # Change the index page
    path('story/create/', create_story_view, name='create'), # Change the index page
    path('story/play/<int:storyId>/', play_story_view, name='play'), # Change the index page
    path('story/play/<int:storyId>/display/', play_story_view, name='display'), # Change the index page


    path('admin/', admin.site.urls),
    path("users/", include("users.urls")),
]
