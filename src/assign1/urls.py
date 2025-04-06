"""
URL configuration for assign1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import core.views as views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('/landpage', views.main_view, name='land_page'),
    path('/register', views.register_view, name='register'),
    path('admin/', admin.site.urls),

    #todo
    path("profile/", views.profile_view, name="profile"),
    path('', views.login_view, name='logout'),
    path('', views.login_view, name='dashboard'),
    path('/tournaments', views.tournaments_view, name='tournaments'),
    path('tournaments/<int:tournament_id>/register/', views.register_for_tournament, name='register_tournament'),
    path('', views.login_view, name='match_schedule'),
    path('', views.login_view, name='match_scores'),
    path('', views.login_view, name='referee_schedule'),
    path('', views.login_view, name='manage_scores'),
    path('', views.login_view, name='user_management'),
    path('', views.login_view, name='tournament_management'),
    path('/matches', views.match_list, name='match_management'),
    path('/landing/export', views.export_matches, name='export_matches'),
    path('/tournament/save', views.save_tournament, name='save_tournament'),
    path('/matches/update', views.update_score, name='update_score'),
    path('tournaments/<int:tournament_id>/delete/', views.delete_tournament, name='delete_tournament'),
    path('landpage/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('users/edit/', views.edit_user_submit, name='edit_user_submit'),
]
