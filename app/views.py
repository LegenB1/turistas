from django.shortcuts import render
from .models import Hotel, Ruta
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserForms


# Create your views here.
def index(request):
    hotel = Hotel.objects.all()
    data ={
        'hotel' : hotel
    }
    return render(request, 'app/index.html', data)



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