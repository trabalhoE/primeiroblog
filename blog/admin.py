from django.contrib import admin
from .models import Especie
from .models import Genero
from .models import Familia
from .models import ClassificacaoTaxonomica

admin.site.register(Especie)
admin.site.register(Genero)
admin.site.register(Familia)
admin.site.register(ClassificacaoTaxonomica)