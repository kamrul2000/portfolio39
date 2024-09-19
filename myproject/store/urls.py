from django.urls import path
from .views import index, project,privacy,terms

urlpatterns = [
    path('', index, name='index'),
    path('project', project, name='project'),
    path('privacy', privacy, name='privacy'), 
    path('terms', terms, name='terms'),   
]
