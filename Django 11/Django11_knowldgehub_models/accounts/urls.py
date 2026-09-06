from django.urls import path

from .views import login_view, register_view, dashboard_view, register_success, logout_view

app_name = 'accounts'

urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("register/success/", register_success, name="register_success"),
    path('logout/', logout_view, name="logout"),
]
