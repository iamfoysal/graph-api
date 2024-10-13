# views.py
from rest_framework import generics
from .models import Division, District, Upazila, Union
from .serializers import DivisionSerializer, DistrictSerializer, UpazilaSerializer, UnionSerializer

class DivisionList(generics.ListCreateAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class DistrictList(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class UpazilaList(generics.ListCreateAPIView):
    queryset = Upazila.objects.all()
    serializer_class = UpazilaSerializer

class UnionList(generics.ListCreateAPIView):
    queryset = Union.objects.all()
    serializer_class = UnionSerializer
