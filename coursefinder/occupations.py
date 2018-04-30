import pandas
import logging
import string
import pkg_resources
from coursefinder.exceptions import MissingDataException
from os.path import join
logger = logging.getLogger(__name__)
datadir = pkg_resources.resource_filename('coursefinder', '../data')


occupations = pandas.read_csv(
    join(datadir, 'census_2011.csv'),
    header=6,
)

code_raw = occupations.Industry.str.split().str.get(0).astype(str)


def to_isic(raw):
    try:
        return str(int(float(raw)*100))
    except ValueError:
        if raw in string.ascii_uppercase:
            return raw


code = [to_isic(r) for r in code_raw]
occupations['isic4'] = code
occupations.set_index('isic4', inplace=True)
occupations.drop('Industry', axis=1, inplace=True)

# total workers by industry
totals = occupations['All categories: Occupation (full)']

# determine hierarchy by the number of digits in the code:
soclevels = occupations.columns.str.split().str.get(0).str.len().values
soclevels[0] = -1  # total columns


def topJobsForIndustries(codes):
    validCodes = totals.index.intersection(codes)
    if not validCodes.any():
        logger.debug('None of the industry codes have census data')
        raise MissingDataException

    total = totals.loc[validCodes].astype(int).sum()

    # for each hierarchy level separately
    topjobs = pandas.Series()
    for level in (1, 2, 3):
        soc_subset = occupations.columns.where(soclevels==level).dropna()
        frac = occupations[soc_subset].loc[validCodes].sum(axis=0) / total
        topjobs = topjobs.append(frac.nlargest(3))
    for title, fraction in topjobs.iteritems():
        logger.debug('%.0f%% %s', fraction*100, title)
    if topjobs.any():
        # lose code as JOBLIST only uses names
        topjobs.index = topjobs.index.str.lstrip('0123456789 ')
    topjobs = topjobs.rename('poccind')
    return topjobs
