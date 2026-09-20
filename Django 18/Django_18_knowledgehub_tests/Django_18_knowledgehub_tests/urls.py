from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from notes import views as notes_views

urlpatterns = [
       path('admin/', admin.site.urls),
    # / -> home
    path("", notes_views.home, name="home"),

    path("about/", notes_views.AboutPageView.as_view(), name="about"),
# / /notes/ -> routes from notes/urls.py
    path("notes/", include("notes.urls")),
    path("accounts/", include("accounts.urls")),
    path("contact/", notes_views.contact_form, name="contact"),
    path("api/", include("api.urls")),

    # OpenAPI schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

]
