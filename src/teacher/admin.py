from django.contrib import admin
from .models import PersonalInformation,AttendenceModel,ReminderModel



class PersonalInfoModelAdmin(admin.ModelAdmin):

	list_display = ["name","dept_name","email"]
	list_display_links = ["name","email"]
	list_filter = ["name"]
	search_fields = ["name","email"]


	class Meta:

		model=PersonalInformation

class AttendenceModelModelAdmin(admin.ModelAdmin):

	list_display = ["class_date","dept_name","email"]
	list_display_links = ["class_date","email"]
	list_filter = ["class_date"]
	search_fields = ["class_date","email"]

	class Meta:

		model=AttendenceModel


class ReminderModelModelAdmin(admin.ModelAdmin):

	list_display = ["class_date","dept_name","email"]
	list_display_links = ["class_date","email"]
	list_filter = ["class_date"]
	search_fields = ["class_date","email"]

	class Meta:

		model=PersonalInformation


admin.site.register(PersonalInformation,PersonalInfoModelAdmin)
admin.site.register(AttendenceModel,AttendenceModelModelAdmin)
admin.site.register(ReminderModel,ReminderModelModelAdmin)
