import graphene
from graphene_django.types import DjangoObjectType
from .models import ExImp

class ExImpType(DjangoObjectType):
    class Meta:
        model = ExImp 

class Query(graphene.ObjectType):
    all_eximps = graphene.List(ExImpType)


def resolve_all_eximps(self, info, **kwargs):
    return ExImp.objects.all()