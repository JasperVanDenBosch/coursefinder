from unittest import TestCase
from mock import patch, Mock


class AreasTests(TestCase):

    def test_country(self):
        from coursefinder.postcode_areas import geo_names_to_postcode_areas
        codes = geo_names_to_postcode_areas(['Wales'])
        self.assertEqual(len(codes), 7)
