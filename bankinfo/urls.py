from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from bankinfo.schema import schema

urlpatterns = [

    path('gql',GraphQLView.as_view(graphiql=True,schema=schema)),
]