"""physee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from tomatoes.views import (
    TomatoPlantView,
    TomatoPlantCreateListView,
    ProductionView,
    ProductionCreateListView,
    SensorDataView,
    SensorDataCreateListView,
    EnvironmentView,
    SoilView,
    TomatoesPlantView,
    ProductionsView,
)


urlpatterns = [
    path('admin/', admin.site.urls),


    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    path('api/tomatoes/<int:pk>', TomatoPlantView.as_view(), name='tomato'),
    path('api/tomatoes',TomatoPlantCreateListView.as_view(), name='tomato-create-list'),

    path('api/production/<int:pk>', ProductionView.as_view(), name='production'),
    path('api/production',ProductionCreateListView.as_view(), name='production-create-list'),

    path('api/sensor/<int:pk>', SensorDataView.as_view(), name='sensor'),
    path('api/sensor',SensorDataCreateListView.as_view(), name='sensor-create-list'),
    path('environment', EnvironmentView.as_view(), name='environment'),
    path('soil', SoilView.as_view(), name='soil'),
    path('tomatoes', TomatoesPlantView.as_view(), name='tomatoes'),
    path('production', ProductionsView.as_view(), name='productions'),

    path('openapi', get_schema_view(
        title="Taxim taxis API",
        description="REST API",
        public=True
    ), name='openapi-schema'),
]
