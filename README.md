# graphql-api

This is a graphql api implemented using graphene and django.
To run the app,please execute the  following command :
  py manage.py runserver

The models.py has been populated automatically using the sql dump file provided.The command executed was :
  py manage.py inspectdb > bankinfo/models.py

The graphql queires can be carried out at '/gql' url using the graphiql interface.No particular frontend has been built.

The schema.py contains a query which takes the bank name and returns required branches information.

A query example can be:

query{
  allBranches(name: 'STATE BANK OF INDIA'){
    ifsc
    address
   }
}

