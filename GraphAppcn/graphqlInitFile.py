# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import VehicleDetails as VehicleModel


class VehicleDetails(SQLAlchemyObjectType):
    class Meta:
        model = VehicleModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(VehicleDetails.connection)
    

schema = graphene.Schema(query=Query)