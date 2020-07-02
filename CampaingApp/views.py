from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect

from .forms import CreateCampaingF
from .models import Campaing, Quest


class CampList (View):
    
    def get(self, request):
        camp = Campaing.objects.all()
        return render(request, "CampList.html", {"camps":camp})

class QuestDetail (View):

    def get(self, request, id):
        camp = Campaing.objects.get(id=id)
        allquest = camp.questo.all()
        return render(request, "QuestDetail.html", {"allquests":allquest, "camp":camp})

def CampaingCreateView(request):
    if request.method == 'POST':
        form = CreateCampaingF(request.POST)
        if form.is_valid():
            form.save()
            return redirect("CampView")
    else:
        form = CreateCampaingF()
        return render(request, 'CreateCampaing.html', {'form':form})

def CampaingCreateView2(request):
    if request.method == 'POST':
        form = CreateCampaingF(request.POST)
        if form.is_valid():
            form.save()
            return redirect("CampView")
    else:
        form = CreateCampaingF()
        return render(request, 'CreateCampaing.html', {'form':form})

