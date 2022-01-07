from django.contrib import admin
from django.db import models
from django.db.models.expressions import OrderBy
from .models import Categoria, Contato
# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
  list_display = ('id','nome', 'sobrenome', 'telefone', 'email', 'mostrar')
  list_display_links = ('id','nome')
  list_per_page = 5
  list_editable = ('telefone', 'mostrar')
 # list_filter = ('nome', 'sobrenome')
  search_fields = ('nome', 'sobrenome', 'telefone')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)