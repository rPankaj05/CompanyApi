
from django.contrib import admin
from django.urls import path,include
from Api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register('companies',CompanyViewSet)
router.register('employees',EmployeeViewSet)

urlpatterns = [
    path('',include(router.urls))
]

# companies/{companyId}/employees
