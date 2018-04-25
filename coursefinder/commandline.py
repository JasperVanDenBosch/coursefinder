import argparse
from coursefinder.industries import industries


class CommandlineInterface(object):

    def parseArguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('industry', type=int,
                            help='The SIC code of an industry sector.')
        args = parser.parse_args()
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
