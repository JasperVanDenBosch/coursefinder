import logging
import json
from pyramid.config import Configurator
log = logging.getLogger(__name__)
from coursefinder.geographies import geographies_as_tree
from coursefinder.industries import industries_as_tree
from coursefinder.engine import Engine


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=600)
    config.add_route('home', '/')
    config.add_view(home,
        route_name='home',
        renderer='templates/home.jinja2',
        http_cache=600,
    )
    config.add_route('courses', '/courses')
    config.add_view(courses,
        route_name='courses',
        renderer='json',
        http_cache=0,
    )
    return config.make_wsgi_app()


def home(request):
    return {
        'regions_json': json.dumps(geographies_as_tree()),
        'industries_json': json.dumps(industries_as_tree())
    }

def courses(request):
    industries = request.GET.getall('industries[]')
    geographies = request.GET.getall('geographies[]')
    courses = Engine().recommendCourses(industries, geographies)
    courses = courses.where(courses.notnull(), other=None)
    return  list(courses.T.to_dict().values())

