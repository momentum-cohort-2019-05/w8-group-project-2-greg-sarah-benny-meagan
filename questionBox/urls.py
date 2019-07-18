from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='index/', permanent=True)),
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
