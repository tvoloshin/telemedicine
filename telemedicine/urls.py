"""
URL configuration for telemedicine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from back import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('measures/new', views.save_measure),
    # path('measures/', views.get_measures),
    # path('measures/<int:pk>/delete/', views.delete_measure),
    path('measures/', views.MeasuresView.as_view()),
    path('measures/<str:pk>/', views.MeasureDetailView.as_view()),
    path('patients/', views.PatientsView.as_view()),
    path('patients/<str:pk>/', views.PatientDetailView.as_view()),
]
