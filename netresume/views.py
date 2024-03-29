from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Skill, Project

# Create your views here.
def index(request):
    all_courses = Course.objects.all()
    all_skills = Skill.objects.all()
    all_projects = Project.objects.all()
    
    social_media_links = {
        'linkedin' : 'https://www.linkedin.com/in/chanchalkmaurya/',
        'github' : 'https://github.com/chanchalkmaurya',
        'youtube' : 'https://www.youtube.com/@HindiMediumWaalaBanda',
    }
    context = {
        'title': "Homepage",
        'all_course': all_courses,
        'all_skill': all_skills,
        'all_projects': all_projects,
        'social': social_media_links,
    }
    return render(request, "index.html", context)
