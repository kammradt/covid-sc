from django.contrib import admin
from apps.hospitals.models import Hospital, HospitalBed


class HospitalBedInline(admin.TabularInline):
    model = HospitalBed

    def get_extra(self, request, obj=None, **kwargs):
        extra = 3
        extra_on_edit = 0

        return extra_on_edit if obj else extra

class HospitalAdmin(admin.ModelAdmin):
    empty_value_display = '--'
    fieldsets = [
         (None, {
            'fields': ['acronym', ('name', 'city'), ('phonenumber', 'email')],
            'classes': ('wide', 'extrapretty'),
        }),
    ]
    inlines = [HospitalBedInline]
    list_display = ['upper_case_acronym', 'upper_case_name', 'city', 'phonenumber', 'email']
    ordering = ['acronym', 'name']
    search_fields = ['acronym', 'name']

    def upper_case_acronym(self, obj):
        return obj.acronym.upper()
    upper_case_acronym.short_description = 'acronym'


    def upper_case_name(self, obj):
        return obj.name.capitalize()
    upper_case_name.short_description = 'name'

admin.site.register(Hospital, HospitalAdmin)