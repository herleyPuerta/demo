from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import Producto
from django.http import HttpResponseRedirect
"""
def edit_product_view(request, id_prod):
	if request.user.is_authenticated():
		info = "inicializando"
		producto = Producto.objects.get(id=id_prod)
		if request.method == 'POST':
			form = addProductForm(request.POST,request.FILES)
			if form.is_valid():
				add_prod = form.save(commit=False)
				add_prod.status = True
				add_prod.save()
				form.save_m2m()
				info = "se ha guardado el produto"
				return HttpResponseRedirect("/producto/%s/"%add_prod.id)
		else:
			form = addProductForm(initial={
								'nombre' 		: producto.nombre,
								'descripcion' 	: producto.descripcion,
								'precio' 		: producto.precio,
								'stock'			: producto.stock,
			})
		ctx={'informacion':info,'form':form}
		return render_to_response("ventas/editProducto.html",ctx,context_instance=RequestContext(request))

"""
def add_product_view(request):
	if request.user.is_authenticated():
		info = "inicializando"
		if request.method == 'POST':
			form = addProductForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.status = True
				add.save()
				form.save_m2m()  # guarda las relaciones ManyToMany
				info = "se ha guardado satisfactoriamente"
				return HttpResponseRedirect('/producto/%s'%add.id)
			else:
				info = "datos incorrectos"
		else:
			form = addProductForm()
		ctx = {'form':form,'informacion':info}
		return render_to_response("ventas/addProducto.html",ctx,context_instance=RequestContext(request))


"""
def add_product_view(request):
	info = "inicializando"
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = addProductForm(request.POST,request.FILES)
			if form.is_valid():
				nombre 		= form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				imagen 		= form.cleaned_data['imagen']
				precio 		= form.cleaned_data['precio']
				stock 		= form.cleaned_data['stock']
				p = Producto()
				if imagen:
					p.imagen	= imagen
				p.nombre 		= nombre
				p.descripcion	= descripcion
				p.precio		= precio
				p.stock			= stock
				p.status		= True
				p.save()
				info = "se guardo satisfactoriamente"
			else:
				info = "informacion con datos incorrectos"
			form = addProductForm()
			ctx = {'form':form, 'informacion':info}
			return render_to_response('ventas/addProducto.html',ctx, context_instance=RequestContext(request))
		else:
			form = addProductForm()
			ctx = {'form':form}
			return render_to_response('ventas/addProducto.html', ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
"""

def edit_product_view(request, id_prod):
	p = Producto.objects.get(id=id_prod)
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			precio = form.cleaned_data['precio']
			stock = form.cleaned_data['stock']
			imagen = form.cleaned_data['imagen']
			p.nombre = nombre
			p.descripcion = descripcion
			p.precio = precio
			p.stock = stock
			if imagen:
				p.imagen = imagen
			p.save() #se guarda el modelo editado
			return HttpResponseRedirect('/producto/%s'%p.id)
	if request.method == "GET":
		form = addProductForm(initial={
								'nombre' 		: p.nombre,
								'descripcion' 	: p.descripcion,
								'precio' 		: p.precio,
								'stock'			: p.stock, 
			})
	ctx = {'form':form,'producto':p}
	return render_to_response('ventas/editProducto.html',ctx, context_instance=RequestContext(request))