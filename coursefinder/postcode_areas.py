import pandas
import logging
logger = logging.getLogger(__name__)

areas = pandas.read_csv(
    'data/postcode_areas.csv',
)
"""
{'Argyllshire',
 'Borders',
 'Greater London',
 'Greater Manchester',
 'Humberside',
 'Isle of Man',
 'Isle of Orkney',
 'Isle of Rhum',
 'Isle of Shetland',
 'Isle of South Uist',
 'Kirkudbrightshire',
 'Lothian',
 'Peebleshire',
 'Rutland',
 'Strathclyde',
 'Tayside',
 'Yorkshire',
 nan}


Argyllshire-> Argyll
Borders -> Berwickshire, Peeblesshire, Roxburghshire, and Selkirkshire and



"""
