import pandas
import logging
import string
logger = logging.getLogger(__name__)

occupations = pandas.read_csv(
    'data/census_2011.csv',
    header=6,
)

# occupations.Industry.str.split().str.get(0)
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


# occupations.loc[str(2340)].astype(int).nlargest()


