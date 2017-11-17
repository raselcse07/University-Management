from django.shortcuts import render,get_object_or_404
from .models import Department,Course
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def DepartmentList(request):

    qs=Department.objects.all()
    context={"qs":qs}
    template_name="Academic/department_list.html"

    return render(request,template_name,context)


def DepartmentDetail(request,short_name=None):

    qs=get_object_or_404(Department,short_name=short_name)
    context={"qs":qs}
    template_name="Academic/department_detail.html"

    return render(request, template_name, context)

def Academic(request):

    template_name="Academic/academic.html"
    return render(request,template_name,{})


def CourseList(request):

    q=request.GET.get("q", None)
    qs=Course.objects.all()

    paginator = Paginator(qs, 15)  # Show 15 contacts per page

    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    if q is not None:
        queryset = qs.filter(Q(course_dept=q))

    template_name="Academic/course_list.html"
    context={"qs":queryset}
    return render(request,template_name,context)

def CourseDetail(request,course_name=None):

    qs2=Course.objects.all()[:5]
    qs=get_object_or_404(Course,course_name=course_name)
    context={"qs":qs,"qs2":qs2}
    template_name="Academic/course_detail.html"

    return render(request,template_name,context)




