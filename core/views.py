from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Profile, SkillCategory, Project, Experience
from .forms import ContactForm

NAV_LINKS = [
    {'label': 'About',      'anchor': 'about'},
    {'label': 'Skills',     'anchor': 'skills'},
    {'label': 'Projects',   'anchor': 'projects'},
    {'label': 'Experience', 'anchor': 'experience'},
    {'label': 'Contact',    'anchor': 'contact'},
]


def index(request):
    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent! I'll get back to you soon.")
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'core/index.html', {
        'profile': profile,
        'skill_categories': skill_categories,
        'projects': projects,
        'experiences': experiences,
        'form': form,
        'nav_links': NAV_LINKS,
    })
