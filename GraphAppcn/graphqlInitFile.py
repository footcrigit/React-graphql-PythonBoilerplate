# flask_sqlalchemy/schema.py
import graphene
from graphene import relay,Schema, ObjectType, Date ,String, Field,Decimal, JSONString
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import VehicleDetails as VehicleModel
import datetime
import decimal

class VehicleDetails(SQLAlchemyObjectType):
    class Meta:
        model = VehicleModel
        interfaces = (relay.Node, )
class Person(ObjectType):
    id = String(required = True)
    name = String(required = True)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(VehicleDetails.connection)
    one_week_from = Date(required=True, date_input=Date(required=True))
    
    add_one_to = Decimal(required=True, decimal_input=Decimal(required=True), decimal_input2=Decimal(required=True))
    show_person = Field(Person, idval = String(required = True))
    def resolve_show_person(parent,info, idval):
        return {"id" : idval, "name" : "subhransu"}

    hello_azure = String()
    def resolve_hello_azure (parent,info):
        return {"hello Azure"}

    def resolve_add_one_to(root, info, decimal_input,decimal_input2):
        return  decimal_input + decimal.Decimal("1") + decimal_input2
    def resolve_one_week_from(root, info, date_input):
        assert date_input == datetime.date(2006, 1, 2)
        return date_input + datetime.timedelta(weeks=1)
    
   

schema = graphene.Schema(query=Query)