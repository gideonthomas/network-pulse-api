from django.contrib import admin

from .models import Entry, Tag

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
