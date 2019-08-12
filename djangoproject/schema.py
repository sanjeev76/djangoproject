import graphene
from eximp.schema import Query as eximps_query

class Query(eximps_query):
   pass 

schema = graphene.Schema(query = Query)