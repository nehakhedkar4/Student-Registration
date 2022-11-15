from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.sign_up,name='signup'),
    path('ApplicationForm/',views.ApplictionForm,name='ApplicationForm'),
    path('<int:id>/',views.s_dashboard,name='s_dashboard'),
    path('f_dashboard/',views.f_dashboard,name='f_dashboard'),
    path('update/<int:id>/',views.action_data,name='update_status'),

]


   