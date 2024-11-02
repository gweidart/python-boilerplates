from litestar import get

@get("/items")
def items() -> str:
    return "Items route!"
