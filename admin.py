# jovens/admin.py

from django.contrib import admin
from .models import Jovem, Atividade

admin.site.register(Jovem)
admin.site.register(Atividade)
