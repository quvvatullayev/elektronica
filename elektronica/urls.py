from django.urls import path
from .views.eliments import ElimentsList
from .views.eliment_info import Eliment_infoList, Eliment_infoGet

urlpatterns = [
    path('eliments/', ElimentsList.as_view()),
    path('eliment_info/', Eliment_infoList.as_view()),
    path('eliment_info/<int:eliments_id>/', Eliment_infoGet.as_view()),
]