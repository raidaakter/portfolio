from django.shortcuts import render

from portfolio.forms import (
    ContactMessageForm,
    ProjectForm,
    SkillForm,
    ExperienceForm,
    EducationForm,
)
from portfolio.models import Language, Project, Skill, Experience, Education


def signup_view(request):
    return render(request, "signup.html")


def login_view(request):
    return render(request, "login.html")


def home_view(request):
    return render(request, "home.html")


def logout_view(request):
    return render(request, "logout.html")


def projects_view(request):
    projects = Project.objects.all()
    return render(request, "projects.html", context={"projects": projects})


def contact_view(request):
    form = ContactMessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactMessageForm()
    context = {"form": form}
    return render(request, "contact.html", context)


def resume_view(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    languages = Language.objects.all()

    context = {
        "experiences": experiences,
        "educations": educations,
        "skills": skills,
        "languages": languages,
    }
    return render(request, "resume.html", context)
