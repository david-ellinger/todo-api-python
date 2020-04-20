from graphene import ObjectType, Schema, String


class ExampleQuery(ObjectType):
    hello = String()

    def resolve_hello(self, info):
        return "World"


class RootQuery(ExampleQuery, ObjectType):
    pass


# class RootMutation(UserMutation, ObjectType):
#     pass


schema = Schema(query=RootQuery)
