from django.shortcuts import render
from .models import Hotel, Ruta
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserForms, FormularioHotel
import random
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.error.transbank_error import TransbankError



# Create your views here.
def index(request):
    hotel = Hotel.objects.all()
    ruta = Ruta.objects.all()
    data ={
        'hotel' : hotel,
        'ruta': ruta      
    }
    
    return render(request, 'app/index.html',data)




def registrar(request):
    
    data = {
        'form':CustomUserForms()
    }
    if request.method == 'POST':
        form = CustomUserForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect(to='index')

    return render(request, 'app/registrar.html', data)

def agregar_hotel(request):
    data = {
        'form' : FormularioHotel
    }
    if request.method == 'POST':
        formulario = FormularioHotel(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"

        else:
            data["form"] = formulario
    return render(request, 'app/agregar_hotel.html', data)

def modificar_hotel(request, id):
    hotel = Hotel.objects.get(id=id)
    data= {
        'form' : FormularioHotel(instance = hotel),
    }

    if request.method == 'POST' : 
        formulario = FormularioHotel(data=request.POST, instance=hotel, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
        data['form'] = FormularioHotel(instance=Hotel.objects.get(id=id))

    return render(request, 'app/modificar_hotel.html', data)

def listar_hotel(request):
    hotel = Hotel.objects.all()
    data ={
        'hotel':hotel,
    }
    return render(request, 'app/listar_hotel.html', data)

def eliminar_hotel(request, id):

    hotel = Hotel.objects.get(id = id)
    hotel.delete()

    return redirect(to="listar_hotel")

def mapa_valpo(request):

    return render(request, 'app/mapa.html')

def lista_categoria(request):
    
    return render(request, 'app/lista_categoria.html')

def categoria_hotel(request, star):
    hotel = Hotel.objects.filter(estrellas = star)
    data = {

        'hotel' : hotel,
    }
    return render(request, 'app/categoria_hotel.html', data)

def webpay_plus_create(request):
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = random.randrange(10000, 1000000)
    return_url = 'http://127.0.0.1:8000/webpay_plus/commit'

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }
    
    response = Transaction.create(buy_order, session_id, amount, return_url)

    data={
        'response' : response
    }
    
    print(response)

    return render(request,'musicproapp/webpay/create.html', data)