from django.conf.urls import url
from . import views

app_name="UserProfile"

urlpatterns = [

    url(r'^$',views.register,name="register"),
    url(r'^login/$',views.user_login,name="login"),
   
]