from django_filters import *

from bangladesh.models import *


class DivisionFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Division
        fields = '__all__'


class DistrictFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    division = CharFilter(field_name='division__name', lookup_expr='icontains')

    class Meta:
        model = District
        fields = '__all__'
        exclude = ['division']


class UpazilaFilter(FilterSet):

    district = CharFilter(field_name='district__name', lookup_expr='icontains')

    class Meta:
        model = Upazila
        fields = '__all__'
        exclude = ['district']

class UnionFilter(FilterSet):

    upazila = CharFilter(field_name='upazila__name', lookup_expr='icontains')

    class Meta:
        model = Union
        fields = '__all__'
        exclude = ['upazila']