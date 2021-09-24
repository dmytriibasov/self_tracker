from django.contrib import admin
from .models import Card, Reminder, Goal

admin.site.register(Goal)
admin.site.register(Reminder)


# Register your models here.
@admin.register(Card)
class CardModelAdmin(admin.ModelAdmin):
    search_fields = ('title', 'user', )
    ordering = ('user', 'created_at', )
    list_filter = ('user', )
    list_display = ('id', 'title', 'user', 'created_at', )
    list_per_page = 10

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
