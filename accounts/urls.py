from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name = 'index'),
   path('accounts/studentregistration', views.studentregistration, name = 'studentregistration'),
   path('accounts/studentlogin', views.studentlogin, name = 'studentlogin'),
   path('accounts/profile/', views.profile, name='profile'),
   path('accounts/busfaculty/', views.busfaculty, name='busfaculty'),
   path('accounts/busdetails/', views.busdetails, name='busdetails'),
   path('accounts/logout/', views.logout, name='logout'),
   path('accounts/passwordreset/', views.passwordreset, name='passwordreset'),
   path('accounts/passwordresetdone/', views.passwordresetdone, name='passwordresetdone'),
   path('accounts/passwordresetconfirm/<uidb64>/<token>/', views.passwordresetconfirm, name='passwordresetconfirm'),
   path('accounts/passwordresetcomplete/', views.passwordresetcomplete, name='passwordresetcomplete'),
   path('announcements/', views.announcements, name='announcements'),
   path('about/', views.about, name='about'),
   #path('adminpage/', views.adminpage, name='adminpage'),
   path('accounts/simplecheckout',views.simplecheckout,name='simplecheckout')
]