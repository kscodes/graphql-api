import graphene
from graphene_django import DjangoObjectType
from .models import Banks,Branches

class BanksType(DjangoObjectType):
    class Meta:
        model = Banks
        fields = ("id" , "name")

class  BranchesType(DjangoObjectType):
    class Meta:
        model = Branches
        fields = ("ifsc","bank","branch","address","city","district","state")

class Query(graphene.ObjectType):
    
    all_branches=graphene.List(BranchesType,name=graphene.String())

    def resolve_all_branches(root,info,name):
        id=Banks.objects.get(name=name).id
        return Branches.objects.filter(bank=id)
        

    
schema = graphene.Schema(query=Query)