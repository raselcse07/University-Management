from django.shortcuts import render
from Academic.models import Course
from django.db.models import Q

def Homepage(request):

    qs=Course.objects.all()
    q=request.GET.get("q",None)

    if q is not None:
        qs=qs.filter(Q(course_dept=q))
        return render(request,"MainSite/course_finder.html",{"qs":qs})

    return render(request,"MainSite/home.html",{})

