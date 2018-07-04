#---------------------------------------------------------
#    Imports
#---------------------------------------------------------

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from dashboard import views

#---------------------------------------------------------
#    Url Paths
#---------------------------------------------------------

urlpatterns = [
    path('', views.login_page, name='login'),
    path('authenticate/', views.login_authenticate, name='authenticate'),
    path('logout/', views.logout_account, name='logout'),
    path('register/', views.register, name='register'),
    path('register/create-profile/', views.create_profile, name='create-profile'),
    path('health/', views.health, name='health'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('news/', views.news, name='news'),
    path('news/create-news/', views.create_news, name='create-news'),
    path('news/update-news/', views.update_news, name='update-news'),
    path('news/delete-news/', views.delete_news, name='delete-news'),
    path('read/', views.read, name='read'),
    path('indicators/', views.indicators, name='indicators'),
    path('changes/', views.changes, name='changes'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile-update'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
