from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

from portfolio.models import ContactMessage, Education, Experience, Project, Skill


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = "__all__"


class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"
