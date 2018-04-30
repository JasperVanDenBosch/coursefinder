import pandas
import logging
from coursefinder.geographies import geos, crosswalk
import pkg_resources
from os.path import join
logger = logging.getLogger(__name__)
datadir = pkg_resources.resource_filename('coursefinder', '../data')

areas = pandas.read_csv(
    join(datadir, 'postcode_areas.csv'),
)

def geo_names_to_postcode_areas(names):
    logger.debug('Geography names: %s', ', '.join(names))
    countries = geos.country.unique().tolist()
    counties = geos.county.unique().tolist()
    county_names = []
    for name in names:
        if name in countries:
            county_names += geos.county[geos.country==name].tolist()
        elif name in counties:
            county_names.append(name)
        else:
            logger.debug('Unknown region: %s', name)
    postal_county_names = []
    for name in county_names:
        postal_county_names += crosswalk.get(name, [name])
    logger.debug('Former postal counties: %s', ', '.join(postal_county_names))
    selection = areas[areas.Former_postal_county.isin(postal_county_names)]
    pareas = selection.Postcode_area.unique()
    logger.debug('Postcode areas: %s', ', '.join(pareas))
    return pareas
