from django.db.models import Q
from graphql import GraphQLError
from graphene import ObjectType, Connection, Node, Int
import math

def authenticate_role(allowed_groups):
    def decorator(func):
        def wrap(*args, **kwargs):
            info = args[1]
            user = info.context.user
            q_objects = Q()
            for group in allowed_groups:
                q_objects |= Q(name__iexact=group)
            if user.is_superuser or user.groups.filter(q_objects).exists():
                group_names = list(user.groups.values_list('name', flat=True))
                return func(*args, **kwargs)
            else:
                response_message = {
                    "message_en": "You are not authorized to perform this action.",
                    "message_pt": "Você não está autorizado a realizar esta ação.",
                    "status_code": 404,
                    "success": False,
                }
                raise GraphQLError(response_message)
        return wrap
    return decorator


class ExtendedConnection(Connection):
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()
   
    def resolve_total_count(root, info, **kwargs):
        return root.length
    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)
    
    '''
    # counting pages based on first argument 
    def resolve_page_count(root, info, **kwargs):
        first_argument = info.variable_values.get('first') 
        return math.ceil(root.length / first_argument)
    '''

