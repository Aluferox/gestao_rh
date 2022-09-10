from django.urls import path
from .views import projetos

urlpatterns = [
    path('', projetos, name='projetos'),
]