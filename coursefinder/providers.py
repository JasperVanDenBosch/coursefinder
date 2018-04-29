import pandas
import logging
import pkg_resources
from os.path import join
logger = logging.getLogger(__name__)
datadir = pkg_resources.resource_filename('coursefinder', '../data')

providers = pandas.read_csv(
    join(datadir, 'learning-providers-plus.csv')
)
providers = providers.set_index('UKPRN')

