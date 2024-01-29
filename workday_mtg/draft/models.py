from django.db import models
from django.forms import ModelForm

class Player(models.Model):
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    slack_user_name = models.TextField(default='')

    def __str__(self):
        return self.slack_user_name
    
class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ["first_name", "last_name", "slack_user_name"]