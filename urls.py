from django.urls import path
from . import views

urlpatterns = [
    #/genres/
    path('', views.index, name="index"),

    #genre/1
    path('<int:genre_id>', views.details, name="details")
]