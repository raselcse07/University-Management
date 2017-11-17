from django.conf.urls import url
from . import views


app_name="student"

urlpatterns = [
	url(r'^student_login/$',views.Student_login,name="student_login"),
    url(r'^results/$',views.Result_Processing,name="result"),
  

]
