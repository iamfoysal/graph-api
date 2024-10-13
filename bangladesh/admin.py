from django.contrib import admin
from . models import * 

class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_bn', 'lat', 'long', 'created']
    search_fields = ['name', 'name_bn', 'lat', 'long', 'created']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['division', 'name', 'name_bn', 'lat', 'long', 'created']
    search_fields = ['division__name', 'name', 'name_bn', 'lat', 'long', 'created']
    list_filter = ['division',]

class UpazilaAdmin(admin.ModelAdmin):
    list_display = ['get_division_name', 'district', 'name', 'name_bn', 'created']
    search_fields = ['district__name', 'name', 'name_bn']

    def get_division_name(self, obj):
        return obj.district.division.name if obj.district.division else ''

    get_division_name.short_description = 'Division'

class UnionAdmin(admin.ModelAdmin):
    list_display = ['get_division_name','get_district_name','upazila', 'name', 'name_bn', 'url']
    search_fields = ['upazila__district__name', 'name', 'name_bn', ]

    def get_district_name(self, obj):
        return obj.upazila.district.name if obj.upazila.district else ''
    
    get_district_name.short_description = 'District'

    def get_division_name(self, obj):
        return obj.upazila.district.division.name if obj.upazila.district.division else ''
    
    get_division_name.short_description = 'Division'


admin.site.register(Division, DivisionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Upazila, UpazilaAdmin)
admin.site.register(Union, UnionAdmin)
