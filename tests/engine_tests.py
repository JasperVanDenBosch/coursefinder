from unittest import TestCase


class EngineTests(TestCase):

    def test_invalid_sic(self):
        from coursefinder.engine import Engine
        from coursefinder.exceptions import InvalidCriteriaException
        with self.assertRaises(InvalidCriteriaException):
            # 'Wizardry' does not exist
            Engine().recommendCourses(['Wizardry'], [])

    def test_nodata_sic2naics(self):
        from coursefinder.engine import Engine
        from coursefinder.exceptions import MissingDataException
        with self.assertRaises(MissingDataException):
            # Wheat (SIC 1111) does not have a corresponding NAICS 2002 code
            Engine().recommendCourses(['Wheat'], [])


