from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    # fields = ('name', 'seconds') #limita a inserção de items no model
    list_display = ('id', 'name', 'email', 'created_at')  #coloca colunas na tabela de usuários no admin
    list_filter = ('id', 'name', 'email', 'created_at') #Cria um filtro na pesquisa
    search_fields = ('id', 'name', 'email', 'created_at')

admin.site.register(User, UserAdmin)
