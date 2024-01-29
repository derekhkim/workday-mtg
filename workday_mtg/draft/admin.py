from django.contrib import admin
from draft.models import Player

class PlayerAdmin(admin.ModelAdmin):
    model = Player
    list_display = ['id', 'first_name', 'last_name', 'slack_user_name']
    ordering = ['-first_name']


admin.site.register(Player, PlayerAdmin)