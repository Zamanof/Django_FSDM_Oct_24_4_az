from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import TagViewSet, NotesViewSet, CategoryViewSet

router = DefaultRouter()

router.register('tags', TagViewSet, basename='tags')
router.register('notes', NotesViewSet, basename='notes')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]