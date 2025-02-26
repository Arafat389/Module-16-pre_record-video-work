from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
   # path('home/' , views.home, name = "home"), # function base
   path('home/' , views.StudentLists.as_view(), name = "home"),  # class base
   # path('create/' , views.create_student, name = "create_student"), # function base
   path('create/' , views.CreateStudentData.as_view(), name = "create_student"), # class base
   # path('edit/<int:id>/' , views.update_student, name = "update_student"), # Function base
   path('edit/<int:id>/' , views.UpdateStudentData.as_view(), name = "update_student"), # Class base
   # path('delete/<int:id>/' , views.delete_student, name = "delete_student"), # function base
   path('delete/<int:id>/' , views.DeleteStudentDate.as_view(), name = "delete_student"), # class base
]