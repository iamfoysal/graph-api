from decorators import authenticate_role
import graphene
from django.utils.timezone import now
from graphene_django.filter import DjangoFilterConnectionField
from bangladesh.models import *
from bangladesh.apis.schema import *


class BangladeshQuery(graphene.ObjectType):

    divisions = DjangoFilterConnectionField(DivisionType)
    districts = DjangoFilterConnectionField(DistrictType)
    upazilas = DjangoFilterConnectionField(UpazilaType)
    unions = DjangoFilterConnectionField(UnionType)

    def resolve_divisions(self, info, **kwargs):
        return Division.objects.all()

    def resolve_districts(self, info, **kwargs):
        return District.objects.all()

    def resolve_upazilas(self, info, **kwargs):
        return Upazila.objects.all()

    def resolve_unions(self, info, **kwargs):
        return Union.objects.all()
