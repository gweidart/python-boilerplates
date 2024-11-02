import cherrypy

class HelloWorld:
    @cherrypy.expose
    def index(self):
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CherryPy App</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Welcome to CherryPy!</h1>
    <p>This is a basic CherryPy application.</p>
</body>
</html>"""

if __name__ == "__main__":
    config = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    cherrypy.quickstart(HelloWorld(), '/', config)
