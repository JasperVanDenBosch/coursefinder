import pandas
import logging
logger = logging.getLogger(__name__)

providers = pandas.read_csv(
    'data/learning-providers-plus.csv'
)
providers = providers.set_index('UKPRN')

