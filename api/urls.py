from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),

    path('dataCreate/', views.ListCreateDataView.as_view(), name="data-list-create"),
    path('songs/', views.ListSongsView.as_view(), name='songs-all'),
    path('data/',views.ListDataView.as_view())


]
