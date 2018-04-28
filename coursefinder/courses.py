import pandas
import logging
from os.path import join, expanduser
from numpy import dtype
logger = logging.getLogger(__name__)

courses = pandas.read_csv(
    expanduser('~/data/coursefinder/on_2018_04_18_14_00_16/KISCOURSE.csv'),
    dtype={
        'ASSURL': dtype('O'),
        'ASSURLW': dtype('O'),
        'CRSEURL': dtype('O'),
        'CRSEURLW': dtype('O'),
        'DISTANCE': dtype('int64'),
        'EMPLOYURL': dtype('O'),
        'EMPLOYURLW': dtype('O'),
        'FOUNDATION': dtype('int64'),
        'HONOURS': dtype('int64'),
        'JACS': dtype('O'),
        'JACS.1': dtype('O'),
        'JACS.2': dtype('O'),
        'KISAIMCODE': dtype('int64'),
        'LDCS': dtype('float64'),
        'LDCS.1': dtype('float64'),
        'LDCS.2': dtype('float64'),
        'LOCCHNGE': dtype('float64'),
        'LTURL': dtype('O'),
        'LTURLW': dtype('O'),
        'NHS': dtype('float64'),
        'NUMSTAGE': dtype('float64'),
        'PUBUKPRN': dtype('int64'),
        'SANDWICH': dtype('int64'),
        'SUPPORTURL': dtype('O'),
        'SUPPORTURLW': dtype('O'),
        'TITLE': dtype('O'),
        'TITLEW': dtype('O'),
        'UCASPROGID': dtype('O'),
        'UKPRNAPPLY': dtype('float64'),
        'YEARABROAD': dtype('int64')
    }
)

courseIndexCols = ['KISCOURSEID', 'KISMODE', 'UKPRN']
courses = courses.set_index(courseIndexCols)

