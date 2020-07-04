from django.urls import path

from .views import (
    Index,
    CampList,
    QuestDetail,
    CampaingCreateView,
    CampaingCreateView2,    
    PjList,
    PjCreate,
)

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('list/', CampList.as_view(), name='camp_list'),
    path('quest/<str:id>', QuestDetail.as_view(), name='QuestDetail'),
    path('create_Campaing/', CampaingCreateView, name='CreateCamp'),
    path('create_Campaing2/', CampaingCreateView2, name='CreateCamp2'),
    path('pj_list/', PjList, name='PjList'),
    path('pj_create/', PjCreate, name='PjCreate'),


]