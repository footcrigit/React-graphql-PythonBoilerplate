from GraphAppcn import app
from GraphAppcn import vehicleDetails
from flask_graphql import GraphQLView
from .graphqlInitFile import schema
# app.add_url_rule('/vehdata', 'vehicleDetails', vehicleDetails.helloVehicle, methods = ['GET'])


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)