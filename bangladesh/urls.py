# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('divisions/', views.DivisionList.as_view(), name='division-list'),
    path('districts/', views.DistrictList.as_view(), name='district-list'),
    path('upazilas/', views.UpazilaList.as_view(), name='upazila-list'),
    path('unions/', views.UnionList.as_view(), name='union-list'),
]
