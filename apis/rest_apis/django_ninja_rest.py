from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello/{name}")
def hello(request, name: str):
    return {"message": f"Hello, {name}, from Django Ninja!"}
