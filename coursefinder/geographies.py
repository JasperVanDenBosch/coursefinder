import pandas
import logging
import pkg_resources
from os.path import join
logger = logging.getLogger(__name__)
datadir = pkg_resources.resource_filename('coursefinder', '../data')

geos = pandas.read_csv(join(datadir, 'geographies.csv'))

crosswalk = {
    'Argyllshire': ['Argyll'],
    'Borders': ['Berwickshire', 'Peeblesshire', 'Roxburghshire', 'Selkirkshire'],
    'Humberside': ['North Humberside', 'South Humberside'],
    'Greater London': ['London'],
    'Greater Manchester': ['M'],
    'Isle of Man': ['Isle of Mannot'],
    'Isle of Orkney': ['Orkney'],
    'Isle of Rhum': ['Isle of Rum'],
    'Isle of Shetland': ['Shetland Islands'],
    'Isle of South Uist': ['Inverness-shire'],
    'Kirkudbrightshire': ['Kirkcudbrightshire'],
    'Lothian': ['MidLothian', 'West Lothian', 'East Lothian'],
    'Peebleshire': ['Peeblesshire'],
    'Rutland': ['Leicestershire / Rutland'],
    'Strathclyde': ['Renfrewshire', 'Ayrshire', 'Dunbartonshire', 'Lanarkshire'],
    'Tayside': ['Angus', 'Kinross-shire', 'Perthshire'],
    'Yorkshire': ['South Yorkshire', 'West Yorkshire', 'North Yorkshire'],
}

def geographies_as_tree():
    countries = geos.country.unique().tolist()
    tree = []
    for country in countries:
        country_branch = {'text': country, 'nodes': []}
        for county in geos.county[geos.country==country].tolist():
            country_branch['nodes'].append({'text': county})
        country_branch['tags'] = [str(len(country_branch['nodes']))]
        tree.append(country_branch)
    return tree
