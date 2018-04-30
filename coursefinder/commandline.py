import argparse
from coursefinder.engine import Engine
from coursefinder.exceptions import MissingDataException
from coursefinder.exceptions import InvalidCriteriaException
import logging
logger = logging.getLogger(__name__)


class CommandlineInterface(object):

    def parseArguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('industries', type=str, nargs='+',
                            help='One or more industry sector names.')
        parser.add_argument('--regions', type=str, nargs='*', default=[],
                            help='Confine recommendations to these areas.')
        parser.add_argument('--debug', action='store_const',
                            const=10, default=30,
                            help='Print debug messages.')
        args = parser.parse_args()
        logging.basicConfig(level=args.debug)
        logger.debug('Verbosity level: %d', args.debug)
        self.industries = args.industries
        self.regions = args.regions

    def recommendCourses(self):
        """Print a list of courses that are a match for the given industry
        """
        try:
            courses = Engine().recommendCourses(self.industries, self.regions)
        except InvalidCriteriaException:
            self.print('Unknown input arguments.')
        except MissingDataException:
            self.print('Missing data.')
        else:
            for _, course in courses.iterrows():
                print('\n')
                print('score: {:.2f}'.format(course.pind))
                print('name: {}'.format(course.TITLE))
                print('provider: {}'.format(course.VIEW_NAME))
    
    def print(self, message):
        print(message)
