from django.conf.urls import url
from dbr import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'dbr'
urlpatterns = [
    #path('', views.index,name='index'),
    path('register', views.register,name='register'),
    path('', views.user_login,name='login'),
    path('logout', views.user_logout,name='logout'),
    path('dashboard', views.dashboard,name='dashboard'),
    #path('date/', TemplateView.as_view(template_name='dbr/date.html'),name='date'),
    path('date', views.date,name='date'),
    path('roaster', views.roaster,name='roaster'),
]
