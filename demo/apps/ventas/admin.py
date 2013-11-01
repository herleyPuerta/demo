from django.contrib import admin
from demo.apps.ventas.models import Cliente, Producto, CategoriaProducto

class productoAdmin(admin.ModelAdmin):
	list_display = ('nombre','thumbnail','precio','stock')
	list_filter = ('nombre','precio')
	search_fields = ['nombre','precio']
	#when update in order
	fields = ('nombre','descripcion','precio','stock','imagen','categorias','status') 

admin.site.register(Cliente)
admin.site.register(Producto,productoAdmin)
admin.site.register(CategoriaProducto)