"""CostCalculation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
# from InjectionToolSelect import views
from InjectionTool import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('InjectionTool.urls')),
    path('injectiontool/', views.material_select, name='material_select'),
    path('get_material_density/', views.get_material_density, name='get_material_density'),
    path('gross_weight/', views.gross_weight, name='gross_weight'),
    path('carve_count/', views.carve_count, name='carve_count'),
    path('recommend_machine_type/', views.recommend_machine_type, name='recommend_machine_type')
    # path('updatesystem/',views.updatesystem,name='updatesystem'),
    # path('getipaddr/',views.getipaddr,name='getipaddr'),
]
