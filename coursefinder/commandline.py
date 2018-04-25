import argparse


class CommandlineInterface(object):

    def parseArguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('industry', help='The SIC code of an industry sector.')
        args = parser.parse_args()
        self.industry = args.industry

    def recommendCourses(self):
        """Print a list of courses that are a match for the given industry

        Args:
            industry (int): SIC code
        """
        print('Industry: ' + self.industry)
