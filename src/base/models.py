from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class User(AbstractUser):
    # AbstractUser class implements a fully featured User model with admin-compliant permissions
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    party = models.BooleanField(default=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']