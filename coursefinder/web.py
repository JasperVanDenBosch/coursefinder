import logging
from pyramid.config import Configurator
log = logging.getLogger(__name__)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600*48)

    config.add_route('home', '/')
    # config.add_route('my/experiment/task/asset', '/asset/{aid}')
    # webtasks.filters.addFilters(config)
    # webtasks.helpers.addHelpers(config)

    config.scan()
    return config.make_wsgi_app()

from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}

