import pandas
import logging
import string
logger = logging.getLogger(__name__)

occupations = pandas.read_csv(
    'data/census_2011.csv',
    header=6,
)
# occupations.dropna

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


def topJobsForIndustries(codesFloat):
    codes = [str(int(code)) for code in codesFloat]
    try:
        total = totals.loc[codes].astype(int).sum()
    except KeyError:
        logger.debug('None of the industry codes have census data')
        return pandas.Series()

    # for each hierarchy level separately
    topjobs = pandas.Series()
    for level in (1, 2, 3):
        soc_subset = occupations.columns.where(soclevels==level).dropna()
        frac = occupations[soc_subset].loc[codes].sum(axis=0) / total
        topjobs = topjobs.append(frac.nlargest(3))
    for title, fraction in topjobs.iteritems():
        logger.debug('%.0f%% %s', fraction*100, title)
    return topjobs
