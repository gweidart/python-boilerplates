from pyramid.config import Configurator
from pyramid.response import Response

def home(request):
    return Response('<h1>Hello, Pyramid!</h1>')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.add_view(home, route_name='home')
    return config.make_wsgi_app()
