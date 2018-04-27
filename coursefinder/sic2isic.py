import pandas
import logging
logger = logging.getLogger(__name__)

def int_or_none(sval):
    return int(sval) if sval.isdigit() else None


sic_to_naics02 = pandas.read_csv(
    'data/1987_SIC_to_2002_NAICS.csv',
    converters={
        'SIC': int_or_none,
        '2002 NAICS': int_or_none
    }
)
sic_to_naics02.set_index('SIC', inplace=True)

naics02_to_naics07 = pandas.read_csv(
    'data/2002_to_2007_NAICS.csv',
    header=2,
    converters={
        '2007 NAICS Code': int_or_none,
        '2002 NAICS Code': int_or_none
    }
)
naics02_to_naics07.set_index('2002 NAICS Code', inplace=True)

naics07_to_isic4 = pandas.read_csv(
    'data/2007_NAICS_to_ISIC_4.csv',
    converters={
        '2007 NAICS US': int_or_none,
        'ISIC 4.0': int_or_none
    }
)
naics07_to_isic4.set_index('2007 NAICS US', inplace=True)


def sic2isic(sic):
    naics02 = sic_to_naics02.loc[sic]['2002 NAICS']
    logger.debug('NAICS 2002 code: %d', naics02)
    naics07 = naics02_to_naics07.loc[naics02]['2007 NAICS Code']
    logger.debug('NAICS 2007 code: %d', naics07)
    isic4 = naics07_to_isic4.loc[naics07]['ISIC 4.0']
    logger.debug('ISIC rev4 code: %d', isic4)
    return isic4