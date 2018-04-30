from unittest import TestCase


class EngineTests(TestCase):

    def test_invalid_sic(self):
        from coursefinder.engine import Engine
        from coursefinder.exceptions import InvalidCriteriaException
        with self.assertRaises(InvalidCriteriaException):
            # SIC 0 does not exist
            Engine().recommendCourses([0], [])

    def test_nodata_sic2naics(self):
        from coursefinder.engine import Engine
        from coursefinder.exceptions import MissingDataException
        with self.assertRaises(MissingDataException):
            # SIC 1111 does not have a corresponding NAICS 2002 code
            Engine().recommendCourses([1111], [])


