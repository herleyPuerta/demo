from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import Producto
from demo.apps.home.forms import ContactForm, LoginForm
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def index_view(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def about_view(request):
	mensaje = "esto es un mensaje desde mi vista"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html',ctx, context_instance=RequestContext(request))

def productos_view(request,pagina):
	lista_prod = Producto.objects.filter(status=True)
	paginator = Paginator(lista_prod,3)
	try:
		page = int(pagina) # por seguridad convierte la pagina enviada a int
	except:
		page = 1 # si no es un entero, la pagina por default es 1
	try:
		productos = paginator.page(page) # trae los productos q tiene page
	except(EmptyPage,InvalidPage):
		productos = paginator.page(paginator,num_pages)#envia a la ultima pagina
	ctx = {'productos':productos}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def singleProduct_view(request,id_prod): # id_prod le va a dar un num difente a cada pro en la url
	prod = Producto.objects.get(id=id_prod)
	ctx = {'producto':prod}
	return render_to_response('home/SingleProducto.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
	info_enviado = False
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']
			# configuracion usando Gmail
			to_admin = 'pruebadjango1@gmail.com'
			html_content = "informacion recibida de [%s]<br>***Mensaje*** <br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		formulario = ContactForm()
	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,  'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():# ya esta logueado?
		return HttResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o password incorrecto"
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')