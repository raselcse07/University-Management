from django.shortcuts import render,get_object_or_404
from .models import PersonalInformation,AttendenceModel,ReminderModel
from .forms import TeacherList,TeacherLogin
from django.db.models import Q




def Profile(request,role=None):

	qs=PersonalInformation.objects.filter(role=role)
	template_name="teacher/tacher_profile.html"
	context={"qs":qs}

	return render(request,template_name,context)


def Teacher_List(request):

	query = request.GET.get("q", None)

	qs=PersonalInformation.objects.all()

	if query is not None:

		qs = qs.filter(Q(dept_name=query))


	template_name="teacher/tacher_list.html"
	context={"qs":qs}

	
	return render(request,template_name,context)


def Teacher_Login(request):

	try:

		form=TeacherLogin(request.POST or None)

		template_name="teacher/tacher_login.html"
		context={"form":form}

		if form.is_valid():

			email=form.cleaned_data["email"]
			secret_key=form.cleaned_data["secret_key"]

			qs=PersonalInformation.objects.get(email=email,TrxID=secret_key)

			if qs:

				att=AttendenceModel.objects.filter(email=email)
				rem=ReminderModel.objects.filter(email=email)

				context={

					"qs":qs,
					"att":att,
					"rem":rem

				}

			return render(request,"teacher/tacher_login_profile.html",context)
	except:
			pass

	return render(request,template_name,context)

