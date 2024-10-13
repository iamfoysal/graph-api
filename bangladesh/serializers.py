from rest_framework import serializers
from .models import Division, District, Upazila, Union

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class UpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upazila
        fields = '__all__'

class UnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Union
        fields = '__all__'
