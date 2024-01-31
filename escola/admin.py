from django.contrib import admin
from escola.models import Aluno, Curso, Matricula
from django.utils.html import format_html

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
    
    def foto_preview(self, obj):
        return format_html(
            f'<img src="{obj.foto.url}" width="{obj.foto.width}" height="{obj.foto.height} style="border-radius: 50% 50%;" />'
            )
    
    readonly_fields = ['foto_preview']

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', )

admin.site.register(Matricula, Matriculas)