import falcon

class HelloWorldResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.text = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Falcon App</title>
</head>
<body>
    <h1>Welcome to Falcon!</h1>
    <p>This is a basic Falcon web application.</p>
</body>
</html>"""

app = falcon.App()
app.add_route('/', HelloWorldResource())

# Run using: gunicorn app:app --reload
