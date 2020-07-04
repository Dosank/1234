from django.urls import path

from .views import (
    CampList,
    QuestDetail,
    CampaingCreateView,
    CampaingCreateView2,
    Index,
)

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('list/', CampList.as_view(), name='camp_list'),
    path('quest/<str:id>', QuestDetail.as_view(), name='QuestDetail'),
    path('create_Campaing', CampaingCreateView, name='CreateCamp'),
    path('create_Campaing2', CampaingCreateView2, name='CreateCamp2')

]