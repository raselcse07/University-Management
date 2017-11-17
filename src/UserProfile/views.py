from django.shortcuts import render
from .forms import UserCreationForm,LoginForm
from django.contrib.auth import login,get_user_model
from students.models import PersonalInfo
from django.http import HttpResponse


User=get_user_model()


def register(request,*args,**kwargs):

	form=UserCreationForm(request.POST or None)

	if form.is_valid():

		req_number_exists=PersonalInfo.objects.filter(reg_number=form.cleaned_data["reg_number"],
													email=form.cleaned_data["email"]).exists()

		if not req_number_exists:

			return HttpResponse("<h1>Invalid Reg. Number or Eamil</h1>")
		
		else:

			form.save()



	return render(request,"UserProfile/register.html",{"form":form})





def user_login(request,*args,**kwargs):

	form=LoginForm(request.POST or None)

	if form.is_valid():

		username_=form.cleaned_data.get('username')
		user_obj=User.objects.get(username__iexact=username_)

		login(request,user_obj)


	return render(request,"UserProfile/login.html",{"form":form})