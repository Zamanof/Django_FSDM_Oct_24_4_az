from django.urls import path

from . import views

urlpatterns = [
    # notes/
    path("", views.notes_list, name="notes_list"),
    path("<int:note_id>/", views.notes_detail, name="notes_detail"),
]