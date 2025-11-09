"""
URL configuration for greenify project.

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
# greenify/urls.py

from django.contrib import admin
from django.urls import path
from usereg import views   # import your app's views here

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # User registration and account management routes
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('eco-tips/', views.eco_tips, name='eco_tips'),
    path('waste-management/', views.waste_management, name='waste_management'),
    path('water_conservation/', views.water_conservation, name='water_conservation'),
    path('energy/', views.energy_conservation, name='energy_conservation'),
    path('carbon-footprint/', views.carbon_footprint, name='carbon_footprint'),
    path('eco-challenges/', views.eco_challenges, name='eco_challenges'),
    path('progress-tracker/', views.progress_tracker, name='progress_tracker'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('rewards/', views.rewards, name='rewards'),
    path('community/', views.community, name='community'),
    path('articles/', views.articles, name='articles'),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about, name='about'),



    # Optional homepage or dashboard
    path('', views.home, name='home'),  # default route
]
