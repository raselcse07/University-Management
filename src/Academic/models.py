from django.db import models
from django.core.urlresolvers import reverse




SEMESTER=[
    ("1st Semester","1st"),
    ("2nd Semester","2nd"),
    ("3rd Semester","3rd"),
    ("4th Semester","4th"),
    ("5th Semester","5th"),
    ("6th Semester","6th"),
    ("7th Semester","7th"),
    ("8th Semester","8th"),

]

def upoload_location(instance,filename):

    return "Course Image/%s/%s/%s" %(instance.course_dept,instance.course_name,filename)


class Department(models.Model):

    dept_name       =models.CharField(max_length=250,unique=True,primary_key=True)
    short_name      =models.CharField(max_length=20,unique=True)
    description     =models.TextField()
    course_file     =models.FileField(default="")

    class Meta:

        ordering=["dept_name"]


    def __str__(self):

        return self.dept_name


class Course(models.Model):

    course_name     =models.CharField(max_length=250,unique=True,primary_key=True,default="")
    course_title    =models.CharField(max_length=250,default="")
    course_dept     =models.ForeignKey(Department,on_delete=models.CASCADE)
    credit          =models.CharField(max_length=20,default="")
    semester        =models.CharField(max_length=250,choices=SEMESTER,default="")
    ref_book        =models.FileField(default="")
    course_image    =models.ImageField(upload_to=upoload_location,
                                       height_field="height_field",
                                       width_field="width_field",
                                       default="")

    height_field    =models.IntegerField(default=0)
    width_field     =models.IntegerField(default=0)
    course_description=models.TextField(default="")
    course_detail   =models.TextField(default="")
    course_fees     =models.CharField(max_length=250,default="")
    course_teacher  =models.TextField(default="")





    class Meta:

        ordering=["course_name"]

    def __str__(self):

        return self.course_name

    def get_absolute_url(self):

        return reverse("Academic:course_detail",kwargs={"course_name":self.course_name})

