from django.contrib import admin
from .models import User
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from users.forms import UserChangeForm, UserCreationForm

User = get_user_model()
admin.site.register(User)
