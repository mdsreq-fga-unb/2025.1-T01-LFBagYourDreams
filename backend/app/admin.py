""" Admin da aplicação """

from django.contrib import admin
from . import models

admin.site.register(models.Produto)
