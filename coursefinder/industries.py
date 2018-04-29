import pandas
import pkg_resources
from os.path import join
datadir = pkg_resources.resource_filename('coursefinder', '../data')

# names for the hierarchy levels
levels = ['lvl1', 'lvl2', 'lvl3']
industries = pandas.read_csv(
    join(datadir, 'industries.csv'),
    header=None,
    names=['SIC']+levels,
    converters={'SIC': lambda s: int(s) if s.isdigit() else None}
)
# drop rows without SIC
industries.dropna(subset =['SIC'], inplace=True)
# drop rows without any label
industries.dropna(subset=levels, thresh=1, inplace=True)
# create a column with the hierarchy level 
level = industries[['lvl1', 'lvl2', 'lvl3']].stack().index.get_level_values(1)
industries['level'] = level
industries.set_index('SIC', inplace=True)

# Determine code range by division
divisions = {}
division = None
startCode = None
code = 100
with open(join(datadir, 'industries.csv')) as fhandle:
    for line in fhandle.readlines()[1:]:
        cell = line.split(',')[0]
        if cell.isnumeric():
            code = int(cell)
        elif len(cell) > 5:
            if division is not None:
                divisions[division] = (startCode, code)
            division = cell.strip('"')
            startCode = code + 1
    # last one
    divisions[division] = (startCode, code)


labels = [' '.join(k.split()[2:]) for k in sorted(divisions.keys())]
bins = [div[1][0] for div in sorted(divisions.items())]
bins += [10000]
divByIndustry = pandas.cut(industries.index, bins=sorted(bins), labels=labels)
industries['div'] = divByIndustry


