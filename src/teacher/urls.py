from django.conf.urls import url
from . import views


app_name="teacher"

urlpatterns = [
	url(r'^teacher_profile/(?P<role>[\w-]+)/$',views.Profile,name="teacher_profile"),
	url(r'^teacher_list/$',views.Teacher_List,name="teacher_list"),
	url(r'^teacher_login/$',views.Teacher_Login,name="teacher_login"),

  

]
