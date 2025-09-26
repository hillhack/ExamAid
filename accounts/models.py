from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # For now, only student role; you can add roles later
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.username
