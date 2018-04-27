import pandas
import logging
from os.path import join, expanduser
logger = logging.getLogger(__name__)

joblist = pandas.read_csv(
    expanduser('~/data/coursefinder/on_2018_04_18_14_00_16/JOBLIST.csv'),
)

joblist[joblist.JOB=='Welfare professionals'].nlargest(30, 'PERC')

top = {'4 Administrative and secretarial occupations': 0.41814631792470536, '242 Business, Research and Administrative Professionals': 0.05391232600879897, '41 Administrative occupations': 0.3826600063743406, '411 Administrative Occupations: Government and Related Organisations': 0.23913308967863195, '3 Associate professional and technical occupations': 0.17237080790299086, '415 Other Administrative Occupations': 0.06943563256394447, '2 Professional occupations': 0.17490714015506925, '35 Business and public service associate professionals': 0.1072304085833177, '24 Business, media and public service professionals': 0.10675829036610757}
topjobs = pandas.Series(top)


