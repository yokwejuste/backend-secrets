import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello from Graphene!"


schema = graphene.Schema(query=Query)
