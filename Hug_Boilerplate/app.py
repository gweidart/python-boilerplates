import hug

@hug.get('/')
def home():
    return '<h1>Welcome to Hug!</h1><p>This is a basic Hug web application.</p>'

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
