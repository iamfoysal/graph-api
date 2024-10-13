import graphene
from schema import *


schema = graphene.Schema(query=Query, mutation=Mutation)