from django.urls import path
from student import views


urlpatterns = [
    path('home/', views.homeView, name="Home"),
    path('register/', views.registerView, name="register"),
    path('student/show/',views.showView,name="show_student"),
    path('register_student/', views.register.as_view(), name="Home"),
    path('register_student/<pk>', views.register.as_view(), name="Home"),
]