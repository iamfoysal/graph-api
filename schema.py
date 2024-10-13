import graphene
from api.schema import *
from bangladesh.apis.query import *
from bangladesh.apis.mutation import *



# schema = graphene.Schema(query=BookQuery,
#                         mutation=BookMutation)

class Query(BangladeshQuery,
            BookQuery,
            graphene.ObjectType):
    pass

class Mutation(BookMutation,
               graphene.ObjectType):
    pass 
