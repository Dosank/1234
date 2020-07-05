from django.shortcuts import render, redirect
from django.views import View

from .forms import CreateCampaingF, CreateCampaingF2, CreatePjF
from .models import Campaing, Quest, Pj, User


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
            return redirect("camp_list")
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
            return redirect("camp_list")
    else:
        form = CreateCampaingF2()
        return render(request, 'CreateCampaing.html', {'form':form})


def PjList(request):
    pj = Pj.objects.all()
    return render(request, "PjList.html", {"pjs":pj})


def PjCreate(request):
    if request.method == 'POST':
        form = CreatePjF(request.POST)
        if form.is_valid():
            pjTemp = Pj()
            pjTemp.name = form.cleaned_data['nameF']
            pjTemp.user = form.cleaned_data['userF']
            pjTemp.race = form.cleaned_data['raceF']
            pjTemp.save()
            return redirect('PjList')
    else:
        form = CreatePjF()
        return render(request, 'PjCreate.html', {'form':form})


class ProfileView(View):

    def get(self, request):
        profile = User.objects.all()
        return render(request, "Profiles.html", {'profiles':profile})


class ProfileDetail(View):

    def get(self, request, id):
        profile = User.objects.get(id=id)
        pj = profile.pjota.all()
        return render(request, "ProfilesDetail.html", {"pjs":pj, 'profile':profile})