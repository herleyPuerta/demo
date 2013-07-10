from django.contrib import admin
from demo.apps.ventas.models import Cliente, Producto, CategoriaProducto

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(CategoriaProducto)