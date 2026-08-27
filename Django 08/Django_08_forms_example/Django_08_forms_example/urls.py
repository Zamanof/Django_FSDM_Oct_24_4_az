"""
URL configuration for Django_08_forms_example project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path

from forms_example import views
urlpatterns = [
    path('', views.contact_page, name='contact_page'),
    path('success/',views.success, name='success'),
    path('feedback/',views.feedback_view, name='feedback'),
    path('notes/', views.note_draft, name='note_draft'),
]
