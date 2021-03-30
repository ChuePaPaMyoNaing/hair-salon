from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('menu/', views.MenuListView.as_view(), name='menu'),
  path('menu/<int:pk>', views.MenuDetailView.as_view(), name='menu-detail'),
  path('stylist/', views.StylistView.as_view(), name='stylist'),
  path('stylist/<int:pk>', views.StylistDetailView.as_view(), name='stylist-detail'),
]