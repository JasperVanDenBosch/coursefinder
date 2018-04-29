import pandas
import logging
logger = logging.getLogger(__name__)

"""
# To determine mismatch: 

geos = pandas.read_csv('data/geographies.csv')
post_counties = areas.Former_postal_county.unique()
geo_counties = geos['Unnamed: 4'].unique()
set(geo_counties).difference(set(post_counties))
"""


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
