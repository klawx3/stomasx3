from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

from ..models import User
from ..forms import RegisterForm

USER_SESSION_VAR = 'user_id'


def index(request):

    return render(request, 'index.html')
    
    #try:
    #    if request.session[USER_SESSION_VAR]:
    #        return HttpResponse("Hola mundo!")
    #    else:
    #        return HttpResponse("Sin logearse")
    #except KeyError:
    #    return HttpResponse("Sin logearse")
     
def login(request):
    try:
        user = User.objects.get(username = request.POST['username'])
        if user.password == request.POST['password']:
            request.session[USER_SESSION_VAR] = user.id
            return HttpResponse("Logeado exitosamente")
        else:
            return HttpResponse("Usuario o contraseña invalidos")
    except User.DoesNotExist:
        return HttpResponse("Usuario o contraseña invalidos")
        
def register(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            persist_form(form)
            return HttpResponse("Usuario creado")
    
    return render(request,'register_form.html',{"form": form})


def persist_form(form):
    user = User(username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],  
                fullname=form.cleaned_data['fullname'],  
                lastlogin=None,  
                apikey=None,  
                castle=form.cleaned_data['castle'],  
                faction=form.cleaned_data['faction'],  
                active=1)
    user.save()
    

    
def login_form(request):
    return render(request,'login_form.html')


