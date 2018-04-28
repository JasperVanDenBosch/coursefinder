import pandas
import logging
from os.path import join, expanduser
logger = logging.getLogger(__name__)

courses = pandas.read_csv(
    expanduser('~/data/coursefinder/on_2018_04_18_14_00_16/KISCOURSE.csv'),
)

courseIndexCols = ['KISCOURSEID', 'KISMODE', 'UKPRN']
courses = courses.set_index(courseIndexCols)

