from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("byebye", views.bye, name="bye"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question>/results/", views.results, name="results"),
    path("<int:question>/vote/", views.vote, name="vote"),
    path("index1", views.index1, name="index1"),

]