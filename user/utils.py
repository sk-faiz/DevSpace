from .models import *
from django.db.models import Q

def searchProfiles(request):
    search_query = ''
    if request.GET.get('name'):
        search_query = request.GET.get('name')
    skills = Skill.objects.filter(Q(name__icontains=search_query))
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query) | Q(skill__in=skills))
 
    return profiles