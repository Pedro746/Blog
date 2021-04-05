from django.contrib import admin
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario', 'email_comentario',
                    'post_comentario', 'data_comentario', 'publicado_comentario',)
    list_editable = ('publicado_comentario',)
    list_display_links = ('id', 'nome_comentario', 'email_comentario',)
    list_per_page = 10


admin.site.register(Comentario, ComentarioAdmin)
