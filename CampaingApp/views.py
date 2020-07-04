from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect

from .forms import CreateCampaingF, CreateCampaingF2
from .models import Campaing, Quest


class Index(View):
    
    def get(self, request):
        return render(request, "Index.html", {})


class CampList (View):
    
    def get(self, request):
        camp = Campaing.objects.all()
        return render(request, "CampList.html", {"camps":camp})
    

class QuestDetail (View):

    def get(self, request, id):
        camp = Campaing.objects.get(id=id)
        allquest = camp.questo.all()
        return render(request, "QuestDetail.html", {"allquests":allquest, "camp":camp})


# Forma de hacerlo
def CampaingCreateView(request):
    if request.method == 'POST':
        form = CreateCampaingF(request.POST)
        if form.is_valid():
            form.save()
            return redirect("CampView")
    else:
        form = CreateCampaingF()
        return render(request, 'CreateCampaing.html', {'form':form})


# Otra forma de hacerlo
def CampaingCreateView2(request):
    if request.method == 'POST':
        form = CreateCampaingF2(request.POST)
        if form.is_valid():
            campTemp = Campaing()
            campTemp.title = form.cleaned_data['title']
            campTemp.master = form.cleaned_data['master']
            campTemp.save()
            return redirect("CampView")
    else:
        form = CreateCampaingF2()
        return render(request, 'CreateCampaing.html', {'form':form})


# 0 - En el Base.html , agregar un link a Index 
# Dicho index debe tener el siguiente icono . https://fontawesome.com/icons/home?style=solid

# 1 - Crear vista para listar personajes del usuario. Agregar boton para crear personaje

#2 - Crear vista para crear un nuevo personaje 

# 3 - Crear una vista para ver los datos del Perfil.