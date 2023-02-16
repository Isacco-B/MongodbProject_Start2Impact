"""migrantSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import (
    CertificateListView,
    CertificateCreateView,
    CertificateDetailView,
    CertificateUpdateView,
    CertificateDeleteView,
)

app_name = 'transactions'

urlpatterns = [
    path('', CertificateListView.as_view(), name='certificate-list'),
    path('create/', CertificateCreateView.as_view(), name='certificate-create'),
    path('<int:pk>/', CertificateDetailView.as_view(), name='certificate-detail'),
    # path('update/<int:pk>/', CertificateUpdateView.as_view(), name='certificate-update'),
    path('delete/<int:pk>/', CertificateDeleteView.as_view(), name='certificate-delete'),
]
