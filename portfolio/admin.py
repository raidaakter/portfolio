from django.contrib import admin


from portfolio.models import ContactMessage, Project, Skill, Experience, Education


admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ContactMessage)
