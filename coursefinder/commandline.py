import argparse
from coursefinder.industries import industries
from coursefinder.sic2isic import sic2isic
import logging
logger = logging.getLogger(__name__)


class CommandlineInterface(object):

    def parseArguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('industry', type=int,
                            help='The SIC code of an industry sector.')
        parser.add_argument('--debug', action='store_const',
                            const=10, default=30,
                            help='Print debug messages.')
        args = parser.parse_args()
        logging.basicConfig(level=args.debug)
        logger.debug('Verbosity level: %d', args.debug)
        self.sic = args.industry

    def recommendCourses(self):
        """Print a list of courses that are a match for the given industry

        Args:
            industry (int): SIC code
        """
        if self.sic not in industries.index:
            print('Unknown industry SIC code.')
        else:
            print(industries.loc[self.sic])
            isic4 = sic2isic(self.sic)
            print(isic4)
