from django.http import HttpResponse
from demo.apps.ventas.models import Producto
#integramos la serializacion de los objetos
from django.core import serializers

def wsProductos_view(request):
	data = serializers.serialize("xml",Producto.objects.filter(status=True))
	#retorna la informacion en formato json
	return HttpResponse(data,mimetype="application/xml")