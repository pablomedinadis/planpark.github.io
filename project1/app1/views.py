from django.shortcuts import render, redirect
from . forms import userForm
from . models import user
# Create your views here.

def home(request):
    form = userForm
    users = user.objects.all
    context = {'form': form,'users':users}
    #context = {'form': form}
    return render(request,'home.html',context)

def database(request):
    form = userForm
    users = user.objects.all
    context = {'form': form,'users':users}
    #context = {'form': form}
    return render(request,'database.html',context)

def registro(request):
    form = userForm
    users = user.objects.all
    context = {'form': form,'users':users}
    #context = {'form': form}
    return render(request,'registro.html',context)

def add(request):
    if request.method=='POST':
        form = userForm(request.POST)
        if form.is_valid:
            form.save()
    return redirect('/')

def modificar(request,id):
    modificado = user.objects.get(id = id)
    form = userForm(request.POST,instance=modificado)
    form.save()
    return redirect('/')

def editar(request,id):
    editado = user.objects.get(id = id)
    return render(request,'editar.html',{'user' : editado})

def eliminar(request,id):
    aeliminar = user.objects.get(id = id)
    aeliminar.delete()
    return redirect('/database/')

def centrosocio(request):
    form = userForm
    users = user.objects.all
    context = {'form': form,'users':users}
    #context = {'form': form}
    return render(request,'centrosocio.html',context)
