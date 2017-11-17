from django.contrib import admin
from .models import PersonalInfo,RegisteredCourse,Result,Attendence,Term_test,Reminder


class PersonalInfoModelAdmin(admin.ModelAdmin):

    list_display = ["reg_number","name","dept_name","semester"]
    list_display_links = ["reg_number","name"]
    list_filter = ["reg_number","name","dept_name","semester"]
    search_fields = ["reg_number","name","dept_name","semester"]

    class Meta:
        model=PersonalInfo

class RegisteredCourseModelAdmin(admin.ModelAdmin):

    list_display = ["reg_number","course_name","course_CGPA"]
    list_display_links = ["reg_number"]
    list_filter = ["course_name"]
    search_fields = ["reg_number","course_name","course_CGPA"]

    class Meta:

        model=RegisteredCourse


class ResultModelAdmin(admin.ModelAdmin):

    list_display = ["reg_number","total_CGPA","grade"]
    list_display_links = ["reg_number"]
    list_filter = ["total_CGPA"]
    search_fields = ["reg_number","total_CGPA","grade"]

    class Meta:

        model=Result


class AttendeceAdmin(admin.ModelAdmin):

    list_display = ["class_date","dept_name","reg_number","course_name","is_attend"]
    list_display_links = ["class_date"]
    list_filter = ["class_date"]
    search_fields = ["dept_name","reg_number","course_name"]

    class Meta:

        model=Attendence


class TermTestAdmin(admin.ModelAdmin):

    list_display = ["exam_date","dept_name","course_name","reg_number","total_marks","obtain_marks"]
    list_display_links = ["course_name","exam_date"]
    list_filter = ["exam_date"]
    search_fields = ["dept_name","reg_number","course_name"]

    class Meta:

        model=Term_test




class RemiderAdmin(admin.ModelAdmin):

    list_display = ["exam_date","dept_name","reg_number","course_list","exam_time"]
    list_display_links = ["exam_date"]
    list_filter = ["exam_date"]
    search_fields = ["dept_name","reg_number","course_list"]

    class Meta:

        model=Reminder


admin.site.register(PersonalInfo,PersonalInfoModelAdmin)
admin.site.register(RegisteredCourse,RegisteredCourseModelAdmin)
admin.site.register(Result,ResultModelAdmin)
admin.site.register(Attendence,AttendeceAdmin)
admin.site.register(Term_test,TermTestAdmin)
admin.site.register(Reminder,RemiderAdmin)
