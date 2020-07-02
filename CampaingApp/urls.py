from django.urls import path

from .views import CampList, QuestDetail, CampaingCreateView

urlpatterns = [
    path('list/', CampList.as_view(), name='CampView'),
    path('quest/<str:id>', QuestDetail.as_view(), name='QuestDetail'),
    path('create_Campaing', CampaingCreateView)

]