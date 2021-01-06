from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from auth.functions.math_cpf import isCpfValid

def validate_cpf(value):
    if not isCpfValid(value):
        raise ValidationError(
            _('%(value) não é um CPF válido'),
            params={'value': value},
        )

class CustomUser(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(_('cpf'), max_length=30, unique=True, validators=[validate_cpf])

    objects = UserManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
