from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.reg,name='register'),
    path('login/',views.login,name='login'),
    path('get/',views.get_data,name='get'),
    path('del/',views.get_users,name='del'),
    path('update/',views.update_user,name='update'),
]
