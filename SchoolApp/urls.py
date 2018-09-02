from .models import *
from django.urls import path

from .views import *


urlpatterns = [
    path('student/add',addStudent, name="add"),
    # path('register/', views.registerView, name="register"),
    #path('student/show/',views.showView,name="show_student"),
    #path('register_student/', views.register.as_view(), name="Home"),
    #path('register_student/<pk>', views.register.as_view(), name="Home"),
]