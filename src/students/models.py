import datetime
from django.db import models
from Academic.models import Department,SEMESTER,Course
from .utils import create_TrxID
from Academic.models import SEMESTER
from django.utils import timezone


def upoload_location(instance,filename):

    return "Student Image/%s/%s/%s" %(instance.dept_name,instance.reg_number,filename)




year_dropdown = []
for y in range(2007, (datetime.datetime.now().year + 12)):
    year_dropdown.append((y, y))



class PersonalInfo(models.Model):

    name        =models.CharField(max_length=250)
    reg_number  =models.CharField(max_length=100,unique=True,primary_key=True)
    email       =models.EmailField(
                            verbose_name='email address',
                            max_length=255,
                            default="",
                            unique=True
                        )
    dept_name   =models.ForeignKey(Department,on_delete=models.CASCADE)
    fathers_name=models.CharField(max_length=250)
    mothers_name=models.CharField(max_length=250)
    birthday    =models.CharField(max_length=250,help_text="Format : DD/MM/YYYY,Example : 01/01/1960")
    blood_group =models.CharField(max_length=20,help_text="Example : AB+")
    semester    =models.CharField(max_length=50,choices=SEMESTER)
    session     =models.IntegerField(('session'), choices=year_dropdown, default=datetime.datetime.now().year)
    TrxID       =models.CharField(max_length=250,null=True,blank=True,unique=True,verbose_name="Password")
    height_field=models.IntegerField(default=100)
    width_field =models.IntegerField(default=100)
    student_image=models.ImageField(upload_to=upoload_location,
                                       height_field="height_field",
                                       width_field="width_field",
                                       default="")
    class Meta:

        ordering=["reg_number"]
        verbose_name_plural="Personal Infomations"
        verbose_name="Personal Information"


    def save(self,*args,**kwargs):

        if self.TrxID is None or self.TrxID == "":

            self.TrxID=create_TrxID(self)

        super(PersonalInfo,self).save(*args,**kwargs)

    def __str__(self):

        return str(self.reg_number)


class RegisteredCourse(models.Model):

    reg_number      =models.ForeignKey(PersonalInfo,on_delete=models.CASCADE)
    course_name     =models.ForeignKey(Course,on_delete=models.CASCADE)
    semster         =models.CharField(max_length=250,choices=SEMESTER,default="")
    course_CGPA     =models.CharField(max_length=250)


    class Meta:

        ordering=["reg_number"]

    def __str__(self):

        return str(self.reg_number)

class Result(models.Model):

    reg_number      =models.ForeignKey(PersonalInfo,on_delete=models.CASCADE)
    total_CGPA      =models.CharField(max_length=250)
    grade           =models.CharField(max_length=250)

    class Meta:

        ordering=["reg_number"]

    def __str__(self):

        return str(self.reg_number)

class Attendence(models.Model):

    class_date  =models.DateField(auto_now=True, auto_now_add=False)
    dept_name   =models.ForeignKey(Department,on_delete=models.CASCADE)
    course_name =models.ForeignKey(Course,on_delete=models.CASCADE)
    reg_number  =models.ForeignKey(PersonalInfo,on_delete=models.CASCADE)
    is_attend   =models.BooleanField(default=False)

    class Meta:

        ordering=["-class_date"]

    def __str__(self):

        return str(self.class_date)

class Term_test(models.Model):

    exam_date   =models.DateField(auto_now=True, auto_now_add=False)
    dept_name   =models.ForeignKey(Department,on_delete=models.CASCADE)
    course_name =course_name =models.ForeignKey(Course,on_delete=models.CASCADE)
    reg_number  =models.ForeignKey(PersonalInfo,on_delete=models.CASCADE)
    total_marks =models.CharField(max_length=20,default="20")
    obtain_marks=models.CharField(max_length=20,default="Absent")

    class Meta:

        ordering=["-exam_date"]

    def __str__(self):

        return str(self.exam_date)

class Reminder(models.Model):

    exam_date   =models.DateField(auto_now=False, auto_now_add=True)
    dept_name   =models.ForeignKey(Department,on_delete=models.CASCADE)
    reg_number  =models.ForeignKey(PersonalInfo,on_delete=models.CASCADE)
    course_list =models.CharField(max_length=250,default="",help_text="Example: CSE-101,CSE-102")
    exam_time   =models.CharField(max_length=250,default="",help_text="Example: CSE-101:10 AM,CSE-102:11 AM")


    class Meta:

        ordering=["-exam_date"]

    def __str__(self):

        return str(self.exam_date)







