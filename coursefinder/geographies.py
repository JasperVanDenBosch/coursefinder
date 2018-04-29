import pandas
import logging
logger = logging.getLogger(__name__)


areas[areas.Former_postal_county=='Avon']
areas.Former_postal_county.unique()
areas.Former_postal_county.unique().shape
geos = pandas.read_csv('data/geographies.csv')
geos.columbs
geos.columns
geos['Unnamed: 2']
geos['Unnamed: 3']
geos['Unnamed: 4']
geos['Unnamed: 4'].unique()
geos['Unnamed: 4'].unique().shape
geo_counties = geos['Unnamed: 4'].unique().shape
post_counties = areas.Former_postal_county.unique()
geo_counties = geos['Unnamed: 4'].unique()
geo_counties = geos['Unnamed: 4'].unique().values
geo_counties = geos['Unnamed: 4'].unique()
set(geo_counties)
set(geo_counties).difference(set(postal_counties))
set(geo_counties).difference(set(post_counties))

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
Humberside -> North Humberside and South Humberside

Greater London
Greater Manchester

Isle of Man -> Isle of Mannot
Isle of Orkney -> Orkney
Isle of Rhum -> Isle of Rum
Isle of Shetland -> Shetland Islands
Isle of South Uist -> Inverness-shire
Kirkudbrightshire -> Kirkcudbrightshire
Lothian -> MidLothian, West Lothian, East Lothian
Peebleshire -> Peeblesshire
Rutland -> Leicestershire / Rutland
Strathclyde -> Renfrewshire, Ayrshire, Dunbartonshire, Lanarkshire
Tayside -> Angus, Kinross-shire, Perthshire
Yorkshire -> South Yorkshire, West Yorkshire, North Yorkshire



"""
