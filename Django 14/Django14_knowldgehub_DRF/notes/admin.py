from django.contrib import admin

from notes.models import Category, Note, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'author', 'created_at', 'updated_at', 'status')
    list_filter = ('created_at', 'category')
    search_fields = ('title', 'content', 'author__username')
    autocomplete_fields = ('author', 'category')
    filter_horizontal = ('tags',)