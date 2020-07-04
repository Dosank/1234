from django.urls import path

from .views import CampList, QuestDetail, CampaingCreateView, CampaingCreateView2

urlpatterns = [
    path('list/', CampList.as_view(), name='CampView'),
    path('quest/<str:id>', QuestDetail.as_view(), name='QuestDetail'),
    path('create_Campaing', CampaingCreateView, name='CreateCamp'),
    path('create_Campaing2', CampaingCreateView2, name='CreateCamp2')

]