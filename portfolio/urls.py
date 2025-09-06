from django.urls import path

from portfolio.views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("projects/", projects_view, name="projects"),
    path("contact/", contact_view, name="contact"),
    path("resume/", resume_view, name="resume"),
]
