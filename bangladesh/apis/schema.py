import graphene
from graphene_django import DjangoObjectType, DjangoListField 
from bangladesh.models import *
from bangladesh.apis.filter import *
from decorators import ExtendedConnection


class DivisionType(DjangoObjectType): 
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = Division
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
        filterset_class = DivisionFilter
        connection_class = ExtendedConnection

class DistrictType(DjangoObjectType): 
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = District
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
        filterset_class = DistrictFilter
        connection_class = ExtendedConnection
    

class UpazilaType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = Upazila
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
        filterset_class = UpazilaFilter
        connection_class = ExtendedConnection



class UnionType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = Union
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
        filterset_class = UnionFilter
        connection_class = ExtendedConnection

