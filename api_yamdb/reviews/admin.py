from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title

admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Comment)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    filter_horizontal = ["genre"]
