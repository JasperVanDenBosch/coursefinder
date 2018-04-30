from unittest import TestCase
from mock import patch, Mock


class CommandlineTests(TestCase):

    def test_missing_data(self):
        from coursefinder.commandline import CommandlineInterface
        from coursefinder.exceptions import MissingDataException

        with patch('coursefinder.commandline.Engine') as Engine:
            Engine().recommendCourses.side_effect = MissingDataException
            cli = CommandlineInterface()
            cli.industries = []
            cli.regions = []
            cli.print = Mock()
            cli.recommendCourses()
        cli.print.assert_called_with('Missing data.')

    def test_invalid_args(self):
        from coursefinder.commandline import CommandlineInterface
        from coursefinder.exceptions import InvalidCriteriaException

        with patch('coursefinder.commandline.Engine') as Engine:
            Engine().recommendCourses.side_effect = InvalidCriteriaException
            cli = CommandlineInterface()
            cli.industries = []
            cli.regions = []
            cli.print = Mock()
            cli.recommendCourses()
        cli.print.assert_called_with('Unknown input arguments.')

