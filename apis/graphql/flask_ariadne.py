from ariadne import QueryType, make_executable_schema, graphql_sync
from flask import Flask, request, jsonify

app = Flask(__name__)

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()


@query.field("hello")
def resolve_hello(_, info):
    return "Hello, world!"


schema = make_executable_schema(type_defs, query)


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
