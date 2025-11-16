from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/", views.view_all_campaigns, name="view"),
    path("add/", views.add_new_campaign, name="add"),
]