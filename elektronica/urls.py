from django.urls import path
from .views.eliments import ElimentsList

urlpatterns = [
    path('eliments/', ElimentsList.as_view()),
]

from .views.eliment_info import Eliment_infoList, Eliment_infoGet, ElimentsCount

urlpatterns += [
    path('eliment_info/', Eliment_infoList.as_view()),
    path('eliment_info/<int:eliments_id>/', Eliment_infoGet.as_view()),
    path('eliments_count/<int:pk>/', ElimentsCount.as_view()),
]