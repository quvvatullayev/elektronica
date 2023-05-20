from django.urls import path
from .views.eliments import ElimentsList

urlpatterns = [
    path('eliments/', ElimentsList.as_view(), name='elements'),
]

from .views.eliment_info import Eliment_infoList, Eliment_infoGet, ElimentsCount

urlpatterns += [
    path('eliment_info/', Eliment_infoList.as_view()),
    path('eliment_info/<int:eliments_id>/', Eliment_infoGet.as_view(), name='eliment_info'),
    path('eliments_count/<int:pk>/', ElimentsCount.as_view(), name='eliments_count'),
]

from .views.sorted import ElimentSorted

urlpatterns += [
    path('sorted/', ElimentSorted.as_view(), name='sorted'),
]