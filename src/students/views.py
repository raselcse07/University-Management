from django.shortcuts import render
from .forms import ResultForm,StudentLoginForm
from .models import PersonalInfo,RegisteredCourse,Result,Attendence,Term_test,Reminder

def Student_login(request):

	try:

		form=StudentLoginForm(request.POST or None)
		template_name="Students/student_login.html"
		context={"form":form}

		if form.is_valid():

			reg_number=form.cleaned_data["Reg_No"]
			secret_key=form.cleaned_data["secret_key"]

			match_key=PersonalInfo.objects.get(reg_number=reg_number,TrxID=secret_key)


			if match_key:

				register_course_info=RegisteredCourse.objects.filter(reg_number=reg_number)
				CGPA=Result.objects.filter(reg_number=reg_number)
				att=Attendence.objects.filter(reg_number=reg_number)
				term=Term_test.objects.filter(reg_number=reg_number)
				next_exam=Reminder.objects.filter(reg_number=reg_number)

			
				context={

					"match_key":match_key,
					"register_course_info":register_course_info,
					"CGPA":CGPA,
					"att":att,
					"term":term,
					"next_exam":next_exam
			
					}

			template_name="Students/student_profile.html"
			return render(request,template_name,context)

	except:

		return render(request,"Students/login404_Not.html",{})

	return render(request,template_name,context)



def Result_Processing(request):

	try:

		form=ResultForm(request.POST or None)
		template_name= "Students/results.html"
		context={"form":form}

		if form.is_valid():

			reg_number=form.cleaned_data["Reg_No"]
			dept_name=form.cleaned_data["Dept_name"]
			session=form.cleaned_data["year"]
			secret_key=form.cleaned_data["secret_key"]

			match_result=PersonalInfo.objects.get(reg_number=reg_number,
												dept_name=dept_name,
												session=session,
												TrxID=secret_key)

			if match_result:

				register_course_info=RegisteredCourse.objects.filter(reg_number=reg_number)
				CGPA=Result.objects.filter(reg_number=reg_number)
				context={
						"match_result":match_result,
						"register_course_info":register_course_info,
						"CGPA":CGPA
						}

				template_name="Students/match_results.html"

				return render(request,template_name,context)
			else:
				context={}
				template_name="Students/results404_Not.html"
				return render(request,template_name,context)
	except:
		return render(request,"Students/results404_Not.html",{})

	return render(request,template_name,context)
