from django.urls import path

from api.views import AllBuyersListView, AllSelllersListView, AllCompetitionsListView, AllBidsListView, LoadModeldata, SellerBidsPerCompetition


app_name = 'api'

urlpatterns = [
    path('all-buyers/', AllBuyersListView.as_view(),
         name='AllBuyersListView'),
    path('all-sellers/', AllSelllersListView.as_view(),
         name='AllSelllersListView'),
    path('all-competitions/', AllCompetitionsListView.as_view(),
         name='AllCompetitionsListView'),
    path('all-bids/', AllBidsListView.as_view(),
         name='AllBidsListView'),
    path('load-data/<file_name>/', LoadModeldata.as_view(),
         name='LoadModeldata'),
    path('all-competitions-seller-bids/',
         SellerBidsPerCompetition.as_view(), name='SellerBidsPerCompetition'),
]
