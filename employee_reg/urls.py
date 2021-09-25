from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form),
    path('list/',views.employee_list),
    path('delete/',views.employee_delete)
    
]
