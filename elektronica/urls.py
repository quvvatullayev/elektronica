from django.urls import path
from .views.eliments import ElimentsList

urlpatterns = [
    path('eliments/', ElimentsList.as_view()),
]