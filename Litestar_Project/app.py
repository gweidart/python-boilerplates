from litestar import Litestar, get

@get("/")
def index() -> str:
    return "Welcome to Litestar!"

app = Litestar(route_handlers=[index])

if __name__ == "__main__":
    app.run(debug=True)
