from sanic import Sanic
from sanic.response import html

app = Sanic("SanicApp")

@app.route("/")
async def home(request):
    return html("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sanic App</title>
</head>
<body>
    <h1>Welcome to Sanic!</h1>
    <p>This is a basic Sanic web application.</p>
</body>
</html>""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
