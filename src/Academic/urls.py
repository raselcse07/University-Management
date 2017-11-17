from django.conf.urls import url
from . import views


app_name="Academic"

urlpatterns = [
    url(r'^$',views.Academic,name="academic"),
    url(r'^department/$', views.DepartmentList,name="dept_list"),
    url(r'^department/(?P<short_name>[-\w]+)/detail/$',views.DepartmentDetail,name="dept_detail"),
    url(r'^course/$',views.CourseList,name="course_list"),
    url(r'^course/(?P<course_name>[-\w]+)/detail/$',views.CourseDetail,name="course_detail"),

]
