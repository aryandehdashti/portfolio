from django.urls import path
from .views import GetAbout, GetMyInfo, GetProject, GetSkill

urlpatterns = [
    path('about/', GetAbout.as_view()),
    path('myinfo/', GetMyInfo.as_view()),
    path('project/', GetProject.as_view()),
    path('skill/', GetSkill.as_view()),
]
