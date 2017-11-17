from django.db import models
from Academic.models import Department,Course
from .utils import create_TrxID
from django.utils import timezone



def upoload_location(instance,filename):

	return "Teacher Image/%s/%s/%s" %(instance.dept_name,instance.name,filename)



class PersonalInformation(models.Model):


	name        =models.CharField(max_length=250)
	role		=models.CharField(max_length=250,default="")
	email       =models.EmailField(
                            verbose_name='email address',
                            max_length=255,
                            default="",
                            unique=True
                        )
	mobile_number=models.CharField(max_length=250,help_text="Format : +8801630603018",default="")
	join_date	=models.CharField(max_length=250,default="",help_text="Format : DD/MM/YYYY,Example : 01/01/1960")
	biography	=models.TextField(default="")
	educational_background=models.TextField()
	dept_name   =models.ForeignKey(Department,on_delete=models.CASCADE)
	fathers_name=models.CharField(max_length=250)
	mothers_name=models.CharField(max_length=250)
	birthday    =models.CharField(max_length=250,help_text="Format : DD/MM/YYYY,Example : 01/01/1960")
	blood_group =models.CharField(max_length=20,help_text="Example : AB+")
	TrxID       =models.CharField(max_length=250,null=True,blank=True,unique=True,verbose_name="Password")
	height_field=models.IntegerField(default=100)
	width_field =models.IntegerField(default=100)
	teacher_image=models.ImageField(upload_to=upoload_location,
                                       height_field="height_field",
                                       width_field="width_field",
                                       default="")
	research_interests=models.TextField(default="")
	active_research_project=models.TextField(default="")
	previous_research_project=models.TextField(default="")
	external_affiliations=models.TextField(default="")
	awards_and_recognition=models.TextField(default="")
	selected_publications=models.TextField(default="")
	conference_proceedings=models.TextField(default="")
	teaching=models.TextField(default="")
	graduate_supervision=models.TextField(default="")



	class Meta:

		ordering=["name"]
		verbose_name_plural="Personal Infomations"
		verbose_name="Personal Information"


	def save(self,*args,**kwargs):

		if self.TrxID is None or self.TrxID == "":

			self.TrxID=create_TrxID(self)

		super(PersonalInformation,self).save(*args,**kwargs)

	def __str__(self):

		return str(self.email)

class AttendenceModel(models.Model):


	class_date  =models.DateField(auto_now=True, auto_now_add=False)
	dept_name   =models.ForeignKey(Department,on_delete=models.CASCADE)
	course_name =models.ForeignKey(Course,on_delete=models.CASCADE)
	email       =models.EmailField(
                            verbose_name='email address',
                            max_length=255,
                            default="",
                        )
	is_attend   =models.BooleanField(default=False)


	class Meta:

		ordering=["-class_date"]

	def __str__(self):

		return str(self.class_date)





class ReminderModel(models.Model):

	class_date   =models.DateField(auto_now=False, auto_now_add=True)
	email        =models.EmailField(
                            verbose_name='email address',
                            max_length=255,
                            default="",
                        
                        )
	dept_name    =models.ForeignKey(Department,on_delete=models.CASCADE,default="")
	course_list  =models.CharField(max_length=250,default="",help_text="Example: CSE-101,CSE-102")
	class_time   =models.CharField(max_length=250,default="",help_text="Example: CSE-101:10 AM,CSE-102:11 AM")

	class Meta:

		ordering=["-class_date"]



	def __str__(self):

		return str(self.class_date)





