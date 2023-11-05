from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from . views import *


urlpatterns = [
    path('', views.ViewRequests.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('my_application/', views.User_requests.as_view(), name='my_application'),
    path('my_application/create/', views.ApplicationCreate.as_view(), name='my_application_create'),
    path('my_application/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='my_application_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
