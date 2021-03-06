from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.employee_form,name="employee_insert"),  #get and post req. for insert opertaion
    path('<int:id>/',views.employee_form,name="employee_edit"),  # get and post req. for update operation
    path('delete/<int:id>',views.employee_delete,name="employee_delete"),
    path('list/',views.employee_list,name="employee_list"), # get req. to retrive and display all records
]