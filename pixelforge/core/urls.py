from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='login.html',
        authentication_form=CustomLoginForm
    ),
    name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create-project/', views.create_project, name='create_project'),
    path('assign/<int:project_id>/', views.assign_developers, name='assign_developers'),
    path('upload/<int:project_id>/', views.upload_document, name='upload_document'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]