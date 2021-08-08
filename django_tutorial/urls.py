from django.contrib import admin
from django.urls import include, path
from django_tutorial import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('polls/', include('polls.urls')),
]
