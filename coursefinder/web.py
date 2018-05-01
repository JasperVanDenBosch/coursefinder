import logging
import json
from pyramid.config import Configurator
log = logging.getLogger(__name__)
from coursefinder.geographies import geographies_as_tree


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=10)
    config.add_route('home', '/')
    config.add_view(home, route_name='home', renderer='templates/home.jinja2')
    return config.make_wsgi_app()


def home(request):
    return {'regions_json': json.dumps(geographies_as_tree())}

