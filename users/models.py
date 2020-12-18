from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(_('cpf'), max_length=30, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

#from django.conf import settings
#from django.db import models

#class User(models.Model):
#    cpf = models.CharField(max_length=400)
#    password = models.TextField(blank=False)


