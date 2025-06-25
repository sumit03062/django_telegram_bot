from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    telegram_username = models.CharField(max_length=255)
